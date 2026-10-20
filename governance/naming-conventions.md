# Naming Conventions

## Scope and version
Local version 1.0, English edition. `agent-sdlc-13-modulos` is a **technical project slug**, not a historical name supplied by the user. Preserve existing paths to maintain compatibility and full original-file integrity.

## Identifiers
- `S-YYYYMMDD-NNN`: documentary session (the date in this case is the documented adoption day, **not** the unknown start of the original chat).
- `DEC-NNNN`: substantive decision.
- `TASK-NNNN`: genuine task when evidenced.
- `EV-NNNN`: append-only event.
- `SRC-NNN`: evidence source; `Q-NNNN`: open question; `CON-NNNN`: constraint.
Never reuse any ID after a record is closed, removed, or superseded.

## Original messages
`raw/<project>/chat-1/turns/0001-user-original.md` and `0002-assistant-original.md`. Numbering reflects the **two supplied documents**, not a certified complete exported ChatGPT transcript. These original files remain in Spanish and unmodified.

## Dates, sentinel values, and paths
Use ISO 8601 date-only (`YYYY-MM-DD`) if no time is known; use timezone-aware RFC 3339 only for observed technical instants. Never invent local timezones or clock times. Use POSIX relative paths and checksums over **stored bytes**. English edition sentinels: `NOT_RECORDED` (unknown/unavailable), `PENDING_VERIFICATION` (assertion not yet checked), `NOT_PERFORMED` (action not evidenced), and `NOT_CONFIGURED` (integration not installed).

## Validation patterns
Project slug `[a-z0-9]+(?:-[a-z0-9]+)*`, session `^S-\d{8}-\d{3}$`, decision `^DEC-\d{4}$`, task `^TASK-\d{4}$`, event `^EV-\d{4}$`. Uniqueness and manifest references are checked by the local validator. External systems do not automatically enforce these conventions.
