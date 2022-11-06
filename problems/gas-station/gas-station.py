'''
Gas Station (#134)
PASSES BUT NOT OPTIMIZED FOR TIME, SPACE, OR READABILITY

There are n gas stations along a circular route where the amount of gas at the
ith station is gas[i]. You have a car with an unlimited gas tank and it costs
cost[i] of gas to travel from the ith to the (i + 1)th station. You start with
an empty tank at one of the gas stations. Given two integer arrays gas and
cost, return the starting gas station's index if you can travel around the
circuit once in the clockwise direction, otherwise return -1. If there exists a
solution, it is guaranteed to be unique.
'''

def find_starting_gas_station(gas, cost):
    n = len(gas)
    gas_gained = []
    for i in range(n):
        gas_gained.append(gas[i] - cost[i])
    tank = [gas_gained[-1]]
    for i in range(n - 1):
        tank.append(tank[-1] + gas_gained[i])
    min_tank = min(tank)
    if min_tank >= 0:
        return n - 1
    for i in reversed(range(n - 1)):
        min_tank += gas_gained[i]
        if min_tank >= 0:
            return i
    return -1

if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(f'Gas: {gas}')
    print(f'Cost: {cost}')
    print(f'Start at index: {find_starting_gas_station(gas, cost)}')

'''
Because you gain and lose gas at each station, it is simpler to work with a
(gas - cost) array.

It is significant that you are traveling clockwise (or left to right). If you
fail a trip starting at station i, it is because the tank went below 0 at some
point. By exploring start stations counterclockwise (or right to left), it is
like attempting the previous trip but starting with (gas - cost) gas gained
from station (i - 1) (and you don't have to travel the last leg of the previous
trip, so it doesn't matter if that leg was a success or not). If that gas fixes
the dips below 0 from the previous trip, you know the current trip will be
successful. (You might be able to explore left to right, but it seems less
intuitive to me. It would be like attempting the previous trip but without the
(gas - cost) gas gained from the first station plus a leg at the end.)
'''

