# External Memory — User Guide

## Purpose and scope
A local external-memory package for **one** project (`agent-sdlc-13-modulos`), **one** documentary chat (`chat-1`), **one** reconstructed session, and **two** verbatim original documents. The system design follows the proposed specification dated October 18, 2026. This is **not** built-in ChatGPT memory, an installed GitHub integration, or an automatically synchronizing agent. Fictional instances from the specification have not been created.

**Documentary owner:** Diego Aguirre, identified by his own statement in the conversation requesting this English edition on October 20, 2026; no independent identity verification is claimed. He explicitly authorized and approved preparation and confirmation of this personal documentation package. This consent does not prove deployment, testing of a future product, ownership of third-party intellectual property, or external certification. The previous research decision remains adopted for personal use only.

**Reference repository:** [Diiegoal/memoria-externa](https://github.com/Diiegoal/memoria-externa), identified as a public repository on October 20, 2026. The new ZIP is **local**: no upload, commit, push, or GitHub Actions execution is asserted for this edition.

## Requirements and preparation
- **Git:** optional; actual local installation/version **NOT_RECORDED**; extracting the ZIP does not create or update a remote repository.
- **Python:** 3.10 or newer recommended; check using `python --version`.
- **Dependencies:** `PyYAML` and `jsonschema` for validation; install in your own controlled environment with `python -m pip install pyyaml jsonschema`.
- **Authentication:** none for the provided local scripts. Do not place tokens or secrets in this tree.

## Architecture map
`raw/` holds immutable original inputs; `projects/agent-sdlc-13-modulos/` holds the decision, session, working state, and knowledge; `events/` records documented events; `indexes/` offers rebuildable views; `governance/` contains policy; `schemas/` defines machine contracts; `procedures/` explains operation; `templates/` supports future authorized records; `tools/` contains local utilities; `.github/` provides GitHub configuration *examples*, not evidence of deployment; `backups/` describes backups that have **not** been performed.

**Evidence hierarchy:** preserved originals > approved decision/documented events > session record > current state/handoff > derived indexes. An assertion in an original document proves its presence there, not necessarily its external factual accuracy.

## Installation and configuration
1. Extract the ZIP while retaining `memoria-externa/` as its root directory.
2. Open a terminal in that directory.
3. Run `python tools/validate_memory.py` (install dependencies if requested).
4. Run `python tools/rebuild_indexes.py --check` to check the indexes.
5. Use `python tools/build_context.py --project agent-sdlc-13-modulos --budget-chars 30000 --output /path/outside/repo/context.md` to assemble a limited, clearly attributed handoff packet.
6. Review sensitive content and obtain appropriate authorization before sharing. Never assume `git push` was performed.

## Operating workflow
1. Open [START_HERE.md](START_HERE.md).
2. Read [current-state.md](projects/agent-sdlc-13-modulos/current-state.md), [handoff.md](projects/agent-sdlc-13-modulos/handoff.md), [DEC-0001.md](projects/agent-sdlc-13-modulos/decisions/DEC-0001.md), and [S-20261020-001.md](projects/agent-sdlc-13-modulos/sessions/S-20261020-001.md).
3. For nuance, consult the full Spanish originals [0001-user-original.md](raw/agent-sdlc-13-modulos/chat-1/turns/0001-user-original.md) and [0002-assistant-original.md](raw/agent-sdlc-13-modulos/chat-1/turns/0002-assistant-original.md). Never confuse an index with the full original.
4. For future sessions, follow the procedures, collect only authorized records, and do not fabricate tasks.
5. Rebuild indexes, validate, and review differences before any optional version-control operation.

## Integrity and security
Use the [SHA-256 manifest](raw/agent-sdlc-13-modulos/chat-1/manifest.sha256) and [validator](tools/validate_memory.py). **The two Spanish originals remain byte-for-byte identical to the inputs**; their hashes are unchanged. The derived English files have new hashes in the regenerated indexes. Content may be sensitive; review it before publishing. `.gitignore` does not encrypt data or delete Git history. External backup and historical recovery **NOT_PERFORMED**: [backup guide](backups/README.md), [recovery runbook](governance/recovery-runbook.md).

## Limitations and internal links
A new chat only receives files deliberately supplied to it or actually read using an authorized connection; a ZIP does not create an automatic ChatGPT–GitHub connection. The presence of a workflow does not prove CI execution. See [manifest](MEMORY_MANIFEST.yaml), [memory policy](governance/memory-policy.md), [session opening](procedures/session-open.md), and [context builder](tools/build_context.py). The personally adopted order is **not** a certification of a production application or of every cited external source.

## Scope and inventory audit for this edition
- **Structural coverage:** root, `.github/`, `governance/`, `schemas/`, `identity/`, `projects/`, `raw/`, `events/`, `indexes/`, `procedures/`, `templates/`, `tools/`, and `backups/`.
- **Single organizational project ID:** `agent-sdlc-13-modulos` is a technical convention, not a verified historical project name. The same ID is used throughout the paths, manifest, events, and indexes.
- **Single documentary chat and session:** `chat-1` and `S-20261020-001`; the ID uses the documented adoption date, **not** an authenticated start time for the historical chat. The two supplied original documents are the defined corpus, not a certified full chat export.
- **One substantive decision:** `DEC-0001`, personally adopted on October 20, 2026. Diego Aguirre's follow-up confirmation for this translated documentation package is recorded **as follow-up packaging authorization**, not retroactively inserted into the original transcript as a new Chat 1 turn.
- **Omitted illustrative instances:** `proyecto-alfa`, `DEC-0002`, example `TASK-0001`/`TASK-0002`, four fictional example sessions, `chat-2` and its turns. The `tasks/` directory is deliberately empty because there is no evidenced committed implementation task.
- **Preserved textual evidence:** both complete Spanish originals; the report's assertion that it retrieved 68 course files does **not** mean those 68 source texts are contained in this ZIP.
- **Dates kept distinct:** October 19, 2026 is the report's cut-off/consultation date; October 20, 2026 its personal adoption date and this English edition's date; the original packaging timestamp remains historical metadata, not a chat timestamp.
- **Remaining limitations:** the report documents focused inspection of 21 lessons and structural inspection of 47, not a complete semantic audit of all 68 nor full historical verification of changing external pages. No implementation, deployment, external backups, incident exercises, or real product tests have been demonstrated.
- **Approval:** Diego Aguirre expressly authorized preparation, approval, and confirmation of this personal package in this conversation. Governance/procedure templates are approved **for documentary use**; operation of unconfigured external systems, retention periods without dates, independent third-party certifications, and future tasks are not falsely marked complete.
- **Language migration:** all non-raw explanatory content is in English. Machine status values are translated consistently (`confirmado` → `confirmed`, `NO_REGISTRADO` → `NOT_RECORDED`) without changing paths, IDs, original bytes, or the content of `manifest.sha256`. See [CHANGELOG.md](CHANGELOG.md).
