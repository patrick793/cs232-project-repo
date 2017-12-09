// 5. Tweets by state unique user id
var mapFunc = function() { 
	emit({
		state_name : this.value.state_name,
		state_acronym : this.value.state_acronym,
		rooted_for :this.value.rooted_for
	}, 1);
}

var reduceFunc = function(keys, count) {
	return Array.sum(count); 
}

db.x_unique_user_id_tweets.mapReduce(
	mapFunc,
	reduceFunc, {
		out: "x_unique_user_id_tweets_by_state"
	}
)