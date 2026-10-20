# Backups — Instructions and Status

## Proposed backup policy
Protect the complete tree, the original raw bytes, checksum manifest, and decision metadata, subject to privacy review. **No actual backup schedule, retention interval, location, or responsible operator has been recorded.** Diego Aguirre has approved use of these personal-documentation guidelines, **not** an imaginary completed backup or a specific retention period. The delivered ZIP is an export, not proof of independent redundant storage.

## Destination and security
A separate encrypted destination, restricted access, and keys stored outside the repository are **recommended but NOT_CONFIGURED**. No external backup or historical restoration tests are evidenced.

## Copy procedure
1. With the owner's authorization, copy the ZIP or complete snapshot to separate storage.
2. Compare the SHA-256 digests for both original raw files and their manifest.
3. Run `python tools/validate_memory.py` in an isolated restoration folder.
4. Rebuild derived indexes if needed; reconcile the restored contents with the authoritative originals.
5. Record the actual destination, operator, timestamp, and test outcome only after those actions occur. Never fabricate an external backup.

## Backup register
**Last proven external backup:** NOT_RECORDED. **Last historical restoration:** NOT_RECORDED. **Actual external restore test:** NOT_PERFORMED.

## Recovery
See [recovery-runbook.md](../governance/recovery-runbook.md). A program cannot restore missing originals unless an intact copy actually exists.
