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

data = plt.load('women-ceo-tweets.npy', allow_pickle='TRUE').tolist()
found = []


for dictionary in data:
    for key in dictionary:
        for tweet in dictionary[key]:
            for kw in key_words:
                kw = kw.lower()
                if hasattr(tweet, 'retweeted_status'):
                    if kw in tweet.retweeted_status.full_text.lower():
                        text = tweet.retweeted_status.full_text.replace("\n", "  ")
                        # print(f"found{kw} in retweet {tweet.retweeted_status.full_text} of {key}")
                        found.append({"tweet":text, "user":key, "date":tweet.created_at})
                else:
                    if kw in tweet.full_text.lower():
                        text = tweet.full_text.replace("\n", "  ")
                        # print(f"found{kw} in {text} of {key}")
                        found.append({"tweet":text, "user":key, "date":tweet.created_at})

print(f"found {len(found)} terms")

found_2020 = []
for each in found:
    if each["date"].year == 2020 or (each["date"].year == 2019 and each["date"].month >= 7):
        found_2020.append(each)
print(len(found_2020))
for each in found_2020:
    print(f"{each['user']}, {each['date']}, {each['tweet']}")

df = pandas.DataFrame(found_2020)
df.to_csv("results.csv")
print(df)

