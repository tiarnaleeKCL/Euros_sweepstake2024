#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 15:49:04 2024

@author: tiarnalee
"""


import numpy as np
import pandas as pd

# Load in participant predictions and rankings sheets
rankings = pd.read_excel('./Euros ranking example.xlsx', header=1)
predictions = pd.read_excel('./Predictions example.xlsx', header=1, index_col=0)

# Replace positions in the competition with position numbers
position_map = {'Winner': 0, 'Runner up': 1, 'Semis': 2, 'Quarters': 3, 'Round of 16': 4, 'Group stage': 5}
rankings['Position'] = rankings['Position'].replace(position_map)

# Points assigned for each category
points = {
    'winner': [6, 4, 3, 2, 1, 0], # More points awarded for guessing the winner
    'runners_up': [4, 6, 3, 2, 1, 0], # Most points awarded for correctly guessing the runner up but more points are awarded
    # for guessing that team as the winner than the semi-finals
    'disappointment': [0, 1, 2, 3, 4, 6], # Most points awarded for the chosen country doing poorly
    'underdogs': [6, 4, 3, 2, 1, 0] # Most points awarded for the chosen country doing well
}

# Function to find the scores
def scoring_system(predictions, rankings):
    '''
    ----------
    predictions : a Dataframe containing the participant names (optional) as the column names.
    The columns should be (in this order) the predictions for the winner, runner up, biggest disappointment and underdogs
    rankings : A Dataframe containing the country name, country ranking, scaled ranking and final position
    in the tournament converted to a numerical position with 0 for the winner, 1 for the runner up etc.

    Returns
    -------
    participant_scores : A list of the participants' final scores in order of their appearance in the spreadsheet

    '''
    participant_scores = np.zeros(len(predictions))
    
    for i, (_, participant) in enumerate(predictions.iterrows()):

        scores = {}
        
        # Iterate over each prediction category and corresponding points
        for category, (col, point_list) in zip(['winner', 'runners_up', 'disappointment', 'underdogs'], enumerate(points.values())):
            # Get the predicted country for the category
            country = participant[col]
            # Find the index of the country in the rankings DataFrame
            country_idx = rankings.index[rankings['Country'] == country].tolist()[0]
            # Get the tournament position of the country
            tournament_position = rankings.at[country_idx, 'Position']
            # Get the scaled ranking of the country
            scaled_ranking = rankings.at[country_idx, 'Scaled_ranking']
            
            # Scale the score for biggest disappointment
            if category == 'disappointment':
                scores[category] = point_list[tournament_position] * scaled_ranking
            # Scale the score for the underdogs
            elif category == 'underdogs':
                scores[category] = point_list[tournament_position] * (1 - scaled_ranking)
            # The winner and runner up scores are unscaled
            else:
                scores[category] = point_list[tournament_position]
        # Total scores for all categories for the current participant
        participant_scores[i] = sum(list(scores.values()))
    
    return participant_scores

# Find the scores for each participant
participant_scores = scoring_system(predictions, rankings)
predictions['Final score'] = participant_scores

# Find the winner and the max score
winner = predictions['Final score'].idxmax()
max_score = predictions['Final score'].max()
print(f"And the winner is... {winner} with {max_score} points")
