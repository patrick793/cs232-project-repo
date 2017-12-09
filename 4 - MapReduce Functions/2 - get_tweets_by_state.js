// 1. Tweets by state
var mapFunc = function() { 
	emit({
		state_name : this.state_name,
		state_acronym : this.state_acronym,
		rooted_for :this.rooted_for
	}, 1);
}

var reduceFunc = function(keys, count) {
	return Array.sum(count); 
}

db.tweets.mapReduce(
	mapFunc,
	reduceFunc, {
		out: "tweets_by_state"
	}
)