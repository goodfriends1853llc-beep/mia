# MIA — Governed Continuity Runtime

**Public Code Release:** v0.1 proof release  
**Frozen Runtime Referenced by Current White Paper:** MIA Runtime v1.0.0 — internally validated; not fully published as source in this repository  
**License:** Apache License 2.0

MIA is a deterministic execution substrate for verifiable computation and governed AI execution.

The public repository currently contains the **MIA v0.1 proof release**. Later governed-runtime work is described through bounded publication evidence, but should not be interpreted as fully published production source, independent certification, or unrestricted deployment readiness.

MIA is not an AI model, agent, or application.

It is infrastructure intended to sit beneath consequential execution.

---

## White Paper

**HSIE-WP-001 — MIA: A Governed Runtime for Evidence-Bound, Replayable AI Execution**  
Tommie Bellamy — Human Systems Architect™  
Release version: **v1.0.0**

[Read the public GitHub edition](./docs/whitepapers/HSIE-WP-001/README.md)

The white paper documents the architecture, frozen runtime evidence, later controlled external-boundary testing, claim ceilings, and open validation gates.

The white paper's release version is a **publication version**. It does not mean that the public code in this repository has silently become MIA Runtime v1.0.0.

---

## Why MIA Exists

AI systems are becoming increasingly capable of proposing decisions and actions across consequential domains.

Capability alone does not establish:

- what authority applied;
- what information was used;
- what actually executed;
- what state changed;
- whether an execution can be reconstructed;
- whether an independent verifier can check the resulting evidence.

MIA explores infrastructure for making execution more reconstructable, replayable, auditable, and independently verifiable.

---

## Public v0.1 Scope

The public v0.1 repository includes code for:

- deterministic execution flows;
- execution snapshots;
- canonical serialization;
- SHA-256 sealing;
- verifier identities and signatures;
- multi-verifier result handling;
- replay of prior executions;
- comparison of replayed state against snapshots;
- diffing between executions;
- external verification of proof artifacts.

These capabilities represent the current public code proof surface.

They should not be interpreted as proof that later runtime capabilities are already fully published here, production-ready, safety-certified, field-validated, or suitable for unrestricted real-world deployment.

---

## Core Principle

> If an execution cannot be replayed and independently verified, it should not be treated as sufficiently trustworthy for consequential use.

MIA separates states that are often collapsed together:

**VALID ≠ PERMITTED ≠ EXECUTED ≠ VERIFIED ≠ COMMITTED ≠ RECEIPTED**

---

## Execution Model

At a high level:

**INPUT → EXECUTION → SNAPSHOT → SEAL → VERIFICATION → REPLAY / DIFF**

The broader governed runtime adds explicit identity, authority, consent, policy, context, planning, execution, effect verification, commit, receipts, proof, replay, and reconstructable history. See HSIE-WP-001 for the current architecture and evidence boundary.

---

## Quick Start

```bash
git clone https://github.com/goodfriends1853llc-beep/mia.git
cd mia
pip install pynacl
python run_demo.py
```
