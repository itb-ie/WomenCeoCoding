import credentials
import tweepy
import users
from datetime import datetime
import json
from matplotlib import pylab as plt



# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_SECRET)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

def get_all_tweets(user):
    print(f"getting for {user}")
    alltweets = []
    new_tweets = api.user_timeline(screen_name=user, count=200, tweet_mode="extended")

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print(f"getting tweets before {oldest}")

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=user, count=200, max_id=oldest, tweet_mode="extended")

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print(f"...{len(alltweets)} tweets downloaded so far")
    return alltweets

def get_tweets(users):
    tweets = []
    for user in users:

        user_tweets = {}
        tws = get_all_tweets(user["ceo"])
        user_tweets[user["ceo"]] = tws

        tws = get_all_tweets(user["company"])
        user_tweets[user["company"]] = tws

        tweets.append(user_tweets)

    return tweets


tweets_structure = get_tweets(users.users)
for dictionary in tweets_structure:
    for key in dictionary:
        print(f"{key}, {len(dictionary[key])}")
plt.save("women-ceo-tweets.npy", tweets_structure)


'''
json_obj = tweet._json
print(json.dumps(json_obj))
dtime = json_obj['created_at']
print(json_obj["retweeted"])
if json_obj["retweeted"]:
    print("This is retweeted!")

# new_datetime = datetime.strftime(datetime.strptime(dtime,'%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d %H:%M:%S')
new_datetime = datetime.strptime(dtime, '%a %b %d %H:%M:%S +0000 %Y')
print(new_datetime, new_datetime.year, new_datetime.month, new_datetime.day)
user_tweets[user["ceo"]].append(json_obj)
'''
