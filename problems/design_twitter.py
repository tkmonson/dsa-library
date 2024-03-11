'''
Design Twitter (#355)

Design a simplified version of Twitter where users can post tweets, follow and
unfollow other users, and see the 10 most recent tweets in their news feed.

Implement the `Twitter` class:

    * Twitter(): Initialize the Twitter object.

    * post_tweet(user_id, tweet_id): Compose a new tweet with the ID `tweet_id`
      by the user `user_id`. Each call to this function will be made with a
      unique `tweet_id` (not necessarily in order).

    * get_news_feed(user_id): Return the 10 most recent tweets in the user's
      news feed. Tweets in the feed must be posts by users who the user is
      following or by the user themself. Tweets must be ordered from most
      recent to least recent.

    * follow(follower_id, followee_id): user `follower_id` starts following
      user `followee_id`.

    * unfollow(follower_id, followee_id): user `follower_id` stops following
      user `followee_id`.
'''

from collections import defaultdict, deque
import heapq

class Tweet:
    def __init__(self, id, timestamp, next=None):
        self.id = id
        self.timestamp = timestamp
        self.next = next

    def __lt__(self, other):
        return -self.timestamp < -other.timestamp


class Twitter:
    def __init__(self):
        self.tweets = defaultdict(lambda: None)
        self.followees = defaultdict(set)
        self.time = 1

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        tweet = Tweet(tweet_id, self.time, self.tweets[user_id])
        self.tweets[user_id] = tweet
        self.time += 1

    # Time: O(10logk), where k is the number of followees a user has
    def get_news_feed(self, user_id: int) -> list[int]:
        pq = []
        if (head := self.tweets[user_id]):
            pq.append(head)
        for followee_id in self.followees[user_id]:
            if (head := self.tweets[followee_id]):
                pq.append(head)
        heapq.heapify(pq)

        feed = []
        while pq and len(feed) < 10:
            if pq[0].next:
                feed.append(heapq.heapreplace(pq, pq[0].next).id)
            else:
                feed.append(heapq.heappop(pq).id)

        return feed

    def follow(self, follower_id: int, followee_id: int) -> None:
        self.followees[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        self.followees[follower_id].discard(followee_id)

'''
This solution is a variation of the "merge k sorted lists" problem. It maps a
user to a linked list of their tweets, sorted from latest to earliest. To get
the news feed for a user, the heads of these lists for all of their followees
are added to a heap and prioritized by recency. The lists are merged in sorted
order until the merged list has 10 elements or until the lists have been
completely merged, whichever comes first.
'''

class Twitter2:
    def __init__(self):
        self.tweets = defaultdict(lambda: deque([], 10))
        self.followees = defaultdict(set)
        self.time = 1

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        self.tweets[user_id].append((-self.time, tweet_id))
        self.time += 1

    # Time: O(10logk), where k is the number of followees a user has
    def get_news_feed(self, user_id: int) -> list[int]:
        pq = []
        self.followees[user_id].add(user_id)
        for followee_id in self.followees[user_id]:
            if (tweets := self.tweets[followee_id]):
                timestamp, tweet_id = tweets[-1]
                pq.append((timestamp, tweet_id, followee_id, len(tweets) - 1))
        self.followees[user_id].remove(user_id)
        heapq.heapify(pq)

        feed = []
        while pq and len(feed) < 10:
            if pq[0][3] > 0:
                followee_id, index = pq[0][2], pq[0][3] - 1
                timestamp, tweet_id = self.tweets[followee_id][index]
                prev_tweet = (timestamp, tweet_id, followee_id, index)
                tweet_id = heapq.heapreplace(pq, prev_tweet)[1]
            else:
                tweet_id = heapq.heappop(pq)[1]
            feed.append(tweet_id)
        return feed

    def follow(self, follower_id: int, followee_id: int) -> None:
        self.followees[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        self.followees[follower_id].discard(followee_id)

'''
Similar to the above solution, but arrays are used instead of linked lists.
'''

class Twitter3:
    def __init__(self):
        self.pq = []
        self.followees = defaultdict(set)

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        self.pq.append((user_id, tweet_id))

    # Time: O(n), where n is number of tweets
    def get_news_feed(self, user_id: int) -> list[int]:
        feed = []
        i = len(self.pq) - 1
        while i >= 0 and len(feed) < 10:
            tweeter_id, tweet_id = self.pq[i]
            if (tweeter_id == user_id or
                tweeter_id in self.followees[user_id]):
                feed.append(tweet_id)
            i -= 1

        return feed

    def follow(self, follower_id: int, followee_id: int) -> None:
        self.followees[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        self.followees[follower_id].discard(followee_id)

'''
This solution does not separate tweets by user but instead puts all tweets into
a list, from earliest to latest, and iterates over it in reverse, selecting any
tweets that were posted by a followee of the given user.
'''

if __name__ == '__main__':
    t = Twitter()
    t.post_tweet(1, 5)
    print(t.get_news_feed(1))
    t.follow(1, 2)
    t.post_tweet(2, 6)
    print(t.get_news_feed(1))
    t.unfollow(1, 2)
    print(t.get_news_feed(1))

