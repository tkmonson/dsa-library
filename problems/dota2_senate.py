'''
Dota2 Senate (#649)

In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate
wants to decide on a change in the Dota2 game. The voting for this change is a
round-based procedure. In each round, each senator can exercise one of the two
rights:
    * Ban one senator's right: A senator can make another senator lose all his
      rights in this and all the following rounds.
    * Announce the victory: If this senator found the senators who still have
      rights to vote are all from the same party, he can announce the victory
      and decide on the change in the game.

Given a string `senate` representing each senator's party belonging. The
character 'R' and 'D' represent the Radiant party and the Dire party. Then if
there are `n` senators, the size of the given string will be `n`.

The round-based procedure starts from the first senator to the last senator in
the given order. This procedure will last until the end of voting. All the
senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his
own party. Predict which party will finally announce the victory and change the
Dota2 game. The output should be "Radiant" or "Dire".
'''

from collections import deque

def predict_party_victory(senate: str) -> str:
    n = len(senate)
    r = deque()
    d = deque()

    for i in range(n):
        if senate[i] == 'R':
            r.append(i)
        else:
            d.append(i)

    while r and d:
        rs, ds = r.popleft(), d.popleft()
        if rs < ds:
            r.append(rs + n)
        else:
            d.append(ds + n)

    return "Radiant" if r else "Dire"

'''
This is a greedy solution. It doesn't matter which future senator is banned, so
you might as well choose the next one. Put the senator's indicies into queues,
one for each party. Have them face off; smaller index wins. Winner is enqueued
as i + n for the next round.
'''

if __name__ == '__main__':
    senate = "RDD"
    print(predict_party_victory(senate))
