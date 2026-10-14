"""SkyRL-Gym text environment wrapper. Stub."""
from __future__ import annotations


class ThreeRewardsSkyRLEnv:
    """Expected shape (verify against skyrl_gym.envs.base_text_env.BaseTextEnv):

        def init(self, prompt) -> (observation, metadata)
        def step(self, action: str) -> BaseTextEnvStepOutput(observations, reward, done, metadata)

    `action` is the model's text; parse the tool call out of it, route through
    env.core.ThreeRewardsEnv.step, return the observation. Reward is 0 until the
    terminal step, then ARM_WEIGHTS-weighted total; breakdown in metadata.
    """

    def __init__(self, env_config=None, extras=None) -> None:
        raise NotImplementedError
