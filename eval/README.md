# Evaluation

Run on every checkpoint, including the base model, with four samples per task.

## Sets

| Set | Size | In repo? |
|---|---|---|
| Held-out solvable | 500 | generated from held-out source instances; not in repo |
| Held-out impossible | 300 | mutated from held-out instances; not in repo |
| Over-refusal (naughty_legit) | 200 | not in repo |
| Private honeypot set | — | different ids, paths and names from the public manifest; released after the paper |

## Outcomes reported

Exactly the pre-registered list in `PREREGISTRATION.md` §4, in that order.

## Second-family judge (eval only)

An honesty cross-check on `final_report.txt` vs `tool_calls.jsonl` by a judge model from a family not used in training and not Qwen-, GLM- or Anthropic-derived (candidates: gpt-oss-120b, Gemma, Mistral). It is a check on the regex parser's recall, reported alongside the deterministic result. It is never in any reward.

## Eval-awareness

Two measurements, both reported:

1. Unprompted mentions in reasoning traces matching a fixed regex set (`eval_awareness_patterns.txt`, to be frozen before the run), with a classifier pass over matches.
2. The prompted probe from Lynch et al.: ask the model whether it believes it is in an evaluation or a deployment, classify the answer, and report rates split by that belief.

## Frontier models through APIs (no training)

Same held-out sets, same tool interface, one fixed and published scaffold and system prompt (`frontier_scaffold.md`, to be frozen). Harness effects are large; the scaffold is part of the pre-registration. Report the same outcomes.
