'''
*
*   ===================================================
*       PROJECT MANAS - RL Workshop
*   ===================================================
*
*  This script is intended to be a Boilerplate for 
*  Training the Q-Learning Agent.
*
*  Filename:		Train.py
*  Author:		    PROJECT MANAS
*
*  This software is made available on an "AS IS WHERE IS BASIS".
*
*****************************************************************************************
'''
import time
import signal
import sys
import argparse

# Import required modules for communication and Q-learning
from Connector import CoppeliaClient       
from Qlearning_key import QLearningController 

# Flag to handle graceful shutdown when Ctrl+C is pressed
stop_requested = False

def signal_handler(sig, frame):
    """
    Signal handler for keyboard interrupt (Ctrl+C).
    It sets the stop_requested flag to exit the training loop safely.
    """
    global stop_requested
    print("\n[TRAIN] Interrupt received. Stopping training gracefully...")
    stop_requested = True

# Register the signal handler to handle SIGINT
signal.signal(signal.SIGINT, signal_handler)

def main():
    """
    Main training loop with Episode support.
    """
    global stop_requested

    # Parse arguments
    parser = argparse.ArgumentParser(description='Train Q-Learning Agent')
    parser.add_argument('--episodes', type=int, default=50, help='Number of episodes to train')
    args = parser.parse_args()

    SAVE_INTERVAL = 100  # Save Q-table to disk every N iterations

    # === Initialize Q-learning Controller ===
    ql = QLearningController()

    # Load existing Q-table if it exists (resumes training from last session)
    ql.load_q_table()

    # === Connect to the CoppeliaSim simulator ===
    client = CoppeliaClient()
    client.connect()

    print(f"[TRAIN] Starting training for {args.episodes} episodes...")

    for episode in range(args.episodes):
        if stop_requested:
            break

        print(f"--- Episode {episode + 1}/{args.episodes} ---")
        client.start_simulation()
        
        iteration = 0
        prev_state = None
        prev_action = None
        
        while not stop_requested:
            sensor_data = client.receive_sensor_data()
            
            if not sensor_data:
                time.sleep(0.05)
                continue  # Skip iteration if sensor data is invalid

            if ql.is_deviated_alot(sensor_data):
                print(f"[TRAIN] Episode {episode + 1} finished at iteration {iteration}")
                break

            state = ql.Get_state(sensor_data)

            if prev_state is not None and prev_action is not None:
                reward = ql.Calculate_reward(state)
                ql.update_q_table(prev_state, prev_action, reward, state)

            action = ql.choose_action(state)

            left_speed, right_speed = ql.perform_action(action)

            client.send_motor_command(left_speed, right_speed)

            prev_state = state
            prev_action = action

            iteration += 1  # Increment training step count

            if iteration % SAVE_INTERVAL == 0:
                ql.save_q_table()

            time.sleep(0.05)
        
        # Decay epsilon after each episode
        ql.decay_epsilon()

        client.stop_simulation()
        time.sleep(1.0)

    ql.save_q_table()
    client.close()
    print("[TRAIN] Training stopped and Q-table saved.")

# Script entry point
if __name__ == "__main__":
    main()
