matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

#print(matches)
'''
number_list = [n for n in range(1, 100)]
square = list(map(lambda n: n**2, number_list))
print(square)
even = list(filter(lambda n: n%2==0, number_list))
print(even)
'''


def extra_f(m):
  n = m.copy()
  n['home_team_score'] = n['home_team_score']+5
  return n

extra = list(map(extra_f, matches))
print(extra)



def winner_f(m):
  if m['home_team_result'].lower() == 'win':
    return m
winner = list(filter(winner_f, matches))
print(winner)

print(matches)