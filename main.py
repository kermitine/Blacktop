import random
import time
from KermLib.KermLib import *
from vars.basketball_ascii import *

version = '2024.12.16.2340.rc'

class BasketballPlayer():
    def __init__(self, name, position, positionnumber, team, threept, passing, drivinglay, tov, perd, intd, interception, passpref, possession, defender, player, points_made, passes_made, interceptions_made, energy):
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



    def commentator_randomizer(self, event, secondary_player):
        if event == '3ptshot':
            last_name = self.name.split(" ")[1]
            announcer_call = random.randint(1, 12)  # Increased range for more variations
            if announcer_call == 1:
                print(self.name, 'fires it from deep!')
            elif announcer_call == 2:
                print(self.name, 'lets it fly!')
            elif announcer_call == 3:
                print(self.name, 'from downtown!')
            elif announcer_call == 4:
                print(self.name, 'steps back and pulls from three!')
            elif announcer_call == 5:
                print('Corner three from', last_name + '!')
            elif announcer_call == 6:
                print(last_name, 'fires a three!')
            elif announcer_call == 7:
                print(self.name, 'pulls up from beyond the arc!')
            elif announcer_call == 8:
                print(last_name, 'launches it from deep!')
            elif announcer_call == 9:
                print('A step-back three from', self.name + '!')
            elif announcer_call == 10:
                print(self.name, 'from way downtown!')
            elif announcer_call == 11:
                print(last_name, 'pulls the trigger from three!')
            elif announcer_call == 12:
                print(self.name, 'shoots it with confidence from beyond the arc!')


        elif event == '3ptmake':
            announcer_call = random.randint(1, 12)  # Increased range for more variations
            if announcer_call == 1:
                print('Count it!')
            elif announcer_call == 2:
                print('BANG!')
            elif announcer_call == 3:
                print('BANG! BANG! WHAT A SHOT FROM', self.name.upper() + '!')
            elif announcer_call == 4:
                print('And he sinks the three!')
            elif announcer_call == 5:
                print('NOTHING BUT NET!')
            elif announcer_call == 6:
                print('And it’s good!')
            elif announcer_call == 7:
                print(self.name, 'with the triple!')
            elif announcer_call == 8:
                print('He’s on fire! Another three from', self.name + '!')
            elif announcer_call == 9:
                print('Splash! What a shot by', self.name + '!')
            elif announcer_call == 10:
                print('That’s three more for', self.team + '!')
            elif announcer_call == 11:
                print('Cold-blooded from beyond the arc by', self.name + '!')
            elif announcer_call == 12:
                print('And he drills it! A dagger from deep!')


        elif event == '3ptmiss':
            announcer_call = random.randint(1, 10)  # Increased range for more variations
            last_name = self.name.split(" ")[1]
            if announcer_call == 1:
                print('And airballs!', self.defender.name, 'gathers it up.')
            elif announcer_call == 2:
                print('And the shot is off the mark.')
            elif announcer_call == 3:
                print('And he bricks it!', self.defender.name, 'brings it back up for the', self.defender.team + '.')
            elif announcer_call == 4:
                print('And he misfires.', self.defender.name, 'with the rebound.')
            elif announcer_call == 5:
                print('SMOTHERED BY', self.defender.name.upper() + '!')
            elif announcer_call == 6:
                print('The three-point attempt rattles out. Tough luck for', last_name + '.')
            elif announcer_call == 7:
                print('It’s no good from downtown!', self.defender.name, 'picks it up for the', self.defender.team + '.')
            elif announcer_call == 8:
                print('Way off target from beyond the arc.')
            elif announcer_call == 9:
                print('And it’s just short! A strong defensive effort by', self.defender.name + '.')
            elif announcer_call == 10:
                print('Off the back iron!', self.defender.name, 'secures the rebound.')


        elif event == 'drive':
            defender_last_name = self.defender.name.split(" ")[1]
            last_name = self.name.split(" ")[1]
            announcer_call = random.randint(1, 11)  # Increased range for more variations
            if announcer_call == 1:
                print(self.name, 'drives into the paint!')
            elif announcer_call == 2:
                print('Here comes ' + self.name + '!')
            elif announcer_call == 3:
                print(self.name, 'drives the lane!')
            elif announcer_call == 4:
                print(self.name, 'cuts to the hoop!')
            elif announcer_call == 5:
                print(last_name, 'spins past', defender_last_name + '!')
            elif announcer_call == 6:
                print(self.name, 'slashes to the basket!')
            elif announcer_call == 7:
                print('A strong move by ' + self.name + ' to the rim!')
            elif announcer_call == 8:
                print(last_name, 'blows by', defender_last_name, 'with a quick step!')
            elif announcer_call == 9:
                print(self.name, 'weaves through traffic and heads to the rack!')
            elif announcer_call == 10:
                print('Explosive drive by ' + last_name + '!')
            elif announcer_call == 11:
                print(last_name, 'cuts inside and challenges', defender_last_name + '!')

        
        elif event == 'drivemake':
            announcer_call = random.randint(1, 10)  # Increased range for more variations
            if announcer_call == 1:
                print('And he rattles it in!')
            elif announcer_call == 2:
                print('AND HE SLAMS IT DOWN!')
            elif announcer_call == 3:
                print('And he lays it up and in!')
            elif announcer_call == 4:
                print('And he brings the house down!')
            elif announcer_call == 5:
                print('And he kisses it off the glass!')
            elif announcer_call == 6:
                print('What a drive! He finishes strong at the rim!')
            elif announcer_call == 7:
                print('And he powers it home with authority!')
            elif announcer_call == 8:
                print('A dazzling move to the basket, and he converts!')
            elif announcer_call == 9:
                print('He takes it all the way and scores with a smooth finish!')
            elif announcer_call == 10:
                print('And he knifes through the defense for two!')


        elif event == 'miss':
            defender_last_name = self.defender.name.split(" ")[1]
            last_name = self.name.split(" ")[1]
            announcer_call = random.randint(1, 10)  # Increased range for more variations
            if announcer_call == 1:
                print('And the ball rims out!', defender_last_name, 'recovers it.')
            elif announcer_call == 2:
                print('A BACKBOARD BLOCK BY', self.defender.name.upper() + '!')
            elif announcer_call == 3:
                print('And he bricks it!', self.defender.name, 'brings it back up for the', self.defender.team + '.')
            elif announcer_call == 4:
                print('And that layup by', last_name, 'is no good.')
            elif announcer_call == 5:
                print('The shot goes wide! What a defensive effort by', self.defender.name + '.')
            elif announcer_call == 6:
                print('Oh, the ball just doesn’t want to go in for', last_name, 'this time.')
            elif announcer_call == 7:
                print('Rejected at the rim! What a block by', self.defender.name + '!')
            elif announcer_call == 8:
                print('And it’s off the front iron. Tough break for', last_name + '.')
            elif announcer_call == 9:
                print('The ball dances around the rim and spills out.', defender_last_name, 'grabs the rebound.')
            elif announcer_call == 10:
                print('A tough miss for', last_name, 'as', defender_last_name, 'comes away with it.')
        
        elif event == 'pass':
            last_name = self.name.split(" ")[1]
            pass_receiver_last_name = secondary_player.name.split(" ")[1]
            announcer_call = random.randint(1, 15)  # Increased range for more variations
            if announcer_call == 1:
                print('And he kicks it out to ' + pass_receiver_last_name + '!')
            elif announcer_call == 2:
                print('He swings it out to ' + secondary_player.name + '!')
            elif announcer_call == 3:
                print('Out to ' + pass_receiver_last_name + '!')
            elif announcer_call == 4:
                print('And he feeds it to ' + secondary_player.name + '!')
            elif announcer_call == 5:
                print(last_name + ', bounce pass to', pass_receiver_last_name + '!')
            elif announcer_call == 6:
                print(last_name + ' finds', pass_receiver_last_name + '!')
            elif announcer_call == 7:
                print('Bullet pass to ' + pass_receiver_last_name + '!')
            elif announcer_call == 8:
                print('Quick dish to ' + secondary_player.name + '!')
            elif announcer_call == 9:
                print('Nice feed to ' + pass_receiver_last_name + '!')
            elif announcer_call == 10:
                print('Sharp pass by ' + last_name + ' to ' + pass_receiver_last_name + '!')
            elif announcer_call == 11:
                print('And a beautiful no-look pass to ' + pass_receiver_last_name + '!')
            elif announcer_call == 12:
                print('A pinpoint pass by ' + last_name + ' to ' + secondary_player.name + '!')
            elif announcer_call == 13:
                print(last_name + ' threads the needle to', pass_receiver_last_name + '!')
            elif announcer_call == 14:
                print('Over to ' + pass_receiver_last_name + ' on the perimeter!')
            elif announcer_call == 15:
                print('He lobs it to ' + pass_receiver_last_name + ' for the setup!')

        
        elif event == 'stolen':
            announcer_call = random.randint(1, 10)  # Increased range for more variations
            if announcer_call == 1:
                print('Stolen by ' + secondary_player.defender.name + '!')
            elif announcer_call == 2:
                print('Stripped away by ' + secondary_player.defender.name + '!')
            elif announcer_call == 3:
                print('Swiped away by ' + secondary_player.defender.name + '!')
            elif announcer_call == 4:
                print('And ' + secondary_player.defender.name + ' intercepts it!')
            elif announcer_call == 5:
                print(self.name, 'turns it over!', secondary_player.defender.name, 'brings it back up the court!')
            elif announcer_call == 6:
                print('Pickpocketed by ' + secondary_player.defender.name + '!')
            elif announcer_call == 7:
                print('And a clean steal by ' + secondary_player.defender.name + '!')
            elif announcer_call == 8:
                print('Fantastic anticipation by ' + secondary_player.defender.name + ', and he takes it away!')
            elif announcer_call == 9:
                print('A quick swipe by ' + secondary_player.defender.name + '! Possession changes hands.')
            elif announcer_call == 10:
                print('And ' + self.name + "'s pass is intercepted by " + secondary_player.defender.name + '!')
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

        # only used for npc
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
    

        
with open("players_and_teams/players_and_teams_data.txt", "r") as file: # INITIALIZES ALL OBJECCTS FROM PLAYERS_AND_TEAMS_DATA
    lines = file.readlines()
    for line in lines:
        exec(line)

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


print(user_team_logo)

print('\n' + '\n')

print('Team selected:', user_team)

print('\n')

print('Choose your player!')

position_number = 0
for player in user_team_list:
    position_number += 1
    print(player.name + ' -- ' + str(position_number))

player_decision = int(KermLib.get_user_input(['1', '2', '3', '4', '5']))

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




print(opposing_team_logo)

print('\n' + '\n')

print('Opposing team selected:', opposing_team)

combined_list = user_team_list + opposing_team_list


# INITIALIZE DEFENDERS
for player in user_team_list:
    defender = KermLib.object_matcher(player, opposing_team_list, 'positionnumber')
    player.defender = defender
    defender.defender = player

time.sleep(2)

for player in user_team_list:
    if player.positionnumber == player_decision:
        player.isplayer = True
        player.haspossession = True
        current_player = player
        print('\n')
        print('Your player: ' + player.name)
        print('Your defender:', current_player.defender.name)
        break



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
                    print(user_team, 'SUBSTITUTION:')
                    print(user_team_list_bench[current_player.positionnumber-1].name, 'comes in for', current_player.name + '!')
                    print('\n')
                    # hand off (possession given to subbed player, defenders reinitialized, lists swapped)
                    user_team_list.insert(current_player.positionnumber-1, user_team_list_bench[current_player.positionnumber-1])   #insert bench player into roster
                    user_team_list_bench.insert(current_player.positionnumber-1, user_team_list[current_player.positionnumber])   # insert former roster player into bench
                    user_team_list.pop(current_player.positionnumber) # remove former roster player from roster
                    user_team_list_bench.pop(current_player.positionnumber) # remove former bench player from bench
                    

                    user_team_list[current_player.positionnumber-1].haspossession = True
                    user_team_list[current_player.positionnumber-1].isplayer = True

                    user_team_list_bench[current_player.positionnumber-1].haspossession = False
                    user_team_list_bench[current_player.positionnumber-1].isplayer = False

                    user_team_list_bench[current_player.positionnumber-1].energy += 10

                    current_player = user_team_list[current_player.positionnumber-1]

                    current_player.haspossession = True
                    current_player.isplayer = True
                    
                    # RE-INITIALIZE DEFENDERS
                    for player in user_team_list:
                        defender = KermLib.object_matcher(player, opposing_team_list, 'positionnumber')
                        player.defender = defender
                        defender.defender = player
                    
                    #update list
                    combined_list = user_team_list + opposing_team_list
                


        
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

