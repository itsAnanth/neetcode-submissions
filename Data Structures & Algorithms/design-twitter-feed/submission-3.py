from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.users = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:

        feed = []

        # own tweets
        feed.extend(self.tweets[userId])

        # followed users tweets
        for uid in self.users[userId]:
            feed.extend(self.tweets[uid])

        # newest first
        feed.sort(reverse=True)

        # only tweet ids
        return [tweetId for time, tweetId in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.users[followerId].discard(followeeId)