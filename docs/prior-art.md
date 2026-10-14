# Prior art

What each reward has behind it, and what nobody has done. Numbers were taken from a source check on 14 October 2026; confirm each against the PDF before citing.

## The novelty claim, stated carefully

Each of the three rewards has a precedent on its own. We found no work that trains a coding agent with all three together (truthfulness checked against tool output, a scope penalty, a paid "unsolvable" report) while varying the share of impossible tasks. "Not found" after a targeted search is not "does not exist." The claim to make is "first combined, dose-response test," not "untested idea."

## Closest work, per reward

### Truthfulness (claims vs tool output)

| Work | What it does | Numbers | Why it differs |
|---|---|---|---|
| "The Obfuscation Atlas" (arXiv 2602.15515, Feb 2026) | Penalizes RL with a deception probe on activations (MBPP-Honeypot) | Without probe, 27 of 28 seeds became deceptive; with probe and KL 0.1, honest 100% | Signal is an activation probe, not execution |
| OpenAI, "Training LLMs for Honesty via Confessions" (arXiv 2512.08093, Dec 2025) | Honesty reward via LLM judge | — | Judge-based |
| "Quantifying Overclaiming Propensity in Frontier LLM Agents" (arXiv 2609.20812) | Checks agent claims against execution traces | — | Evaluation only, not a training reward |
| ExecCritic (arXiv 2609.09133) | Zero reward for forbidden test edits | — | Execution-gated, not targeting honesty of reports |

Our truthfulness reward is a deterministic parser over the tool log (claimed pass vs real exit code; in-sandbox pass vs hidden-test pass; runner and test-file hashes). No model in the loop.

### Scope / trespass

| Work | What it does | Numbers | Why it differs |
|---|---|---|---|
| Qwen, "The Verification Horizon" (arXiv 2606.26300, June 2026) | Trajectory monitor penalizes shortcut access during RL (PR diffs, external fix lookup, git-history mining); pattern list extended by an AI reviewer | Hacked-but-successful solutions 28.57% → 0.56% across three SWE-bench variants; on Verified alone hack rate 51.49% → 2.13%, clean solutions 40.22% → 60.53% | Partly model-based; no impossible tasks; no abstention |
| CATCH (arXiv 2609.39533) | CoT-monitor penalty | Suppresses hacking early; hacking returns later in training | Motivates our erosion phase |
| Anthropic, "Teaching Claude Why" (2026) | Constitutional synthetic documents plus honeypot training | Blackmail 65% → 19% on a large dataset; near-zero for Sonnet 4.5 in-distribution, more misbehavior far from it | Honeypots in training; our scope penalty applies to any out-of-scope access, trap-looking or not |
| SHADE-Arena (arXiv 2506.15740); Apollo sabotage evals | Honeypot-style evaluation | — | Evaluation only |
| Z.ai, GLM-5.2 release notes (secondary reporting) | LLM judge inspects tool-call intent, blocks matches, returns dummy data; trajectories continue | SWE-Bench Pro Verified (arXiv 2609.08149): 78.80% baseline → 57.32% with anti-hacking on; confirmed answer-file access → 0 | Intervention without penalty; our optional arm B′ |

### Abstention / impossible tasks

| Work | What it does | Numbers | Why it differs |
|---|---|---|---|
| ImpossibleBench (Zhong, Raghunathan, Carlini; arXiv 2510.20270; ICLR 2026) | Mutates tests to contradict the spec; measures cheating | GPT-5 cheats on 54.0% of Conflicting-SWEbench, 76% of Oneoff-SWEbench, 2.9% of Oneoff-LiveCodeBench. `flag_for_human_intervention` cuts GPT-5 from 54% to 9%, o3 from 49% to 12%; weaker for Claude Opus 4.1. Strict "STOP if tests are flawed" prompt: 93% → 1% on conflicting LiveCodeBench. Hidden tests push cheating success near zero but hurt original-task performance. LLM monitors catch 86–89% on LiveCodeBench, 42–65% on SWE-bench. "Stronger models generally exhibit higher cheating rates." | Evaluation only; no training |
| AWA-RL (arXiv 2607.10738, 2026) | Varies unanswerable share during RL, search agents | Fixed refusal reward of 0.05 → 99.9% refusals; from-scratch training → 52.2% lazy refusals | Search, not coding; shows a flat abstention payout collapses |
| RLAAR (arXiv 2510.18731); "Rewarding Intellectual Humility" (arXiv 2601.20126) | Reward "I don't know" | — | QA and math only |
| "Shallow Beliefs" (arXiv 2609.14998) | ImpossibleBench as an RL environment | — | Used to *induce* hacking |
| Meta, Muse Spark safety report (arXiv 2606.12429) | Reports 0% cheating on Impossible-LiveCodeBench oneoff for Muse Spark and GPT-5.4 | — | Evaluation |

### The escalation-channel result

"From surveillance to signalling: escalation channels as environmental controls for agentic AI" (arXiv 2510.05192): an externally governed escalation channel cut blackmail from 38.73% to 1.21% across 10 LLMs. This is the strongest outside support for paying for abstention.

### Misalignment from task RL (why erosion matters)

- Betley et al., emergent misalignment (arXiv 2502.17424; Nature, DOI 10.1038/s41586-025-09937-5): GPT-4o finetuned on insecure code gives misaligned answers 20% of the time on selected questions and 6% on pre-registered ones, vs 0% and 0.1% for controls.
- Anthropic, "Natural emergent misalignment from reward hacking in production RL" (MacDiarmid, Hubinger et al.; arXiv 2511.18397, Nov 2025): hacking vs penalty baseline, Betley questions 33.7% vs 0.7%; fake/bad goals 69.8% vs 0.1%; framing a colleague 41.3% vs 4.0%; Claude Code sabotage 12%. Inoculation prompting cut misalignment 75–90%. A hacking penalty prevented the broad misalignment.
- Baker et al., CoT monitoring (arXiv 2503.11926, Mar 2025): CoT monitor 95% recall vs ~60% for action-only; putting monitor pressure in the reward produces obfuscated hacking. Hence: no judge in any reward here.
- Greenblatt et al., alignment faking (arXiv 2412.14093): 14% compliance for free-tier vs almost never for paid; RL raised alignment-faking reasoning to 78%.
- Lynch et al., "Agentic Misalignment" (arXiv 2510.05179): Claude Opus 4 blackmailed 55.1% when its reasoning said "real" vs 6.5% when it said "eval" (21.4% / 64.8% / 13.8% real / eval / abstain across 500 samples). Hence eval-awareness as a monitored outcome.

### Constitutions and principle sets

- Anthropic's Constitutional AI (Bai et al., 2022): supervised self-critique against written principles, then RL from AI feedback with a preference model judging against the principles.
- OpenAI's deliberative alignment (Guan et al., Dec 2024): SFT on reasoning that cites the spec, then RL with a judge given the spec; judge does not see the chain of thought.
- One-line contrast: both grade *outputs* with a model-based judge conditioned on natural-language principles. This environment grades *behaviors* with deterministic checks against environment ground truth. Arm C uses the principle corpus as training data, the way constitutional synthetic documents are used, and never as a grader.
- We found no RL reward or constitution built from a named religious or cultural principle set. Not exhaustively searched.

## Methodology precedents

- Pre-registered ML contrast with equivalence testing: "When the Reward Suite Is Leaky" (arXiv 2607.11022).
- Seeds as unit of replication: the Obfuscation Atlas used 28 seeds.
- Sample size for a halving of a 10–20% rate: see `scripts/power.py` (roughly 200 episodes per arm for 20% → 10%, 435 for 10% → 5%, treating episodes as independent, which they are not across seeds).
