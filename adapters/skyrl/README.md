# SkyRL adapter

Secondary adapter. Wraps `env.core.ThreeRewardsEnv` as a SkyRL-Gym text environment (`init` / `step` returning observation, reward, done, metadata). Same tool server, same verifiers, same `ARM_WEIGHTS`.

Status: stub (`env.py`). Check the installed SkyRL-Gym base-class signature before implementing.

Why keep it: SkyRL has published RL-from-base results on Qwen3-14B/32B with OpenHands-style agents, which is the base-model path in `PREREGISTRATION.md`.
