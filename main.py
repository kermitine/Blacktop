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

# PASSING STAT UNUSED

import random

class BasketballPlayer():
    def __init__(self, name, position, team, threept, passing, drivinglay, tov, perd, intd, interception, passpref, posession, defender):
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
        self.passpref = passpref
        self.hasposession = posession
        self.defender = defender

    def decision(self):
        generated_probability = random.randint(1, 100)
        modified_probability  = generated_probability * (1 + self.passpref)
        if 66.6 > modified_probability >= 33.3:
            return 'drive'
        elif 150 >= modified_probability >= 66.6:
            return '3pt'
        else:
            return 'pass'
    
    def action_success(self, decision, defender_perd):
        if decision == '3pt':
            print(self.name, 'fires from three!')
            make_chance = 10 - ( random.uniform(1, 4) * (1 + self.threept) ) - ( 1 + defender_perd ) * 1.5
            if make_chance > 4.5:
                print('Bang! Bang!')
                return True
            else:
                print('Brick!')
                return False




d_knecht = BasketballPlayer("Dalton Knecht", "Shooting Guard", "Los Angeles Lakers", .461, 0.25, 0.521, 0.143, 0, 0, 0.04, 0.2, False, None)


a_coffey = BasketballPlayer("Amir Coffey", "Shooting Guard", "LA Clippers", .381, 0.25, 0.554, 0.071, 0, 0, 0.086, 0.2, False, d_knecht)



print(a_coffey.name)

decision = a_coffey.decision()

print(decision)

print(a_coffey.action_success(decision, d_knecht.perd))