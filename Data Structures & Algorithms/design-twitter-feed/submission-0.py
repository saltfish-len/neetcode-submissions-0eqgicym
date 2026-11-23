class Twitter:

    def __init__(self):
        self.time = 0
        self.followee = {} # user: {followed}
        self.tweet = {} # user: [(time,tweet)]
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId] = self.tweet.get(userId, [])
        self.tweet[userId].append((self.time,tweetId))
        while len(self.tweet[userId]) > 10:
            self.tweet[userId].pop(0)
        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        self.followee[userId] = self.followee.get(userId,set())
        users = self.followee[userId] | {userId}
        tweets = sum((self.tweet.get(u,[]) for u in users), [])
        tweets = sorted(tweets, key=lambda x: x[0],reverse = True)
        return [t[1] for t in tweets][:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followee[followerId] = self.followee.get(followerId, set())
        self.followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followee[followerId] = self.followee.get(followerId, set())
        if followeeId not in self.followee[followerId]:
            return None
        self.followee[followerId].remove(followeeId)
