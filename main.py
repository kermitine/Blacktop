import random
import time
from KermLib.KermLib import *
from vars.basketball_ascii import *

version = '2025.2.19.1130.stable'


# TEAM AND PLAYER DATA ARE LOADED FROM PLAYERS_AND_TEAMS, DONT WORRY IF EDITOR SAYS THAT VARIABLES ARE UNRECOGNIZED

class BasketballPlayer():
    def __init__(self, name, position, positionnumber, team, threept, passing, drivinglay, tov, perd, intd, interception, passpref, possession, defender, player, points_made, passes_made, interceptions_made, energy, nickname):
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
        self.haspossession = possession
        self.defender = defender
        self.isplayer = player
        self.pointsMade = points_made
        self.passesMade = passes_made
        self.interceptionsMade = interceptions_made
        self.energy = energy
        self.nickname = nickname



    def commentator_randomizer(self, event, secondary_player):

        num = random.randint(1, 4) # 50% to use last name (if nickname exists, otherwise 75%), 25% for full name, 25% for nickname
        if num in [1, 2]:
            primary_name = self.name.split(" ")[1]
        elif num == 3 and self.nickname:
            primary_name = self.nickname
        else:
            primary_name = self.name
        
        num = random.randint(1, 4)
        if num in [1, 2]:
            defender_name = self.defender.name.split(" ")[1]
        elif num == 3 and self.defender.nickname:
            defender_name = self.defender.nickname
        else:
            defender_name = self.defender.name

        if secondary_player:
            num = random.randint(1, 4)
            if num in [1, 2]:
                secondary_player_name = secondary_player.name.split(" ")[1]
            elif num == 3 and secondary_player.nickname:
                secondary_player_name = secondary_player.nickname
            else:
                secondary_player_name = secondary_player.name

            num = random.randint(1, 4)
            if num in [1, 2]:
                secondary_player_defender_name = secondary_player.defender.name.split(" ")[1]
            elif num == 3 and secondary_player.defender.nickname:
                secondary_player_defender_name = secondary_player.defender.nickname
            else:
                secondary_player_defender_name = secondary_player.defender.name
            

        if event == '3ptshot':
            commentary_variation = random.randint(1, 13)

            match commentary_variation:
                case 1:
                    print('A confident three from', primary_name + '!')
                case 2:
                    print(primary_name, 'lets it fly!')
                case 3:
                    print(primary_name, 'from downtown!')
                case 4:
                    print(primary_name, 'steps back and pulls up from three!')
                case 5:
                    print('Corner three from', primary_name + '!')
                case 6:
                    print(primary_name, 'fires a three!')
                case 7:
                    print(primary_name, 'pulls up from beyond the arc!')
                case 8:
                    print(primary_name, 'launches it from deep!')
                case 9:
                    print('A step-back three from', primary_name + '!')
                case 10:
                    print(primary_name, 'from WAY downtown!')
                case 11:
                    print(primary_name, 'from three!')
                case 12:
                    print("That's a deep three for", primary_name + '!')
                case 13:
                    print(primary_name, 'for three!')

        elif event == '3ptmake':
            commentary_variation = random.randint(1, 14)  # Increased range for more variations

            match commentary_variation:
                case 1:
                    print('Count it!')
                case 2:
                    print('BANG!')
                case 3:
                    print('BANG! BANG! WHAT A SHOT FROM', primary_name.upper() + '!')
                case 4:
                    print('And he sinks the three!')
                case 5:
                    print('NOTHING BUT NET!')
                case 6:
                    print('And it’s good!')
                case 7:
                    print(primary_name, 'with the triple!')
                case 8:
                    print('He’s on fire! Another three from', primary_name + '!')
                case 9:
                    print('Splash! What a shot by', primary_name + '!')
                case 10:
                    print('That’s three more for', primary_name + '!')
                case 11:
                    print('Cold-blooded from beyond the arc by', primary_name + '!')
                case 12:
                    print('And he drills it! A dagger from deep!')
                case 13:
                    print("And it's good!", primary_name, 'with the triple!')
                case 14:
                    print('GOT IT!')


        elif event == '3ptmiss':
            commentary_variation = random.randint(1, 11)  # Increased range for more variations
            
            match commentary_variation:
                case 1:
                    print('And airballs!', defender_name, 'gathers it up.')
                case 2:
                    print('And the shot is off the mark.')
                case 3:
                    print('And he bricks it!', defender_name, 'brings it back up for the', self.defender.team + '.')
                case 4:
                    print('And he misfires.', defender_name, 'with the rebound.')
                case 5:
                    print('SMOTHERED BY', defender_name.upper() + '!')
                case 6:
                    print('The three-point attempt rattles out. Tough luck for', primary_name + '.')
                case 7:
                    print('It’s no good from downtown!', defender_name, 'picks it up for the', self.defender.team + '.')
                case 8:
                    print('Way off target from beyond the arc.')
                case 9:
                    print('And it’s just short! A strong defensive effort by', defender_name + '.')
                case 10:
                    print('Off the back iron!', defender_name, 'secures the rebound.')
                case 11:
                    print('Off the rim, recovered by', defender_name)


        elif event == 'drive':
            commentary_variation = random.randint(1, 12)  # Increased range for more variations

            match commentary_variation:
                case 1:
                    print(primary_name, 'drives into the paint!')
                case 2:
                    print('Here comes ' + primary_name + '!')
                case 3:
                    print(primary_name, 'drives the lane!')
                case 4:
                    print(primary_name, 'cuts to the hoop!')
                case 5:
                    print(primary_name, 'spins past', defender_name + '!')
                case 6:
                    print(primary_name, 'slashes to the basket!')
                case 7:
                    print('A strong move by ' + primary_name + ' to the rim!')
                case 8:
                    print(primary_name, 'blows by', defender_name, 'with a quick step!')
                case 9:
                    print(self.name, 'weaves through traffic and heads to the rack!')
                case 10:
                    print('Explosive drive by ' + primary_name + '!')
                case 11:
                    print(primary_name, 'cuts inside and challenges', defender_name + '!')
                case 12:
                    print('Here we go!')

        
        elif event == 'drivemake':
            commentary_variation = random.randint(1, 11)  # Increased range for more variations

            match commentary_variation:
                case 1:
                    print('And he rattles it in!')
                case 2:
                    print('AND HE SLAMS IT DOWN!')
                case 3:
                    print('And he lays it up and in!')
                case 4:
                    print('And he brings the house down!')
                case 5:
                    print('And he kisses it off the glass!')
                case 6:
                    print('What a drive! He finishes strong at the rim!')
                case 7:
                    print('And he powers it home with authority!')
                case 8:
                    print('A dazzling move to the basket, and he converts!')
                case 9:
                    print('He takes it all the way and scores with a smooth finish!')
                case 10:
                    print('And he knifes through the defense for two!')
                case 11:
                    print('And he works his way inside!')


        elif event == 'miss':
            commentary_variation = random.randint(1, 10) 

            match commentary_variation:
                case 1:
                    print('And the ball rims out!', defender_name, 'recovers it.')
                case 2:
                    print('A BACKBOARD BLOCK BY', defender_name.upper() + '!')
                case 3:
                    print('And he bricks it!', defender_name, 'brings it back up for the', self.defender.team + '.')
                case 4:
                    print('And that layup by', primary_name, 'is no good.')
                case 5:
                    print('The shot goes wide! What a defensive effort by', defender_name + '.')
                case 6:
                    print('Oh, the ball just doesn’t want to go in for', primary_name, 'this time.')
                case 7:
                    print('Rejected at the rim! What a block by', defender_name + '!')
                case 8:
                    print('And it’s off the front iron. Tough break for', primary_name + '.')
                case 9:
                    print('The ball dances around the rim and spills out.', defender_name, 'grabs the rebound.')
                case 10:
                    print('A tough miss for', primary_name, 'as', defender_name, 'comes away with it.')
        
        elif event == 'pass': # UNSPAGHETTIFY
            commentary_variation = random.randint(1, 15)  # Increased range for more variations

            match commentary_variation:
                case 1:
                    print('And he kicks it out to ' + secondary_player_name + '!')
                case 2:
                    print('He swings it out to ' + secondary_player_name + '!')
                case 3:
                    print('Out to ' + secondary_player_name + '!')
                case 4:
                    print('And he feeds it to ' + secondary_player_name + '!')
                case 5:
                    print(primary_name + ', bounce pass to', secondary_player_name + '!')
                case 6:
                    print(primary_name + ' finds', secondary_player_name + '!')
                case 7:
                    print('Bullet pass to ' + secondary_player_name + '!')
                case 8:
                    print('Quick dish to ' + secondary_player_name + '!')
                case 9:
                    print('Nice feed to ' + secondary_player_name + '!')
                case 10:
                    print('Sharp pass by ' + primary_name + ' to ' + secondary_player_name + '!')
                case 11:
                    print('And a beautiful no-look pass to ' + secondary_player_name + '!')
                case 12:
                    print('A pinpoint pass by ' + primary_name + ' to ' + secondary_player_name + '!')
                case 13:
                    print(primary_name + ' threads the needle to', secondary_player_name + '!')
                case 14:
                    print('Over to ' + secondary_player_name + ' on the perimeter!')
                case 15:
                    print('He lobs it to ' + secondary_player_name + ' for the setup!')

        
        elif event == 'stolen':
            commentary_variation = random.randint(1, 10)  # Increased range for more variations

            match commentary_variation:
                case 1:
                    print('Stolen by ' + secondary_player_defender_name + '!')
                case 2:
                    print('Stripped away by ' + secondary_player_defender_name + '!')
                case 3:
                    print('Swiped away by ' + secondary_player_defender_name + '!')
                case 4:
                    print('And ' + secondary_player_defender_name + ' intercepts it!')
                case 5:
                    print(self.name, 'turns it over!', secondary_player_defender_name, 'brings it back up the court!')
                case 6:
                    print('Pickpocketed by ' + secondary_player_defender_name + '!')
                case 7:
                    print('And a clean steal by ' + secondary_player_defender_name + '!')
                case 8:
                    print('Fantastic anticipation by ' + secondary_player_defender_name + ', and he takes it away!')
                case 9:
                    print('A quick swipe by ' + secondary_player_defender_name + '! Possession changes hands.')
                case 10:
                    print('And ' + self.name + "'s pass is intercepted by " + secondary_player_defender_name + '!')
            
        print('\n')

    def decision(self):
        generated_probability = random.randint(1, 100)
        modified_probability  = generated_probability * (1 + self.passpref)
        if self.energy <= 11:
            return 'pass'
        if 81 > modified_probability >= 33.3:
            return 'pass'
        elif 150 >= modified_probability >= 81:
            if self.threept != 0:
                return '3pt'
            else:
                return 'drive'
        else:
            return 'drive'
    
    def action_success(self, decision, defender_perd, defender_intd, pass_receiver_preset, active_team):
        if decision == '3pt':
            self.commentator_randomizer('3ptshot', None)
            self.energy -= (28 + random.randint(1, 7))
            make_chance = 10 - ( random.uniform(1, 4) * (1 + self.threept) ) - ( 1.5 + defender_perd ) * 1.5
            if make_chance > 4.8:
                self.commentator_randomizer('3ptmake', None)
                print(harden_shooting)
                self.pointsMade += 3
                self.haspossession = False
                self.defender.haspossession = True
                return 'shot', 3
            else:
                self.commentator_randomizer('3ptmiss', None)
                self.haspossession = False
                self.defender.haspossession = True
                return 'miss', 0

        if decision == 'drive':
            self.commentator_randomizer('drive', None)
            self.energy -= (34 + random.randint(1, 7))
            make_chance = 10 - ( random.uniform(1, 4) * (1 + self.drivinglay) ) - ( 1 + defender_intd ) * 1.5
            if make_chance > 3.8:
                self.commentator_randomizer('drivemake', None)
                print(lebron_dwyane)
                self.pointsMade += 2
                self.haspossession = False
                self.defender.haspossession = True
                return 'shot', 2
            else:
                self.commentator_randomizer('miss', None)
                self.haspossession = False
                self.defender.haspossession = True
                return 'miss', 0
            
        if decision == 'pass':


            if pass_receiver_preset:
                if calculate_turnover_chance(self, pass_receiver_preset.defender) is False: 
                    self.commentator_randomizer('pass', pass_receiver_preset)
                    self.energy -= (13 + random.randint(1, 4))
                    self.passesMade += 1
                    pass_receiver_preset.haspossession = True
                    self.haspossession = False
                    return 'miss', 0
                else:
                    self.commentator_randomizer('pass', pass_receiver_preset)
                    self.commentator_randomizer('stolen', pass_receiver_preset)
                    self.energy -= (13 + random.randint(1, 4))
                    pass_receiver_preset.defender.interceptionsMade += 1
                    pass_receiver_preset.defender.haspossession = True
                    self.haspossession = False
                    return 'miss', 0
            else:
                while True:
                    pass_receiver_position_number = random.randint(1, 5)
                    if self.positionnumber != pass_receiver_position_number:
                        break
                if active_team == user_team:
                    for pass_receiver in user_team_list:
                        if pass_receiver.positionnumber == pass_receiver_position_number:
                            break
                    if calculate_turnover_chance(self, pass_receiver.defender) is False: 
                        self.commentator_randomizer('pass', pass_receiver)
                        self.energy -= (13 + random.randint(1, 4))
                        print(haliburton)

                        self.passesMade += 1
                        pass_receiver.haspossession = True
                        self.haspossession = False
                        return 'miss', 0
                    else:
                        self.commentator_randomizer('pass', pass_receiver)
                        self.commentator_randomizer('stolen', pass_receiver)
                        self.energy -= (13 + random.randint(1, 4))
                        pass_receiver.defender.interceptionsMade += 1
                        pass_receiver.defender.haspossession = True
                        self.haspossession = False
                        return 'miss', 0

                else:
                    for pass_receiver in opposing_team_list:
                        if pass_receiver.positionnumber == pass_receiver_position_number:
                            break
                    if calculate_turnover_chance(self, pass_receiver.defender) is False: 
                        self.commentator_randomizer('pass', pass_receiver)
                        print(haliburton)
                        self.energy -= (13 + random.randint(1, 4))

                        self.passesMade += 1
                        pass_receiver.haspossession = True
                        self.haspossession = False
                        return 'miss', 0
                    else:
                        self.commentator_randomizer('pass', pass_receiver)
                        self.commentator_randomizer('stolen', pass_receiver)
                        self.energy -= (13 + random.randint(1, 4))
                        pass_receiver.defender.interceptionsMade += 1
                        pass_receiver.defender.haspossession = True
                        self.haspossession = False
                        return 'miss', 0
                    
    def substitution(self):

        global current_player
        
        if self.team == user_team:
            print(user_team, 'SUBSTITUTION:')
            print('Substituting', self.name, 'for', user_team_list_bench[self.positionnumber-1].name + '!')

            # hand off (possession given to subbed player, defenders reinitialized, lists swapped)
            user_team_list.insert(self.positionnumber-1, user_team_list_bench[self.positionnumber-1])   #insert bench player into roster
            user_team_list_bench.insert(self.positionnumber-1, user_team_list[self.positionnumber])   # insert former roster player into bench
            user_team_list.pop(self.positionnumber) # remove former roster player from roster
            user_team_list_bench.pop(self.positionnumber) # remove former bench player from bench
            
            if user_team_list_bench[self.positionnumber-1].haspossession == False:
                pass
            else:
                user_team_list_bench[self.positionnumber-1].haspossession = False
                user_team_list[self.positionnumber-1].haspossession = True

            if user_team_list_bench[self.positionnumber-1].isplayer == False:
                pass
            else:
                user_team_list_bench[self.positionnumber-1].isplayer = False
                user_team_list[self.positionnumber-1].isplayer = True
                current_player = user_team_list[current_player.positionnumber-1]
                current_player.haspossession = True
                current_player.isplayer = True


            user_team_list_bench[self.positionnumber-1].energy += 10

            # RE-INITIALIZE DEFENDERS
            for player in user_team_list:
                defender = KermLib.object_matcher(player, opposing_team_list, 'positionnumber')
                player.defender = defender
                defender.defender = player
            combined_list = user_team_list + opposing_team_list
            print('\n')
            return combined_list
        else:
            print(opposing_team, 'SUBSTITUTION:')
            print('Substituting', self.name, 'for', opposing_team_list_bench[self.positionnumber-1].name + '!')

            # hand off (possession given to subbed player, defenders reinitialized, lists swapped)
            opposing_team_list.insert(self.positionnumber-1, opposing_team_list_bench[self.positionnumber-1])   #insert bench player into roster
            opposing_team_list_bench.insert(self.positionnumber-1, opposing_team_list[self.positionnumber])   # insert former roster player into bench
            opposing_team_list.pop(self.positionnumber) # remove former roster player from roster
            opposing_team_list_bench.pop(self.positionnumber) # remove former bench player from bench
            
            if opposing_team_list_bench[self.positionnumber-1].haspossession == False:
                pass
            else:
                opposing_team_list_bench[self.positionnumber-1].haspossession = False
                opposing_team_list[self.positionnumber-1].haspossession = True

            opposing_team_list_bench[self.positionnumber-1].energy += 10
            # RE-INITIALIZE DEFENDERS
            for player in opposing_team_list:
                defender = KermLib.object_matcher(player, user_team_list, 'positionnumber')
                player.defender = defender
                defender.defender = player

        #update list
        combined_list = user_team_list + opposing_team_list
        print('\n')
        return combined_list
    

def calculate_turnover_chance(passer, receiver_defender):
    """
    Calculate the chance of a turnover during a pass.
    Factors include passer's turnover tendency, passing skill, and receiver defender's interception skill.
    """
    
    base_chance = 0.05  
    
    
    turnover_factor = passer.tov * 15  
    passing_factor = passer.passing * -12  
    interception_factor = receiver_defender.interception * 20  
    
    
    dynamic_factor = random.uniform(-0.02, 0.02) * (1 - passer.passing)
    
   
    turnover_chance = base_chance + turnover_factor + passing_factor + interception_factor + dynamic_factor
    
    
    turnover_chance = max(0.0, min(0.4, turnover_chance))
    
    
    random_roll = random.random()  
    if random_roll < turnover_chance:
        return True  
    else:
        return False  


def turn_over_chance(passer, receiver_defender):
    base_chance = 0.10  
    
    turnover_factor = passer.tov * 25
    passing_factor = passer.passing * -7.8
    interception_factor = receiver_defender.interception * 25
    
    turnover_chance = base_chance + turnover_factor + passing_factor + interception_factor
    
    turnover_chance = max(0.1, min(0.25, turnover_chance))
    turnover_chance = round(turnover_chance, 1)
    return turnover_chance * 100




with open("players_and_teams/players_and_teams_data.txt", "r") as file: # INITIALIZES ALL OBJECCTS FROM PLAYERS_AND_TEAMS_DATA
    lines = file.readlines()
    for line in lines:
        exec(line)


KermLib.ascii_run()
print('Blacktop ' + version + '\n')


print('Select your team!')

team = 1
for team_name in teams_names:
    print(team, 'for the', team_name)
    team += 1
team_quantity = list(range(1, team))
team_quantity = [str(x) for x in team_quantity]
user_team_input = KermLib.get_user_input(team_quantity)


print('\n')
if user_team_input == '1':
    user_team = 'LA Clippers'
    user_team_list = clippers_list
    user_team_logo = clippers_logo
    user_team_list_bench = clippers_bench_list
elif user_team_input == '2':
    user_team = 'Los Angeles Lakers'
    user_team_list = lakers_list
    user_team_logo = lakers_logo
    user_team_list_bench = lakers_bench_list
elif user_team_input == '3':
    user_team = 'Boston Celtics'
    user_team_list = celtics_list
    user_team_logo = celtics_logo
    user_team_list_bench = celtics_bench_list
elif user_team_input == '4':
    user_team = 'New York Knicks'
    user_team_list = knicks_list
    user_team_logo = knicks_logo
    user_team_list_bench = knicks_bench_list
elif user_team_input == '5':
    user_team = 'Phoenix Suns'
    user_team_list = suns_list
    user_team_logo = suns_logo 
    user_team_list_bench = suns_bench_list
elif user_team_input == '6':
    user_team = 'Philadelphia 76ers'
    user_team_list = sixers_list
    user_team_logo = sixers_logo
    user_team_list_bench = sixers_bench_list
elif user_team_input == '7':
    user_team = 'Golden State Warriors'
    user_team_list = warriors_list
    user_team_logo = warriors_logo
    user_team_list_bench = warriors_bench_list
elif user_team_input == '8':
    user_team = 'Orlando Magic'
    user_team_list = magic_list
    user_team_logo = magic_logo
    user_team_list_bench = magic_bench_list
elif user_team_input == '9':
    user_team = 'Dallas Mavericks'
    user_team_list = mavericks_list
    user_team_logo = mavericks_logo
    user_team_list_bench = mavericks_bench_list
elif user_team_input == '10':
    user_team = 'Denver Nuggets'
    user_team_list = nuggets_list
    user_team_logo = nuggets_logo
    user_team_list_bench = nuggets_bench_list
elif user_team_input == '11':
    user_team = 'New Orleans Pelicans'
    user_team_list = pelicans_list
    user_team_logo = pelicans_logo
    user_team_list_bench = pelicans_bench_list
elif user_team_input == '12':
    user_team = "'13-'14 LA Clippers"
    user_team_list = retro_clippers_list
    user_team_logo = retro_clippers_logo
    user_team_list_bench = retro_clippers_bench_list
elif user_team_input == '13':
    user_team = "Oklahoma City Thunder"
    user_team_list = thunder_list
    user_team_logo = thunder_logo
    user_team_list_bench = thunder_bench_list
elif user_team_input == '14':
    user_team = "Memphis Grizzlies"
    user_team_list = grizzlies_list
    user_team_logo = grizzlies_logo
    user_team_list_bench = grizzlies_bench_list
elif user_team_input == '15':
    user_team = "Houston Rockets"
    user_team_list = rockets_list
    user_team_logo = rockets_logo
    user_team_list_bench = rockets_bench_list
elif user_team_input == '16':
    user_team = "Washington Wizards"
    user_team_list = wizards_list
    user_team_logo = wizards_logo
    user_team_list_bench = wizards_bench_list


print(user_team_logo)

print('\n' + '\n')

print('Team selected:', user_team)

print('\n')




print('\n' + '\n')


print('Select your opposing team!')
team = 1
forbidden = None
for team_name in teams_names:
    if team_name != user_team:
        print(team, 'for the', team_name)
        team += 1
    else:
        forbidden = team
        team += 1

team_quantity = list(range(1, team))
team_quantity = [str(x) for x in team_quantity]

while True:
    user_decision = KermLib.get_user_input(team_quantity)
    if user_decision == str(forbidden):
        print('Input not recognized. Please try again:')
        continue
    else:
        break

opposing_team = teams_names[int(user_decision)-1]

if opposing_team == 'LA Clippers':
    opposing_team_list = clippers_list
    opposing_team_logo = clippers_logo
    opposing_team_list_bench = clippers_bench_list
elif opposing_team == 'Los Angeles Lakers':
    opposing_team_list = lakers_list
    opposing_team_logo = lakers_logo
    opposing_team_list_bench = lakers_bench_list
elif opposing_team == 'Boston Celtics':
    opposing_team_list = celtics_list
    opposing_team_logo = celtics_logo
    opposing_team_list_bench = celtics_bench_list
elif opposing_team == 'New York Knicks':
    opposing_team_list = knicks_list
    opposing_team_logo = knicks_logo
    opposing_team_list_bench = knicks_bench_list
elif opposing_team == 'Phoenix Suns':
    opposing_team_list = suns_list
    opposing_team_logo = suns_logo
    opposing_team_list_bench = suns_bench_list
elif opposing_team == 'Philadelphia 76ers':
    opposing_team_list = sixers_list
    opposing_team_logo = sixers_logo
    opposing_team_list_bench = sixers_bench_list
elif opposing_team == 'Golden State Warriors':
    opposing_team_list = warriors_list
    opposing_team_logo = warriors_logo
    opposing_team_list_bench = warriors_bench_list
elif opposing_team == 'Orlando Magic':
    opposing_team_list = magic_list
    opposing_team_logo = magic_logo
    opposing_team_list_bench = magic_bench_list
elif opposing_team == 'Dallas Mavericks':
    opposing_team_list = mavericks_list
    opposing_team_logo = mavericks_logo
    opposing_team_list_bench = mavericks_bench_list
elif opposing_team == 'Denver Nuggets':
    opposing_team_list = nuggets_list
    opposing_team_logo = nuggets_logo
    opposing_team_list_bench = nuggets_bench_list
elif opposing_team == 'New Orleans Pelicans':
    opposing_team_list = pelicans_list
    opposing_team_logo = pelicans_logo
    opposing_team_list_bench = pelicans_bench_list
elif opposing_team == "'13-'14 LA Clippers":
    opposing_team_list = retro_clippers_list
    opposing_team_logo = retro_clippers_logo
    opposing_team_list_bench = retro_clippers_bench_list
elif opposing_team == "Oklahoma City Thunder":
    opposing_team_list = thunder_list
    opposing_team_logo = thunder_logo
    opposing_team_list_bench = thunder_bench_list
elif opposing_team == "Memphis Grizzlies":
    opposing_team_list = grizzlies_list
    opposing_team_logo = grizzlies_logo
    opposing_team_list_bench = grizzlies_bench_list
elif opposing_team == "Houston Rockets":
    opposing_team_list = rockets_list
    opposing_team_logo = rockets_logo
    opposing_team_list_bench = rockets_bench_list
elif opposing_team == "Washington Wizards":
    opposing_team_list = wizards_list
    opposing_team_logo = wizards_logo
    opposing_team_list_bench = wizards_bench_list




print(opposing_team_logo)

print('\n' + '\n')

print('Opposing team selected:', opposing_team)

combined_list = user_team_list + opposing_team_list

print('\n' + '\n')

print('(A)utoplay mode or (M)anual?')
auto_or_manual = str(KermLib.get_user_input(['A', 'a', 'm', 'M']))
print('\n')




if auto_or_manual in ['m', "M"]:
    print('Manual selected')
    print('Choose your player!')

    position_number = 0
    for player in user_team_list:
        position_number += 1
        print(player.name + ' -- ' + str(position_number))

    player_decision = int(KermLib.get_user_input(['1', '2', '3', '4', '5']))
else:
    print('Auto selected')


# INITIALIZE DEFENDERS
for player in user_team_list:
    defender = KermLib.object_matcher(player, opposing_team_list, 'positionnumber')
    player.defender = defender
    defender.defender = player

time.sleep(2)

print('\n' + '\n')

if auto_or_manual in ['m', "M"]:
    for player in user_team_list:
        if player.positionnumber == player_decision:
            player.isplayer = True
            player.haspossession = True
            current_player = player
            print('\n')
            print('Player selected:', current_player.name)
            break
else:
    user_team_list[0].haspossession = True
    current_player = None

print('\n' + '\n')

print(user_team, 'vs.', opposing_team)
print('\n')
print('Starting lineup:')
for x in range(5):
    if user_team_list[x] == current_player:
        print('(You)', user_team_list[x].name, ' -- ', opposing_team_list[x].name)
    else:
        print(user_team_list[x].name, ' -- ', opposing_team_list[x].name)

print('\n' + '\n')

print('Bench lineup:')
for x in range(5):
    print(user_team_list_bench[x].name, ' -- ', opposing_team_list_bench[x].name)

print('\n' + '\n')

print('Game start!')

time.sleep(2)

# -----------------------------------------------------------------------------------------

end_score = 25

opposing_team_score = 0
user_team_score = 0



while True:

    if opposing_team_score >= end_score or user_team_score >= end_score:
        if opposing_team_score >= end_score:
            print('\n' + '\n' + '\n')
            print('---------------------------------------------------------------------------------------------------------')
            print(opposing_team + ' win! Final score:', opposing_team_score, '-', user_team_score)
            print('---------------------------------------------------------------------------------------------------------')
            print(opposing_team_logo)
        else:
            print('\n' + '\n' + '\n')
            print('---------------------------------------------------------------------------------------------------------')
            print(user_team + ' win! Final score:', user_team_score, '-', opposing_team_score)
            print('---------------------------------------------------------------------------------------------------------')
            print(user_team_logo)

        highest_score = 0
        highest_scorer = None

        highest_interceptions = 0
        highest_interceptor = None

        highest_passes = 0
        highest_passer = None

        for player in combined_list + user_team_list_bench + opposing_team_list_bench:
            if player.pointsMade > highest_score:
                highest_score = player.pointsMade
                highest_scorer = player
            if player.passesMade > highest_passes:
                highest_passes = player.passesMade
                highest_passer = player
            if player.interceptionsMade > highest_interceptions:
                highest_interceptions = player.interceptionsMade
                highest_interceptor = player

        time.sleep(1.5)

        print('\n')
        if highest_scorer:
            print('Most points scored:', highest_scorer.name, 'with', str(highest_score))
        else:
            print('0 points scored')
        time.sleep(1.5)
        if highest_passer:
            print('Most passes performed:', highest_passer.name, 'with', str(highest_passes))
        else:
            print('0 passes made')
        time.sleep(1.5)
        if highest_interceptor:
            print('Most interceptions:', highest_interceptor.name, 'with', str(highest_interceptions))
        else:
            print('0 interceptions made')
        time.sleep(1.5)

        print('\n')

        if highest_interceptor is not None:
            if highest_interceptor.team == highest_passer.team == highest_scorer.team:
                print('Wow! A clean sweep by the', highest_interceptor.team, 'as they claim the entire leaderboard!')
        else:
            if highest_passer.team == highest_scorer.team:
                print('Wow! A double by the', highest_scorer.team, 'as they claim two leaderboard spots!')


        
        time.sleep(5)
        break

    if user_team_score > opposing_team_score:
        print('---------------------------------------------------------------------------------------------------------')
        print('Current score:', user_team_score, '-', opposing_team_score,  ', ' + user_team, 'lead by',  (user_team_score - opposing_team_score))
        print('---------------------------------------------------------------------------------------------------------')
    elif user_team_score < opposing_team_score:
        print('---------------------------------------------------------------------------------------------------------')
        print('Current score:', opposing_team_score, '-', user_team_score,  ', ' + opposing_team, 'lead by',  (opposing_team_score - user_team_score))
        print('---------------------------------------------------------------------------------------------------------')
    else:
        print('---------------------------------------------------------------------------------------------------------')
        print('Tie game:',  user_team_score, '-', opposing_team_score)
        print('---------------------------------------------------------------------------------------------------------')
    position_number = 0

    print('\n')

    time.sleep(3.5)

    for player in user_team_list_bench + opposing_team_list_bench: #RECUPERATE 6 ENERGY TO EACH PLAYER ON THE BENCH PER TURN
        if random.randint(1, 2) != 2:
            player.energy += 9
        if player.energy > 100: #CLAMP VALUES BETWEEN 0 AND 100
            player.energy = 100
        elif player.energy < 0:
            player.energy = 0


    for player in combined_list: # ENSURE THAT NO PLAYER'S ENERGY IS EVER OUTSIDE THE NORMAL RANGE
        if player.energy > 100:
            player.energy = 100
        elif player.energy < 0:
            player.energy = 0


    for player in combined_list:

        if player.energy <= 7 and player != current_player: #IF AI PLAYER ENERGY IS TOO LOW, SUB
                print(player.name, 'is gassed!')
                combined_list = player.substitution()



        if player.haspossession is True:
            


            print(player.name, 'has the basketball!')
            print(player.name + "'s energy:", str(player.energy) + '%')
            if player.isplayer == True:
                if player.energy != 0:
                    print('What will you do? (pass), (drive), shoot a (3pt), or manually (substitute)?')
                    player_action_decision = KermLib.get_user_input(['pass', 'drive', '3pt', 'substitute'])
                    print('\n' + '\n')
                else:
                    print(player.name + "'s energy is too low! Forcing substitution!")
                    player_action_decision = 'substitute'
                    print('\n')
                    time.sleep(1)
                
                if player_action_decision in ['pass', 'Pass']:
                    print('Who will you pass to?')

                    for player in user_team_list:
                        if player == current_player:
                            position_number += 1
                            continue
                        position_number += 1
                        print(player.name + ' -- ' + str(position_number), '(defended by', player.defender.name + ')', '(Chance of turnover:', str(turn_over_chance(current_player, player.defender)) + '%)', '(Energy:', str(player.energy) + '%)')
                
                    while True:
                        player_decision = str(input())
                        if player_decision == str(current_player.positionnumber):
                            print('Decision not recognized. Please try again')
                            continue
                        elif player_decision not in ['1', '2', '3', '4', '5']:
                            print('Decision not recognized. Please try again')
                            continue
                        else:
                            player_decision = int(player_decision)
                            break


                    print('\n')

                    for player in user_team_list:
                        if player.positionnumber == player_decision:
                            pass_receiver = player
                            break
                    outcome, points = current_player.action_success('pass', 0, 0, pass_receiver, current_player.team)
                    if outcome == 'shot' and player.team == user_team:
                        user_team_score += points
                        break
                    elif outcome == 'shot' and player.team == opposing_team:
                        opposing_team_score += points
                        break
                    break
                elif player_action_decision in ['drive', 'Drive']:
                    outcome, points = current_player.action_success('drive', current_player.defender.perd, current_player.defender.intd, None, current_player.team)
                    if outcome == 'shot' and player.team == user_team:
                        user_team_score += points
                        break
                    elif outcome == 'shot' and player.team == opposing_team:
                        opposing_team_score += points
                        break
                    break   
                elif player_action_decision in ['3pt', '3PT', '3Pt']:
                    outcome, points = current_player.action_success('3pt', current_player.defender.perd, current_player.defender.intd, None, current_player.team)
                    if outcome == 'shot' and player.team == user_team:
                        user_team_score += points
                        break
                    elif outcome == 'shot' and player.team == opposing_team:
                        opposing_team_score += points
                        break
                    break   
                elif player_action_decision == 'substitute':
                    combined_list = current_player.substitution()

            else:
                decision = player.decision()
                outcome, points = player.action_success(decision, player.defender.perd, player.defender.intd, None, player.team)
                if outcome == 'shot' and player.team == user_team:
                    user_team_score += points
                    break
                elif outcome == 'shot' and player.team == opposing_team:
                    opposing_team_score += points
                    break
                break   

