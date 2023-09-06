'''
Asteroid Collision (#735)

There is an array of integers representing asteroids in a row. For each
integer, the absolute value represents the size of the asteroid and the sign
represents the direction the asteroid moves (positive is right, negative is
left). Each asteroid moves at the same speed, and no asteroid has a size of 0.
If two asteroids collide, the smaller one will explode. If both are the same
size, both will explode. Given this array of integers, return the array after
all collisions.
'''

def asteroid_collision(asteroids: list[int]) -> list[int]:
    i = 0
    pos_stack = []

    while i < len(asteroids):
        if asteroids[i] < 0:
            if pos_stack:
                pos_asteroid = asteroids[pos_stack[-1]]
                neg_asteroid = asteroids[i]
                if pos_asteroid >= -neg_asteroid:
                    asteroids[i] = 0
                if pos_asteroid <= -neg_asteroid:
                    asteroids[pos_stack.pop()] = 0
                    i -= 1
        else:
            pos_stack.append(i)
        i += 1

    return list(filter(lambda x: x, asteroids))

'''
Asteroids move either left or right, but it is conceptually simpler to consider
some to be stationary and the rest to move in one direction. Let the positive
asteroids be stationary and let the negative asteroids move left. Then, every
positive asteroid to the left of a negative asteroid is a potential collision.

Loop through the asteroids. If you come across a positive asteroid, add it to a
stack of asteroids that a negative asteroid could collide with. If you come
across a negative asteroid and there are positive asteroids in the stack, there
will be a collision. Only move on if the negative asteroid explodes or there
are no more positive asteroids left to collide with. Set exploded asteroids to
0. After all collisions, filter the 0s from the array.
'''

if __name__ == '__main__':
    asteroids = [10, 2, -5]
    print(asteroid_collision(asteroids))

