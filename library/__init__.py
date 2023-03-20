from gym.envs.registration import register

register(
    id='gym_cartpole/CartPole-3actions',
    entry_point='CartPoleEnvInstaDeep:CartPoleEnvInsstaDeep',
    max_episode_steps=500,
)