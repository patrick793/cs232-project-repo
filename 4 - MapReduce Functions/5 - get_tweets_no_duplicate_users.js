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