# HSIE-WP-002 — TECHNICAL REVIEW CANDIDATE

# Reality ≠ Representation

## A Systems Architecture for Keeping AI Records, Inferences, and Governed State Separate from the World They Describe

**Author:** Tommie Bellamy  
**Author Identity:** Human Systems Architect™  
**Candidate Publication ID:** HSIE-WP-002  
**Draft Version:** v0.2.0  
**Document State:** TECHNICAL REVIEW CANDIDATE  
**Publication State:** NOT PUBLISHED  
**Foundation:** TB-SUB-001 v1.0.0  
**Foundational Amendment:** NONE  
**Relationship to MIA:** Compatible architectural doctrine; not a MIA runtime release  
**Relationship to HSIE:** Cross-system epistemic discipline  
**Technical Review Pass 1:** COMPLETE  
**Claim Review:** OPEN  
**Owner Publication Authorization:** NOT ISSUED

---

## Abstract

AI systems do not have unmediated access to the world they describe or affect. They perceive, reason, remember, and govern action through observations, interfaces, records, measurements, retrieved information, sensor outputs, model outputs, summaries, labels, profiles, and other internal or external representations.

In this paper, **reality** means the external, physical, organizational, or human state that a system is attempting to describe, reason about, or affect. The term is operational. It is not a claim that software can obtain philosophically complete or perfect access to objective reality.

That distinction is easy to state and easy to violate.

When a system collapses a representation into the thing represented, stale records can be consumed as current state, model inference can be promoted as accepted fact, generated summaries can become authoritative memory, reported intention can become assumed consent, and an execution record can be treated as false proof that an external effect occurred.

This paper develops **Reality ≠ Representation** as a systems-architecture discipline for consequential AI. The principle requires AI environments to preserve explicit distinctions between the world, evidence about the world, records derived from evidence or assertion, interpretations generated from records, governed state accepted under defined authority and purpose, AI context constructed for a task, actions taken, outcomes observed, and later evidence that may confirm, contradict, or supersede earlier representations.

The paper argues that consequential AI systems should preserve provenance, time, identity, purpose, authority, scope, uncertainty, evidence relationships, transformation history, promotion history, supersession history, and verification state around representations.

It further argues that human beings must not be reduced to stored profiles and that current governed state must not silently rewrite historical state.

The result is not a claim that software can directly possess reality.

It is a narrower architectural requirement:

> **A system should know when it is holding a representation, preserve how that representation was produced, and refuse to promote it beyond the evidence, authority, scope, and verification that support it.**

---

# 1. The Problem

Digital systems operate on encoded representations of internal or external state.

A database contains records rather than the physical or human reality those records describe.

A camera produces or captures image data rather than the scene itself.

A sensor produces measurements rather than the phenomenon measured.

A transcript stores words rather than the complete human interaction.

A trained model encodes learned statistical structure in parameters rather than containing the world from which its training data was produced.

An AI assistant operates on a context representation rather than on the person or situation itself.

These distinctions are not merely philosophical.

They become operationally important when representations are used to make decisions, allocate authority, trigger actions, update memory, generate AI context, or alter governed state.

A representation may be incomplete.

It may be stale.

It may be wrong.

It may be accurate only within a narrow scope.

It may have weak provenance.

It may describe a past condition that no longer exists.

It may be an inference rather than an observation.

It may have been generated or transformed by another AI system.

It may have been superseded by later evidence.

It may be a faithful description and still carry no authority.

The architecture must therefore preserve distinctions between:

**what exists;**

**what was observed;**

**what was reported;**

**what was recorded;**

**what was inferred;**

**what was accepted for a defined purpose;**

**what was verified;**

and **what later evidence changed.**

---

# 2. The Core Principle

The governing statement is:

> **REALITY ≠ REPRESENTATION**

Representations are necessary.

Without representations, software cannot reason about or act on external conditions.

The requirement is not to eliminate representation.

The requirement is to prevent a representation from silently becoming equivalent to the thing represented.

A person's profile is not the person.

A preference record is not a permanent preference.

A clinical record is not the entirety of a person's condition.

A financial record is not identical to economic reality.

A governance policy is not enforcement.

A model confidence score is not, by itself, proof that the represented claim is true.

A returned API response is not necessarily verified external effect.

A generated answer is not automatically accepted governed state.

This distinction should remain visible throughout the system lifecycle.

---

# 3. Representation Layers

A consequential AI environment may contain several layers that should remain separable.

A useful conceptual loop is:

**Reality / Current State → Evidence → Record → Interpretation → Governed State → AI Context → Action → Outcome → New Evidence → Calibration → Updated Governed State**

These terms are conceptual categories. They do not require every implementation to create an object with exactly these names.

**Reality / Current State** is the external, physical, organizational, or human condition the system is attempting to describe, reason about, or affect.

**Evidence** is material that supports or challenges a claim about that state: direct observation, a document, a measurement, a sensor reading, testimony, a transaction record, or another trace.

**Record** is a stored representation derived from evidence, assertion, or prior system state.

**Interpretation** is a conclusion, classification, summary, prediction, inference, or model-generated explanation based on one or more records.

**Governed State** is a representation accepted under defined governance rules, authority, purpose, and scope. Acceptance changes its governance status. It does not transform the representation into objective reality.

**AI Context** is the subset of governed or candidate representations supplied to an AI capability for a particular task.

**Action** is what an authorized human or machine attempts or performs.

**Outcome** is what subsequently occurs or is observed.

**New Evidence** is the evidence generated or discovered after action or passage of time.

**Calibration** is the process of comparing earlier representations, interpretations, or expectations against later evidence and outcomes.

These layers may interact.

They should not silently collapse into one another.

---

# 4. Evidence Does Not Eliminate Interpretation

Evidence can support a claim, but the strength of that support depends on provenance, relevance, reliability, scope, and the inference connecting the evidence to the claim.

A photograph may show an object while leaving its context unclear.

A sensor reading may be accurate while the sensor is poorly positioned for the question being asked.

A transaction may establish that money moved without establishing why it moved.

A message may establish that words were sent without establishing motive.

A database record may establish what a system stored without establishing that the stored value was correct.

For this reason, evidence should carry provenance and scope.

A governed system should be able to preserve, where relevant:

- what the evidence object is;
- who or what produced it;
- when it was produced;
- what entity, event, or relationship it concerns;
- what transformation produced the current representation;
- what uncertainty remains;
- what authority claim, consent claim, or permission state the evidence documents, if any;
- what purpose and scope the evidence is being used for;
- whether later evidence strengthens, weakens, supersedes, or contradicts it.

Evidence may document authority.

Evidence does not create authority merely by existing.

W3C PROV provides an established technical precedent for representing provenance through entities, activities, agents, derivation, attribution, and time. HSIE does not claim conformance with W3C PROV, and TB-SUB-001 retains its own Entity/Event/Relationship foundation. The adjacent technical problem is shared: representations are more assessable when origin, transformation, and attribution remain reconstructable.

---

# 5. Inference Is Not Accepted State

Modern AI systems are powerful inference engines.

They can infer preferences, intentions, categories, risks, likely outcomes, emotional tone, similarity, priority, and relationships from incomplete information.

That capability can be useful.

It becomes dangerous when inference is silently promoted into authoritative state.

Consider the difference between:

**“The model inferred that the user prefers X.”**

and:

**“The user prefers X.”**

The second sentence carries stronger epistemic force.

It should not be created merely because the first sentence exists.

The same applies to summaries.

An AI-generated summary may be useful as a working representation of a longer record.

It does not automatically replace the source material.

It should not erase disagreement, uncertainty, provenance, or omitted detail.

A governed system therefore needs explicit promotion rules.

Inference may remain candidate context.

Human acceptance may authorize a candidate interpretation to enter governed state for a defined purpose without converting that interpretation into objective fact.

Additional evidence may strengthen, weaken, or contradict an inference.

Later evidence may supersede an earlier interpretation for current use.

Promotion should be a recorded **Event**, not an invisible side effect of model generation.

A promotion event should preserve at least:

- the prior status;
- the new status;
- the accepting identity;
- the authority basis;
- the purpose and scope;
- the time;
- the evidence basis;
- and any remaining uncertainty.

---

# 6. Human Reality Must Not Collapse Into a Profile

The Reality ≠ Representation principle becomes especially important when systems model people.

A person is not reducible to:

a profile;

a memory summary;

a risk score;

a preference vector;

a diagnostic label or clinical record;

a recommendation history;

a behavioral label;

a set of embeddings;

or a longitudinal record.

These representations may support useful assistance.

They do not become the human being.

Human reality remains upstream.

A human-centered architecture should preserve a chain such as:

**Human Reality → Evidence → Human Record → Governed Human Model → AI Context → Assistance → Action → Outcome → Calibration**

The human remains distinct from every downstream representation.

This prevents historical data from being silently treated as permanently current.

A person can change.

A preference can change.

Authority can change.

Consent can change.

Relationships can change.

Context can change.

The architecture must allow current governed state to update without rewriting historical state.

A useful sub-principle is:

> **HUMAN REALITY ≠ HUMAN RECORD ≠ AI INTERPRETATION**

---

# 7. Time Is Part of Meaning

A representation without temporal context can become misleading even when it was once correct.

“Authorized” may be true at one moment and false later.

“Lives at this address” may be true during one period and false during another.

“Prefers this workflow” may be current, historical, or unknown.

“Credential valid” may depend on expiration and revocation.

“Consent granted” may be scoped to a task and period.

Time is therefore not merely decorative metadata.

It can change the meaning and validity of a representation.

Where applicable, an architecture should be able to distinguish:

- `created_at`;
- `observed_at`;
- `recorded_at`;
- `valid_from`;
- `valid_until`;
- `verified_at`;
- `superseded_at`.

The architecture should distinguish:

**valid then** from **valid now**;

**known then** from **known now**;

**recorded then** from **verified now**.

A later correction may supersede an earlier representation for current use while preserving the fact that the earlier representation existed and may have influenced prior decisions.

---

# 8. Representation Does Not Create Authority

A representation can describe authority without creating authority.

A database field may say `AUTHORIZED = TRUE`.

A model may predict that a person would probably approve.

A historical record may show that similar actions were approved before.

None of those facts necessarily creates present authority.

Authority must come from a governing source recognized by the architecture: for example, an authorized person, institutional role, contract, policy, law, delegation, or other valid source.

The representation records, evaluates, or carries evidence about that authority.

It does not create authority merely by existing.

The same rule applies to consent.

Past consent is not automatically current consent.

Consent for one purpose is not automatically consent for another purpose.

A stored representation of consent should therefore preserve the subject, scope, purpose, time, authority basis, and revocation state that give it meaning.

This produces another useful distinction:

> **AUTHENTICATION ≠ AUTHORITY**

Authentication may establish who or what is presenting a credential.

It does not, by itself, establish what that identity is allowed to do.

---

# 9. Execution Records Are Not External Reality

Reality ≠ Representation also applies to machine action.

An execution record may establish that software attempted an operation.

It may establish that a tool returned a result.

It may establish that a provider accepted a request.

Those facts do not necessarily establish that the intended external effect occurred.

For consequential systems:

> **EXECUTION ≠ EFFECT**

and:

> **RETURNED OUTPUT ≠ VERIFIED EXTERNAL CONSEQUENCE**

The execution trace is a representation of what the runtime observed.

Where a claim depends on an external effect, the system should require evidence appropriate to the operation's verification standard or effect contract.

When verification is unavailable, uncertainty should remain explicit.

An explicit `UNKNOWN` state is preferable to falsely asserting success or failure when the external outcome has not been established.

---

# 10. Memory Requires Provenance

AI memory creates a second-order representation problem.

A system may remember not only direct records but also prior summaries, inferences, corrections, imported data, and model-generated descriptions.

If memory flattens these categories, interpretation can later be consumed as though it were direct fact.

A robust memory system should therefore retain provenance.

It should be possible to distinguish:

- a statement directly supplied by the subject;
- a third-party report;
- an imported record;
- a model inference;
- a model-generated summary;
- a human-accepted conclusion;
- a correction;
- a superseded representation;
- a disputed representation;
- an unresolved contradiction.

Source attribution does not establish truth.

It establishes where a representation came from.

Memory should preserve continuity without pretending continuity means certainty.

Reconstructability is more valuable than a clean but misleading single story.

---

# 11. Minimum Representation Envelope

Reality ≠ Representation becomes useful only if the distinction can survive implementation.

An architecture applying this principle should be able to preserve enough information to identify a representation, connect it to what it represents, reconstruct how it was produced, distinguish epistemic state from governance state, and determine whether later evidence changed its standing.

The fields below are a **candidate minimum representation envelope**.

They are not new TB-SUB foundational primitives.

Implementations may encode them differently.

### 11.1 Identity

- `representation_id`
- `represented_entity_ref`, `represented_event_ref`, or equivalent
- `source_ref`
- `source_type`

The representation itself must have an identity distinct from the entity or event it represents.

### 11.2 Provenance

- `provenance_chain`
- `transformation_history`
- `evidence_refs`
- `generated_by` or equivalent producer identity

A representation should preserve how it was created, transformed, summarized, imported, or inferred.

### 11.3 Time

- `created_at`
- `observed_at`, where applicable
- `recorded_at`
- `valid_from`, where applicable
- `valid_until`, where applicable
- `verified_at`, where applicable
- `superseded_at`, where applicable

### 11.4 Epistemic Status

Epistemic status describes what kind of knowledge claim the representation currently supports.

Candidate states may include:

- `OBSERVED`
- `REPORTED`
- `INFERRED`
- `VERIFIED`
- `DISPUTED`
- `UNRESOLVED`

These states are not equivalent.

`VERIFIED` should only be used relative to an identified verification method and claim.

### 11.5 Governance Status

Governance status describes how the system is allowed to use the representation.

Candidate states may include:

- `CANDIDATE`
- `ACCEPTED_FOR_PURPOSE`
- `REJECTED`
- `SUPERSEDED`

**Epistemic status ≠ Governance status.**

A representation may be accepted for a defined operational purpose without being independently verified as objective fact.

A representation may also be well-evidenced yet remain unauthorized for a particular use.

### 11.6 Scope and Purpose

- `purpose_scope`
- `authority_scope`, where relevant
- `subject_scope`
- `use_constraints`

A representation accepted for one purpose should not silently gain authority for another purpose.

### 11.7 Uncertainty

- `uncertainty_state`
- `confidence_basis`, where meaningful
- `unknowns`
- `contradiction_refs`
- `dispute_refs`

Uncertainty should be preserved rather than converted into certainty for convenience.

### 11.8 Promotion

A change in governance status should occur through a recorded Event.

A promotion event should preserve:

- prior governance status;
- new governance status;
- accepting identity;
- authority basis;
- purpose;
- scope;
- time;
- evidence basis;
- remaining uncertainty.

Promotion changes system treatment.

It does not make the representation equivalent to reality.

### 11.9 Supersession

A representation may be superseded when later evidence or authority changes which representation should be treated as current for a defined purpose.

Supersession should preserve:

- `supersedes`;
- `superseded_by`;
- supersession time;
- supersession reason;
- evidence or authority basis.

Supersession changes current use.

It does not delete historical existence.

### 11.10 Verification

Verification should preserve:

- what claim was verified;
- what method was used;
- who or what performed verification;
- when verification occurred;
- what evidence supported the result;
- what uncertainty remains.

A verification result should not silently expand beyond the claim actually tested.

---

# 12. Relationship to TB-SUB, MIA, and HSIE

TB-SUB-001 v1.0.0 remains the foundational substrate.

Its primitives remain:

**Entity**

**Event**

**Relationship**

Reality ≠ Representation does not amend that foundation.

Instead, it governs how representations built from or associated with those structures should be interpreted, promoted, superseded, and used.

MIA's runtime contract operationalizes selected parts of this discipline through identity, evidence, authority, effect verification, commit, receipts, replay, and preserved failure state.

Within the broader HSIE architecture, this discipline is intended to apply across governed intelligence environments.

The principle is therefore cross-cutting.

It is not owned by one model, provider, application, or runtime.

---

# 13. Relationship to Existing Technical Guidance

The principle has adjacent precedent in established technical work.

The W3C PROV family treats provenance as information about entities, activities, agents, derivation, attribution, and time. Its purpose includes enabling assessments of origin, responsibility, and transformation history.

NIST AI RMF 1.0 is a voluntary framework for managing AI risk across the lifecycle. Its Core is organized around GOVERN, MAP, MEASURE, and MANAGE.

NIST AI 600-1, the Generative AI Profile, includes guidance related to content provenance and provenance tracking, including the origin and history of digital content, data inputs, metadata, and synthetic content.

These frameworks do not establish the Reality ≠ Representation doctrine described here.

This paper does not claim conformance, certification, equivalence, or endorsement.

They provide adjacent technical precedent for treating provenance, context, documentation, responsibility, and lifecycle traceability as substantive systems concerns rather than decorative metadata.

For publication purposes, AI RMF 1.0 should be cited as the published 2023 framework. NIST has stated that AI RMF 1.0 is undergoing revision; this paper does not speculate about the contents or final state of a future revision.

---

# 14. Failure Modes

Systems violate Reality ≠ Representation when they promote a representation beyond what its evidence, authority, time, purpose, scope, or verification supports.

These failures can be grouped into several classes.

## 14.1 Epistemic Promotion Failure

- treating inference as fact;
- treating a model-generated summary as equivalent to its source;
- treating a confidence score as proof;
- treating unresolved information as verified.

## 14.2 Human-Model Failure

- treating a stored profile as the person;
- treating historical data as permanently current;
- treating a diagnostic label, risk score, or preference vector as a complete human description.

## 14.3 Temporal Failure

- treating old consent as current consent;
- treating past authority as present authority;
- treating current state as if it had always been true.

## 14.4 Authority Failure

- treating authentication as authority;
- treating a stored authorization flag as the source of authority;
- treating evidence of past approval as permission for a new purpose.

## 14.5 Provenance Failure

- losing source identity;
- losing transformation history;
- flattening direct evidence, third-party reports, model inference, and human acceptance into the same category.

## 14.6 Effect-Verification Failure

- treating a tool return as verified external effect;
- treating an execution log as proof of external consequence;
- converting an unknown external outcome into success or failure without evidence.

## 14.7 History and Supersession Failure

- erasing contradictory history;
- overwriting earlier records without preserving supersession;
- treating a correction as though the earlier representation never existed.

## 14.8 Observation Failure

- treating absence of recorded evidence as proof of non-occurrence without a justified observation model.

These failures share the same structural error:

> **the representation is promoted beyond what its evidence, authority, time, purpose, scope, or verification supports.**

---

# 15. Claim Boundary

This paper is an architectural and epistemic systems paper.

It does not claim that MIA, HSIE, or any AI system can obtain direct and complete access to objective reality.

It does not claim that provenance eliminates uncertainty.

It does not claim that human acceptance makes a statement objectively true.

It does not claim that every representation can be externally verified.

It does not claim independent validation of every architecture discussed.

It does not claim that the candidate Minimum Representation Envelope is a frozen conformance standard.

The narrower claim is:

> **Consequential AI systems can be designed to preserve explicit distinctions between external or human state and internal representations; track representation provenance and transformation; govern promotion into accepted state; preserve supersession history; and retain uncertainty when stronger verification is unavailable.**

---

# 16. Conclusion

AI systems increasingly operate through records about people, organizations, software systems, and the physical world.

The danger is not merely that a model may produce an incorrect answer.

The deeper systems risk is loss of representation status: an inference, summary, historical record, or execution trace may later be consumed as though it were current verified fact.

A prediction can become a profile.

A profile can become policy.

A policy can become automated action.

A log can become false proof.

A historical record can become present identity.

An inference can be repeatedly reused until later systems consume it without remembering that it began as inference.

Reality ≠ Representation is a refusal to allow those promotions to happen invisibly.

A system may model reality.

It may store evidence.

It may infer.

It may summarize.

It may remember.

It may act.

But it must preserve the boundary between the world and what the system believes, records, or says about the world.

That boundary is not a philosophical luxury.

It is part of the architecture of trustworthy consequential AI.

---

# Evidence Status Note

This document is a technical review candidate.

It does not represent independent validation, field validation, production deployment, certification, or a frozen conformance standard.

Where this draft conflicts with TB-SUB-001 v1.0.0, frozen MIA artifacts, governed evidence, or later owner-authorized canon, the governed source retains authority.

**REALITY ≠ REPRESENTATION**

**HUMAN REALITY ≠ HUMAN RECORD ≠ AI INTERPRETATION**

**RECORD ≠ REALITY**

**INFERENCE ≠ ACCEPTED STATE**

**EPISTEMIC STATUS ≠ GOVERNANCE STATUS**

**POLICY ≠ ENFORCEMENT**

**AUTHENTICATION ≠ AUTHORITY**

**EXECUTION ≠ EFFECT**

**MEMORY ≠ HUMAN**

---

# Selected External References

1. Moreau, L., and Missier, P., eds. *PROV-DM: The PROV Data Model.* W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-dm/
2. Tabassi, E. *Artificial Intelligence Risk Management Framework (AI RMF 1.0).* NIST AI 100-1. National Institute of Standards and Technology, 2023. DOI: 10.6028/NIST.AI.100-1.
3. Autio, C., Schwartz, R., Dunietz, J., Jain, S., Stanley, M., Tabassi, E., Hall, P., and Roberts, K. *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile.* NIST AI 600-1. National Institute of Standards and Technology, 2024. DOI: 10.6028/NIST.AI.600-1.

---

# Draft Control

**Candidate Publication ID:** HSIE-WP-002  
**Draft Version:** v0.2.0  
**Document State:** TECHNICAL REVIEW CANDIDATE  
**Technical Review Pass 1:** COMPLETE  
**Technical Review Pass 2:** OPEN  
**Claim Review:** OPEN  
**External Reference Review:** INITIAL PASS COMPLETE  
**Minimum Representation Envelope:** CANDIDATE / NOT FROZEN  
**Owner Publication Authorization:** NOT ISSUED  
**Public Release:** NOT AUTHORIZED
