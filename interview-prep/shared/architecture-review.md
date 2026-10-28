# Architecture review

**Status:** Owner-approved · **Last reviewed:** 28 October 2026

How an Architecture Review Board works, what a Product Owner brings to it, and a worked answer from Smart Timesheet, where you were in the room. Use it with [Connect the dots](connect-the-dots.md) and the [decision lists](decision-ledger.md).

## What a review board is for

An Architecture Review Board (ARB) checks that a design fits the organisation's principles, standards and risk appetite before money or production access is committed. TOGAF calls it the Architecture Board; many UK organisations call it a design authority. It usually ends in one of four outcomes: approve, approve with conditions, defer, or reject. Sometimes it grants a time-limited exception to a standard.

A Change Advisory Board (CAB) is different. A CAB asks “is this change safe to make now?”; an ARB asks “is this the right design?”. You have worked with both at Northern Powergrid: Smart Timesheet went through the ARB, and the infrastructure programme used the ARB for upgrades and the weekly CAB for every production change.

## Who brings what

| Role | Brings | Typical content |
| --- | --- | --- |
| Product Owner | The why and the what | Problem, users and value, with the number; scope in, out and deferred; non-functional needs grounded in research; rollout plan and how to reverse it; how success is measured |
| Architect | The how | C4 context and container views; options considered, with an ADR; how the design meets standards; security and data model; run cost and support model |
| Delivery lead | The when and the risk | Plan and dependencies; RAID log highlights; environments and release approach; who closes each condition, and by when |

## The one-page pack

In the order the board reads it:

1. **Decision asked:** what you want the board to approve today.
2. **Problem and value:** who has the problem, and the number.
3. **Scope:** in, out and deferred.
4. **Context view:** users, the system and its neighbours.
5. **Options and recommendation:** two or three options and the trade-off.
6. **Quality needs:** availability, security and data, and how each is met.
7. **Risks and exceptions:** open risks, compliance, and any standard waived.
8. **Cost and support:** build cost, run cost, and who supports it.

## Answering “how do you represent a design at an ARB?”

### Q1. How do you represent a design or architecture at a review board?

**Model answer:** “I treat the review board as a decision meeting, not a show-and-tell. Beforehand I agree with the architect who presents what. I bring the why and the what: the problem, the value, the users, the scope and the rollout. The architect brings the how: the options, the design and how it meets the standards. We send a one-page pack in advance that opens with the decision we're asking for. In the room I start with the decision and the value, the architect walks through the container view and the main trade-off, and I take the questions on scope and risk. Any conditions go into the backlog as items with an owner and a date, and I report on them at the next review. That keeps governance a check on risk instead of a queue.”

## Three traps panels listen for

- Showing the solution before the problem. Boards approve value and risk, not diagrams.
- Answering outside your lane: the Product Owner defending design details they didn't own, or the architect fielding value questions.
- Treating conditions as paperwork. A condition with no owner or date in the backlog is the most common way governance turns into delay.

## Worked example: Smart Timesheet

Northern Powergrid, 2019 to March 2020, while you were the TCS Product Owner. The initiative needed rulings from several perspectives at Northern Powergrid's board (data sovereignty, GDPR impact and design review), and the data-sharing ruling decided whether it was viable. When a panel asks “which architecture concerns have you dealt with?”, name those three.

The facts that shape the answer:

- TCS, as implementation partner, chose OutSystems to get from prototype to production quickly.
- OutSystems ran the platform in its own cloud on AWS. Northern Powergrid had no direct relationship with AWS.
- Only three fields crossed to the cloud: employee ID, name and day rate. The native app worked offline, and the desktop web app was deferred so mobile shipped first.
- You were in the room at the ARB.

So the honest answer to “how did you handle the AWS architecture?” is that the AWS layer was the vendor's. The decisions that mattered to Northern Powergrid were about data: where it lived and what left Oracle. Those went through the ARB, and you were there.

How the system worked:

1. Engineers submit their time in the OutSystems native app. It stores timesheets on the phone and syncs when back online.
2. Supervisors approve timesheets in the same app.
3. The app calls the .NET layer whenever it needs employee data.
4. The .NET layer reads Oracle HCM. This is where employee data leaves Northern Powergrid's systems for a vendor cloud; the ARB approved only employee ID, name and day rate.
5. It also calls Oracle CRM through its API: the second legacy dependency, and the second delivery risk.
6. When a timesheet is approved, API calls send what each system needs to HCM, CRM and payroll.

The full decision list is in [Decision lists](decision-ledger.md#s3-smart-timesheet).

### Q2. On the timesheet project, how did you handle the AWS architecture, what did you decide and what did the architect decide, and how did you present it to the ARB?

**Stakes.** “Smart Timesheet replaced paper timesheets for over two thousand Northern Powergrid field engineers. Forms went back to depots by hand and payroll keyed them in two to three days later, so mistakes turned into pay complaints.”

**Split.** “I was the TCS Product Owner, and the decisions sat at three levels. I owned what we built and in what order: the users, the first release, the acceptance criteria and the rollout. TCS, as the implementation partner, chose OutSystems so we could move from prototype to production quickly, and our architect and engineering lead owned the integration design. The decisions that could make or break the initiative belonged to Northern Powergrid's Architecture Review Board: data sovereignty and GDPR.”

**Sketch.** “In three boxes: an OutSystems app for engineers and supervisors, running in OutSystems' own cloud on AWS; a .NET integration layer; and the legacy Oracle HCM and CRM systems behind it, which held the employee data. Northern Powergrid had no AWS account of its own. OutSystems ran that layer. So the arrow that mattered was employee data leaving Oracle for a vendor's cloud.”

**Shape.** “That turned the AWS question into two product questions: where does the data live, and what data does the app actually need? We sent the cloud only what the app needed: employee ID, name and day rate. Every extra field would have made the GDPR case harder. Engineers often worked without signal, so the native app stored timesheets on the phone and synced when back online, and I deferred the desktop web app so mobile shipped first. Field research also gave the architect real usability requirements: gloves, rain and small screens, so the app had to be simple and forgiving. I moved the Oracle integration work to the front of the backlog so it was proven before the alpha, and the alpha at one depot doubled as a live test of the integration.”

**Show.** “I was in the room at the ARB, because the initiative needed decisions from several architecture perspectives: data sovereignty, GDPR impact and design review. I presented the why and the what: the problem, the value, the users, the data we needed and the rollout. Our architect presented the design. The board required the data to stay in the UK and approved only those three fields. Nothing else left Northern Powergrid's systems. The service grew to over three thousand users and saved around half a million pounds a year. I own the why and the what, the architects and the board own the how and the guardrails, and the backlog is where they meet.”

Say “hosted in the UK” rather than naming an AWS region, unless you know which one OutSystems used. If they ask why AWS decisions weren't yours: “On a managed platform the infrastructure is the vendor's job. Our job was deciding what we trusted the vendor with.” Before you say the £500k figure, know how it was calculated: paper processing removed, fewer office visits and faster payroll.

**One level down:**

1. **Who ran the AWS side?** OutSystems did, as a managed cloud. In GDPR terms that usually makes Northern Powergrid the controller, OutSystems a processor and AWS a sub-processor. That chain is what the ARB had to be satisfied with.
2. **How did the cloud app reach Oracle?** The .NET middleware called Oracle HCM and CRM through APIs, and approval triggered the calls to HCM, CRM and payroll. If pressed on the network path, the patterns are in the [SAA-C03 handbook](../../handbooks/aws-saa-c03/saa-c03-visual-handbook-2026.09.html#hybrid-connectivity-title): VPN versus Direct Connect, and hybrid connectivity.
3. **What if signal or Oracle was down?** Offline-first on the phone covered no signal. For Oracle outages at payroll cut-off: timeouts, retries, a circuit breaker or queued submissions. See [System Design v6](../../handbooks/system-design/system-design-concept-handbook-v6.html#c13), chapters 10, 13 and 14.
4. **Who could sign in, and how?** The usual pattern is single sign-on against the corporate directory. Check what Smart Timesheet actually used before you say it.
5. **How did you handle data sovereignty and GDPR?** UK hosting and data minimisation: three fields crossed. Day rate is pay data, so prepare for “why did the cloud need it?”. Encryption is covered in the SAA-C03 handbook; a processing agreement with the vendor is the contractual side. This is your strongest level-3 topic, because you were in the room for it.
6. **How available did it need to be?** Peaks around submission deadlines and the payroll cut-off. See [System Design v6](../../handbooks/system-design/system-design-concept-handbook-v6.html#c16), chapter 16, on SLOs.
