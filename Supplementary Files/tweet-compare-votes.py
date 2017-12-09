from pymongo import MongoClient
import json

c = MongoClient(port=27017)
db = c.tweets

states = {
    "AL": {
		"state_name" : "Alabama",
		"electoral_votes" : 9,
		"voted_for" : "Republican"
	},
    "AK": {
		"state_name" : "Alaska",
		"electoral_votes" : 3,
		"voted_for" : "Republican"
	},
    "AZ": {
		"state_name" : "Arizona",
		"electoral_votes" : 11,
		"voted_for" : "Republican"
	},
    "AR": {
		"state_name" : "Arkansas",
		"electoral_votes" : 6,
		"voted_for" : "Republican"
	},
    "CA": {
		"state_name" : "California",
		"electoral_votes" : 55,
		"voted_for" : "Democrat"
	},
    "CO": {
		"state_name" : "Colorado",
		"electoral_votes" : 9,
		"voted_for" : "Democrat"
	},
    "CT": {
		"state_name" : "Connecticut",
		"electoral_votes" : 7,
		"voted_for" : "Democrat"
	},
    "DE": {
		"state_name" : "Delaware",
		"electoral_votes" : 3,
		"voted_for" : "Democrat"
	},
    "DC": {
		"state_name" : "District Of Columbia",
		"electoral_votes" : 3,
		"voted_for" : "Democrat"
	},
    "FL": {
		"state_name" : "Florida",
		"electoral_votes" : 29,
		"voted_for" : "Republican"
	},
    "GA": {
		"state_name" : "Georgia",
		"electoral_votes" : 16,
		"voted_for" : "Republican"
	},
    "HI": {
		"state_name" : "Hawaii",
		"electoral_votes" : 4,
		"voted_for" : "Democrat"
	},
    "ID": {
		"state_name" : "Idaho",
		"electoral_votes" : 4,
		"voted_for" : "Republican"
	},
    "IL": {
		"state_name" : "Illinois",
		"electoral_votes" : 20,
		"voted_for" : "Democrat"
	},
    "IN": {
		"state_name" : "Indiana",
		"electoral_votes" : 11,
		"voted_for" : "Republican"
	},
    "IA": {
		"state_name" : "Iowa",
		"electoral_votes" : 6,
		"voted_for" : "Republican"
	},
    "KS": {
		"state_name" : "Kansas",
		"electoral_votes" : 6,
		"voted_for" : "Republican"
	},
    "KY": {
		"state_name" : "Kentucky",
		"electoral_votes" : 8,
		"voted_for" : "Republican"
	},
    "LA": {
		"state_name" : "Louisiana",
		"electoral_votes" : 8,
		"voted_for" : "Republican"
	},
    "ME": {
		"state_name" : "Maine",
		"electoral_votes" : 4,
		"voted_for" : "Democrat"
	},
    "MD": {
		"state_name" : "Maryland",
		"electoral_votes" : 10,
		"voted_for" : "Democrat"
	},
    "MA": {
		"state_name" : "Massachusetts",
		"electoral_votes" : 11,
		"voted_for" : "Democrat"
	},
    "MI": {
		"state_name" : "Michigan",
		"electoral_votes" : 16,
		"voted_for" : "Republican"
	},
    "MN": {
		"state_name" : "Minnesota",
		"electoral_votes" : 10,
		"voted_for" : "Democrat"
	},
    "MS": {
		"state_name" : "Mississippi",
		"electoral_votes" : 6,
		"voted_for" : "Republican"
	},
    "MO": {
		"state_name" : "Missouri",
		"electoral_votes" : 10,
		"voted_for" : "Republican"
	},
    "MT": {
		"state_name" : "Montana",
		"electoral_votes" : 3,
		"voted_for" : "Republican"
	},
    "NE": {
		"state_name" : "Nebraska",
		"electoral_votes" : 5,
		"voted_for" : "Republican"
	},
    "NV": {
		"state_name" : "Nevada",
		"electoral_votes" : 6,
		"voted_for" : "Democrat"
	},
    "NH": {
		"state_name" : "New Hampshire",
		"electoral_votes" : 4,
		"voted_for" : "Democrat"
	},
    "NJ": {
		"state_name" : "New Jersey",
		"electoral_votes" : 14,
		"voted_for" : "Democrat"
	},
    "NM": {
		"state_name" : "New Mexico",
		"electoral_votes" : 5,
		"voted_for" : "Democrat"
	},
    "NY": {
		"state_name" : "New York",
		"electoral_votes" : 29,
		"voted_for" : "Democrat"
	},
    "NC": {
		"state_name" : "North Carolina",
		"electoral_votes" : 15,
		"voted_for" : "Republican"
	},
    "ND": {
		"state_name" : "North Dakota",
		"electoral_votes" : 3,
		"voted_for" : "Republican"
	},
    "OH": {
		"state_name" : "Ohio",
		"electoral_votes" : 18,
		"voted_for" : "Republican"
	},
    "OK": {
		"state_name" : "Oklahoma",
		"electoral_votes" : 7,
		"voted_for" : "Republican"
	},
    "OR": {
		"state_name" : "Oregon",
		"electoral_votes" : 7,
		"voted_for" : "Democrat"
	},
    "PA": {
		"state_name" : "Pennsylvania",
		"electoral_votes" : 20,
		"voted_for" : "Republican"
	},
    "RI": {
		"state_name" : "Rhode Island",
		"electoral_votes" : 4,
		"voted_for" : "Democrat"
	},
    "SC": {
		"state_name" : "South Carolina",
		"electoral_votes" : 9,
		"voted_for" : "Republican"
	},
    "SD": {
		"state_name" : "South Dakota",
		"electoral_votes" : 3,
		"voted_for" : "Republican"
	},
    "TN": {
		"state_name" : "Tennessee",
		"electoral_votes" : 11,
		"voted_for" : "Republican"
	},
    "TX": {
		"state_name" : "Texas",
		"electoral_votes" : 38,
		"voted_for" : "Republican"
	},
    "UT": {
		"state_name" : "Utah",
		"electoral_votes" : 6,
		"voted_for" : "Republican"
	},
    "VT": {
		"state_name" : "Vermont",
		"electoral_votes" : 3,
		"voted_for" : "Democrat"
	},
    "VA": {
		"state_name" : "Virginia",
		"electoral_votes" : 13,
		"voted_for" : "Democrat"
	},
    "WA": {
		"state_name" : "Washington",
		"electoral_votes" : 12,
		"voted_for" : "Democrat"
	},
    "WV": {
		"state_name" : "West Virginia",
		"electoral_votes" : 5,
		"voted_for" : "Republican"
	},
    "WI": {
		"state_name" : "Wisconsin",
		"electoral_votes" : 10,
		"voted_for" : "Republican"
	},
    "WY": {
		"state_name" : "Wyoming",
		"electoral_votes" : 3,
		"voted_for" : "Republican"
	}
}

ev_real_d = 0
ev_real_r = 0
ev_twit_d = 0
ev_twit_r = 0
cursor = db.tweet_rooted_for_by_state.find()
total_votes_d = 0
total_votes_r = 0
for i in range(0, cursor.count(),2 ):
# for document in cursor:
	document = cursor[i]
	state_name = document['_id']['state_name']
	state_acronym = document['_id']['state_acronym']
	value_democrat = document['value']
	total_votes_d += value_democrat
		
	document = cursor[i+1]
	value_republican = document['value']
	total_votes_r += value_republican
		
	rooted_for = "Democrat"
	if value_democrat < value_republican:
		rooted_for = "Republican"
	
	if value_democrat < value_republican:
		ev_twit_r += states[state_acronym]['electoral_votes']
	else:
		ev_twit_d += states[state_acronym]['electoral_votes']
		
	if states[state_acronym]['voted_for'] == "Republican":
		ev_real_r += states[state_acronym]['electoral_votes']
	else:
		ev_real_d += states[state_acronym]['electoral_votes']
	
	print(states[state_acronym]['state_name'] + " votes " +  states[state_acronym]['voted_for'] +" and tweets for "+ rooted_for + " d:r " + str(ev_real_d) +":"+ str(ev_real_r) + " " + str(ev_twit_d)+":"+str(ev_twit_r));
print ("Votes for Democrats: " + str(total_votes_d))
print ("Votes for Republicans: " + str(total_votes_r))	