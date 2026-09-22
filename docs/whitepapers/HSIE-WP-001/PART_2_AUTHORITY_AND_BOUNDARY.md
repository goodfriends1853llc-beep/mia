# HSIE-WP-001 — Part 2

# 7. Capability Does Not Create Authority

MIA distinguishes the identity submitting a request from the identity whose authority is being exercised.

The runtime contract separately represents the Caller, Actor, Subject, Runtime, Capability Provider, and Assessor or Verifier.

Caller and Actor may be identical.

They are not assumed to be identical.

This distinction matters because possession of a capability does not grant authority to exercise it.

A model may know how to invoke a financial service.

That does not establish permission to move money.

An automated agent may technically be able to send a message.

That does not establish whose authority the message represents.

A credential may authenticate a principal.

Authentication does not create unlimited authorization.

A policy may allow an operation for one purpose or subject.

That permission does not automatically extend to another scope, target, purpose, or time.

MIA therefore treats identity, authority, consent, eligibility, purpose, scope, and policy as explicit runtime concerns.

This has conceptual overlap with zero-trust security principles. NIST SP 800-207 rejects implicit trust based solely on network location or ownership and treats authentication and authorization as discrete functions before access to protected resources.

MIA does not claim conformance with NIST Zero Trust Architecture; the relationship is conceptual rather than certificatory.

---

# 8. Intelligence Remains Inference Until Governed Promotion

One of MIA's central protections is the separation between model inference and governed state.

A model can interpret.

A model can propose.

A model can classify.

A model can rank possibilities.

A model can create candidate structured information.

But model output does not automatically become authoritative state.

The preserved runtime validation record includes a passing path demonstrating that model output remains inference until human acceptance.

This becomes particularly important in systems maintaining continuity about human beings.

An AI system may infer that a person prefers something.

It may infer that a person intends something.

It may identify a possible behavioral pattern.

It may infer that a person's circumstances have changed.

These representations may be useful.

They remain representations.

MIA preserves the distinction between what intelligence generated and what an authorized human or governed process actually accepted.

NIST's Generative AI Profile similarly emphasizes governance, documentation, human oversight, tracking, and risk management around generative systems.

MIA's mechanism is its own and does not imply NIST certification or formal conformance.

---

# 9. Execution Is Not Effect

One of the most important distinctions in MIA occurs after execution.

The runtime contract states:

> **Execution and effect are distinct.**

After a consequential capability returns, MIA must determine whether the intended internal or external effect actually occurred.

The effect contract maintains a separate effect state and explicitly states that a returned API, model, or tool result does not automatically equal confirmed effect.

This prevents a common automation failure:

> **“The request was sent” becomes “the thing happened.”**

Those are different claims.

A request may be accepted by an interface while downstream work fails.

A provider may acknowledge submission before completing an operation.

A remote system may receive a request immediately before connectivity is lost.

A timeout may leave the outcome uncertain.

A software response may claim success incorrectly.

A physical consequence may require evidence outside the process that initiated it.

For this reason:

> **EXECUTION ≠ EFFECT**

and:

> **DISPATCH ≠ VERIFIED EFFECT**

---

# 10. Verified Effect Is Not Governed Commit

Even a verified effect is not necessarily the final state transition.

MIA defines **commit** independently.

Commit is the governed acceptance of resulting changes into MIA-controlled state and history.

The runtime contract requires commit to preserve pre-state and post-state references, evidence, provenance, uncertainty, and the authority and policy basis of the change. Events and Relationships are created or superseded rather than silently overwritten.

This produces a core MIA distinction:

> **VALID ≠ PERMITTED ≠ EXECUTED ≠ VERIFIED ≠ COMMITTED ≠ RECEIPTED**

Valid asks whether the operation meets structural requirements.

Permitted asks whether governance allows the operation.

Executed asks whether execution was attempted.

Verified asks whether the required result is sufficiently evidenced.

Committed asks whether the result was accepted into governed state.

Receipted asks whether an attributable immutable record exists for the operation.

Collapsing these states makes software simpler.

Separating them makes consequential software more reconstructable.

---

# 11. External-Boundary Validation

The frozen MIA Runtime v1.0.0 establishes the core governed runtime.

Later development examined a narrower problem:

> **What happens at the point where governed intention approaches an external capability?**

This work occurred in separate development copies.

It did not modify frozen MIA Runtime v1.0.0.

Three distinct external-boundary evidence stages are relevant.

## 11.1 Gate-Repair Candidate 3 — Target, Credential, and Dispatch Separation

An earlier sealed gate-repair Candidate 3 was preserved with SHA-256:

`73ccaa32757f8b743cb39b9bc058fae39eb5c65e922796e765517158f628b96c`

Controlled tests recorded:

- **Target admission:** 6/6 PASS
- **Credential gate:** 10/10 PASS
- **Simulated dispatcher:** 7/7 PASS

Credential denial cases included wrong scope, expiration, revocation, malformed records, and credentials identified as originating from a discovered or public-repository context.

Denied paths produced zero simulated calls.

A permitted dispatch returned:

`DISPATCHED_UNVERIFIED`

An effector failure returned:

`UNKNOWN`

with one attempt and no silent retry.

The associated dispatch evidence report was recorded with SHA-256:

`395dbfa577477bbfb30e1c0898b1ac970c8fdead6499a4bdb5873bbce3b7e396`

The supported conclusion was narrow:

A controlled offline boundary could distinguish denial, attempted dispatch, uncertain failure, and dispatched-but-unverified state without automatically representing attempted execution as confirmed external effect.

## 11.2 Offline Boundary Candidate 2 — Authority Ordering

The next development stage tested an additional problem:

> **What happens when authority changes close to the execution boundary?**

Offline Boundary Candidate 2 was packaged with SHA-256:

`b775044b2d59b42f2974d709d145630674c435651ea3a9b95e6efdda594a873c`

The authority-ordering suite passed **3/3 controlled tests**.

A revocation established before dispatch prevented the external call.

Observed external calls:

`0`

A revocation requested while an authorized dispatch was already active waited behind the in-flight operation rather than retroactively rewriting the authority state under which that operation began.

A simulated tool or effector exception produced an `UNKNOWN` execution result and released the execution lock.

These results matter because authority is temporal.

The statement:

> **“authority is revoked”**

does not, by itself, answer whether revocation occurred before an operation was authorized, during an active operation, or after an effect occurred.

MIA therefore treats ordering as evidence rather than silently allowing later state to rewrite earlier history.

The result does not prove a complete production concurrency model.

It establishes the tested ordering behavior in the controlled offline boundary.

---

# 12. Persistent Request Identity, Crash Uncertainty, and Concurrency

A further boundary problem remained.

Even if target, credentials, authority, and dispatch are governed, repeated or concurrent requests can still create dangerous ambiguity.

A caller can retry after a timeout.

A process can crash after reserving work.

Two processes may submit the same request simultaneously.

A network failure may leave the system uncertain whether the external side effect occurred.

Naively retrying such operations can create duplicate consequences.

To address this problem, the external-boundary development lineage introduced a persistent request ledger.

The request-ledger evidence suite passed six controlled tests:

- same-request-ID duplicate suppression;
- rejection when the same request ID was reused with changed request content;
- persistence of request state after ledger reopen;
- blocking of automatic retry after an `UNKNOWN` result;
- preservation of a `RESERVED` state after simulated crash conditions;
- concurrent same-request callers resulting in only one dispatch.

The ledger evidence artifact was recorded with SHA-256:

`9d47e3032c391ac1148759f45ca73676324197f851ffefbaa32d9cf1cb0369e8`

The resulting Offline Boundary Candidate 3 was packaged separately from the earlier gate-repair candidate.

Its SHA-256 is:

`37c5b9f810308660bd35ba2d3316bcc938d305a4f04caef76b06dc9a8685d823`

The package contains the external-boundary modules for target, credential, dispatch, and authority behavior together with the persistent request-ledger implementation and its test suite.

This creates another important distinction:

> **DUPLICATE SUPPRESSION ≠ EXACTLY-ONCE EXTERNAL EFFECT**

The controlled evidence shows that the tested runtime can prevent multiple local dispatches for the same governed request identity under the tested duplicate, reopen, crash, unknown-result, and concurrent-caller scenarios.

It does not prove that an external system cannot independently duplicate an effect.

It does not prove distributed exactly-once semantics.

It does not prove transactional atomicity across a remote provider boundary.

It does not prove that an `UNKNOWN` operation did or did not produce an external effect.

That uncertainty is deliberately preserved rather than converted into success or safe-to-retry by assumption.

This is a central MIA principle:

> **When the system does not know, UNKNOWN is a valid state.**

---

[Continue to Part 3](./PART_3_EVIDENCE_AND_CLAIMS.md)
