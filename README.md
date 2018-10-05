# Multiple task MuJoCo through OpenAI gym
- This codebase has been built on top of [OpenAI gym](https://github.com/openai/gym) version '0.9.3' code and has been tested on `MuJoCo mjpro131`. 
- You can install it as 
```
git clone https://github.com/sanjaythakur/Multiple_Task_MuJoCo_Domains
cd gym
pip install -e .
```

### What does this repository do
- The repository allows for creating multiple different tasks on the MuJoCo domains that vary in their dynamics. This will be handy in performing experiments across multiple tasks. The details of how to tasks are created is summarized down in this readme file.
Note that this repository currently supports creating `20` different tasks only on `HalfCheetah` and `Swimmer` domains.

### How to use this repository
##### Creating tasks
- The following example shows how to create a unique task variant (task identity of 2) on a HalfCheetah environment.
```
from gym.multiple_tasks import get_task_on_MUJOCO_environment

env = get_task_on_MUJOCO_environment(env_name='HalfCheetah', task_identity='2')
observation = env.reset()
for _ in range(1000):
  env.render()
  action = env.action_space.sample()
  observation, reward, done, info = env.step(action)
```
Note that both arguments `env_name` and `task_identity` need a string value. This current repository allows for HalfCheetah and Swimmer envionments with task identities ranging from 0 to 19.

##### Proof of learnability of tasks
- We confirmend that the changes in the task dynamics are not too drastic to render them unlearnable by training agents using [PPO code here](https://github.com/pat-coady/trpo/tree/sanjaythakur-master). The performance plots can be seen under `multiple_task_examples_and_plots/plots/` directory in this repository.