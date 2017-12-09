db.tweets.remove({
	state_acronym : {
		$in: [
			"AS", 
			"FM", 
			"GU", 
			"MH", 
			"MP", 
			"PW", 
			"PR", 
			"VI"
		]
	}
})