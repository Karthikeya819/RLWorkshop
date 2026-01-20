# PROJECT MANAS RL Workshop
'''
*
*   ===================================================
*       PROJECT MANAS - RL Workshop
*   ===================================================
*
*  This script contains the Q-Learning Logic and Definitions.
*
*  Filename:		QLearning.py
*  Author:		    PROJECT MANAS
*
*  This software is made available on an "AS IS WHERE IS BASIS".
*
*****************************************************************************************
'''
import numpy as np
ACTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT']

def get_reward(state, goal_state):
    pass
    ## [WORKSHOP] Implement the reward function

def get_action(q_table, state, epsilon, action_space_size):
    pass
    ## [WORKSHOP] Implement the action selection function

def update_q_table(q_table, state, action, reward, next_state, alpha, gamma):
    pass
    ## [WORKSHOP] Implement the Q-table update function