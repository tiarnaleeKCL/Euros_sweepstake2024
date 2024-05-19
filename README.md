# The sweepstake with a twist!

Pick the winners, runners up, biggest disappointment and the underdogs. The winner will be the person who scores the most points!

The rankings are from the [official UEFA website](https://www.uefa.com/nationalassociations/uefarankings/country/?year=2024) and are accurate as of the tournament starting.

We know some of you like data, so here's the scoring system:

|   **Round**   | **Winner guess** | **Runner up guess** | **Biggest disappointment** |  **The underdogs** |
|:-------------:|:----------------:|:-------------------:|:--------------------------:|:------------------:|
|     Winner    |         6        |          4          |  0 * (1 - scaled ranking)  | 6 * scaled ranking |
|   Runner up   |         4        |          6          |  1 * (1 - scaled ranking)  | 4 * scaled ranking |
|   Semi-final  |         3        |          3          |  2 * (1 - scaled ranking)  | 3 * scaled ranking |
| Quarter final |         2        |          2          |  3 * (1 - scaled ranking)  | 2 * scaled ranking |
|  Round of 16  |         1        |          1          |  4 * (1 - scaled ranking)  | 1 * scaled ranking |
|  Group stage  |         0        |          0          |  6 * (1 - scaled ranking)  | 0 * scaled ranking |

where the scaled ranking is the $\frac{country   Ranking}{lowest   Country   Ranking}$ i.e. $\frac{country   Ranking}{Albania    (47)}$. This scales the points so that _bigger_ disappointments and underdogs get more points.

#### Want to see how we calculate the final scores?

Check out the `calculate_participant_scores.py` script with the example files. The `Euro ranking example` spreadsheet contains the country ranking and some theoretical final positions. The `Predictions example` spreadsheet contains some example predictions from some participants.
