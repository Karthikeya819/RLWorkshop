'''
*
*   ===================================================
*       PROJECT MANAS - RL Workshop
*   ===================================================
*
*  This script contains the Custom GridWorld Environment
*  for the Q-Learning Agent.
*
*  Filename:		env.py
*  Author:		    PROJECT MANAS
*
*  This software is made available on an "AS IS WHERE IS BASIS".
*
*****************************************************************************************
'''
import numpy as np
import pygame
import time

class GridWorld:
    def __init__(self):
        self.height = 6
        self.width = 6
        self.grid_size = 100
        self.window_size = (self.width * self.grid_size, self.height * self.grid_size)
        
        self.start_state = (0, 0)
        self.goal_state = (5, 0)
        self.agent_pos = self.start_state
        
        self.obstacles = [
            (2, 0), (2, 1),
            (1, 4), (2, 4),
            (5, 4), (5, 5)
        ]
        
        self.actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        self.action_space_size = len(self.actions)
        
        # Pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("RL GridWorld")
        self.font = pygame.font.SysFont(None, 36)
        
        # Load Images
        self.agent_img = None
        self.goal_img = None
        try:
            self.agent_img = pygame.image.load('assets/agent.png')
            self.agent_img = pygame.transform.scale(self.agent_img, (self.grid_size, self.grid_size))
            self.goal_img = pygame.image.load('assets/goal.png')
            self.goal_img = pygame.transform.scale(self.goal_img, (self.grid_size, self.grid_size))
        except:
            pass # Keep None, use shapes logic
        
    def reset(self):
        self.agent_pos = self.start_state
        return self.agent_pos
        
    def step(self, action_idx):
        action = self.actions[action_idx]
        x, y = self.agent_pos
        
        dx, dy = 0, 0
        if action == 'UP':
            dy = 1
        elif action == 'DOWN':
            dy = -1
        elif action == 'LEFT':
            dx = -1
        elif action == 'RIGHT':
            dx = 1
            
        new_x = x + dx
        new_y = y + dy
        
        if new_x < 0 or new_x >= self.width or new_y < 0 or new_y >= self.height:
            new_x, new_y = x, y
        
        if (new_x, new_y) in self.obstacles:
            new_x, new_y = x, y
            
        self.agent_pos = (new_x, new_y)
        
        done = False
        reward = -1
        
        if self.agent_pos == self.goal_state:
            reward = 100
            done = True
            
        return self.agent_pos, reward, done
        
    def render(self, mode='human'):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        self.screen.fill((30, 30, 30))
        
        for x in range(0, self.window_size[0], self.grid_size):
            pygame.draw.line(self.screen, (60, 60, 60), (x, 0), (x, self.window_size[1]))
        for y in range(0, self.window_size[1], self.grid_size):
            pygame.draw.line(self.screen, (60, 60, 60), (0, y), (self.window_size[0], y))
            
        def to_pixels(pos):
            logical_x, logical_y = pos
            px = logical_x * self.grid_size
            py = (self.height - 1 - logical_y) * self.grid_size
            return px, py
            
        for obs in self.obstacles:
            px, py = to_pixels(obs)
            pygame.draw.rect(self.screen, (200, 200, 200), (px, py, self.grid_size, self.grid_size))
          # Draw Goal
        goal_px, goal_py = to_pixels(self.goal_state)
        
        if self.goal_img:
            self.screen.blit(self.goal_img, (goal_px, goal_py))
        else:
            center_x = goal_px + self.grid_size // 2
            center_y = goal_py + self.grid_size // 2
            
            points = [
                (center_x, goal_py + 10),
                (goal_px + 10, goal_py + self.grid_size - 10),
                (goal_px + self.grid_size - 10, goal_py + self.grid_size - 10)
            ]
            pygame.draw.polygon(self.screen, (255, 165, 0), points)
        
        # Draw Agent
        agent_px, agent_py = to_pixels(self.agent_pos)
        
        if self.agent_img:
            self.screen.blit(self.agent_img, (agent_px, agent_py))
        else:
            pygame.draw.circle(self.screen, (100, 100, 255), (agent_px + self.grid_size // 2, agent_py + self.grid_size // 2), 30)
        
        pygame.display.flip()
        
    def close(self):
        pygame.quit()
