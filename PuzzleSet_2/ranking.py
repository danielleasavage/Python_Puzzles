import sys

match_input = sys.stdin.read().strip()

stars_needed = {1:5,2:5,3:5,4:5,5:5,
                6:5,7:5,8:5,9:5,10:5,
                11:4,12:4,13:4,14:4,15:4,
                16:3,17:3,18:3,19:3,20:3,
                21:2,22:2,23:2,24:2,25:2}

class Player:
    def __init__(self):
        self.stars = 0
        self.rank = 25
        self.wins = 0
        
    def update_rank(self, outcome):
        if outcome == 'W':
            self.rank -= 1
        else:
            self.rank += 1
        
    def update_stars(self,stars):
        self.stars = stars
        
    def update_wins(self, outcome):
        if outcome == 'W':
            self.wins += 1
        else:
            self.wins = 0


def find_final_rank(match_input):
    spencer = Player()
    for outcome in match_input:
        if spencer.rank == 0:
            return 'Legend'
        if outcome == 'W':
            spencer.update_wins('W')
            if 5 < spencer.rank < 26 and spencer.wins > 2:
                spencer.update_stars(spencer.stars+2)
            else:
                spencer.update_stars(spencer.stars+1)
            if stars_needed[spencer.rank] < spencer.stars:
                stars = spencer.stars - stars_needed[spencer.rank]
                spencer.update_rank('W')
                spencer.update_stars(stars)
        else:
            spencer.update_wins('L')
            if spencer.rank <20:
                if spencer.stars == 0:
                    spencer.update_rank('L')
                    stars = stars_needed[spencer.rank] - 1
                    spencer.update_stars(stars)
                else:
                    spencer.update_stars(spencer.stars -1)

    return spencer.rank

print(find_final_rank(match_input))
