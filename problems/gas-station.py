'''
Gas Station (#134)

There are n gas stations along a circular route where the amount of gas at the
ith station is gas[i]. You have a car with an unlimited gas tank and it costs
cost[i] of gas to travel from the ith to the (i + 1)th station. You start with
an empty tank at one of the gas stations. Given two integer arrays gas and
cost, return the starting gas station's index if you can travel around the
circuit once in the clockwise direction, otherwise return -1. If there exists a
solution, it is guaranteed to be unique.
'''

# Time: O(n)
# Auxiliary space: O(1)
def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    total_gain = 0
    tank = 0
    start = 0
    
    for i in range(len(gas)):
        total_gain += gas[i] - cost[i]
        tank += gas[i] - cost[i]
        
        if tank < 0:
            tank = 0
            start = i + 1
            
    return start if total_gain >= 0 else -1

'''
gain[i] = gas[i] - cost[i]

If you start at station A and get stuck at station B, there is no station C
between A and B from which you could start and get to B (because you had to
have had non-negative gas at C when starting at A and getting to B, so starting
at C with zero gas will not help). So you should try starting at the next
station after B.

Let station 0 be the start station. Iterate through the stations. Accumulate
the gain at each station into tank. If tank is ever negative during the
iteration, reset it to zero and consider the next station to be the start
station. Whatever the start station is at the end of the iteration is the
answer, as long as the total sum of the gains is non-negative (i.e. there is
enough gas available to make looping possible).
'''

# Time: O(n)
# Auxiliary space: O(1)
def can_complete_circuit2(gas: list[int], cost: list[int]) -> int:
    tank = 0
    tank_min = gas[0] - cost[0]
    for i in range(n := len(gas)):
        tank += gas[i] - cost[i]
        tank_min = min(tank_min, tank)

    if tank_min >= 0:
        return 0

    for i in range(n - 1, 0, -1):
        tank_min += gas[i] - cost[i]
        if tank_min >= 0:
            return i

    return -1

'''
If you fail a trip starting at station i, it is because the tank went below
zero at some point. If you instead start at station i - 1, the tank will have
an additional gain[i - 1] gas in it at each station. If that is enough gas to
keep the tank from going below zero, then the trip will be successful when
starting from station i - 1.

Start at station 0. Iterate through all the stations, keeping track of the
minimum tank value (min_tank). After iteration, if min_tank is negative, then
the loop cannot be completed when starting at station 0. If min_tank can be
made non-negative by starting at station n - 1 (adding gain[n - 1] to
min_tank), then the loop can be completed from n - 1. If min_tank is still
negative, try adding gain[n - 2] to it, and so on, all the way to considering
station 1 as the start. If min_tank cannot be made non-negative, completing a
loop is impossible.
'''

if __name__ == '__main__':
    gas = [11, 4, 7, 1, 0]
    cost = [2, 5, 5, 9, 1]
    print(can_complete_circuit(gas, cost))

