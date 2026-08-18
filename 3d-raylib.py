import utils.transport
import utils.session
from pyray import *
import math
import random

# TODO: tween the cube


def main():
    init_window(900, 500, "3d movement")
    rl_set_line_width(3)
    camera = Camera3D((0,0.5,0), (1,.5,1), (0,1,0), 60, CAMERA_PERSPECTIVE)
    map_size = 3
    player = Player()

    # build the cabinet once
    cabinet = Cube()
    drawer = Cube()


    while not window_should_close():
        player.controls()
        camera.position =  player.pos
        camera.target = vector3_add(player.pos, player.direction)

        begin_drawing()

        clear_background(SKYBLUE)
        begin_mode_3d(camera)

        draw_grid(map_size * 10, 0.2)
        draw_plane((0, -.01, 0),(map_size * 2, map_size * 2), WHITE)

        # TODO: make a drawer in the cabinet, and make it slide in and out
        draw_cube(cabinet.pos, 0.4, 1.0, 0.25, GRAY)


        # this moves the cube between two places -- use this to open and close it
        if is_key_down(KEY_T):
            cube.move_cube(Vector3(1, 0.0, 1))
            draw_cube(cube.pos, 0.4, 1.0, 0.25, GRAY)

        if is_key_down(KEY_Q):
            cube.move_cube(Vector3(1, 0.0, .5))
            draw_cube(cube.pos, 0.4, 1.0, 0.25, GRAY)

        end_mode_3d()


        end_drawing()

class Cube():
    def __init__(self) -> None:
        # TODO hardcoded, should change in the future to take user input
        self.pos = (Vector3(1, 0.0, 0.5))
    def move_cube(self, new_pos: Vector3) -> None:
        self.pos = new_pos

class Player():

    def __init__(self) -> None:
        self.pos = Vector3(0.0, 0.5, 0.0)
        self.yaw = 0
        self.pitch = 0
        self.sensitivity = .003
        self.direction = Vector3(1, 0, 1)
        self.speed = 2
        disable_cursor()

    def controls(self):
        speed = get_frame_time() * self.speed
        mouse_delta = get_mouse_delta()
        self.yaw -= mouse_delta.x * self.sensitivity
        self.pitch = max(-1.57, min(1.57, self.pitch - mouse_delta.y * self.sensitivity))
        sin_yaw, cos_yaw = math.sin(self.yaw), math.cos(self.yaw)

        # adjust camera direction
        self.direction.x = math.cos(self.pitch) * sin_yaw
        self.direction.y = math.sin(self.pitch)
        self.direction.z = math.cos(self.pitch) * cos_yaw

        forward = is_key_down(KEY_W) - is_key_down(KEY_S)
        sideward = is_key_down(KEY_D) - is_key_down(KEY_A)

        if forward != 0 and sideward != 0:
            speed *= .707

        nx, nz = self.pos.x, self.pos.z

        nx += speed * (sin_yaw * forward - cos_yaw * sideward)
        nz += speed * (cos_yaw * forward + sin_yaw * sideward)

        self.pos.x, self.pos.z = nx, nz

if __name__ == "__main__":
    main()