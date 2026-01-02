"""
Copyright (C) 2025 Ayrik Nabirahni. This file
is apart of the Blacktop project, and licensed under
the GNU AGPL-3.0-or-later. See LICENSE and README for more details.
"""

import random
import time
from utils.KermLib.KermLib import KermLib
from utils.ascii.basketball_ascii import *
from blacktop.commentary.commentary import *
from config.settings import *

class Team():
    def __init__(self, team_name, list, bench_list, logo, coach):
        self.team_name = team_name
        self.list = list
        self.bench_list = bench_list
        self.logo = logo
        self.coach = coach

def free_throws(player, quantity_of_free_throws):
        global last_event
        points_scored = 0
        first_free_throw = True
        for x in range(quantity_of_free_throws):
            time.sleep(3)
            if random.randint(0, 10) >= 5:
                if first_free_throw == True:
                    last_event = CommentaryEngine.commentator(player, 'firstfreethrowmake', None)
                    first_free_throw = False
                else:
                    last_event = CommentaryEngine.commentator(player, 'secondfreethrowmake', None)
                points_scored += 1
            else:
                if first_free_throw == True:
                    last_event = CommentaryEngine.commentator(player, 'firstfreethrowmiss', None)
                    first_free_throw = False
                else:
                    last_event = CommentaryEngine.commentator(player, 'secondfreethrowmiss', None)
        print(str(points_scored) + '/' + str(quantity_of_free_throws))
        time.sleep(1)
        return points_scored


class BasketballPlayer():
    def __init__(self, name, position, position_number, team, threefg_percent, passing, drivinglay, tov, perd, intd, interception, passpref, possession, defender, player, points_made, passes_made, interceptions_made, energy, nicknames):
        self.name = name
        self.position = position
        self.position_number = position_number
        self.team = team
        self.threefg_percent = threefg_percent
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
        self.nicknames = nicknames

    def decision(self):
        generated_probability = random.randint(1, 100)
        modified_probability  = generated_probability * (1 + self.passpref)
        if self.energy <= 11:
            return 'pass'
        if 81 > modified_probability >= 33.3:
            return 'pass'
        elif 150 >= modified_probability >= 81:
            if self.threefg_percent != 0:
                return '3pt'
            else:
                return 'drive'
        else:
            return 'drive'
    
    def action_success(self, decision, defender_perd, defender_intd, pass_receiver_preset, active_team):
        global last_event
        if decision == '3pt':
            last_event = CommentaryEngine.commentator(self, '3ptshot', None)
            self.energy -= (threept_energy_drain + random.randint(1, 7))

            time.sleep(1)

            make_chance = 10 - ( random.uniform(1, 4) * (1 + self.threefg_percent) ) - ( 1.5 + defender_perd ) * 1.5
            if make_chance > 4.8:
                print(harden_shooting)
                last_event = CommentaryEngine.commentator(self, '3ptmake', None)
                self.pointsMade += 3
                self.haspossession = False
                self.defender.haspossession = True
                time.sleep(1)
                return 'shot', 3
            else:
                last_event = CommentaryEngine.commentator(self, '3ptmiss', None)
                self.haspossession = False
                self.defender.haspossession = True
                time.sleep(1)
                return 'miss', 0

        if decision == 'drive':
            last_event = CommentaryEngine.commentator(self, 'drive', None)
            time.sleep(0.7)
            self.energy -= (drive_energy_drain + random.randint(1, 7))
            make_chance = 10 - ( random.uniform(1, 4) * (1 + self.drivinglay) ) - ( 1 + defender_intd ) * 1.5
            fouled = False

            if random.randint(0, 100) <= foul_chance:
                fouled = True

            if make_chance > 3.8:
                self.haspossession = False
                self.defender.haspossession = True
                if fouled == True:
                    print(lebron_dwyane)
                    last_event = CommentaryEngine.commentator(self, 'drivemakefoul', None)
                    free_throw_points = free_throws(self, 1)
                    self.pointsMade += (2 + free_throw_points)
                    return 'shot', (2 + free_throw_points)
                else:
                    print(lebron_dwyane)
                    last_event = CommentaryEngine.commentator(self, 'drivemake', None)
                    self.pointsMade += 2
                    return 'shot', 2
            else:
                self.haspossession = False
                self.defender.haspossession = True
                if fouled == True:
                    print(draymond)
                    last_event = CommentaryEngine.commentator(self, 'drivemissfoul', None)
                    free_throw_points = free_throws(self, 2)
                    self.pointsMade += (free_throw_points)
                    return 'shot', (free_throw_points)
                else:
                    last_event = CommentaryEngine.commentator(self, 'drivemiss', None)
                    return 'miss', 0
            
        if decision == 'pass':

            if pass_receiver_preset:
                if calculate_turnover_chance(self, pass_receiver_preset.defender) is False: 
                    last_event = CommentaryEngine.commentator(self, 'pass', pass_receiver_preset)
                    self.energy -= (pass_energy_drain + random.randint(1, 4))
                    self.passesMade += 1
                    pass_receiver_preset.haspossession = True
                    self.haspossession = False
                    return 'miss', 0
                else:
                    last_event = CommentaryEngine.commentator(self, 'pass', pass_receiver_preset)
                    last_event = CommentaryEngine.commentator(self, 'stolen', pass_receiver_preset)
                    self.energy -= (pass_energy_drain + random.randint(1, 4))
                    pass_receiver_preset.defender.interceptionsMade += 1
                    pass_receiver_preset.defender.haspossession = True
                    self.haspossession = False
                    return 'miss', 0
            else:
                while True:
                    pass_receiver_position_number = random.randint(1, 5)
                    if self.position_number != pass_receiver_position_number:
                        break
                if active_team == user_team:
                    for pass_receiver in user_team_list:
                        if pass_receiver.position_number == pass_receiver_position_number:
                            break
                    if calculate_turnover_chance(self, pass_receiver.defender) is False: 
                        print(haliburton)
                        last_event = CommentaryEngine.commentator(self, 'pass', pass_receiver)
                        self.energy -= (pass_energy_drain + random.randint(1, 4))
                        

                        self.passesMade += 1
                        pass_receiver.haspossession = True
                        self.haspossession = False
                        return 'miss', 0
                    else:
                        last_event = CommentaryEngine.commentator(self, 'pass', pass_receiver)
                        last_event = CommentaryEngine.commentator(self, 'stolen', pass_receiver)
                        self.energy -= (pass_energy_drain + random.randint(1, 4))
                        pass_receiver.defender.interceptionsMade += 1
                        pass_receiver.defender.haspossession = True
                        self.haspossession = False
                        return 'miss', 0

                else:
                    for pass_receiver in opposing_team_list:
                        if pass_receiver.position_number == pass_receiver_position_number:
                            break
                    if calculate_turnover_chance(self, pass_receiver.defender) is False: 
                        print(haliburton)
                        last_event = CommentaryEngine.commentator(self, 'pass', pass_receiver)
                        self.energy -= (pass_energy_drain + random.randint(1, 4))

                        self.passesMade += 1
                        pass_receiver.haspossession = True
                        self.haspossession = False
                        return 'miss', 0
                    else:
                        last_event = CommentaryEngine.commentator(self, 'pass', pass_receiver)
                        last_event = CommentaryEngine.commentator(self, 'stolen', pass_receiver)
                        self.energy -= (pass_energy_drain + random.randint(1, 4))
                        pass_receiver.defender.interceptionsMade += 1
                        pass_receiver.defender.haspossession = True
                        self.haspossession = False
                        return 'miss', 0
                    
    def substitution(self):
        global last_event
        global current_player
        
        if last_event == 'substitution_final':
            print('\n')

        if self.team == user_team:
            last_event = CommentaryEngine.commentator(self, 'substitution_initial', None)
            time.sleep(3)
            last_event = CommentaryEngine.commentator(user_team_list_bench[self.position_number-1], 'substitution_final', self)
            time.sleep(3)

            # hand off (possession given to subbed player, defenders reinitialized, lists swapped)
            user_team_list.insert(self.position_number-1, user_team_list_bench[self.position_number-1])   #insert bench player into roster
            user_team_list_bench.insert(self.position_number-1, user_team_list[self.position_number])   # insert former roster player into bench
            user_team_list.pop(self.position_number) # remove former roster player from roster
            user_team_list_bench.pop(self.position_number) # remove former bench player from bench
            
            if user_team_list_bench[self.position_number-1].haspossession == False:
                pass
            else:
                user_team_list_bench[self.position_number-1].haspossession = False
                user_team_list[self.position_number-1].haspossession = True
            if user_team_list_bench[self.position_number-1].isplayer == False:
                pass
            else:
                user_team_list_bench[self.position_number-1].isplayer = False
                user_team_list[self.position_number-1].isplayer = True
                current_player = user_team_list[current_player.position_number-1]
                current_player.haspossession = True
                current_player.isplayer = True


            user_team_list_bench[self.position_number-1].energy += 10

            # RE-INITIALIZE DEFENDERS
            for player in user_team_list:
                defender = KermLib.object_matcher(player, opposing_team_list, 'position_number')
                player.defender = defender
                defender.defender = player
            combined_list = user_team_list + opposing_team_list
            return combined_list
        else:
            last_event = CommentaryEngine.commentator(self, 'substitution_initial', None)
            time.sleep(3)
            last_event = CommentaryEngine.commentator(opposing_team_list_bench[self.position_number-1], 'substitution_final', self)
            time.sleep(3)

            # hand off (possession given to subbed player, defenders reinitialized, lists swapped)
            opposing_team_list.insert(self.position_number-1, opposing_team_list_bench[self.position_number-1])   #insert bench player into roster
            opposing_team_list_bench.insert(self.position_number-1, opposing_team_list[self.position_number])   # insert former roster player into bench
            opposing_team_list.pop(self.position_number) # remove former roster player from roster
            opposing_team_list_bench.pop(self.position_number) # remove former bench player from bench
            
            if opposing_team_list_bench[self.position_number-1].haspossession == False:
                pass
            else:
                opposing_team_list_bench[self.position_number-1].haspossession = False
                opposing_team_list[self.position_number-1].haspossession = True

            opposing_team_list_bench[self.position_number-1].energy += 10
            # RE-INITIALIZE DEFENDERS
            for player in opposing_team_list:
                defender = KermLib.object_matcher(player, user_team_list, 'position_number')
                player.defender = defender
                defender.defender = player

        #update list
        combined_list = user_team_list + opposing_team_list
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





# NUGGETS STARTING UNIT
j_murray = BasketballPlayer("Jamal Murray", "Point Guard", 1, "Denver Nuggets", .400, 0.85, 0.70, 0.12, 0.28, 0.22, 0.12, 0.40, False, None, False, 0, 0, 0, 100, ["The Blue Arrow"])
c_braun = BasketballPlayer("Christian Braun", "Shooting Guard", 2, "Denver Nuggets", .370, 0.50, 0.65, 0.11, 0.22, 0.20, 0.10, 0.30, False, None, False, 0, 0, 0, 100, None)
m_porter_jr = BasketballPlayer("Michael Porter Jr.", "Small Forward", 3, "Denver Nuggets", .430, 0.60, 0.65, 0.10, 0.25, 0.22, 0.10, 0.35, False, None, False, 0, 0, 0, 100, ["MPJ"])
a_gordon = BasketballPlayer("Aaron Gordon", "Power Forward", 4, "Denver Nuggets", .350, 0.50, 0.70, 0.12, 0.30, 0.25, 0.15, 0.30, False, None, False, 0, 0, 0, 100, ["AG"])
n_jokic = BasketballPlayer("Nikola Jokic", "Center", 5, "Denver Nuggets", .500, 0.90, 0.75, 0.12, 0.40, 0.30, 0.15, 0.50, False, None, False, 0, 0, 0, 100, ["the Joker"])


# NUGGETS BENCH UNIT
r_westbrook = BasketballPlayer("Russell Westbrook", "Point Guard", 1, "Denver Nuggets", 0.430, 0.60, 0.68, 0.15, 0.30, 0.25, 0.12, 0.40, False, None, False, 0, 0, 0, 100, ["Brodie"])
j_strawther = BasketballPlayer("Julian Strawther", "Shooting Guard", 2, "Denver Nuggets", 0.420, 0.65, 0.70, 0.10, 0.25, 0.20, 0.12, 0.30, False, None, False, 0, 0, 0, 100, None)
h_tyson = BasketballPlayer("Hunter Tyson", "Small Forward", 3, "Denver Nuggets", 0.400, 0.60, 0.65, 0.11, 0.22, 0.18, 0.10, 0.32, False, None, False, 0, 0, 0, 100, None)
p_watson = BasketballPlayer("Peyton Watson", "Power Forward", 4, "Denver Nuggets", 0.380, 0.55, 0.62, 0.12, 0.25, 0.22, 0.12, 0.35, False, None, False, 0, 0, 0, 100, None)
j_valanciunas = BasketballPlayer("Jonas Valanciunas", "Center", 5, "Denver Nuggets", 0.300, 0.60, 0.75, 0.13, 0.30, 0.28, 0.15, 0.40, False, None, False, 0, 0, 0, 100, None)


# 76ers STARTING UNIT
t_maxey = BasketballPlayer("Tyrese Maxey", "Point Guard", 1, "Philadelphia 76ers", 0.420, 0.75, 0.70, 0.10, 0.25, 0.22, 0.10, 0.35, False, None, False, 0, 0, 0, 100, None)
k_oubre = BasketballPlayer("Kelly Oubre Jr.", "Shooting Guard", 2, "Philadelphia 76ers", 0.430, 0.55, 0.70, 0.12, 0.25, 0.22, 0.12, 0.35, False, None, False, 0, 0, 0, 100, None)
p_george = BasketballPlayer("Paul George", "Small Forward", 3, "Philadelphia 76ers", 0.380, 0.65, 0.68, 0.11, 0.28, 0.25, 0.13, 0.35, False, None, False, 0, 0, 0, 100, ["PG13", "Pandemic-P", "Playoff-P", "Podcast-P", "Wayoff-P", "George Paul"])
g_yabusele = BasketballPlayer("Guerschon Yabusele", "Power Forward", 4, "Philadelphia 76ers", 0.380, 0.50, 0.60, 0.12, 0.22, 0.20, 0.10, 0.30, False, None, False, 0, 0, 0, 100, None)
j_embiid = BasketballPlayer("Joel Embiid", "Center", 5, "Philadelphia 76ers", 0.370, 0.60, 0.75, 0.13, 0.30, 0.25, 0.15, 0.40, False, None, False, 0, 0, 0, 100, ["The Process"])


# 76ers BENCH UNIT
r_jackson = BasketballPlayer("Reggie Jackson", "Point Guard", 1, "Philadelphia 76ers", 0.374, 0.60, 0.70, 0.12, 0.20, 0.18, 0.10, 0.30, False, None, False, 0, 0, 0, 100, ["the Big Government", "Mr. June"])
k_lowry = BasketballPlayer("Kyle Lowry", "Shooting Guard", 2, "Philadelphia 76ers", 0.400, 0.80, 0.70, 0.10, 0.30, 0.25, 0.12, 0.40, False, None, False, 0, 0, 0, 100, None)
c_martin = BasketballPlayer("Caleb Martin", "Small Forward", 3, "Philadelphia 76ers", 0.370, 0.55, 0.65, 0.09, 0.22, 0.20, 0.12, 0.30, False, None, False, 0, 0, 0, 100, None)
p_nance = BasketballPlayer("Pete Nance", "Power Forward", 4, "Philadelphia 76ers", 0.380, 0.60, 0.65, 0.12, 0.22, 0.20, 0.12, 0.30, False, None, False, 0, 0, 0, 100, None)
a_drummond = BasketballPlayer("Andre Drummond", "Center", 5, "Philadelphia 76ers", 0.1, 0.20, 0.60, 0.15, 0.18, 0.30, 0.15, 0.30, False, None, False, 0, 0, 0, 100, None)


sixers_list = [t_maxey, k_oubre, p_george, g_yabusele, j_embiid]
sixers_bench_list = [r_jackson, k_lowry, c_martin, p_nance, a_drummond]


nuggets_list = [j_murray, c_braun, m_porter_jr, a_gordon, n_jokic]
nuggets_bench_list = [r_westbrook, j_strawther, h_tyson , p_watson, j_valanciunas]


teams_names = ['Philadelphia 76ers', 'Denver Nuggets']

sixers_team = Team("Philadelphia 76ers", sixers_list, sixers_bench_list, sixers_logo, 'Nick Nurse')
nuggets_team = Team("Denver Nuggets", nuggets_list, nuggets_bench_list, nuggets_logo, 'Mike Malone')


list_of_team_objects = [sixers_team, nuggets_team]







KermLib.ascii_run()
print('Blacktop ' + version)
print('\n')

print('Select your team!')

team = 1
for team_name in teams_names:
    print(team, 'for the', team_name)
    team += 1
team_quantity = list(range(1, team))
team_quantity = [str(x) for x in team_quantity]
user_team_input = KermLib.get_user_input(team_quantity)
user_team_input = int(user_team_input)

print('\n')
match user_team_input:
    case 1:
        user_team_object = sixers_team
    case 2:
        user_team_object = nuggets_team


user_team = user_team_object.team_name
user_team_list = user_team_object.list
user_team_list_bench = user_team_object.bench_list
user_team_logo = user_team_object.logo

print(user_team_logo)

print('\n' + '\n')

print('Team selected:', user_team)

print('\n' + '\n' + '\n')


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

if opposing_team == 'Philadelphia 76ers':
    opposing_team_object = sixers_team
elif opposing_team == 'Denver Nuggets':
    opposing_team_object = nuggets_team


opposing_team = opposing_team_object.team_name
opposing_team_list = opposing_team_object.list
opposing_team_list_bench = opposing_team_object.bench_list
opposing_team_logo = opposing_team_object.logo


print(opposing_team_logo)

print('\n' + '\n')

print('Opposing team selected:', opposing_team)

combined_list = user_team_list + opposing_team_list

print('\n' + '\n' + '\n')

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
    defender = KermLib.object_matcher(player, opposing_team_list, 'position_number')
    player.defender = defender
    defender.defender = player

time.sleep(2)

print('\n' + '\n')

if auto_or_manual in ['m', "M"]:
    for player in user_team_list:
        if player.position_number == player_decision:
            player.isplayer = True
            current_player = player
            print('\n')
            print('Player selected:', current_player.name)
            break
else:
    current_player = None

print('\n' + '\n')

print(user_team, 'vs.', opposing_team)
print('\n')

time.sleep(0.5)

print('Starting lineup:')
for x in range(5):
    if user_team_list[x] == current_player:
        print('(You)', user_team_list[x].name, ' -- ', opposing_team_list[x].name)
    else:
        print(user_team_list[x].name, ' -- ', opposing_team_list[x].name)
    time.sleep(0.3)

print('\n' + '\n')

print('Bench lineup:')
for x in range(5):
    print(user_team_list_bench[x].name, ' -- ', opposing_team_list_bench[x].name)
    time.sleep(0.3)

print('\n' + '\n')

print('First to', str(end_score) +  '! Game start!')
print('\n' * 3)
start_time = time.time()

time.sleep(2)



#-------------------------------

# TIP OFF
last_event = CommentaryEngine.commentator(user_team_list[4], 'tipoff', opposing_team_list[4])
time.sleep(1.5)
if random.randint(1, 2) == 1:
    tip_receiver_index = random.randint(0, 3)
    last_event = CommentaryEngine.commentator(user_team_list[4], 'tipoffoutcome', user_team_list[tip_receiver_index])
    user_team_list[tip_receiver_index].haspossession = True
else:
    tip_receiver_index = random.randint(0, 3)
    last_event = CommentaryEngine.commentator(opposing_team_list[4], 'tipoffoutcome', opposing_team_list[tip_receiver_index])
    opposing_team_list[tip_receiver_index].haspossession = True



while True:
    end_time = time.time()  

    if opposing_team_score >= end_score or user_team_score >= end_score:
        if opposing_team_score >= end_score:
            print('---------------------------------------------------------------------------------------------------------')
            print(opposing_team + ' win! Final score:', opposing_team_score, '-', user_team_score)
            print('---------------------------------------------------------------------------------------------------------')
            print(opposing_team_logo)
            winning_team_list = opposing_team_list
            winning_team_list_bench = opposing_team_list_bench
            losing_team_list = user_team_list
            losing_team_list_bench = user_team_list_bench
        else:
            print('---------------------------------------------------------------------------------------------------------')
            print(user_team + ' win! Final score:', user_team_score, '-', opposing_team_score)
            print('---------------------------------------------------------------------------------------------------------')
            print(user_team_logo)
            winning_team_list = user_team_list
            winning_team_list_bench = user_team_list_bench
            losing_team_list = opposing_team_list
            losing_team_list_bench = opposing_team_list_bench

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

        
        time.sleep(3)
        print('Game duration:', round((end_time - start_time)/60, 1), 'minutes')
        print('\n' + '\n' + 'Box score (Points, Passes, Interceptions)' + '\n')
        print(user_team + ':')
        for x in range(5):
            if user_team_list[x] == current_player:
                print('(You)', user_team_list[x].name + ':', str(user_team_list[x].pointsMade) + ',', str(user_team_list[x].passesMade) + ',', str(user_team_list[x].interceptionsMade))
            else:
                print(user_team_list[x].name + ':', str(user_team_list[x].pointsMade) + ',', str(user_team_list[x].passesMade) + ',', str(user_team_list[x].interceptionsMade))
            time.sleep(0.3)
        
        print('\n')
        for x in range(5):
            if user_team_list_bench[x] == current_player:
                print('(You)', user_team_list_bench[x].name + ':', str(user_team_list_bench[x].pointsMade) + ',', str(user_team_list_bench[x].passesMade) + ',', str(user_team_list_bench[x].interceptionsMade))
            else:
                print(user_team_list_bench[x].name + ':', str(user_team_list_bench[x].pointsMade) + ',', str(user_team_list_bench[x].passesMade) + ',', str(user_team_list_bench[x].interceptionsMade))
            time.sleep(0.3)

        print('\n' + '\n')
        print(opposing_team + ':')

        for x in range(5):
            if opposing_team_list[x] == current_player:
                print('(You)', opposing_team_list[x].name + ':', str(opposing_team_list[x].pointsMade) + ',', str(opposing_team_list[x].passesMade) + ',', str(opposing_team_list[x].interceptionsMade))
            else:
                print(opposing_team_list[x].name + ':', str(opposing_team_list[x].pointsMade) + ',', str(opposing_team_list[x].passesMade) + ',', str(opposing_team_list[x].interceptionsMade))
            time.sleep(0.3)
        
        print('\n')
        for x in range(5):
            if opposing_team_list_bench[x] == current_player:
                print('(You)', opposing_team_list_bench[x].name + ':', str(opposing_team_list_bench[x].pointsMade) + ',', str(opposing_team_list_bench[x].passesMade) + ',', str(opposing_team_list_bench[x].interceptionsMade))
            else:
                print(opposing_team_list_bench[x].name + ':', str(opposing_team_list_bench[x].pointsMade) + ',', str(opposing_team_list_bench[x].passesMade) + ',', str(opposing_team_list_bench[x].interceptionsMade))
            time.sleep(0.3)

        print('\n' + '\n')



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

        highest_ppi = 0
        mvp = None
        for player in winning_team_list + winning_team_list_bench:
            ppi = player.pointsMade + player.passesMade + player.interceptionsMade
            if ppi > highest_ppi:
                highest_ppi = ppi
                mvp = player

        if mvp is None: # if no SVP, default to winning team point guard
            mvp = winning_team_list[0]

        print('\n')
        print('MVP:', mvp.name, '(' + str(highest_ppi), 'PPI)')


        highest_ppi = 0
        mvp = None
        for player in losing_team_list + losing_team_list_bench:
            ppi = player.pointsMade + player.passesMade + player.interceptionsMade
            if ppi > highest_ppi:
                highest_ppi = ppi
                mvp = player
    
        if mvp is None: # if no SVP, default to losing team point guard
            mvp = losing_team_list[0]

        time.sleep(1.5)
        print('SVP:', mvp.name, '(' + str(highest_ppi), 'PPI)')


        print('\n')

        
        time.sleep(5)


        exit_key = input('Press enter to exit....')

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
                combined_list = player.substitution()



        if player.haspossession is True:
            if last_event == 'substitution_final':
                print('\n')
            print(player.name + "'s energy:", str(player.energy) + '%')
            if last_event != 'pass':
                last_event = CommentaryEngine.commentator(player, 'haspossession', player.defender)
            time.sleep(0.8)
            time.sleep(0.8)
            if player.isplayer == True:
                if player.energy != 0:
                    print('What will you do? (pass), (drive), shoot a (3pt), or manually (substitute)?')
                    player_action_decision = KermLib.get_user_input(['pass', 'drive', '3pt', 'substitute'])
                else:
                    print(player.name + "'s energy is too low! Forcing substitution!")
                    player_action_decision = 'substitute'
                    time.sleep(1)
                
                if player_action_decision in ['pass', 'Pass']:
                    print('Who will you pass to?')

                    for player in user_team_list:
                        if player == current_player:
                            position_number += 1
                            continue
                        position_number += 1
                        print(player.name + ' -- ' + str(position_number), '(defended by', player.defender.name + ')', '(Energy:', str(player.energy) + '%)')
                
                    while True:
                        player_decision = str(input())
                        if player_decision not in ['1', '2', '3', '4', '5'] or player_decision == str(current_player.position_number):
                            print('Decision not recognized. Please try again')
                            continue
                        else:
                            player_decision = int(player_decision)
                            break



                    for player in user_team_list:
                        if player.position_number == player_decision:
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

