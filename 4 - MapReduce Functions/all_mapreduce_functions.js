
	
db.tweets.remove({state_acronym:{$in:["AS", "FM", "GU", "MH", "MP", "PW", "PR", "VI"]}})
		
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
//////////////////////////////////

// 2. Rooted for by state based on tweets

var mapFunc = function() { 
    emit({   
        state_name : this._id.state_name,
        state_acronym : this._id.state_acronym  
    }, {
        rooted_for : this._id.rooted_for,
        count : this.value
    });
}

var reduceFunc = function(keys, data) {
    var rooted_for_democrats = data[0].count;
    var rooted_for_republicans = data[1].count;
    
    
    var voted_for = "Republican";
    if (rooted_for_democrats > rooted_for_republicans) {
        voted_for = "Democrat";
    }
    
    var result = {
        voted_for : voted_for,
        data : data
    }    
    
    return result; 
}

db.tweets_by_state.mapReduce(
	mapFunc,
	reduceFunc, {
		out: "tweets_voted_for_by_state"
	}
)


//////////////////////////////////////////////

// 3. Rooted for and voted for by state based on actual results and tweets

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

/////////////////////////////////////////////////////

// Tweets no duplicate users

var mapFunc = function () {
    emit(this.user_id, {   
        state_name : this.state_name,
        state_acronym : this.state_acronym,
        rooted_for :this.rooted_for
    });
}

var reduceFunc = function (key, value) {
    
    var rooted_for_democrats = 0;
    var rooted_for_republicans = 0;
    var state_name = value[0].state_name;
    var state_acronym = value[0].state_acronym;
       
    for (var i = 0 ; i < value.length ; i++) {
        var x = value[i];
        if (x.rooted_for == "Democrat") {
            rooted_for_democrats++;
        } else {
            rooted_for_republicans++;
        }        
    }
    
    var rooted_for = "Neutral";
    if(rooted_for_democrats > rooted_for_republicans) {
        rooted_for = "Democrat";        
    } else if(rooted_for_democrats < rooted_for_republicans) {
        rooted_for = "Republican";
    }
    
    var result = {
        state_acronym : state_acronym,
        state_name : state_name,
        rooted_for : rooted_for
    }        
    
    return result
}

db.tweets.mapReduce(
	mapFunc,
	reduceFunc, {
		out: "x_unique_user_id_tweets"
	}
)

//////////////////////////////////

// 1. Tweets by state unique user id
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


//////////////////////////////////

// 2. Rooted for by state based on tweets (unique user id)

var mapFunc = function() { 
    emit({   
        state_name : this._id.state_name,
        state_acronym : this._id.state_acronym  
    }, {
        rooted_for : this._id.rooted_for,
        count : this.value
    });
}

var reduceFunc = function(keys, data) {
    var rooted_for_democrats = data[0].count;
	var neutral = data[1].count;
    var rooted_for_republicans = data[2].count;
    
    
    var voted_for = "Republican";
    if (rooted_for_democrats > rooted_for_republicans) {
        voted_for = "Democrat";
    } else if( rooted_for_democrats == rooted_for_republicans) {
		voted_for = "Neutral";
	}
    
    var result = {
        voted_for : voted_for,
        data : data
    }    
    
    return result; 
}

db.x_unique_user_id_tweets_by_state.mapReduce(
	mapFunc,
	reduceFunc, {
		out: "x_unique_user_id_tweets_voted_for_by_state"
	}
)

//////////////////////////////////////////////

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

