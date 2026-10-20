# Procedure — Close a Session

## Procedure control
**Version:** 1.0, English edition. **Purpose:** close a session with verifiable traceability. **Authorizing documentary owner:** Diego Aguirre (self-identified on October 20, 2026). **Operating actor:** an actually authorized operator, not assumed to be a specific person. **Trigger:** After a genuinely new session has produced authorized source material.

## Preconditions
Real access to local files and permission to operate; protection of secrets; relevant originals available before promoting new claims. **Present package scope:** one documentary chat, one session, one adopted decision, and no committed implementation tasks. The owner approves these instructions as documentation; no unperformed procedural run is claimed.

## Inputs
`MEMORY_MANIFEST.yaml`, [current state](../projects/agent-sdlc-13-modulos/current-state.md), [handoff](../projects/agent-sdlc-13-modulos/handoff.md), originals [user document](../raw/agent-sdlc-13-modulos/chat-1/turns/0001-user-original.md) and [assistant document](../raw/agent-sdlc-13-modulos/chat-1/turns/0002-assistant-original.md) where relevant, and governance policies. Own Git commit: **NOT_RECORDED**.

## Operational steps
1. Save each available message verbatim as a separate raw file, after a privacy review. Do not fabricate missing exchanges.
2. Preserve only known original timestamps; calculate SHA-256 and update the relevant raw manifest.
3. Write a session record distinguishing sourced facts, open questions, proposed decisions, and approved decisions.
4. Create tasks only where a real commitment exists; append evidence-backed events for actual recorded actions.
5. Update decisions, evidence, current state, handoff, and timeline; do not erase prior raw material.
6. Rebuild indexes, validate the schemas, hashes, and links, and review the resulting diff.
7. Commit, push, or open a pull request only with real permissions and an explicit instruction; record the commit SHA only after verification.

## Outputs and evidence
Record only the files actually created or modified, source references, source hashes, actual dates, IDs, and real test outputs. A reconstructed summary never proves the historical chat ended at a particular time. Claim a Git commit or approval in GitHub only if the action actually occurred.

## Exceptions and rollback
If a source is inaccessible, state it was **not read**. If a raw hash differs, halt promotion and follow [recovery-runbook.md](../governance/recovery-runbook.md). If a decision conflicts, preserve earlier history and seek actual owner approval. If validation fails, restore an intact local copy; never overwrite the preserved raw originals with guessed text.

## Completion criteria
Relevant primary evidence exists; authorized changes have traceable sources; schemas and hashes match; indexes are reconciled; and any required human judgment has actually occurred. The future operator and execution date remain **NOT_RECORDED** until the procedure is performed.
