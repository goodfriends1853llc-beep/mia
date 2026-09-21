# MIA — Governed Continuity Runtime

**Public Release:** v0.1  
**Internal Runtime Version:** v0.8 — active development  
**License:** Apache License 2.0

MIA is a deterministic execution substrate for verifiable computation.

The public repository currently contains the MIA v0.1 proof release. A broader governed continuity runtime is under active development and is not represented here as fully published or production-ready.

MIA is not an AI model, agent, or application.

It is infrastructure intended to sit beneath consequential execution.

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

These capabilities represent the current public proof surface.

They should not be interpreted as proof that later roadmap capabilities are already implemented, production-ready, safety-certified, or suitable for unrestricted real-world deployment.

---

## Core Principle

> If an execution cannot be replayed and independently verified, it should not be treated as sufficiently trustworthy for consequential use.

MIA separates several states that are often collapsed together:

**PROPOSED ≠ PERMITTED ≠ EXECUTED ≠ VERIFIED ≠ COMMITTED ≠ RECEIPTED**

---

## Execution Model

At a high level:

**INPUT → EXECUTION → SNAPSHOT → SEAL → VERIFICATION → REPLAY / DIFF**

Given the same input, execution logic, and governed environment, MIA is designed to produce reproducible execution results.

---

## Quick Start

```bash
git clone https://github.com/goodfriends1853llc-beep/mia.git
cd mia
pip install pynacl
python run_demo.py
