from pyray import *
import math
import random

def main():
    init_window(900, 500, "3d movement")
    rl_set_line_width(3)
    camera = Camera3D((0,0.5,0), (1,.5,1), (0,1,0), 60, CAMERA_PERSPECTIVE)
    map_size = 10

    while not window_should_close():
        begin_drawing()

        clear_background(SKYBLUE)
        begin_mode_3d(camera)

        draw_grid(map_size * 10, 0.2)
        draw_plane((0, -.01, 0),(map_size * 2, map_size * 2), WHITE)

        end_mode_3d()


        end_drawing()


if __name__ == "__main__":
    main()