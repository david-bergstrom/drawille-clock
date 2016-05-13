import math
from time import localtime
from drawille import Canvas, line, animate


def clock():
    radius = 16

    while True:
        frame = []

        hour, minute, second = localtime()[3:6]

        hours = math.pi * (4 * hour / 24. - 1./2)
        minutes = math.pi * (2 * minute / 60. - 1. / 2)
        seconds = math.pi * (2 * second / 60. - 1. / 2)

        for angle, length in [(hours, radius / 2), (minutes, 3 * radius / 4),
                              (seconds, radius)]:
            frame.extend([c for c in line(radius,
                                          radius,
                                          radius + length * math.cos(angle),
                                          radius + length * math.sin(angle))])

        frame.extend([(radius + radius * math.cos(math.radians(x)),
                       radius + radius * math.sin(math.radians(x)))
                      for x in range(0, 360, 3)])

        yield frame


if __name__ == '__main__':
    animate(Canvas(), clock, 1./2)
