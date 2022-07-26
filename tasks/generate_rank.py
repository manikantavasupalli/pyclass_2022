#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
def generate_ranksreport(lrank):
    rdict ={}
    rank = 1
    for k in lrank:
        if k not in rdict.keys():
            rdict[k] = rank
            rank += 1
    return rdict

def update_ranksreport(lrank, rank):
    isupdated = False
    for r in range(len(lrank)):
        if rank > lrank[r]:
            lrank.insert(r,rank)
            isupdated = True
            break
    if not isupdated:
        lrank.append(rank)
    urdict = generate_ranksreport(lrank)  
    return urdict

def climbingLeaderboard(ranked, player):
    rank_report = generate_ranksreport(ranked)
    player_ranks = []
    print(rank_report)
    for attempt in player:
        if attempt in rank_report.keys():
            player_ranks.append(rank_report[attempt])
        else:
            rank_report = update_ranksreport(ranked, attempt)
            player_ranks.append(rank_report[attempt])
    return player_ranks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
