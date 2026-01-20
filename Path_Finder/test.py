# PROJECT MANAS RL Workshop
'''
*
*   ===================================================
*       PROJECT MANAS - RL Workshop
*   ===================================================
*
*  This script is intended to be a Boilerplate for 
*  Testing the Q-Learning Agent.
*
*  Filename:		test.py
*  Author:		    PROJECT MANAS
*
*  This software is made available on an "AS IS WHERE IS BASIS".
*
*****************************************************************************************
'''
import numpy as np
import pickle
import time
import pygame
from envs.env import GridWorld

def test():
    env = GridWorld()
    
    # Load Q-Table
    try:
        with open('models/q_table.pkl', 'rb') as f:
            q_table = pickle.load(f)
        print("Q-Table loaded successfully.")
    except FileNotFoundError:
        print("Error: 'models/q_table.pkl' not found. Train the agent first using 'python train.py'.")
        return

    print("Starting Testing...")
    
    # Test Policy
    state = env.reset()
    done = False
    env.render()
    time.sleep(1)
    
    steps = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
        
        x, y = state
        action = np.argmax(q_table[x, y])
        
        state, reward, done = env.step(action)
        print(f"Step: {steps}, Action: {env.actions[action]}, State: {state}, Reward: {reward}")
        
        env.render()
        time.sleep(0.5)
        steps += 1
        
    print("Goal Reached!" if reward > 0 else "Finished.")
    time.sleep(2)
    env.close()

if __name__ == "__main__":
    test()
