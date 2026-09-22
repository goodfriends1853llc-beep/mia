# HSIE-WP-002 — Technical Review Pass 1

**Manuscript:** Reality ≠ Representation  
**Draft reviewed:** v0.1.0  
**Review state:** PASS 1 COMPLETE / REVISION REQUIRED  
**Review scope:** truth/technical precision, architectural necessity, claim ceiling, canon compatibility  
**Manuscript mutation:** NONE — v0.1.0 remains unchanged by this review

## Overall Disposition

**HOLD FOR v0.2.0 REVISION.**

No critical contradiction with the stated TB-SUB/MIA/HSIE boundaries is identified in this pass.

The draft has a defensible central thesis, but it currently reads partly as an epistemic essay and only partly as a systems-architecture paper. Before promotion to v0.2.0, it needs a more explicit operational definition of "reality," a stronger representation-state mechanism, cleaner separation between evidence and authority, and several wording corrections that remove avoidable absolutes.

The largest architectural gap is Section 11. The paper says systems must preserve distinctions, but it does not yet specify enough of the minimum representation envelope and promotion/supersession rules that make the doctrine implementable.

---

## Abstract

**Truth/precision:** REVISE  
**Architectural necessity:** PASS  
**Claim ceiling:** REVISE

### Finding

The sentence "Artificial intelligence systems do not operate directly on reality" is too absolute. AI systems with sensors and actuators can interact with the physical world, even though their perception and internal state are mediated through interfaces and representations.

### Required revision

Replace the absolute with an operational statement such as:

> AI systems do not have unmediated access to the world they describe or affect. They perceive, reason, remember, and govern action through observations, interfaces, records, and internal representations.

Add an explicit paper-level definition:

> In this paper, "reality" means the external, physical, organizational, or human state a system is attempting to describe, reason about, or affect. The term is operational, not a claim that software can obtain philosophically complete access to objective reality.

The central thesis passes and should remain.

---

## 1. The Problem

**Truth/precision:** REVISE  
**Architectural necessity:** PASS  
**Claim ceiling:** PASS after wording correction

### Findings

"Every digital system works through representation" is directionally sound but unnecessarily absolute.

"A camera stores an image" and "A sensor stores a measurement" are not universally true; devices may stream or produce data without storage.

"A model stores parameters rather than the lived reality represented in its training data" is technically imprecise. Model parameters encode learned statistical structure; they should not be described as simply "storing" the lived reality of training data.

"An AI assistant stores context" is also not universally true because context may be transient.

### Required revision

Use:

> Digital systems operate on encoded representations of internal or external state.

Use "produces or captures image data," "produces measurements," and:

> A trained model encodes learned statistical structure in parameters rather than containing the world from which its training data was produced.

For assistants:

> An AI assistant operates on a context representation rather than on the person or situation itself.

---

## 2. The Core Principle

**Truth/precision:** PASS WITH DEFINITION  
**Architectural necessity:** PASS  
**Claim ceiling:** PASS

### Finding

The principle is strong, but "Reality" must have the operational definition added in the Abstract/early introduction. Without it, the paper risks being read as making a metaphysical claim rather than a systems distinction.

### Required revision

Keep the examples.

Consider changing:

> A model confidence score is not truth.

to:

> A model confidence score is not, by itself, proof that the represented claim is true.

This is more technically bounded.

---

## 3. Representation Layers

**Truth/precision:** PASS WITH STRUCTURAL IMPROVEMENT  
**Architectural necessity:** PASS — CORE SECTION  
**Claim ceiling:** PASS

### Finding

The chain is useful:

Reality → Evidence → Record → Interpretation → Governed State → AI Context → Action → Outcome → Calibration

However, it currently reads as a one-way pipeline. Action and outcome create new conditions and new evidence.

### Required revision

Render it as a feedback loop:

> Reality / Current State → Evidence → Record → Interpretation → Governed State → AI Context → Action → Outcome → New Evidence → Calibration → Updated Governed State

Preserve the existing chain where it is canonical for human-model work, but explain that it is a conceptual ordering rather than a claim that every implementation has exactly these objects.

Add:

> "Governed State" means state accepted under defined governance rules; acceptance does not convert a representation into objective reality.

---

## 4. Evidence Does Not Eliminate Interpretation

**Truth/precision:** REVISE  
**Architectural necessity:** PASS  
**Claim ceiling:** PASS after revision

### Findings

"Evidence is stronger than unsupported assertion" is too categorical because evidence varies in relevance, reliability, provenance, and quality.

The bullet "what authority, if any, the evidence supports" risks implying that evidence creates authority.

The W3C PROV comparison is technically defensible, provided the paper keeps the non-conformance disclaimer.

### Required revision

Replace the opening with:

> Evidence can support a claim, but the strength of that support depends on provenance, relevance, reliability, scope, and the inference connecting the evidence to the claim.

Replace the authority bullet with:

> what authority claim, consent claim, or permission state the evidence documents, if any;

Do not imply that evidence itself creates authority.

---

## 5. Inference Is Not Accepted State

**Truth/precision:** REVISE  
**Architectural necessity:** PASS — CORE SECTION  
**Claim ceiling:** REVISE

### Finding

"Human acceptance may promote some inferences" needs a harder boundary. Human acceptance can govern a representation's status, but it does not make the inference objectively true.

### Required revision

Use:

> Human acceptance may authorize a candidate interpretation to enter governed state for a defined purpose, without converting that interpretation into objective fact.

Replace "Independent evidence may strengthen others" with "Additional evidence may strengthen, weaken, or contradict an inference" unless independence is actually established.

Add an explicit promotion event:

> Promotion should record the prior status, new status, accepting authority, purpose, time, evidence basis, and any remaining uncertainty.

This is an important bridge to TB-SUB Event semantics.

---

## 6. Human Reality Must Not Collapse Into a Profile

**Truth/precision:** PASS WITH LANGUAGE HARDENING  
**Architectural necessity:** PASS  
**Claim ceiling:** PASS

### Findings

The core distinction is sound.

"A diagnosis" is too broad and can read as dismissing legitimate clinical assessment. "Diagnostic label or clinical record" is more precise.

"Old data becomes a permanent sentence" is rhetorically effective but weaker technically.

### Required revision

Use:

> a diagnostic label or clinical record;

and:

> This prevents historical data from being silently treated as permanently current.

Retain:

> Human Reality ≠ Human Record ≠ AI Interpretation

as an explicit sub-principle.

---

## 7. Time Is Part of Meaning

**Truth/precision:** PASS  
**Architectural necessity:** PASS — REQUIRED  
**Claim ceiling:** PASS

### Finding

This section is structurally necessary and one of the strongest sections.

### Required revision

Add explicit temporal fields to the later architecture section:

- observed_at;
- recorded_at;
- valid_from;
- valid_until, where applicable;
- superseded_at;
- verified_at, where applicable.

Clarify that a correction may supersede a record for current use while preserving historical existence and prior effects.

---

## 8. Representation Does Not Create Authority

**Truth/precision:** REVISE ONE SENTENCE  
**Architectural necessity:** PASS — REQUIRED  
**Claim ceiling:** PASS

### Finding

"Authority must come from the governing source defined by the system" gives the system too much sovereignty. A system may recognize authority established by a person, institution, law, contract, role, or other external governance source.

### Required revision

Use:

> Authority must come from a governing source recognized by the architecture; the representation records or evaluates that authority but does not create it merely by existing.

Keep the consent distinctions.

Add:

> AUTHENTICATION ≠ AUTHORITY

as a linked distinction.

---

## 9. Execution Records Are Not External Reality

**Truth/precision:** PASS WITH GENERALIZATION  
**Architectural necessity:** PASS  
**Claim ceiling:** PASS

### Finding

This section is technically aligned with the MIA effect distinction. Because WP-002 is broader than MIA, "effect contract required by the operation" should not sound as though every external system already implements MIA's contract.

### Required revision

Use:

> Where a claim depends on an external effect, the system should require evidence appropriate to the operation's verification standard or effect contract.

Replace:

> UNKNOWN is preferable to invented certainty.

with:

> An explicit UNKNOWN state is preferable to falsely asserting success or failure when the external outcome has not been established.

---

## 10. Memory Requires Provenance

**Truth/precision:** PASS  
**Architectural necessity:** PASS — REQUIRED  
**Claim ceiling:** PASS

### Finding

Strong section.

### Required revision

Add one sentence:

> Source attribution does not establish truth; it establishes where a representation came from.

Add "model-generated summary" as a distinct provenance type.

Keep reconstructability over narrative cleanliness.

---

## 11. Architectural Requirements

**Truth/precision:** REVISE  
**Architectural necessity:** PASS — THIS MUST BECOME THE TECHNICAL CENTER OF THE PAPER  
**Claim ceiling:** REVISE

### Critical finding

"A conforming architecture" implies a formal conformance standard that this paper has not defined.

The section is currently too short for a paper whose subtitle promises "A Systems Architecture."

### Required revision

Replace "A conforming architecture" with:

> An architecture applying this principle should be able to preserve...

Expand this section into a **Minimum Representation Envelope**. The paper should specify candidate fields or capabilities without turning them into new TB-SUB primitives.

Recommended minimum envelope:

- representation_id;
- represented_entity_or_event_ref;
- source_ref;
- source_type;
- provenance_chain;
- created_at;
- observed_at, where applicable;
- valid_from / valid_until, where applicable;
- epistemic_status;
- governance_status;
- authority_scope, if relevant;
- purpose_scope;
- uncertainty;
- evidence_refs;
- transformation_history;
- supersedes / superseded_by;
- accepted_by and acceptance_event, if promoted;
- verification_state;
- contradiction_or_dispute_refs.

Separate at least two axes:

**Epistemic status:** observed / reported / inferred / verified / disputed / unresolved.

**Governance status:** candidate / accepted-for-purpose / superseded / rejected.

Do not collapse "accepted" and "verified." They answer different questions.

Add promotion rules:

> A representation may change governance status only through a recorded Event with identity, authority, time, purpose, evidence basis, and prior/new state.

Add supersession rule:

> Supersession changes which representation is current for a defined purpose; it does not delete historical existence.

This expansion is the single most important change required for v0.2.0.

---

## 12. Relationship to TB-SUB, MIA, and HSIE

**Truth/precision:** PASS WITH CLAIM HARDENING  
**Architectural necessity:** PASS  
**Claim ceiling:** REVISE

### Finding

The relationship is coherent, but "HSIE applies the same discipline" can sound like a completed implementation claim.

### Required revision

Use:

> Within the HSIE architecture, this discipline is intended to apply across governed intelligence environments.

Use:

> MIA's runtime contract operationalizes selected parts of this discipline through identity, evidence, authority, effect verification, commit, receipts, replay, and preserved failure state.

If implementation evidence is cited, identify which parts have actually been tested rather than implying all doctrine is implemented.

---

## 13. Relationship to Existing Technical Guidance

**Truth/precision:** PASS WITH CURRENTNESS NOTE  
**Architectural necessity:** PASS  
**Claim ceiling:** PASS

### External verification

W3C lists PROV-DM as a Recommendation dated 30 April 2013 and describes it as a core provenance model involving entities, activities, agents, derivation, and time.

NIST AI RMF 1.0 is a voluntary framework whose Core is organized around GOVERN, MAP, MEASURE, and MANAGE, with risk management intended to operate throughout the AI lifecycle.

NIST AI 600-1 discusses provenance data tracking as recording the origin and history of digital content, data inputs, metadata, and synthetic content.

### Required revision

Add publication-grade citations.

Because NIST states AI RMF 1.0 is currently being revised, the final paper should cite AI RMF 1.0 as the 2023 published framework and note the review date rather than implying that 1.0 is the final permanent version.

Avoid saying these frameworks "prove" the doctrine. "Adjacent technical precedent" is the correct framing.

---

## 14. Failure Modes

**Truth/precision:** REVISE ONE ITEM  
**Architectural necessity:** PASS  
**Claim ceiling:** PASS

### Finding

"Treat missing evidence as evidence of absence" is directionally useful but too absolute. In some well-designed observation systems, absence of an expected record can itself be informative.

### Required revision

Use:

> treat absence of recorded evidence as proof of non-occurrence without a justified observation model.

Consider grouping failure modes under:

- epistemic promotion failure;
- temporal failure;
- authority failure;
- provenance failure;
- effect-verification failure;
- history/supersession failure.

That will strengthen the architecture.

---

## 15. Claim Boundary

**Truth/precision:** PASS WITH WORDING HARDENING  
**Architectural necessity:** PASS — REQUIRED  
**Claim ceiling:** PASS

### Finding

The boundary is good.

The final positive claim should be more operational and should not imply that a system can directly compare its representations against metaphysical reality.

### Required revision

Use:

> Consequential AI systems can be designed to preserve explicit distinctions between external or human state and internal representations; track representation provenance and transformation; govern promotion into accepted state; and preserve uncertainty when stronger verification is unavailable.

Keep all negative claim statements.

---

## 16. Conclusion

**Truth/precision:** REVISE RHETORIC  
**Architectural necessity:** PASS  
**Claim ceiling:** PASS after revision

### Findings

"Artificial intelligence will increasingly operate..." is predictive and unnecessary.

"The deeper danger is that systems may forget what kind of thing an answer is" anthropomorphizes the system.

"An inference can become truth simply because it survived long enough in memory" is vivid but should be framed as a representation-management failure rather than literal truth creation.

### Required revision

Use:

> AI systems increasingly operate through records about people, organizations, software systems, and the physical world.

Use:

> The deeper systems risk is loss of representation status: an inference, summary, or historical record may later be consumed as though it were current verified fact.

The closing paragraph should remain. It is the correct conceptual endpoint.

---

# Evidence Status Note

**Disposition:** PASS

No change required other than adding:

> DRAFT REVIEW STATUS: TECHNICAL REVIEW PASS 1 COMPLETE / REVISION REQUIRED

Do not change publication authorization.

---

# External References

**Disposition:** PASS WITH BIBLIOGRAPHIC NORMALIZATION

Before v1.0.0:

1. Normalize W3C citation to the W3C Recommendation dated 30 April 2013.
2. Preserve NIST AI 100-1 DOI: 10.6028/NIST.AI.100-1.
3. Preserve NIST AI 600-1 DOI: 10.6028/NIST.AI.600-1.
4. Add access/review date only if the publication format requires it.
5. Do not claim conformance, certification, or endorsement.

---

# Pass 1 Promotion Gate

The manuscript should **not** move directly from v0.1.0 to release.

Recommended next state:

**HSIE-WP-002 v0.2.0 — TECHNICAL REVIEW CANDIDATE**

Promotion to v0.2.0 requires:

1. operational definition of "reality";
2. removal of absolute claims about AI/digital systems;
3. correction of model/camera/sensor/context language;
4. separation of evidence from authority;
5. explicit rule that human acceptance changes governance status, not objective truth;
6. expanded Minimum Representation Envelope;
7. explicit epistemic-status vs governance-status separation;
8. promotion and supersession Event rules;
9. feedback-loop treatment of outcome/new evidence/calibration;
10. normalized external citations and currentness note.

After those changes, perform:

**Technical Review Pass 2 → Claim Review → v0.3.0 publication candidate.**
