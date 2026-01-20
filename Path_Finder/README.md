# PROJECT MANAS - RL Workshop

Welcome to the Reinforcement Learning Workshop!

This boilerplate code is designed to help you implement and train a Q-Learning Agent to navigate a GridWorld.

## Goal
The goal is to teach the Robot (Agent) to navigate through the grid, avoid obstacles, and reach the Manas Logo (Goal).

## Project Structure
- `train.py`: The main training loop. **(Make changes here!)**
- `test.py`: Visualizes the trained agent.
- `QLearning.py`: Contains the core Q-Learning logic, rewards, and action selection. **(Make changes here!)**
- `env.py`: The GridWorld environment. (No changes needed usually)

## Setup

1. **Create and Activate Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # venv\Scripts\activate   # Windows
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## YOUR TASK

Look for `[WORKSHOP]` comments in the code. These mark the places where you need to implement logic or tune parameters.

### 1. Define Q-Learning Logic
Open **`QLearning.py`** and implement the following functions:
- `get_reward(state, goal_state)`: Define the reward for reaching the goal vs stepping.
- `get_action(...)`: Implement **Epsilon-Greedy** strategy (Explore vs Exploit).
- `update_q_table(...)`: Implement the **Bellman Equation** to update Q-values.

### 2. Hyperparameter Tuning
Open **`train.py`** and adjust the parameters:
- `alpha`: Learning Rate.
- `gamma`: Discount Factor.
- `epsilon`: Exploration Rate.

## Running the Code

### 1. Train the Agent
Once you have implemented the logic, run the training script:
```bash
python train.py
```
*Options:*
- `python train.py --fast` (Train instantly without visualization)
- `python train.py --speed 0.1` (Train slowly to watch)

### 2. Test the Agent
After training, run the test script to see your agent in action!
```bash
python test.py
```

## Troubleshooting
- If `NameError: name 'pygame' is not defined`: Ensure you have `import pygame` (it should be there).
- If the agent spins in circles: Check your Reward function in `QLearning.py`.
- If the agent never explores: Check your Epsilon in `train.py`.

Good Luck!
