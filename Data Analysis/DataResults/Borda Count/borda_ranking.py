#import mlpython
import pandas as pd
from collections import defaultdict


path = '/Users/mosesopenja/Documents/summer2021/mouna/'
# Load the exported Google Form CSV
df = pd.read_csv(path+'Smells-ranking.csv')

# Extract only the ranking columns
vote_cols = df.columns#[0:]
df = df[vote_cols]
# Calculate total number of candidates
candidates = set()
for i, col in enumerate(df.columns):
    for candidate in df[col]:
        candidates.add(candidate)
n_candidates = len(candidates)


print('candidates: ', candidates)
print(n_candidates, 'candidates')
# Get how many ranks were available to give
n_ranks = len(vote_cols)
print(n_ranks, 'ranks')
print('='*20)
for label, base_points in [('candidates', n_candidates), ('ranks', n_ranks)]:
    print('Using {} as base points:'.format(label))
    # Assuming first column is highest rank
    scores = defaultdict(int)
    for i, col in enumerate(df.columns):
        points = base_points - i
        for candidate in df[col]:
            scores[candidate] += points
    print(label)

    # Sort candidates by score, descending
    ranking = sorted(scores.items(), key=lambda i: i[1], reverse=True)
    for cand, score in ranking:
        print(cand,' = ', score)
    print('='*20)#import mlpython
import pandas as pd
from collections import defaultdict


path = '/Users/mosesopenja/Documents/summer2021/mouna/'
# Load the exported Google Form CSV
df = pd.read_csv(path+'Smells-ranking.csv')

# Extract only the ranking columns
vote_cols = df.columns#[0:]
df = df[vote_cols]
# Calculate total number of candidates
candidates = set()
for i, col in enumerate(df.columns):
    for candidate in df[col]:
        candidates.add(candidate)
n_candidates = len(candidates)


print('candidates: ', candidates)
print(n_candidates, 'candidates')
# Get how many ranks were available to give
n_ranks = len(vote_cols)
print(n_ranks, 'ranks')
print('='*20)
for label, base_points in [('candidates', n_candidates), ('ranks', n_ranks)]:
    print('Using {} as base points:'.format(label))
    # Assuming first column is highest rank
    scores = defaultdict(int)
    for i, col in enumerate(df.columns):
        points = base_points - i
        for candidate in df[col]:
            scores[candidate] += points
    print(label)

    # Sort candidates by score, descending
    ranking = sorted(scores.items(), key=lambda i: i[1], reverse=True)
    for cand, score in ranking:
        print(cand,' = ', score)
    print('='*20)