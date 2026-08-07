from pyray import *

def build_cube():
    # build_cube() # trying to build a cube
    vec = Vector3(30,30,0)
    draw_cube(vec, 100, 100, 10, GREEN)

def build_billboard():
    pass

def begin_camera():
    begin_mode_3d(Camera3D(Vector3(10,10,0)))

# TODO: build a box
# TODO: slide the box
# TODO: add tween to the box
    
def main():
    init_window(800, 450, "A 3d world")

    camera = Camera3D()
    camera.position = Vector3(0.2, 0.4, 0.4)
    camera.target = Vector3(0.185, 0.4, 0.0)
    camera.up = Vector3(0.0, 1.0, 0.0)
    camera.fovy = 45.0

    disable_cursor()
    set_target_fps(60)

    while not window_should_close():

        begin_drawing()

        clear_background(WHITE)

        begin_mode_3d(camera)
        draw_text("Hello worl d", 190, 200, 20, VIOLET)



        build_cube()

        draw_fps(10,10)


        end_drawing()
    close_window()

if __name__ == "__main__":
    main()
  