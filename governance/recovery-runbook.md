# Recovery Runbook

## Incident classification
Examples: altered raw hash, missing source, stale index, leaked private information, or failed workflow. **Currently documented actual incidents:** none. **Operator for a future incident:** NOT_RECORDED; Diego Aguirre is the owner who may authorize recovery but no incident response has been performed.

## Containment
Pause editing and distribution, preserve the affected copy, and do not upload raw private data. If a genuine credential leaked, revoke it with the provider before restoration.

## Diagnosis
Run `python tools/validate_memory.py`, compare `manifest.sha256`, list affected relative paths, and identify the latest **actually verified** backup. The local English ZIP has no evidenced Git commit or external redundant backup.

## Restoration
Recover an existing verified ZIP or backup (if one exists), extract into an isolated directory, check raw digests, JSONL, and schemas; run index freshness checks and rebuild only derived indexes when needed. Do not invent a recovery snapshot.

## Resumption
Obtain Diego Aguirre's approval for any future incident-specific restoration, record the real date and results, and resume only after the sources and state match. A historical disaster-recovery test is **NOT_PERFORMED**.

## Incident report
Document cause, timeline, scope, observed checks, preventive actions, and approval. **Actual incident report:** NOT_RECORDED.
