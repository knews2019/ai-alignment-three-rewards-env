#!/usr/bin/env bash
# Pilot: one node, one day. Purpose is NOT a result; it is to confirm that
#   - honeypots get touched under a curious prompt,
#   - the spoof/tamper detectors fire under an adversarial prompt,
#   - report_unsolvable gets used at all on impossible tasks,
#   - the baseline attempted-faking rate at 40% is above the floor,
# and to set the TBD-pilot thresholds in PREREGISTRATION.md, which are then frozen.
#
# Everything below is a placeholder until env/ and rewards/ are implemented.
set -euo pipefail

TASKS=${TASKS:-tasks.jsonl}
MODEL=${MODEL:-Qwen/Qwen3-8B}
STEPS=${STEPS:-40}

echo "pilot: model=$MODEL steps=$STEPS tasks=$TASKS"
echo "1. dev-loop sanity: every verifier must fire at least once (samples/README.md)"
echo "2. arm A at 40% impossible, 1 seed, $STEPS steps  -> baseline rates"
echo "3. arm B at 40% impossible, 1 seed, $STEPS steps  -> sanity on reward scale"
echo "4. write pilot numbers into PREREGISTRATION.md §5, then freeze"
exit 1  # not implemented
