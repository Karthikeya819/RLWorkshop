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
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import time
import sys

class CoppeliaClient:
    def __init__(self):
        self.client = None
        self.sim = None
        self.left_motor = None
        self.right_motor = None
        self.vision_sensor = None # Example sensor
        self.default_speed = 2 # Default speed

    def connect(self):
        """
        Connects to CoppeliaSim using ZMQ Remote API.
        Attempts to get handles for motors and sensors.
        """
        print("[CONNECTOR] Connecting to CoppeliaSim via ZMQ...")
        try:
            self.client = RemoteAPIClient()
            self.sim = self.client.require('sim')
            
            # Retrieved from user-provided Scene Hierarchy image
            try:
                # Motors
                self.left_motor = self.sim.getObject('/DynamicLeftJoint') 
                self.right_motor = self.sim.getObject('/DynamicRightJoint')
                
                # Sensors
                # Mapping: Code Key -> CoppeliaSim Object Name
                self.sensor_map = {
                    'left_corner': '/LeftcornerSensor',
                    'left': '/LeftSensor',
                    'middle': '/MiddleSensor',
                    'right': '/RightSensor',
                    'right_corner': '/RightcornerSensor'
                }
                
                self.sensors = {}
                for key, name in self.sensor_map.items():
                    self.sensors[key] = self.sim.getObject(name)
                
                print("[CONNECTOR] Successfully connected and retrieved object handles.")
            except Exception as e:
                print(f"[CONNECTOR] Connected, but could not find some objects: {e}")
                print("[CONNECTOR] Ensure object names (LeftcornerSensor, LeftSensor, etc.) function in your scene.")
                
        except Exception as e:
            print(f"[CONNECTOR] Failed to connect to CoppeliaSim: {e}")
            sys.exit(1)

    def start_simulation(self):
        if self.sim:
            print("[CONNECTOR] Starting simulation...")
            self.sim.startSimulation()

    def stop_simulation(self):
        if self.sim:
            print("[CONNECTOR] Stopping simulation...")
            self.sim.stopSimulation()
            while self.sim.getSimulationState() != self.sim.simulation_stopped:
                time.sleep(0.1)

    def send_motor_command(self, left_speed, right_speed):
        """
        Sets the target velocity for the motors.
        """
        if self.sim and self.left_motor and self.right_motor:
            self.sim.setJointTargetVelocity(self.left_motor, left_speed)
            self.sim.setJointTargetVelocity(self.right_motor, right_speed)

    def receive_sensor_data(self):
        """
        Retrieves sensor data.
        Returns a dictionary of sensor readings with keys:
        ['left_corner', 'left', 'middle', 'right', 'right_corner']
        """
        data = {}
        if self.sim and hasattr(self, 'sensors'):
            for key, handle in self.sensors.items():
                # readVisionSensor returns (result, auxiliaryValues, auxiliaryPacketData)
                response = self.sim.readVisionSensor(handle)
                # print(f"DEBUG {key}: {response}") # Uncomment to see raw data
                
                val = 0.0
                if isinstance(response, (list, tuple)):
                    # response[0] is detection state (bool-like or -1)
                    # response[1] is auxValues (list of 15 floats)
                    
                    aux_values = response[1]
                    if aux_values and len(aux_values) > 0:
                        # Try index 10 (standard), else 0, else 1
                        # Often index 10 is intensity, but sometimes it depends on the filter
                        if len(aux_values) > 10:
                            val = aux_values[10]
                        else:
                            val = aux_values[0]
                    else:
                         val = response[0] # Fallback
                else:
                    val = response

                data[key] = val 
                
        return data if data else None

    def close(self):
        pass
