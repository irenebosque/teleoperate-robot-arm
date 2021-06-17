'''
Author: Irene Bosque, https://github.com/irenebosque
Date: 17/6/21
'''

from main_init import env, max_num_of_episodes, max_time_steps_episode, feedback_joystick, initial_action
import numpy as np

# Start training loop
for i_episode in range(max_num_of_episodes):
    print('Starting episode number: ', i_episode)

    # reset environment at the beginning of the episode
    observation = env.reset()
    action = np.array(initial_action)


    # Iterate over the episode
    for t in range(int(max_time_steps_episode)):
        env.render()  # Make the environment visible
        if (t % 10 == 0):
            print("Time step: ", t)
            print('Action: ', action, '\n')

        # Get the feedback from the joystick
        action = feedback_joystick.get_h()
        action = np.array(action)


        # Apply the action into the environment
        observation, reward, environment_done, info = env.step(action)

        if info['success'] == 0:
            environment_done = False
        else:
            environment_done = True


        # Compute done
        done = feedback_joystick.ask_for_done() or environment_done

        # End of episode
        if done:
            break



