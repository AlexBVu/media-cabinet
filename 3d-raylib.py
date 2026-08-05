from pyray import *
import math
import random

def main():
    init_window(900, 500, "3d movement")
    rl_set_line_width(3)
    camera = Camera3D((0,0.5,0), (1,.5,1), (0,1,0), 60, CAMERA_PERSPECTIVE)
    map_size = 10
    player = Player()

    while not window_should_close():
        player.controls()
        camera.position =  player.pos
        camera.target = vector3_add(player.pos, player.direction)

        begin_drawing()

        clear_background(SKYBLUE)
        begin_mode_3d(camera)

        draw_grid(map_size * 10, 0.2)
        draw_plane((0, -.01, 0),(map_size * 2, map_size * 2), WHITE)

        end_mode_3d()


        end_drawing()

class Player():

    def __init__(self) -> None:
        self.pos = Vector3(1.5, 0.5, 1.5)
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