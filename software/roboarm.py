from time import sleep
import motors


class Gripper():

    def __init__(self):
        # init gripper to close
        self.opening_value = 0

    def set_gripper(self, value, speed):                                        # speed is meant as value from 1 to 100
        speed = 1/speed                                                         # TODO: ensure, that speed cannot be 0 (would be div / 0)(try/except)
        if self.opening_value > value:
            for self.opening_value > value:
                # move servo -1
                self.opening_value -= 1
                sleep(speed)
        if self.opening_value < value:
            for self.opening_value < value:
                # move servo +1
                opening_value += 1
                sleep(speed)


class Axis():

    def __init__(self):
        self.rotation_angle

    def set_rotation_angle(self, value, speed):                                 # speed is meant as value from 1 to 100
        speed = 1/speed                                                         # TODO: ensure, that speed cannot be 0 (would be div / 0)(try/except)
        if self.rotation_angle > value:
            for self.rotation_angle > value:
                # move servo -1
                self.rotation_angle -= 1
                sleep(speed)
        if self.rotation_angle < value:
            for self.rotation_angle < value:
                # move servo +1
                self.rotation_angle += 1
                sleep(speed)
