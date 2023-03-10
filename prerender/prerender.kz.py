#!/usr/bin/python3

import subprocess
from multiprocessing import cpu_count
from collections import namedtuple
import math


def prepare_coordinates(x_min_20, x_max_20, y_min_20, y_max_20, zoom):
    Coordinates = namedtuple('–°oordinates', ['x_min', 'x_max', 'y_min', 'y_max'])
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
    Coordinates = namedtuple('–°oordinates', ['x_min', 'x_max', 'y_min', 'y_max'])
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

    # –ö–į–∑–į—Ö—Ā—ā–į–Ĺ
    prerender(x_min_20=659708,
              x_max_20=778612,
              y_min_20=329404,
              y_max_20=394796,
              start_zoom=9,
              render_zoom=12,
              cmd_prefix=cmd_prefix)

    # –ź–Ľ–ľ–į-–ź—ā–į 1801713 43¬į15‚Ä≤ —Ā. —ą. 76¬į54‚Ä≤ –≤. –ī. 682 –ļ–ľ¬≤
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

    # –ź—Ā—ā–į–Ĺ–į 1032475 51¬į08‚Ä≤ —Ā. —ą. 71¬į26‚Ä≤ –≤. –ī. 797,33 –ļ–ľ¬≤
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

    # –®—č–ľ–ļ–Ķ–Ĺ—ā 951605 42¬į18‚Ä≤ —Ā. —ą. 69¬į36‚Ä≤ –≤. –ī. 1162,8 –ļ–ľ¬≤
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

    # –ö–į—Ä–į–≥–į–Ĺ–ī–į 501097 49¬į48‚Ä≤ —Ā. —ą. 73¬į07‚Ä≤ –≤. –ī. 550 –ļ–ľ¬≤
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

    # –ź–ļ—ā–ĺ–Ī–Ķ 420151 50¬į18‚Ä≤ —Ā. —ą. 57¬į10‚Ä≤ –≤. –ī. 297,39 –ļ–ľ¬≤
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

    # –Ę–į—Ä–į–∑ 356461 42¬į53‚Ä≤ —Ā. —ą. 71¬į22‚Ä≤ –≤. –ī. 788,97 –ļ–ľ¬≤
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

    # –ü–į–≤–Ľ–ĺ–ī–į—Ä 334906 52¬į18‚Ä≤56‚Ä≥ —Ā. —ą. 76¬į57‚Ä≤23‚Ä≥ –≤. –ī. 400 –ļ–ľ¬≤
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

    # –£—Ā—ā—Ć-–ö–į–ľ–Ķ–Ĺ–ĺ–≥–ĺ—Ä—Ā–ļ 329048 49¬į57‚Ä≤ —Ā. —ą. 82¬į37‚Ä≤ –≤. –ī. 543,15 –ļ–ľ¬≤
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

    # –°–Ķ–ľ–Ķ–Ļ 321842 50¬į24‚Ä≤40‚Ä≥ —Ā. —ą. 80¬į13‚Ä≤39‚Ä≥ –≤. –ī. 210 –ľ¬≤
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

    # –ö–ĺ—Ā—ā–į–Ĺ–į–Ļ 239532 53¬į13‚Ä≤09‚Ä≥ —Ā. —ą. 63¬į38‚Ä≤03‚Ä≥ –≤. –ī. 240 –ļ–ľ¬≤
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

    # –ź—ā—č—Ä–į—É 237298 47¬į07‚Ä≤ —Ā. —ą. 51¬į53‚Ä≤ –≤. –ī. ?
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

    # –ö—č–∑—č–Ľ–ĺ—Ä–ī–į 236087 44¬į51‚Ä≤ —Ā. —ą. 65¬į31‚Ä≤ –≤. –ī. 240 –ļ–ľ¬≤
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

    # –£—Ä–į–Ľ—Ć—Ā–ļ 235749 51¬į14‚Ä≤ —Ā. —ą. 51¬į22‚Ä≤ –≤. –ī. 700 –ļ–ľ¬≤
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

    # –ü–Ķ—ā—Ä–ĺ–Ņ–į–≤–Ľ–ĺ–≤—Ā–ļ 217106 54¬į51‚Ä≤44‚Ä≥ —Ā. —ą. 69¬į08‚Ä≤27‚Ä≥ –≤. –ī. 224,9 –ļ–ľ¬≤
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

    # –ź–ļ—ā–į—É 183581 43¬į39‚Ä≤ —Ā. —ą. 51¬į09‚Ä≤ –≤. –ī. 76,48 –ļ–ľ¬≤
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

    # –Ę–Ķ–ľ–ł—Ä—ā–į—É 178880 50¬į04‚Ä≤ —Ā. —ą. 72¬į58‚Ä≤ –≤. –ī. 296,1 –ļ–ľ¬≤
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

    # –Ę—É—Ä–ļ–Ķ—Ā—ā–į–Ĺ 161251 43¬į18‚Ä≤00‚Ä≥ —Ā. —ą. 68¬į14‚Ä≤37‚Ä≥ –≤. –ī. 196,27 –ļ–ľ¬≤
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

    # –ö–ĺ–ļ—ą–Ķ—ā–į—É 145762 53¬į17‚Ä≤30‚Ä≥ —Ā. —ą. 69¬į23‚Ä≤30‚Ä≥ –≤. –ī. 400 –ļ–ľ¬≤
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

    # –Ę–į–Ľ–ī—č–ļ–ĺ—Ä–≥–į–Ĺ 145732 45¬į01‚Ä≤ —Ā. —ą. 78¬į22‚Ä≤ –≤. –ī. 100 –ļ–ľ¬≤
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

    # –≠–ļ–ł–Ī–į—Ā—ā—É–∑ 134121 51¬į43‚Ä≤47‚Ä≥ —Ā. —ą. 75¬į19‚Ä≤35‚Ä≥ –≤. –ī. 188 –ļ–ľ¬≤
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

    # –†—É–ī–Ĺ—č–Ļ 115506 52¬į58‚Ä≤ —Ā. —ą. 63¬į07‚Ä≤ –≤. –ī. 193,13 –ļ–ľ¬≤
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
