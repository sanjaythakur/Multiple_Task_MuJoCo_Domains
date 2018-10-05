from gym.multiple_tasks import get_task_on_MUJOCO_environment

env = get_task_on_MUJOCO_environment(env_name='HalfCheetah', task_identity='2')
observation = env.reset()
for _ in range(1000):
  env.render()
  action = env.action_space.sample()
  observation, reward, done, info = env.step(action)
