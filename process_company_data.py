from datetime import datetime
import json
from matplotlib import pylab as plt
import re
import pandas


key_words = ["Corporate Social Responsibility",
            "Corporate Responsibility",
            "Sustainability",
            "Sustainable development",
            "Corporate Accountability",
            "Crating Shared Value",
            "Citizenship",
            "Social Responsibility",
            "Environmental, Social and Governance",
            "shared value",
            "social",
            "responsibility",
            "CSR ",
            "CR ",
            "ESG"]

data = plt.load('company-tweets.npy', allow_pickle='TRUE').tolist()
# data = plt.load('competitor-tweets.npy', allow_pickle='TRUE').tolist()
found = {}

for key in data:
    print(key, len(data[key]))
    found[key] = []
    for tweet in data[key]:
        #print(tweet)
        for kw in key_words:
            kw = kw.lower()
            if hasattr(tweet, 'retweeted_status'):
                if kw in tweet.retweeted_status.full_text.lower():
                    text = tweet.retweeted_status.full_text.replace("\n", "  ")
                    # print(f"found{kw} in retweet {tweet.retweeted_status.full_text} of {key}")
                    found[key].append({"tweet":text, "user":key, "date":tweet.created_at})
                    print("Adding {}".format(text))
            else:
                if kw in tweet.full_text.lower():
                    text = tweet.full_text.replace("\n", "  ")
                    # print(f"found{kw} in {text} of {key}")
                    found[key].append({"tweet":text, "user":key, "date":tweet.created_at})
                    print("Adding2 {}".format(text))
    print(found)

# print(f"found {len(found)} terms")

fp = open("results_companies/general.txt", "w")
#fp = open("results_competitors/general.txt", "w")
df_general = pandas.DataFrame()

found_2020 = {}
for company in found:
    found_2020[company] = []
    for each in found[company]:
        if each["date"].year == 2020 or (each["date"].year == 2019 and each["date"].month >= 7):
            found_2020[company].append(each)
    fp.write("Company {} has {} matched tweets in 2020\n".format(company, len(found_2020[company])))
    # now write the file with all the tweets
    df = pandas.DataFrame(found_2020[company])
    df.to_csv("results_companies/{}_results.csv".format(company))
    # df.to_csv("results_competitors/{}_results.csv".format(company))

sum = 0

df_general["Company Twitter"] = pandas.Series(list(found_2020.keys()))


nr_tweets = []
for key in found_2020:
    sum += len(found_2020[key])
    nr_tweets.append(len(found_2020[key]))
df_general["Num Tweets"] = pandas.Series(nr_tweets)

fp.write("Total number of matched tweets in 2020: {} \n".format(sum))
fp.close()
# df_general.to_csv("results_competitors/general.csv")
df_general.to_csv("results_companies/general.csv")

'''
for each in found_2020:
    print(f"{each['user']}, {each['date']}, {each['tweet']}")
    
df = pandas.DataFrame(found_2020)
df.to_csv("results.csv")
print(df)
'''
