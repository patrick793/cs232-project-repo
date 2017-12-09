// 3. Rooted for and voted for by state based on actual results and tweets (unique user id)
var mapStates = function () {
    emit({
        state_name : this.state_name,
		state_acronym : this.state_acronym
    }, {
        electoral_votes : this.electoral_votes,
        voted_for_actual : this.voted_for       
    });
}

var mapTweetsVotedForByState = function () {
    emit({
        state_name : this._id.state_name,
		state_acronym : this._id.state_acronym
    }, {
        voted_for_tweets : this.value.result.voted_for
    });    
}

var reduceFunc = function (keys, value) {
    
    var voted_for_tweets = value[0].voted_for_tweets;
    var voted_for_actual = value[1].voted_for_actual;
    var electoral_votes = value[1].electoral_votes;
    
    var result = {
        voted_for_actual : voted_for_actual,
        voted_for_tweets : voted_for_tweets,
        electoral_votes : electoral_votes
    }
    
    return result;
}

db.states.mapReduce(mapStates, reduceFunc, {out: {reduce: "voted_for_actual_and_tweets"}});
db.tweets_voted_for_by_state.mapReduce(mapTweetsVotedForByState, reduceFunc, {out: {reduce: "voted_for_actual_and_tweets"}});
