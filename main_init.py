'''
Author: Irene Bosque, https://github.com/irenebosque
Date: 17/6/21
'''

from metaworld.envs import (ALL_V2_ENVIRONMENTS_GOAL_OBSERVABLE)
from feedback_joystick import feedbackJoystick


# Create environment
plate_slide_goal_observable_cls = ALL_V2_ENVIRONMENTS_GOAL_OBSERVABLE["plate-slide-v2-goal-observable"]
env = plate_slide_goal_observable_cls()
observation = env.reset()
env.render()


# Joystick
feedback_joystick = feedbackJoystick()


# General parameters
max_num_of_episodes = 10
max_time_steps_episode = 500
initial_action = [0,0,0,0]