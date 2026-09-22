# HSIE-WP-002 — Technical Review Pass 2

**Manuscript reviewed:** DRAFT_v0.2.0.md  
**Candidate Publication ID:** HSIE-WP-002  
**Review state:** PASS 2 COMPLETE / TARGETED REVISION REQUIRED  
**Review scope:** structural coherence, category separation, minimum representation envelope, implementation-neutrality, claim ceiling, external-reference accuracy  
**Manuscript mutation:** NONE — v0.2.0 remains preserved

## Overall Disposition

**PASS WITH TARGETED REVISION TO v0.3.0 PUBLICATION CANDIDATE.**

The central thesis survives technical review.

No foundational amendment to TB-SUB-001 is required.

No conflict was identified with the paper's stated boundaries that:

- Entity / Event / Relationship remain foundational;
- representation status is not a new foundational primitive;
- inference does not automatically become accepted state;
- acceptance does not establish objective truth;
- execution does not establish external effect;
- supersession does not erase history.

The remaining changes are structural rather than conceptual.

---

# 1. Conceptual Model — PASS WITH ONE ADDITION

The loop:

**Reality / Current State → Evidence → Record → Interpretation → Governed State → AI Context → Action → Outcome → New Evidence → Calibration → Updated Governed State**

is useful but can be misread as saying all records begin with evidence.

Some records begin as assertions, reports, imported claims, or model-generated candidates that do not yet qualify as evidence for the proposition they contain.

## Required v0.3 change

Represent ingress as:

**Reality / Current State → Observation / Assertion / Evidence → Record → Interpretation → Governed State → AI Context → Action → Outcome → New Evidence → Calibration**

Add:

> A record may enter the system through evidence, direct assertion, imported data, or generated interpretation. Entry into the record system does not determine epistemic status.

This prevents "stored" from silently meaning "evidenced."

---

# 2. Minimum Representation Envelope — PASS WITH AXIS REPAIR

The v0.2 envelope is the correct technical center of the paper.

However, two candidate status lists still combine concepts that should remain orthogonal.

## 2.1 Epistemic status

The current list:

- OBSERVED
- REPORTED
- INFERRED
- VERIFIED
- DISPUTED
- UNRESOLVED

mixes **origin/basis**, **verification result**, and **dispute state**.

A representation can be both REPORTED and VERIFIED.

It can be OBSERVED and DISPUTED.

It can be INFERRED and later VERIFIED relative to a defined claim.

These therefore should not be treated as one mutually exclusive enum.

### Required v0.3 change

Replace a single epistemic status with explicit facets such as:

**representation_basis**
- OBSERVATION
- ASSERTION
- IMPORT
- INFERENCE
- DERIVATION
- SUMMARY

**verification_state**
- NOT_CHECKED
- PARTIALLY_VERIFIED
- VERIFIED_FOR_CLAIM
- FAILED_VERIFICATION
- UNRESOLVED

**dispute_state**
- UNDISPUTED
- DISPUTED
- CONTRADICTED

The exact labels remain candidate, not frozen canon.

The important rule is:

> Representation basis, verification state, and dispute state answer different questions and must not be collapsed.

## 2.2 Governance status

The current list:

- CANDIDATE
- ACCEPTED_FOR_PURPOSE
- REJECTED
- SUPERSEDED

mixes governance disposition with lifecycle/currentness.

A representation may have been ACCEPTED_FOR_PURPOSE and later become SUPERSEDED. Those facts should both remain reconstructable.

### Required v0.3 change

Separate:

**governance_disposition**
- CANDIDATE
- ACCEPTED_FOR_PURPOSE
- REJECTED

from:

**lifecycle_state**
- CURRENT
- SUPERSEDED
- RETIRED, if a system needs such a state

Again, labels are candidate.

Add:

> Governance disposition ≠ lifecycle state.

---

# 3. Verification — PASS WITH CLAIM-SCOPE RULE

The v0.2 sentence that VERIFIED applies relative to an identified method and claim is correct.

## Required v0.3 strengthening

Add a non-expansion invariant:

> Verification of claim C under method M does not verify broader claim C+ unless separately established.

This prevents a narrow verification result from being promoted into a broader claim.

Example:

A receipt may verify that a request was accepted by an API.

It does not thereby verify that the intended downstream real-world effect occurred.

---

# 4. Promotion — PASS WITH IDENTITY RULE

Promotion as a recorded Event is architecturally sound and consistent with the stated substrate.

## Required v0.3 strengthening

Add:

> Promotion changes the representation's governed treatment; it does not change the identity of the underlying representation and does not erase its prior status history.

If a promoted representation is materially transformed rather than merely reclassified, the implementation should preserve lineage to the earlier representation.

---

# 5. Supersession — PASS

The distinction is technically strong:

**supersession changes current use without deleting historical existence.**

No structural correction required.

Add one sentence:

> Supersession is purpose-scoped where necessary; a representation may be superseded for one use while remaining historically relevant for another.

---

# 6. Authority and Consent — PASS

The v0.2 correction that authority comes from a governing source recognized by the architecture is materially better than the v0.1 wording.

No new blocker.

Preserve:

**AUTHENTICATION ≠ AUTHORITY**

Add the parallel statement:

**RECORD OF CONSENT ≠ CONSENT OUTSIDE ITS RECORDED SCOPE / TIME**

This should be explanatory language, not a new foundational primitive.

---

# 7. Memory — PASS

The provenance treatment is adequate for the scope of this paper.

Add one explicit rule:

> A memory retrieval should preserve or make recoverable the provenance category of the retrieved representation rather than presenting all retrieved content as equivalent fact.

No need to prescribe a specific database or memory implementation.

---

# 8. Human Representation — PASS

The section correctly avoids reducing the human to a profile or record.

No diagnosis or behavioral scoring claim is required.

Preserve:

**HUMAN REALITY ≠ HUMAN RECORD ≠ AI INTERPRETATION**

Add:

> A governed human model is still a representation and remains downstream of the human.

This makes the hierarchy explicit.

---

# 9. Relationship to MIA — REVISE TO PUBLICLY TRACEABLE CLAIM

The sentence:

> MIA's runtime contract operationalizes selected parts of this discipline...

is plausible within the architecture, but the public paper should point readers to the already-released MIA white paper rather than ask them to accept an unsupported cross-system claim.

## Required v0.3 change

Use:

> HSIE-WP-001 describes how MIA applies related distinctions at runtime, including inference versus accepted state, execution versus verified effect, governed commit, receipts, replay, and preserved uncertainty. WP-002 generalizes the representation problem beyond runtime execution.

Add HSIE-WP-001 to the references.

This creates a public trace from WP-002 back to the already-published MIA paper.

---

# 10. External Technical Guidance — VERIFIED

External reference claims were checked against primary sources.

## W3C PROV

W3C records PROV-DM as a Recommendation dated **30 April 2013**.

PROV-DM describes provenance in terms of entities, activities, agents, derivations, responsibility/attribution, and time.

The paper's use remains appropriately bounded as adjacent technical precedent rather than a conformance claim.

## NIST AI RMF 1.0

NIST AI 100-1 was published **January 26, 2023**.

NIST describes it as voluntary, rights-preserving, non-sector-specific, and use-case agnostic.

Its Core contains the four functions:

**GOVERN, MAP, MEASURE, MANAGE**

NIST currently states that AI RMF 1.0 is being revised.

The final paper should cite the 2023 publication as AI RMF 1.0 and separately note the current revision status as of the publication review date.

## NIST AI 600-1

NIST AI 600-1 was published **July 26, 2024** as the Generative AI Profile companion to AI RMF 1.0.

Its content-provenance section discusses provenance tracking as recording the origin and history of digital content, including input data, metadata, and synthetic content.

The draft's characterization is supportable.

---

# 11. Normative Language — PASS WITH CONSISTENCY EDIT

Because WP-002 is an architecture paper rather than a frozen conformance standard:

- use **should** for candidate implementation guidance;
- use **must not** only for principles the paper explicitly defines as doctrine;
- avoid "conforming implementation" language;
- keep the Minimum Representation Envelope explicitly candidate/reference architecture.

No need to weaken the central doctrine:

> Reality ≠ Representation.

---

# 12. Claim Ceiling — PASS

The positive claim is appropriately bounded.

The paper does not claim:

- perfect access to objective reality;
- elimination of uncertainty;
- independent validation;
- universal implementation;
- production deployment;
- certification;
- formal W3C or NIST conformance;
- a frozen representation schema.

No additional disclaimer is required beyond the publication-state note.

---

# 13. Required Changes Before v0.3.0

v0.3.0 should incorporate all of the following:

1. permit assertion/import/generated representation ingress before evidence qualification;
2. split representation basis from verification state and dispute state;
3. split governance disposition from lifecycle/currentness;
4. add claim-scoped verification non-expansion;
5. preserve representation identity/history through promotion;
6. make supersession purpose-scoped where needed;
7. add scoped-consent representation warning;
8. add provenance-category preservation on memory retrieval;
9. state explicitly that governed human models remain representations;
10. cross-reference HSIE-WP-001 for publicly traceable MIA relationship;
11. normalize references and add external-reference review date;
12. retain the Minimum Representation Envelope as candidate/reference architecture rather than frozen standard.

---

# Pass 2 Gate Result

**TECHNICAL REVIEW PASS 2: PASS WITH TARGETED REVISION**

Authorized next manuscript state:

**HSIE-WP-002 v0.3.0 — PUBLICATION CANDIDATE**

After v0.3.0 is created:

1. perform dedicated Claim Review;
2. perform final reference/bibliography review;
3. perform final publication consistency review;
4. resolve any remaining blockers;
5. if all gates pass and owner authorization is issued, promote to HSIE-WP-002 v1.0.0.
