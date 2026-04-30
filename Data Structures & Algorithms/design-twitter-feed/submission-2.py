import heapq
class Twitter:

    def __init__(self):
        self.tweets = {} # user_id: int -> tweets: list[tuple[int, int]]
        self.user_follow = {} # user_id: int -> followed_users: set[int]
        self.counter = 1 # maintains order of the submitted tweets, primary to the tweetId

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        
        self.tweets[userId].append((self.counter, tweetId))
        self.counter += 1
    
    # we can add to a heap of 10 elements, compare Ids of tweets
    # from person or people they follow
    # compare to first element, if larger, add it, if smaller dont add it 
    def getNewsFeed(self, userId: int) -> List[int]:
        combined = [] 
        for tweet in self.tweets.get(userId, []):
            combined.append(tweet)

        user_follows = self.user_follow.get(userId, [])

        for user_id in user_follows:
            if user_id in self.tweets:
                tweets = self.tweets[user_id]
                combined.extend(tweets)

        h = []
        heapq.heapify_max(h)

        for tweet_id in combined:
            heapq.heappush_max(h, tweet_id)

            if len(h) > 10:
                heapq.heappop_max(h)

        tweets = [item[1] for item in h]
        tweets.sort(reverse=True)
        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        if followerId not in self.user_follow:
            self.user_follow[followerId] = set()

        self.user_follow[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_follow:
            return

        self.user_follow[followerId].remove(followeeId)
