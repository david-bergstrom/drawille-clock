import math
from time import localtime
from drawille import Canvas, line, animate


def clock():
    radius = 16

    while True:
        frame = []

        current_time = localtime()
        hours = math.pi * (2 * current_time[3] / 24. - 1. / 2)
        minutes = math.pi * (2 * current_time[4] / 60. - 1. / 2)
        seconds = math.pi * (2 * current_time[5] / 60. - 1. / 2)

        for angle, length in [(hours, radius / 3), (minutes, 3 * radius / 4),
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
