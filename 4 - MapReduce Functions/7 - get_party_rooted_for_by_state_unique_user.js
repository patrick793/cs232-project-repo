// 6. Rooted for by state based on tweets (unique user id)
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