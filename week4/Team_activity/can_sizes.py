# Import the standard math module so that
# math.pi can be used in this program.
import math


def main():
    name = "#1 Picnic"
    radius = 6.83
    height = 10.16
    volume = cylinder_volume(radius, height)
    surf_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.2f}")

    name = "#1 Tall"
    radius = 7.78
    height = 11.91
    volume = cylinder_volume(radius, height)
    surf_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.2f}")

    name = "#2"
    radius = 8.73
    height = 11.59
    volume = cylinder_volume(radius, height)
    surf_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.2f}")

    name = "#2.5"
    radius = 10.32
    height = 11.91
    volume = cylinder_volume(radius, height)
    surf_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.2f}")

    name = "#3 Cylinder"
    radius = 10.79
    height = 17.78
    volume = cylinder_volume(radius, height)
    surf_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.2f}")

    name = "#5"
    radius = 13.02
    height = 14.29
    volume = cylinder_volume(radius, height)
    surf_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.2f}")

    name = "#6Z"
    radius = 5.4
    height = 8.89
    volume = cylinder_volume(radius, height)
    surf_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.2f}")

    name = "#8Z short"
    radius = 6.83
    height = 7.62
    volume = cylinder_volume(radius, height)
    surf_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.2f}")

    name = "#10"
    radius = 15.72
    height = 17.78
    volume = cylinder_volume(radius, height)
    surf_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.2f}")

    name = "#211"
    radius = 6.83
    height = 12.38
    volume = cylinder_volume(radius, height)
    surf_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.2f}")

    name = "#300"
    radius = 7.62
    height = 11.27
    volume = cylinder_volume(radius, height)
    surf_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.2f}")

    name = "#303"
    radius = 8.1
    height = 11.11
    volume = cylinder_volume(radius, height)
    surf_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.2f}")

def compute_storage_efficiency(radius, height):
    """Compute and return the storage efficiency of a steel can size.
    The storage efficiency is the volume of the can divided by its
    surface area.

    Parameters
        radius: the radius of the steel can
        height: the height of the steel can
    Return: the storage efficiency of the steel can
    """
    volume = cylinder_volume(radius, height)
    surf_area = cylinder_surface_area(radius, height)
    efficiency = volume / surf_area
    return efficiency

def cylinder_volume(radius, height):
    """Compute and return the volume of a cylinder.

    Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: the volume of the cylinder
    """
    volume = math.pi * radius**2 * height
    return volume


def cylinder_surface_area(radius, height):
    """Compute and return the surface area of a cylinder.

    Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: the surface area of the cylinder
    """
    surf_area = 2 * math.pi * radius * (radius + height)
    return surf_area


# Start this program by
# calling the main function.
main()