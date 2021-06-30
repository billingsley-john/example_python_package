
import paramak as p

def multiply_two_numbers(number_1, number_2):
    return number_1 * number_2

def make_example_paramak_shape(height, inner_radius, outer_radius, rotation_angle):

    shape = p.CenterColumnShieldCylinder(
        height=height,
        inner_radius=inner_radius,
        outer_radius=outer_radius,
        rotation_angle=rotation_angle
    )

    return shape