import vincent
import pandas as pd
from pymongo import MongoClient
c = MongoClient(port=27017)
db = c.us_elections_db
vfr = 0
vfd = 0
cursor = db.tweets_voted_for_by_state.find()
# cursor = db.x_unique_user_id_tweets_voted_for_by_state.find()
yoy = {
	"states" : [],
	"voted_for_tweets_r" : [],
	"voted_for_tweets_r_per" : [],
	"voted_for_tweets_d" : [],
	"voted_for_tweets_d_per" : [],
	"total_votes" : []
}
for i in range(0, cursor.count()):
	document = cursor[i]
	yoy['states'].append(document['_id']['state_name'])
	vd = document['value']['result']['data'][0]['count']
	vr = document['value']['result']['data'][1]['count']
	vfd += vd
	vfr += vr
	yoy['voted_for_tweets_d'].append(str(vd))
	yoy['voted_for_tweets_r'].append(str(vr))
	yoy['voted_for_tweets_d_per'].append( str(("%.2f" % (vd/(vd+vr)))) + "%")
	yoy['voted_for_tweets_r_per'].append( str(("%.2f" % (vr/(vd+vr)))) + "%")

# yoy = pd.DataFrame(yoy)
yoy["total_votes"].append("Democrat: " + str(vfd))
yoy["total_votes"].append("Republican: " + str(vfr))

print(yoy)