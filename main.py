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
    def __init__(self, name, position, positionnumber, team, threept, passing, drivinglay, tov, perd, intd, interception, passpref, posession, defender, player):
        self.name = name
        self.position = position
        self.positionnumber = positionnumber
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
        self.isplayer = player

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
            
        if decision == 'pass':
            pass_receiver_position = random.randint(1,4)
            if pass_receiver_position == 1:
                if self.team == 'LA Clippers':
                    for player in clippers_list:
                        pass_receiver = player
                        if pass_receiver.position == 'Point Guard':
                            print('Passing to ' + pass_receiver.name)
                            break
                    if random.randint(1, 100) < 90: # PLACEHOLDER, NEEDS TO INCORPORATE STATS
                        print('Pass succesful! ' + pass_receiver.name + ' now has the ball!')
                        pass_receiver.hasposession = True
                        self.hasposession = False
                    else:
                        print('Oh no! Stolen by ' + pass_receiver.defender.name + '!')
                        pass_receiver.defender.haspossesion = True
                        self.hasposession = False


     
d_knecht = BasketballPlayer("Dalton Knecht", "Shooting Guard", 2, "Los Angeles Lakers", .461, 0.25, 0.521, 0.143, 0.25, 0, 0.04, 0.2, False, None, False)
a_coffey = BasketballPlayer("Amir Coffey", "Shooting Guard", 2, "LA Clippers", .381, 0.25, 0.554, 0.071, 0, 0, 0.086, 0.2, False, None, False)

#placeholder stats for James Harden, Austin Reaves

j_harden = BasketballPlayer("James Harden", "Point Guard", 1, "LA Clippers", .381, 0.25, 0.554, 0.071, 0, 0, 0.086, 0.2, False, None, False)
a_reaves = BasketballPlayer("Austin Reaves", "Point Guard", 1, "Los Angeles Lakers", .381, 0.25, 0.554, 0.071, 0, 0, 0.086, 0.2, False, None, False)


#initializing defenders

d_knecht.defender = a_coffey
a_coffey.defender = d_knecht

j_harden.defender = a_reaves
a_reaves.defender = j_harden

#adding to lists

clippers_list = [j_harden, a_coffey]
lakers_list = [a_reaves, d_knecht]

# ------------------------------------------------------------------------------------------------------------------

user_team_input = input('Select your team! 1 for the LA Clippers, 2 for the Los Angeles Lakers!' + '\n')
if user_team_input == '1':
    user_team = 'LA Clippers'
else:
    user_team = 'Los Angeles Lakers'


print('Choose your player!')
position_number = 0
if user_team == 'LA Clippers':

    for player in clippers_list:
        position_number += 1
        print(player.name + ' -- ' + str(position_number))
        
    player_decision = int(input())\
    
    for bballplayer in clippers_list:
        if player.positionnumber == player_decision:
            player.isplayer == True
            player.hasposession == True
            print('Player selected: ' + player.name)
            break
            
