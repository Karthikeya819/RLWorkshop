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
import time
import signal
import sys

from Connector import CoppeliaClient      
from Qlearning_key import QLearningController 

stop_requested = False

def signal_handler(sig, frame):
    """
    Signal handler to catch keyboard interrupt (Ctrl+C).
    It sets a flag to stop the main testing loop gracefully.
    """
    global stop_requested
    print("\n[TEST] Interrupt received. Stopping testing gracefully...")
    stop_requested = True

signal.signal(signal.SIGINT, signal_handler)

def main():
    global stop_requested

    ql = QLearningController()
    ql.epsilon = 0.01 # Test with exploitation only
    
    loaded = ql.load_q_table()
    if not loaded:
        print("[TEST] No Q-table found. Exiting.")
        return

    client = CoppeliaClient()
    client.connect()
    print("[TEST] Connected to CoppeliaSim.")
    
    client.start_simulation()

    print("[TEST] Starting test loop...")

    while not stop_requested:
        sensor_data = client.receive_sensor_data()
        if not sensor_data:
            time.sleep(0.05)  
            continue
        state = ql.Get_state(sensor_data)

        action = ql.choose_action(state)

        left_speed, right_speed = ql.perform_action(action)

        #  Send the motor command to the simulator
        client.send_motor_command(left_speed, right_speed)

        time.sleep(0.05)

    client.stop_simulation()
    
    client.close()  
    print("[TEST] Testing stopped.")


# Entry point for the script
if __name__ == "__main__":
    main()
