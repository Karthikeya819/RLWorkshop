# PROJECT MANAS RL Workshop
'''
*
*   ===================================================
*       PROJECT MANAS - RL Workshop
*   ===================================================
*
*  This script is intended to be a Boilerplate for 
*  Training the Q-Learning Agent.
*
*  Filename:		train.py
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
import os
from envs.env import GridWorld
import argparse

def train():
    parser = argparse.ArgumentParser(description="Train Q-Learning Agent")
    parser.add_argument('--speed', type=float, default=0.05, help='Speed of visualization (seconds per step). Default: 0.05')
    parser.add_argument('--fast', action='store_true', help='Disable visualization for fastest training.')
    args = parser.parse_args()

    env = GridWorld()
    
    # [WORKSHOP] Tune the Hyperparameters
    alpha = 0.1  # Learning Rate
    gamma = 0.99 # Discount Factor
    epsilon = 1.0 # Exploration Rate
    epsilon_decay = 0.995
    min_epsilon = 0.01
    episodes = 500
    
    q_table = np.zeros((env.width, env.height, env.action_space_size))

    VISUALIZE_TRAINING = not args.fast
    speed = args.speed
    
    print("Starting Training...")
    
    for episode in range(episodes):
        state = env.reset()
        done = False
        total_reward = 0
        
        while not done:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    env.close()
                    return

            x, y = state
            
            if np.random.uniform(0, 1) < epsilon:
                action = np.random.randint(0, env.action_space_size) # Explore
            else:
                action = np.argmax(q_table[x, y]) # Exploit
            
            next_state, reward, done = env.step(action)
            next_x, next_y = next_state
            
            old_value = q_table[x, y, action]
            next_max = np.max(q_table[next_x, next_y])
            
            new_value = old_value + alpha * (reward + gamma * next_max - old_value)
            q_table[x, y, action] = new_value
            
            state = next_state
            total_reward += reward
            
            if VISUALIZE_TRAINING:
                env.render()
                time.sleep(speed)
            
        # Decay Epsilon
        epsilon = max(min_epsilon, epsilon * epsilon_decay)
        
        if episode % 50 == 0:
            print(f"Episode: {episode}, Total Reward: {total_reward}, Epsilon: {epsilon:.2f}")

    print("Training Finished!")
    
    # Save Q-Table
    if not os.path.exists('models'):
        os.makedirs('models')
        
    with open('models/q_table.pkl', 'wb') as f:
        pickle.dump(q_table, f)
    print("Q-Table saved to 'models/q_table.pkl'")
    
    env.close()

if __name__ == "__main__":
    train()
