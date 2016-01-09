from __future__ import print_function
from drawille import Canvas, line, animate
from time import localtime
import math

def __main__():
    i = 0
    radius = 16

    while True:
        frame = []

        t = localtime()

        h = 2 * math.pi * (t[3] / 24.) - math.pi / 2
        m = 2 * math.pi * (t[4] / 60.) - math.pi / 2
        s = 2 * math.pi * (t[5] / 60.) - math.pi / 2

        for p, l in [(h, radius / 3), (m, 3 * radius / 4), (s, radius)]:
            frame.extend([coords for coords in
                          line(radius,
                               radius,
                               radius + l * math.cos(p),
                               radius + l * math.sin(p))])

        frame.extend([(radius + radius * math.cos(math.radians(x)),
                       radius + radius * math.sin(math.radians(x)))
                      for x in range(0, 360, 3)])

        yield frame


if __name__ == '__main__':
    animate(Canvas(), __main__, 1./2)
