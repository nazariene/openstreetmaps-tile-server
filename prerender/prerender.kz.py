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

    # Казахстан
    prerender(x_min_20=659708,
              x_max_20=778612,
              y_min_20=329404,
              y_max_20=394796,
              start_zoom=9,
              render_zoom=12,
              cmd_prefix=cmd_prefix)

    # Алма-Ата 1801713 43°15′ с. ш. 76°54′ в. д. 682 км²
    latdeg = 43.25
    londeg = 76.90
    distance = 1000
    coordinates = min_max_coordinates(latdeg, londeg, distance)
    prerender(x_min_20=coordinates.x_min,
              x_max_20=coordinates.x_max,
              y_min_20=coordinates.y_min,
              y_max_20=coordinates.y_max,
              start_zoom=13,
              render_zoom=17,
              cmd_prefix=cmd_prefix)

    # Астана 1032475 51°08′ с. ш. 71°26′ в. д. 797,33 км²
    latdeg = 51.13333
    londeg = 71.43333
    distance = 1000
    coordinates = min_max_coordinates(latdeg, londeg, distance)
    prerender(x_min_20=coordinates.x_min,
              x_max_20=coordinates.x_max,
              y_min_20=coordinates.y_min,
              y_max_20=coordinates.y_max,
              start_zoom=13,
              render_zoom=17,
              cmd_prefix=cmd_prefix)

    # Шымкент 951605 42°18′ с. ш. 69°36′ в. д. 1162,8 км²
    latdeg = 42.30000
    londeg = 69.60000
    distance = 1000
    coordinates = min_max_coordinates(latdeg, londeg, distance)
    prerender(x_min_20=coordinates.x_min,
              x_max_20=coordinates.x_max,
              y_min_20=coordinates.y_min,
              y_max_20=coordinates.y_max,
              start_zoom=13,
              render_zoom=17,
              cmd_prefix=cmd_prefix)

    # Караганда 501097 49°48′ с. ш. 73°07′ в. д. 550 км²
    latdeg = 49.80000
    londeg = 73.11667
    distance = 500
    coordinates = min_max_coordinates(latdeg, londeg, distance)
    prerender(x_min_20=coordinates.x_min,
              x_max_20=coordinates.x_max,
              y_min_20=coordinates.y_min,
              y_max_20=coordinates.y_max,
              start_zoom=13,
              render_zoom=17,
              cmd_prefix=cmd_prefix)

    # Актобе 420151 50°18′ с. ш. 57°10′ в. д. 297,39 км²
    latdeg = 50.30000
    londeg = 57.16667
    distance = 400
    coordinates = min_max_coordinates(latdeg, londeg, distance)
    prerender(x_min_20=coordinates.x_min,
              x_max_20=coordinates.x_max,
              y_min_20=coordinates.y_min,
              y_max_20=coordinates.y_max,
              start_zoom=13,
              render_zoom=17,
              cmd_prefix=cmd_prefix)

    # Тараз 356461 42°53′ с. ш. 71°22′ в. д. 788,97 км²
    latdeg = 42.88333
    londeg = 71.36667
    distance = 500
    coordinates = min_max_coordinates(latdeg, londeg, distance)
    prerender(x_min_20=coordinates.x_min,
              x_max_20=coordinates.x_max,
              y_min_20=coordinates.y_min,
              y_max_20=coordinates.y_max,
              start_zoom=13,
              render_zoom=17,
              cmd_prefix=cmd_prefix)

    # Павлодар 334906 52°18′56″ с. ш. 76°57′23″ в. д. 400 км²
    latdeg = 52.31556
    londeg = 76.95639
    distance = 400
    coordinates = min_max_coordinates(latdeg, londeg, distance)
    prerender(x_min_20=coordinates.x_min,
              x_max_20=coordinates.x_max,
              y_min_20=coordinates.y_min,
              y_max_20=coordinates.y_max,
              start_zoom=13,
              render_zoom=17,
              cmd_prefix=cmd_prefix)

    # Усть-Каменогорск 329048 49°57′ с. ш. 82°37′ в. д. 543,15 км²
    latdeg = 49.95000
    londeg = 82.61667
    distance = 400
    coordinates = min_max_coordinates(latdeg, londeg, distance)
    prerender(x_min_20=coordinates.x_min,
              x_max_20=coordinates.x_max,
              y_min_20=coordinates.y_min,
              y_max_20=coordinates.y_max,
              start_zoom=13,
              render_zoom=17,
              cmd_prefix=cmd_prefix)

    # Семей 321842 50°24′40″ с. ш. 80°13′39″ в. д. 210 м²
    latdeg = 50.41111
    londeg = 80.22750
    distance = 300
    coordinates = min_max_coordinates(latdeg, londeg, distance)
    prerender(x_min_20=coordinates.x_min,
              x_max_20=coordinates.x_max,
              y_min_20=coordinates.y_min,
              y_max_20=coordinates.y_max,
              start_zoom=13,
              render_zoom=17,
              cmd_prefix=cmd_prefix)

    # Костанай 239532 53°13′09″ с. ш. 63°38′03″ в. д. 240 км²
    latdeg = 53.219333
    londeg = 63.634194
    distance = 300
    coordinates = min_max_coordinates(latdeg, londeg, distance)
    prerender(x_min_20=coordinates.x_min,
              x_max_20=coordinates.x_max,
              y_min_20=coordinates.y_min,
              y_max_20=coordinates.y_max,
              start_zoom=13,
              render_zoom=17,
              cmd_prefix=cmd_prefix)

    # Атырау 237298 47°07′ с. ш. 51°53′ в. д. ?
    latdeg = 47.11667
    londeg = 51.88333
    distance = 250
    coordinates = min_max_coordinates(latdeg, londeg, distance)
    prerender(x_min_20=coordinates.x_min,
              x_max_20=coordinates.x_max,
              y_min_20=coordinates.y_min,
              y_max_20=coordinates.y_max,
              start_zoom=13,
              render_zoom=17,
              cmd_prefix=cmd_prefix)

    # Кызылорда 236087 44°51′ с. ш. 65°31′ в. д. 240 км²
    latdeg = 44.85000
    londeg = 65.51667
    distance = 250
    coordinates = min_max_coordinates(latdeg, londeg, distance)
    prerender(x_min_20=coordinates.x_min,
              x_max_20=coordinates.x_max,
              y_min_20=coordinates.y_min,
              y_max_20=coordinates.y_max,
              start_zoom=13,
              render_zoom=17,
              cmd_prefix=cmd_prefix)

    # Уральск 235749 51°14′ с. ш. 51°22′ в. д. 700 км²
    latdeg = 51.23333
    londeg = 51.36667
    distance = 300
    coordinates = min_max_coordinates(latdeg, londeg, distance)
    prerender(x_min_20=coordinates.x_min,
              x_max_20=coordinates.x_max,
              y_min_20=coordinates.y_min,
              y_max_20=coordinates.y_max,
              start_zoom=13,
              render_zoom=17,
              cmd_prefix=cmd_prefix)

    # Петропавловск 217106 54°51′44″ с. ш. 69°08′27″ в. д. 224,9 км²
    latdeg = 54.86222
    londeg = 69.14083
    distance = 250
    coordinates = min_max_coordinates(latdeg, londeg, distance)
    prerender(x_min_20=coordinates.x_min,
              x_max_20=coordinates.x_max,
              y_min_20=coordinates.y_min,
              y_max_20=coordinates.y_max,
              start_zoom=13,
              render_zoom=17,
              cmd_prefix=cmd_prefix)

    # Актау 183581 43°39′ с. ш. 51°09′ в. д. 76,48 км²
    latdeg = 43.65000
    londeg = 51.15000
    distance = 200
    coordinates = min_max_coordinates(latdeg, londeg, distance)
    prerender(x_min_20=coordinates.x_min,
              x_max_20=coordinates.x_max,
              y_min_20=coordinates.y_min,
              y_max_20=coordinates.y_max,
              start_zoom=13,
              render_zoom=17,
              cmd_prefix=cmd_prefix)

    # Темиртау 178880 50°04′ с. ш. 72°58′ в. д. 296,1 км²
    latdeg = 50.06667
    londeg = 72.96667
    distance = 200
    coordinates = min_max_coordinates(latdeg, londeg, distance)
    prerender(x_min_20=coordinates.x_min,
              x_max_20=coordinates.x_max,
              y_min_20=coordinates.y_min,
              y_max_20=coordinates.y_max,
              start_zoom=13,
              render_zoom=17,
              cmd_prefix=cmd_prefix)

    # Туркестан 161251 43°18′00″ с. ш. 68°14′37″ в. д. 196,27 км²
    latdeg = 43.30000
    londeg = 68.24361
    distance = 200
    coordinates = min_max_coordinates(latdeg, londeg, distance)
    prerender(x_min_20=coordinates.x_min,
              x_max_20=coordinates.x_max,
              y_min_20=coordinates.y_min,
              y_max_20=coordinates.y_max,
              start_zoom=13,
              render_zoom=17,
              cmd_prefix=cmd_prefix)

    # Кокшетау 145762 53°17′30″ с. ш. 69°23′30″ в. д. 400 км²
    latdeg = 53.29167
    londeg = 69.39167
    distance = 200
    coordinates = min_max_coordinates(latdeg, londeg, distance)
    prerender(x_min_20=coordinates.x_min,
              x_max_20=coordinates.x_max,
              y_min_20=coordinates.y_min,
              y_max_20=coordinates.y_max,
              start_zoom=13,
              render_zoom=17,
              cmd_prefix=cmd_prefix)

    # Талдыкорган 145732 45°01′ с. ш. 78°22′ в. д. 100 км²
    latdeg = 45.01667
    londeg = 78.36667
    distance = 200
    coordinates = min_max_coordinates(latdeg, londeg, distance)
    prerender(x_min_20=coordinates.x_min,
              x_max_20=coordinates.x_max,
              y_min_20=coordinates.y_min,
              y_max_20=coordinates.y_max,
              start_zoom=13,
              render_zoom=17,
              cmd_prefix=cmd_prefix)

    # Экибастуз 134121 51°43′47″ с. ш. 75°19′35″ в. д. 188 км²
    latdeg = 51.729778
    londeg = 75.326583
    distance = 200
    coordinates = min_max_coordinates(latdeg, londeg, distance)
    prerender(x_min_20=coordinates.x_min,
              x_max_20=coordinates.x_max,
              y_min_20=coordinates.y_min,
              y_max_20=coordinates.y_max,
              start_zoom=13,
              render_zoom=17,
              cmd_prefix=cmd_prefix)

    # Рудный 115506 52°58′ с. ш. 63°07′ в. д. 193,13 км²
    latdeg = 52.96667
    londeg = 63.11667
    distance = 200
    coordinates = min_max_coordinates(latdeg, londeg, distance)
    prerender(x_min_20=coordinates.x_min,
              x_max_20=coordinates.x_max,
              y_min_20=coordinates.y_min,
              y_max_20=coordinates.y_max,
              start_zoom=13,
              render_zoom=17,
              cmd_prefix=cmd_prefix)


if __name__ == "__main__":
    main()
