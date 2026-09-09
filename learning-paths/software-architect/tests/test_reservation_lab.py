"""Exercise the teaching implementation against real SQLite transactions."""
import concurrent.futures
import importlib.util
import pathlib
import tempfile
import unittest

PATH = pathlib.Path(__file__).resolve().parents[1] / 'practice' / 'reservation-lab.py'
LAB = None
if PATH.exists():
    SPEC = importlib.util.spec_from_file_location('reservation_lab', PATH)
    LAB = importlib.util.module_from_spec(SPEC)
    SPEC.loader.exec_module(LAB)


class ReservationTests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(LAB, 'Runnable reservation teaching lab is missing')
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.db = pathlib.Path(self.temp.name) / 'lab.db'
        LAB.initialise(self.db, stock=1)

    def test_concurrent_requests_cannot_oversell(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(lambda key: LAB.reserve(self.db,key,1), ['order-a','order-b']))
        self.assertEqual(sorted(r['status'] for r in results), ['rejected','reserved'])
        self.assertEqual(LAB.snapshot(self.db)['stock'], 0)

    def test_retry_after_lost_response_returns_same_reservation(self):
        first = LAB.reserve(self.db,'order-a',1)
        self.assertEqual(LAB.reserve(self.db,'order-a',1),first)
        self.assertEqual(LAB.snapshot(self.db)['reservations'],1)
        self.assertEqual(LAB.snapshot(self.db)['outbox'],1)
        with self.assertRaises(ValueError):
            LAB.reserve(self.db,'order-a',2)

    def test_crash_before_commit_leaves_no_partial_reservation(self):
        with self.assertRaises(RuntimeError):
            LAB.reserve(self.db,'order-a',1,crash_before_commit=True)
        self.assertEqual(LAB.snapshot(self.db), {'stock':1,'reservations':0,'outbox':0,'pending':0,'effects':0})

    def test_duplicate_delivery_after_relay_crash_has_one_effect(self):
        LAB.reserve(self.db,'order-a',1)
        with self.assertRaises(RuntimeError):
            LAB.relay(self.db,crash_after_effect=True)
        self.assertEqual(LAB.snapshot(self.db)['pending'],1)
        LAB.relay(self.db)
        self.assertEqual(LAB.snapshot(self.db)['effects'],1)
        self.assertEqual(LAB.snapshot(self.db)['pending'],0)

    def test_invalid_quantities_are_rejected_without_mutation(self):
        for quantity in [0,-1,True,1.5,'1']:
            with self.subTest(quantity=quantity), self.assertRaises(ValueError):
                LAB.reserve(self.db,'invalid',quantity)
        self.assertEqual(LAB.snapshot(self.db)['stock'],1)


if __name__ == '__main__':
    unittest.main()
