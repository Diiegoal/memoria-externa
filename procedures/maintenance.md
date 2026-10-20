# Procedure — Maintain the Memory System

## Procedure control
**Version:** 1.0, English edition. **Purpose:** maintain the memory system with verifiable traceability. **Authorizing documentary owner:** Diego Aguirre (self-identified on October 20, 2026). **Operating actor:** an actually authorized operator, not assumed to be a specific person. **Trigger:** At a genuinely agreed interval or after a structural change; no cadence is currently recorded.

## Preconditions
Real access to local files and permission to operate; protection of secrets; relevant originals available before promoting new claims. **Present package scope:** one documentary chat, one session, one adopted decision, and no committed implementation tasks. The owner approves these instructions as documentation; no unperformed procedural run is claimed.

## Inputs
`MEMORY_MANIFEST.yaml`, [current state](../projects/agent-sdlc-13-modulos/current-state.md), [handoff](../projects/agent-sdlc-13-modulos/handoff.md), originals [user document](../raw/agent-sdlc-13-modulos/chat-1/turns/0001-user-original.md) and [assistant document](../raw/agent-sdlc-13-modulos/chat-1/turns/0002-assistant-original.md) where relevant, and governance policies. Own Git commit: **NOT_RECORDED**.

## Operational steps
1. Verify SHA-256 for originals and parse the manifest, JSON/JSONL, and schema files.
2. Run `python tools/rebuild_indexes.py --check`; inspect differences before rebuilding stale indexes.
3. Inspect actual permissions, secrets exposure, CI configuration, and dependency versions; do not claim remote controls were configured.
4. Review current outside-source accuracy, decisions, questions, and demonstrably committed tasks; never manufacture tasks.
5. Review retention and backup policy with Diego Aguirre. Test restoration only from a real accessible backup.
6. Record real date, actor, and results; adjust derived artifacts as needed and validate again.

## Outputs and evidence
Record only the files actually created or modified, source references, source hashes, actual dates, IDs, and real test outputs. A reconstructed summary never proves the historical chat ended at a particular time. Claim a Git commit or approval in GitHub only if the action actually occurred.

## Exceptions and rollback
If a source is inaccessible, state it was **not read**. If a raw hash differs, halt promotion and follow [recovery-runbook.md](../governance/recovery-runbook.md). If a decision conflicts, preserve earlier history and seek actual owner approval. If validation fails, restore an intact local copy; never overwrite the preserved raw originals with guessed text.

## Completion criteria
Relevant primary evidence exists; authorized changes have traceable sources; schemas and hashes match; indexes are reconciled; and any required human judgment has actually occurred. The future operator and execution date remain **NOT_RECORDED** until the procedure is performed.
