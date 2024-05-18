# The sweepstake with a twist!

Pick the winners, runners up, biggest disappointment and the underdogs. The winner will be the person who scores the most points!

The rankings are from the [official UEFA website](https://www.uefa.com/nationalassociations/uefarankings/country/?year=2024) and are accurate as of the tournament starting.

We know some of you like data, so here's the scoring system:

|   **Round**   | **Winner guess** | **Runner up guess** | **Biggest disappointment** |     **The underdogs**    |
|:-------------:|:----------------:|:-------------------:|:--------------------------:|:------------------------:|
|     Winner    |         5        |          3          |     0 * scaled ranking     | 5 * (1 - scaled ranking) |
|   Runner up   |         3        |          5          |     1 * scaled ranking     | 3 * (1 - scaled ranking) |
|   Semi-final  |         2        |          2          |     2 * scaled ranking     | 2 * (1 - scaled ranking) |
| Quarter final |         1        |          1          |     3 * scaled ranking     | 1 * (1 - scaled ranking) |
|  Group stage  |         0        |          0          |     5 * scaled ranking     | 0 * (1 - scaled ranking) |

where the scaled ranking is the $\frac{country   Ranking}{lowest   Country   Ranking}$ i.e. $\frac{country   Ranking}{Albania    (47)}$. This scales the points so that _bigger_ disappointments and underdogs get more points.

#### Want to see how we calculate the final scores?

Check out the `calculate_participant_scores.py` script with the example files. The `Euro ranking example` spreadsheet contains the country ranking and some theoretical final positions. The `Predictions example` spreadsheet contains some example predictions from some participants.
