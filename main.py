#basketgame
#0.0.0

'''
You start the game with the possession ->

OFFENSIVE LOOP

you get the option to drive, pass, or shoot from 3 ->
drive uses stats from your defender's int-defense stats and your layup % to determine outcome (math tbd) - >
pass prompts you with who to pass to. Pass outcome determined with your TOV% and the player you're passing too's defender's interception stats ->
    pass receiver semi-randomly decides whether to pass, shoot, or defend (light influence by IRL stats)
shooting outcome determined via your 3pt stats and defender's perimeter defense stats



'''

#PLACEHOLDER STATS: 0.20 PASSING FOR SG, 0.4 FOR PG, 0.1 FOR ALL ELSE. FG% used for drivinglay

#amir coffey turnover stat derived from 7 possessions a game average, with 0.5 turnovers a game = 1/14 possesions turned over


import random

class BasketballPlayer():
    def __init__(self, name, position, team, threept, passing, drivinglay, tov, perd, intd, interception, threeptpref, passpref, laypref):
        self.name = name
        self.position = position
        self.team = team
        self.threept = threept
        self.passing = passing
        self.tov = tov
        self.drivinglay = drivinglay
        self.perd = perd
        self.intd = intd
        self.interception = interception
        self.threeptpref = threeptpref
        self.passpref = passpref
        self.laypref = laypref

    def decision(self):
        generated_probability = random.randint(1, 100)
        modified_probability  = generated_probability * (1 + self.passpref)
        if 66.6 > modified_probability >= 33.3:
            return 'drive'
        elif 150 >= modified_probability >= 66.6:
            return 'pass'
        else:
            return '3pt'
    
    def shot_is_make(self, decision):
        if decision == '3pt':
            print(self.name, 'fires from three!')




a_coffey = BasketballPlayer("Amir Coffey", "Shooting Guard", "Clippers", .381, 0.25, 0.554, 0.071, 0, 0, 0.086, 0.3, 0.1, 0.6)




print(a_coffey.name)
decision = a_coffey.decision()
print(decision)
a_coffey.shot_is_make(decision)