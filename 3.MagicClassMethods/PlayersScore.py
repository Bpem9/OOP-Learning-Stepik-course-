import sys

class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score= score
    def __bool__(self):
        return True if self.score > 0 else False
    def __repr__(self):
        return self.name

lst_in = ['Балакирев; 34; 2048',
'Mediel; 27; 0',
'Влад; 18; 9012',
'Nina P; 33; 0']
players = []
for pl in lst_in:
    name, old, score = pl.split('; ')
    players.append(Player(name, old, int(score)))

players_filtered = list(filter(lambda x: bool(x), players))
print(players_filtered)