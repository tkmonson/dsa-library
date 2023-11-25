'''
Car Fleet (#853)

There are `n` cars going to the same destination along a one-lane road. The
destination is `target` miles away. You are given two integer arrays,
`position` and `speed`, both of length `n`, where `position[i]` is the position
of the ith car and `speed[i]` is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and
drive bumper to bumper at the same speed. The faster car will slow down to
match the slower car's speed. In this situation, the cars would also have the
same position.

A car fleet is some non-empty set of cars driving at the same position and same
speed. Note that a single car is also a car fleet. If a car catches up to a car
fleet right at the destination point, it will still be considered as one car
fleet.

Return the number of car fleets that will arrive at the destination.
'''

def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    cars = sorted(zip(position, speed), reverse=True)
    stack = []
    for p, s in cars:
        stack.append((target - p) / s)
        if len(stack) > 1 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)

'''
Assume that the cars are traveling left to right and that the rightmost car is
the car closest to the destination. The rightmost car is guaranteed to drive
the same speed the whole time because it has no cars in front of it. Assuming
that it does not catch up to another car, the ith car will get to the
destination in (target - position[i]) / speed[i] hours. If a car has a shorter
time-to-destination than the car in front of it, it will form a car fleet.

Let's say we want to know if a car B will catch up to the car F in front of it.
If B and F are the two leftmost cars, it would be difficult to calculate their
times because we would not know whether or not they would slow down in the
future after joining a car fleet. If B and F are the two rightmost cars, it
would be easier; F would have a constant speed and B would either have a
constant slower speed or its time would be the same as F's time.
'''

if __name__ == '__main__':
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    print(car_fleet(target, position, speed))

