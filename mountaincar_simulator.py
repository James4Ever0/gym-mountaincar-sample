import logging

import gym

import bonsai
from gym_common import GymSimulator

ENVIRONMENT = 'MountainCar-v0'
RECORD_PATH = None
SKIPPED_FRAME = 4


class MountainCarSimulator(GymSimulator):

    def __init__(self, env, skip_frame, record_path, render_env):
        super().__init__(
            env, skip_frame=skip_frame,
            record_path=record_path, render_env=render_env)

    def get_state(self):
        state_schema = super().get_state()
        return {"x_position": state_schema[0],
                "x_velocity": state_schema[1]}

if __name__ == "__main__":
    env = gym.make(ENVIRONMENT)
    logging.basicConfig(level=logging.INFO)
    base_args = bonsai.parse_base_arguments()
    simulator = MountainCarSimulator(
        env, SKIPPED_FRAME, RECORD_PATH, not base_args.headless)
    bonsai.run_with_url("mountaincar_simulator", simulator,
                        base_args.brain_url)