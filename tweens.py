from math import pi, sin, cos, pow

# fast at the start, then slows down at the end
def ease_out_sine(x: float) -> float:
    return sin((x * pi) / 2)

# slow to fast
def ease_in_quad(x: float) -> float:
    return x * x

# fast at the start, overshoots, then slowly bounces back
def ease_out_back(x: float) -> float:
    c1 = 1.70158
    c3 = c1 + 1
    return 1 + c3 * pow(x - 1, 3) + c1 * pow(x - 1, 2)

# goes below start, then increases to end
def ease_in_back(x: float) -> float:
    c1 = 1.70158
    c3 = c1 + 1

    return c3 * x * x * x - c1 * x * x