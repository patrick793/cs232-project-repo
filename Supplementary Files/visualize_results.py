import vincent
import pandas as pd
from pymongo import MongoClient
c = MongoClient(port=27017)
db = c.us_elections_db

vincent.core.initialize_notebook()



yoy = {
    "NAME" : [],
    "VOTES" : []
}

# cursor = db.voted_for_actual_and_tweets.find()
cursor = db.x_unique_user_id_voted_for_actual_and_tweets.find()
voted_for_tweets_r = 0
voted_for_tweets_d = 0

for i in range(0, cursor.count()):
    document = cursor[i]
    if document['value']['voted_for_actual'] == "Republican":
        voted_for_tweets_r += document['value']['electoral_votes']
    else:
        voted_for_tweets_d += document['value']['electoral_votes']        

# cursor = db.voted_for_actual_and_tweets.find()
cursor = db.x_unique_user_id_voted_for_actual_and_tweets.find()
for i in range(0, cursor.count()):
    document = cursor[i]
    yoy['NAME'].append(document['_id']['state_name'])
    if document['value']['voted_for_actual'] == "Republican":
        yoy['VOTES'].append(0)
    else:
        yoy['VOTES'].append(1)

yoy = pd.DataFrame(yoy)

print("Republican: " + str(voted_for_tweets_r))
print("Democrat: " + str(voted_for_tweets_d))


geo_data = [{'name': 'states',
             'url': "https://raw.githubusercontent.com/wrobstory/vincent_map_data/master/us_states.topo.json",
             'feature': 'us_states.geo'}]
vis = vincent.Map(data=yoy, geo_data=geo_data, scale=1000,
                  projection='albersUsa', data_bind='VOTES', data_key='NAME',
                  map_key={'states': 'properties.NAME'}, brew='RdBu')
#Custom threshold scale
vis.legend(title='US Election Results Actual')
vis.to_json('vega.json')
vis.display()