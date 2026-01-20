'''
*
*   ===================================================
*       PROJECT MANAS - RL Workshop
*   ===================================================
*
*  This script is intended to be a Boilerplate for 
*  Testing the Q-Learning Agent.
*
*  Filename:		Test.py
*  Author:		    PROJECT MANAS
*
*  This software is made available on an "AS IS WHERE IS BASIS".
*
*****************************************************************************************
'''
import numpy as np
import random
import pickle
import os

class QLearningController:
    def __init__(self, n_states=32, n_actions=5, filename="q_table.pkl"): 
        """
        Initialize the Q-learning controller.

        Parameters:
        - n_states (int): Total number of discrete states.
        - n_actions (int): Total number of discrete actions.
        - filename (str): File to save/load Q-table.
        """

        self.n_states = n_states
        self.n_actions = n_actions

        # === Define Hyperparameters ===
        self.lr = 0.95      # Learning Rate
        self.epsilon = 0.01 # Exploration Rate
        self.gamma = 0.9    # Discount Factor
        self.epsilon_decay = 0.02 
        self.min_epsilon = 0.01

        self.filename = filename

        # Initialize Q-table
        self.q_table = np.zeros((n_states, n_actions))

        # === Define Actions ===
        # 0 - forward, 1 - left, 2 - right, 3 - sharp_left, 4 - sharp_right
        self.action_list = [0, 1, 2, 3, 4] 

        # Map actions to motor speeds [Left, Right]
        self.actions = {
            0: [1.0, 1.0],
            1: [0.5, 1.0],
            2: [1.0, 0.5],
            3: [0.0, 1.0],
            4: [1.0, 0.0]
        }

        self.devi_count = 0 
    
    def decay_epsilon(self):
        """
        Reduce epsilon (exploration rate) over time.
        """
        self.epsilon = max(self.min_epsilon, self.epsilon - self.epsilon_decay)

    def Get_state(self, sensor_data):
        """
        Convert sensor data to a state index.
        
        Input: 
        - sensor_data (dict): {'left_corner': float, 'left': float, 'middle': float, 'right': float, 'right_corner': float}
        
        Output:
        - state (int): Index representing the state (0 to n_states-1).
        """
        state = 0
        # TODO: Implement state/discretization logic
        
        return state

    def Calculate_reward(self, state):
        """
        Compute reward for the current state.
        
        Input:
        - state (int): Current state index.
        
        Output:
        - reward (float): Reward value (e.g., +1 for line, -1 for lost).
        """
        reward = 0
        # TODO: Implement reward logic based on state
        
        return reward
    
    def is_deviated_alot(self, sensor_data):
        """
        Check if the robot has lost the line for too long.
        
        Input: 
        - sensor_data (dict)
        
        Output:
        - (bool): True if deviated/lost, False otherwise.
        """
        # TODO: Implement deviation check logic
        return False
        
    
    def update_q_table(self, state, action, reward, next_state):
        """
        Update Q-table using the Bellman equation.
        
        Input:
        - state (int): Current state.
        - action (int): Action taken.
        - reward (float): Received reward.
        - next_state (int): New state.
        """
        # TODO: Implement Q-learning update
        pass

    def choose_action(self, state):
        """
        Select an action using Epsilon-Greedy strategy.
        
        Input:
        - state (int): Current state.
        
        Output:
        - action (int): Selected action from self.action_list.
        """
        # TODO: Implement Epsilon-Greedy action selection
        return self.action_list[0] 

    def perform_action(self, action):
        """
        Convert action index to motor speeds.
        
        Input:
        - action (int): Action index.
        
        Output:
        - (left_speed, right_speed): Tuple of float speeds.
        """
        # TODO: Return motor speeds for the given action
        return 0, 0

    def save_q_table(self):
        """ Save Q-table to file. """
        with open(self.filename, 'wb') as f:
            pickle.dump({
                'q_table': self.q_table,
                'epsilon': self.epsilon,
                'n_action': self.n_actions,
                'n_states': self.n_states
            }, f)

    def load_q_table(self):
        """ Load Q-table from file. """
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                data = pickle.load(f)
            self.q_table = data.get('q_table', self.q_table)
            self.epsilon = data.get('epsilon', self.epsilon)
            self.n_actions = data.get('n_action', self.n_actions)
            self.n_states = data.get('n_states', self.n_states)
            return True
        return False
