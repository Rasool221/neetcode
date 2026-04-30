import heapq
class Twitter:

    def __init__(self):
        self.tweets = {} # user id (int) -> tweet arr (set[int])
        self.user_follow = {} # user id (int) -> followed user ids (set[int])

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = set()
        
        self.tweets[userId].add(tweetId)
    
    # we can add to a heap of 10 elements, compare Ids of tweets
    # from person or people they follow
    # compare to first element, if larger, add it, if smaller dont add it 
    def getNewsFeed(self, userId: int) -> List[int]:
        user_tweets = list(self.tweets.get(userId, []))
        user_follows = self.user_follow.get(userId, [])

        for f in user_follows:
            user_tweets += list(self.tweets.get(f, []))

        h = []
        heapq.heapify_max(h)

        for tweet_id in user_tweets:
            heapq.heappush_max(h, tweet_id)

            if len(h) > 10:
                heapq.heappop_max(h)

        return h

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_follow:
            self.user_follow[followerId] = set()

        self.user_follow[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_follow:
            return

        self.user_follow[followerId].remove(followeeId)
