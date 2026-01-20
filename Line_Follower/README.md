# PROJECT MANAS - RL Workshop

Welcome to the Reinforcement Learning Workshop by Project Manas! This boilerplate code is designed to help you get started with Q-learning for robot control in CoppeliaSim.

## Installation

1.  **Install Python 3**: Ensure you have Python 3 installed on your system.
2.  **Install CoppeliaSim**: Download and install CoppeliaSim Edu from [https://www.coppeliarobotics.com/downloads](https://www.coppeliarobotics.com/downloads).
3.  **Install Python Dependencies**:
    This project now uses the **ZeroMQ Remote API** directly. Install the required packages using the provided file:
    ```bash
    pip install -r requirements.txt
    ```

## File Overview

-   **`Qlearning.py`**: This is the core file where you will implement your Q-learning logic. You need to define the state space, reward function, and the Q-learning update rule.
-   **`Train.py`**: Runs the training loop. It connects directly to the simulator via ZMQ, runs for a set number of episodes, and saves the learned model.
-   **`Test.py`**: Runs the trained agent. It loads the saved Q-table and controls the robot based on the learned policy without updating the Q-values.
-   **`Connector.py`**: Handles the communication between the Python script and CoppeliaSim using the ZMQ Remote API.

## How to Run

1.  **Start CoppeliaSim**: Open the provided scene file `task_scene.ttt` in CoppeliaSim.
2.  **Run Training**:
    Open a terminal and run `Train.py`. You can specify the number of episodes:
    ```bash
    python3 Train.py --episodes 50
    ```
    This will start the training process. The Q-table will be saved to `q_table.pkl`.
3.  **Run Testing**:
    After training, run:
    ```bash
    python3 Test.py
    ```
    This will run the robot using the saved Q-table for evaluation.

## Tasks to Complete

Open `Qlearning.py` and implement the following functions:
1.  `Get_state(self, sensor_data)`: Convert raw sensor readings into a discrete state.
2.  `Calculate_reward(self, state)`: Define the reward function.
3.  `update_q_table(self, state, action, reward, next_state)`: Implement the Q-learning update equation.
4.  `choose_action(self, state)`: Implement epsilon-greedy action selection.
5.  `perform_action(self, action)`: Translate discrete actions into motor speeds.
6.  `is_deviated_alot(self, sensor_data)`: Implement logic to detect if the robot has lost the line.

Good luck!

## Reinforcement Learning Resources

To help you understand the core concepts, here is a brief explanation of the Q-Learning loop and some resources.

### The Q-Learning Loop

1.  **Observe State ($s$)**: The robot reads sensors to understand its current environment.
2.  **Choose Action ($a$)**: Even based on policy (e.g., $\epsilon$-greedy):
    -   **Explore**: Choose a random action to discover new possibilities.
    -   **Exploit**: Choose the action with the highest Q-value for the current state.
3.  **Perform Action**: The robot moves (e.g., sets motor speeds).
4.  **Receive Reward ($r$)**: The environment provides feedback (positive for good behavior, negative for bad).
5.  **Observe New State ($s'$)**: Read sensors again to see where the robot ended up.
6.  **Update Q-Table**: Update the Q-value for the previous state-action pair using the Bellman Equation:
    $$Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma \max_{a'} Q(s', a') - Q(s, a)]$$
    -   $\alpha$ (alpha): Learning rate (how much we accept new information).
    -   $\gamma$ (gamma): Discount factor (importance of future rewards).

### Useful Links
-   **Q-Learning Explained (GeeksforGeeks)**: [https://www.geeksforgeeks.org/q-learning-in-python/](https://www.geeksforgeeks.org/q-learning-in-python/)
