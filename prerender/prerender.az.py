#!/usr/bin/python3

import subprocess
from multiprocessing import cpu_count
from collections import namedtuple
import math


def prepare_coordinates(x_min_20, x_max_20, y_min_20, y_max_20, zoom):
    Coordinates = namedtuple('Сoordinates', ['x_min', 'x_max', 'y_min', 'y_max'])
    coordinates = Coordinates(x_min=x_min_20 / 2 ** zoom,
                              x_max=x_max_20 / 2 ** zoom,
                              y_min=y_min_20 / 2 ** zoom,
                              y_max=y_max_20 / 2 ** zoom)
    return coordinates


def prerender(x_min_20, x_max_20, y_min_20, y_max_20, start_zoom, render_zoom, cmd_prefix):
    z_max = 20
    z = start_zoom
    while z <= render_zoom:
        coordinates = prepare_coordinates(x_min_20, x_max_20, y_min_20, y_max_20, z_max - z)
        cmd_args = ['-z{}'.format(z),
                    '-Z{}'.format(z),
                    '--min-x={}'.format(coordinates.x_min),
                    '--max-x={}'.format(coordinates.x_max),
                    '--min-y={}'.format(coordinates.y_min),
                    '--max-y={}'.format(coordinates.y_max)]
        cmd = cmd_prefix + cmd_args

        try:
            subprocess.run(cmd, check=True)
        except OSError as error:
            print(error)
            exit(1)

        z += 1


def min_max_coordinates(latdeg, londeg, distance):
    x_center, y_center = convert_coordinates(latdeg, londeg)
    Coordinates = namedtuple('Сoordinates', ['x_min', 'x_max', 'y_min', 'y_max'])
    coordinates = Coordinates(x_min=x_center-distance,
                              x_max=x_center+distance,
                              y_min=y_center-distance,
                              y_max=y_center+distance)
    return coordinates


def convert_coordinates(latdeg, londeg, zoom=20):
    latrad = math.radians(latdeg)
    n = 2.0 ** zoom
    xtile = int((londeg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(latrad) + (1 / math.cos(latrad))) / math.pi) / 2.0 * n)
    return xtile, ytile


def main():
    cmd_prefix = ['render_list', '-a', '-n {}'.format(cpu_count())]

    # WORLD
    cmd_args = ['-z1', '-Z8']
    cmd = cmd_prefix + cmd_args
    try:
        subprocess.run(cmd, check=True)
    except OSError as error:
        print(error)
        exit(1)

    # Azerbaijan
    prerender(x_min_20=654661,
              x_max_20=672927,
              y_min_20=389587,
              y_max_20=403008,
              start_zoom=9,
              render_zoom=16,
              cmd_prefix=cmd_prefix)

    # Baku 40°21′ с. ш. 49°50′ в. д. 2140 км²
    latdeg = 40.369566
    londeg = 49.835029
    distance = 1000
    coordinates = min_max_coordinates(latdeg, londeg, distance)
    prerender(x_min_20=coordinates.x_min,
              x_max_20=coordinates.x_max,
              y_min_20=coordinates.y_min,
              y_max_20=coordinates.y_max,
              start_zoom=13,
              render_zoom=20,
              cmd_prefix=cmd_prefix)

if __name__ == "__main__":
    main()
