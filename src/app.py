

import os
import requests 
import tweepy
import pandas as pd 
from dotenv import load_dotenv

# load_dotenv()
load_dotenv()

consumer_key = "SgzyNRayEzRCOP3CvWvuWGck3" 
consumer_secret = "sfrTztYnTg8gyAx1Z5Z5JKgA0Ru8BztOa9ZDYD5CKZUYimaSnG"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAB6%2FdwEAAAAA1MmgS8K4455DZD6CSu%2B9Jnm82Nk%3D0cPOgSVpOvqZ1EbqZEGuwS32j7P2gZB0peGvzVEjHWqMufD73y"



# Creando cliente de Twitter

client = tweepy.Client( bearer_token=bearer_token, 
                        consumer_key=consumer_key, 
                        consumer_secret=consumer_secret,
                        return_type = requests.Response,
                        wait_on_rate_limit=True)


# Definiendo el query para Tweeter

query = '#100daysofcode (pandas OR python) -is:retweet'      

tweets = client.search_recent_tweets(query=query, 
                                    tweet_fields=['author_id','created_at','lang'],
                                     max_results=100)



tweets

## Convert to pandas Dataframe

# Save data as dictionary
tweets_dict = tweets.json()
list(tweets_dict)


# Extract "data" value from dictionary
tweets_data = tweets_dict['data'] 
tweets_data

list(tweets_data[1])

# Transform to pandas Dataframe
df_twets = pd.json_normalize(tweets_data)
df_twets # look dataframe

# save df
df_twets.to_csv("coding-tweets.csv")

df_twets.head(5)


# analizando texto ahora vamos a contar cuantos Twetts tienen la palabra 'python' y 'pandas':

#import re
import re

#define your function here
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)

    if match:
        return True
    return False 


# Initialize list to store tweet counts
[pandas, python] = [0, 0]

# Iterate through df, counting the number of tweets in which each(pandas and python) is mentioned.
for index, row in df_twets.iterrows():
    pandas += word_in_text('pandas', row['text'])
    python += word_in_text('python', row['text'])


print(type(df_twets))

print(type(pandas))

# Visualización 
# Import packages
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['pandas', 'python']

# Plot the bar chart
ax = sns.barplot(cd, [pandas, python])
ax.set(ylabel="count")
plt.show()




