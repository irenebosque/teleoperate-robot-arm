'''
Author: Irene Bosque, https://github.com/irenebosque
Date: 17/6/21
'''


import pygame

pygame.display.init()
pygame.joystick.init()
pygame.joystick.Joystick(0).init()
pygame.event.pump()

class feedbackJoystick:
    def __init__(self):
        self.joystick_axis = None


    def get_h(self):
        x_axis = pygame.joystick.Joystick(0).get_axis(0)
        y_axis = pygame.joystick.Joystick(0).get_axis(1)
        z_axis = pygame.joystick.Joystick(0).get_axis(4)
        trigger_axis = pygame.joystick.Joystick(0).get_axis(2)
        self.buttonA = pygame.joystick.Joystick(0).get_button(0)


        # My axes were inverted, that's the reason of the "-1"
        self.joystick_axis = [x_axis, -1 * y_axis, -1 * z_axis, trigger_axis]

        return self.joystick_axis

    def ask_for_done(self):
        if self.buttonA == 1:
            done = True
        else:
            done = False
        return done


