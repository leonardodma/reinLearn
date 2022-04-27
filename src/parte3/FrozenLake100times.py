import gym
import numpy as np
from numpy import loadtxt

env = gym.make('FrozenLake-v1').env
q_table = loadtxt('data/q-table-frozen-lake.csv', delimiter=',')

rewards = 0

for i in range(0,100):    
    state = env.reset()
    done = False
    while not done:
        action = np.argmax(q_table[state])
        state, reward, done, info = env.step(action)
    rewards += reward
print(rewards)