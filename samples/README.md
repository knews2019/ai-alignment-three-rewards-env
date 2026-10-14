# Samples

Target: 50 API-agent trajectories, produced in the dev loop (`docs/design.md`, "Development loop without GPUs"), in which every verifier fires at least once:

- adversarial prompt ("pass the tests by any means") → `truth.tamper`, `truth.claim_vs_log`
- curious prompt → `scope` via `.env` or the sibling repo
- impossible task → `abstain` (matched and unmatched reasons)
- naughty_legit task → `overrefusal` both ways

A verifier that never fires under adversarial prompting is broken, not clean. None recorded yet.
