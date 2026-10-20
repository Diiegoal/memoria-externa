# Procedure — Resolve Conflicts

## Procedure control
**Version:** 1.0, English edition. **Purpose:** resolve conflicts with verifiable traceability. **Authorizing documentary owner:** Diego Aguirre (self-identified on October 20, 2026). **Operating actor:** an actually authorized operator, not assumed to be a specific person. **Trigger:** Two records, source statements, or decisions disagree.

## Preconditions
Real access to local files and permission to operate; protection of secrets; relevant originals available before promoting new claims. **Present package scope:** one documentary chat, one session, one adopted decision, and no committed implementation tasks. The owner approves these instructions as documentation; no unperformed procedural run is claimed.

## Inputs
`MEMORY_MANIFEST.yaml`, [current state](../projects/agent-sdlc-13-modulos/current-state.md), [handoff](../projects/agent-sdlc-13-modulos/handoff.md), originals [user document](../raw/agent-sdlc-13-modulos/chat-1/turns/0001-user-original.md) and [assistant document](../raw/agent-sdlc-13-modulos/chat-1/turns/0002-assistant-original.md) where relevant, and governance policies. Own Git commit: **NOT_RECORDED**.

## Operational steps
1. Identify both claims, original paths, sections, dates, status, and scope.
2. Check raw integrity before changing derived records; retain the old evidence.
3. Distinguish contradictions in outside facts from revised personal decisions and reversible preferences.
4. For an external factual conflict, consult a period-appropriate independent source; mark **PENDING_VERIFICATION** when unavailable.
5. For a substantive decision, obtain the owner’s scoped approval and create a successor decision/event with `supersedes` references; preserve history.
6. Correct current state, handoff, and derived indexes; rerun validation and document observed results.

## Outputs and evidence
Record only the files actually created or modified, source references, source hashes, actual dates, IDs, and real test outputs. A reconstructed summary never proves the historical chat ended at a particular time. Claim a Git commit or approval in GitHub only if the action actually occurred.

## Exceptions and rollback
If a source is inaccessible, state it was **not read**. If a raw hash differs, halt promotion and follow [recovery-runbook.md](../governance/recovery-runbook.md). If a decision conflicts, preserve earlier history and seek actual owner approval. If validation fails, restore an intact local copy; never overwrite the preserved raw originals with guessed text.

## Completion criteria
Relevant primary evidence exists; authorized changes have traceable sources; schemas and hashes match; indexes are reconciled; and any required human judgment has actually occurred. The future operator and execution date remain **NOT_RECORDED** until the procedure is performed.
