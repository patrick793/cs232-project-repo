# from pymongo import MongoClient
import re
from random import randint
from twarc import Twarc
import json
import sys
from textblob import TextBlob

# client = MongoClient(port=27017)
# db = client.us_elections_2016


consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

t = Twarc(consumer_key, consumer_secret, access_token, access_token_secret)

states = {
    "AL": "Alabama",
    "AK": "Alaska",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "DC": "District Of Columbia",
    "FL": "Florida",
    "GA": "Georgia",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming"
}

counter = 0
iterations = 0

out_file = open(sys.argv[1] + ".json", "w")
out_file.write("[")

democrats_cnt = 0
republicans_cnt = 0

for tweet in t.hydrate(open(sys.argv[1],'r',encoding='utf8')):
    # temp_obj = json.loads(tweet)
    iterations +=1
    try:
        clean_tweet = tweet['full_text'].lower()
        clean_tweet = clean_tweet.replace("#", "")
        clean_tweet = clean_tweet.replace("@", "")
        clean_tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", clean_tweet).split())        
        analysis = TextBlob(clean_tweet)
        
        rooted_for = "None"       
        keyword = "None"
        twt = clean_tweet
        
        if ("hillary" in twt) or ("democrat" in twt) or ("madampresident" in twt) or ("clinton" in twt) or ("kaine" in twt):
            keyword = "Democrat"
            if analysis.sentiment.polarity > 0.0:
                rooted_for = "Democrat"
            elif analysis.sentiment.polarity < 0.0:
                rooted_for = "Republican"
        elif ("trump" in twt) or ("yourefired" in twt) or ("republican" in twt) or ("gop" in twt) or ("donald" in twt) or ("makeamericagreatagain" in twt) or ("pence" in twt):
            keyword = "Republican"
            if analysis.sentiment.polarity > 0.0:
                rooted_for = "Republican"
            elif analysis.sentiment.polarity < 0.0:
                rooted_for = "Democrat"
        
        # print(rooted_for + str(analysis.sentiment.polarity) + " : " + keyword + " : " + clean_tweet)
        
        if rooted_for != "None":
            temp_obj = {
                'tweet_id' : tweet['id'],
                'user_id' : tweet['user']['id'],
                'full_text': tweet['full_text'],
                'state_acronym': tweet['user']['location'][-2:],
                'state_name': states[tweet['user']['location'][-2:]],
                'hashtags' : tweet['entities']['hashtags'],
                'retweet_count' : tweet['retweet_count'],
                'favorite_count' : tweet['favorite_count'],
                'rooted_for' : rooted_for,
                'created_at': tweet['created_at']
            }
            # out_file.write(repr(temp_obj) + ",")
            # result = db.tweets.insert_one(temp_obj)
            
            if rooted_for != "Republican":
                republicans_cnt = republicans_cnt + 1
            else:
                democrats_cnt+=1
            
            # print(json.dumps(temp_obj) + ",")
            out_file.write(json.dumps(temp_obj) + ",")
            counter = counter + 1
            # print(str(counter) + " : " + str(tweet['id']) + " inserted from " + temp_obj['state_name'] + " (" + temp_obj['state_acronym'] + ")")
            print(str(iterations) + " : " + str(counter) + " : " + rooted_for)
    except:
        pass
out_file.write("]")

print("Democrats: " + str(democrats_cnt))
print("Repulicans: " + str(republicans_cnt))

print('Finished creating ' + str(counter) + ' Tweets')