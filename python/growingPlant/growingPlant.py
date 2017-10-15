"""
Each day a plant is growing by upSpeed meters. Each night that plant's height decreases by downSpeed meters due to the lack of sun heat. Initially, plant is 0 meters tall. We plant the seed at the beginning of a day. We want to know when the height of the plant will reach a certain level.

Example

For upSpeed = 100, downSpeed = 10 and desiredHeight = 910, the output should be
growingPlant(upSpeed, downSpeed, desiredHeight) = 10.

Input/Output

[time limit] 4000ms (py)
[input] integer upSpeed

A positive integer representing the daily growth.

Guaranteed constraints:
5 <= upSpeed <= 100.

[input] integer downSpeed

A positive integer representing the nightly decline.

Guaranteed constraints:
2 <= downSpeed < upSpeed.

[input] integer desiredHeight

A positive integer representing the threshold.

Guaranteed constraints:
4 <= desiredHeight <= 1000.

[output] integer

The number of days that it will take for the plant to reach/pass desiredHeight (including the last day in the total count).
"""


def growingPlant(upSpeed, downSpeed, desiredHeight):
    current_height = 0
    day = 0

    while True:
        day += 1
        current_height += upSpeed

        if current_height >= desiredHeight:
            break

        else:
            current_height -= downSpeed

    return day


if __name__ == '__main__':
    print growingPlant(100, 10, 910)