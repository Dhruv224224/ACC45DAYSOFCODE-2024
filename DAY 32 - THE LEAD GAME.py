# Initialize scores and variables
cumulative_score_player1 = 0
cumulative_score_player2 = 0
max_lead = 0
winner = 0

# Hardcoded rounds of scores
rounds = [
    (140, 82),
    (89, 134),
    (90, 110),
    (112, 106),
    (88, 90)
]

# Process each round
for score1, score2 in rounds:
    cumulative_score_player1 += score1
    cumulative_score_player2 += score2
    
    # Calculate lead and determine winner
    if cumulative_score_player1 > cumulative_score_player2:
        lead = cumulative_score_player1 - cumulative_score_player2
        if lead > max_lead:
            max_lead = lead
            winner = 1
    else:
        lead = cumulative_score_player2 - cumulative_score_player1
        if lead > max_lead:
            max_lead = lead
            winner = 2

# Print the result
print("Winner:", winner)
print("Maximum Lead:", max_lead)


