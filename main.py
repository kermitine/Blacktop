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
    
    def action_success(self, decision, defender_perd, defender_intd, pass_receiver_preset):
        if decision == '3pt':
            print(self.name, 'fires from three!')
            make_chance = 10 - ( random.uniform(1, 4) * (1 + self.threept) ) - ( 1 + defender_perd ) * 1.5
            if make_chance > 4.5:
                print('Bang! Bang!')
                return True
            else:
                print('Brick!')
                return False

        if decision == 'drive':
            print(self.name, 'drives in for a layup!')
            make_chance = 10 - ( random.uniform(1, 4) * (1 + self.drivinglay) ) - ( 1 + defender_intd ) * 1.5
            if make_chance > 3.8:
                print('He rattles it in!')
                return True
            else:
                print('Boing!')
                return False
            
        if decision == 'pass':
            if pass_receiver_preset:
                if random.randint(1, 100) < 90: # PLACEHOLDER, NEEDS TO INCORPORATE STATS
                        print('Pass succesful! ' + pass_receiver_preset.name + ' now has the ball!')
                        pass_receiver_preset.hasposession = True
                        self.hasposession = False
                        return True
                else:
                    print('Oh no! Stolen by ' + pass_receiver.defender.name + '!')
                    pass_receiver.defender.haspossesion = True
                    self.hasposession = False
                    return False
                
        # must INCORPORATE NPC PASSING




#placeholder stats for James Harden, Austin Reaves, Ivica Zubac, Anthony Davis, Rui Hachimura, Kawhi Leonard, Norman Powell and Cam Reddish

d_knecht = BasketballPlayer("Dalton Knecht", "Shooting Guard", 2, "Los Angeles Lakers", .461, 0.25, 0.521, 0.143, 0.25, 0, 0.04, 0.2, False, None, False)
a_coffey = BasketballPlayer("Amir Coffey", "Shooting Guard", 2, "LA Clippers", .381, 0.25, 0.554, 0.071, 0, 0, 0.086, 0.2, False, None, False)

j_harden = BasketballPlayer("James Harden", "Point Guard", 1, "LA Clippers", .381, 0.25, 0.554, 0.071, 0, 0, 0.086, 0.2, False, None, False)
a_reaves = BasketballPlayer("Austin Reaves", "Point Guard", 1, "Los Angeles Lakers", .381, 0.25, 0.554, 0.071, 0, 0, 0.086, 0.2, False, None, False)

a_davis = BasketballPlayer("Anthony Davis", "Center", 5, "Los Angeles Lakers", .381, 0.25, 0.554, 0.071, 0, 0, 0.086, 0.2, False, None, False)
i_zubac = BasketballPlayer("Ivica Zubac", "Center", 5, "LA Clippers", .381, 0.25, 0.554, 0.071, 0, 0, 0.086, 0.2, False, None, False)

r_hachimura = BasketballPlayer("Rui Hachimura", "Power Forward", 4, "Los Angeles Lakers", .381, 0.25, 0.554, 0.071, 0, 0, 0.086, 0.2, False, None, False)
k_leonard = BasketballPlayer("Kawhi Leonard", "Power Forward", 4, "LA Clippers", .381, 0.25, 0.554, 0.071, 0, 0, 0.086, 0.2, False, None, False)

n_powell = BasketballPlayer("Norman Powell", "Small Forward", 3, "LA Clippers", .381, 0.25, 0.554, 0.071, 0, 0, 0.086, 0.2, False, None, False)
l_james = BasketballPlayer("LeBron James", "Small Forward", 3, "Los Angeles Lakers", .381, 0.25, 0.554, 0.071, 0, 0, 0.086, 0.2, False, None, False)

#initializing defenders

d_knecht.defender = a_coffey
a_coffey.defender = d_knecht

j_harden.defender = a_reaves
a_reaves.defender = j_harden

a_davis.defender = i_zubac
i_zubac.defender = a_davis

r_hachimura.defender = k_leonard
k_leonard.defender = r_hachimura

n_powell.defender = l_james
l_james.defender = n_powell

#adding to lists

clippers_list = [j_harden, a_coffey, n_powell, k_leonard, i_zubac]
lakers_list = [a_reaves, d_knecht, l_james, r_hachimura, a_davis]
combined_list = clippers_list + lakers_list

# ------------------------------------------------------------------------------------------------------------------

user_team_input = input('Select your team! 1 for the LA Clippers, 2 for the Los Angeles Lakers!' + '\n')
if user_team_input == '1':
    user_team = 'LA Clippers'
    user_team_list = clippers_list
else:
    user_team = 'Los Angeles Lakers'
    user_team_list = lakers_list


print('Choose your player!')
position_number = 0
if user_team == 'LA Clippers':

    for player in clippers_list:
        position_number += 1
        print(player.name + ' -- ' + str(position_number))

    player_decision = int(input())\
    
    
    for player in clippers_list:
        if player.positionnumber == player_decision:
            player.isplayer = True
            player.hasposession = True
            current_player = player
            print('Player selected: ' + player.name)
            break
else:
    for player in lakers_list:
        position_number += 1
        print(player.name + ' -- ' + str(position_number))

    player_decision = int(input())\
    
    for player in lakers_list:
        if player.positionnumber == player_decision:
            player.isplayer = True
            player.hasposession = True
            current_player = player
            print('Player selected: ' + player.name)
            break
    print('Game start!')

# -----------------------------------------------------------------------------------------

while True:
    position_number = 0

    for player in combined_list:

        if player.hasposession is True:
            print(player.name, 'has the basketball!')

            if player.isplayer == True:
                player_action_decision = input('What will you do? Pass, drive, or shoot a 3-pointer?' + '\n')
                if player_action_decision in ['pass', 'Pass']:
                    print('Who will you pass to?')

                    for player in user_team_list:
                        if player == current_player:
                            position_number += 1
                            continue
                        position_number += 1
                        print(player.name + ' -- ' + str(position_number))

                    player_decision = int(input())

                    for player in user_team_list:
                        if player.positionnumber == player_decision:
                            pass_receiver = player
                            break
                    print('Passing to ' + pass_receiver.name)
                    current_player.action_success('pass', 0, 0, pass_receiver)
            else:
                player.action_success(player.decision())

                    
                            






