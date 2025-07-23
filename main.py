import random
import time
from KermLib.KermLib import *
from vars.basketball_ascii import *
from commentary import *
version = '2025.5.26.1820.stable'

end_score = 21 # target score to win
foul_chance = 28 # chance of a foul on a drive in percent

pass_energy_drain = 13 # this is base chance, plus random number between 1 and 4
threept_energy_drain = 28 # this is base chance, plus random number between 1 and 7
drive_energy_drain = 34 # this is base chance, plus random number between 1 and 7


opposing_team_score = 0 # Start score for each team. DO NOT CHANGE
user_team_score = 0 # Start score for each team. DO NOT CHANGE

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
    def __init__(self, name, position, positionnumber, team, threept, passing, drivinglay, tov, perd, intd, interception, passpref, possession, defender, player, points_made, passes_made, interceptions_made, energy, nicknames):
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
        self.nicknames = nicknames

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
        global last_event
        if decision == '3pt':
            last_event = CommentaryEngine.commentator(self, '3ptshot', None)
            self.energy -= (threept_energy_drain + random.randint(1, 7))

            time.sleep(1)

            make_chance = 10 - ( random.uniform(1, 4) * (1 + self.threept) ) - ( 1.5 + defender_perd ) * 1.5
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
                    if self.positionnumber != pass_receiver_position_number:
                        break
                if active_team == user_team:
                    for pass_receiver in user_team_list:
                        if pass_receiver.positionnumber == pass_receiver_position_number:
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
                        if pass_receiver.positionnumber == pass_receiver_position_number:
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
        
        if last_event is 'substitution_final':
            print('\n')

        if self.team == user_team:
            last_event = CommentaryEngine.commentator(self, 'substitution_initial', None)
            time.sleep(3)
            last_event = CommentaryEngine.commentator(user_team_list_bench[self.positionnumber-1], 'substitution_final', self)
            time.sleep(3)

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
            return combined_list
        else:
            last_event = CommentaryEngine.commentator(self, 'substitution_initial', None)
            time.sleep(3)
            last_event = CommentaryEngine.commentator(opposing_team_list_bench[self.positionnumber-1], 'substitution_final', self)
            time.sleep(3)

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







# PELICANS STARTING UNIT
d_murray = BasketballPlayer("Dejounte Murray", "Point Guard", 1, "New Orleans Pelicans", .450, 0.80, 0.72, 0.12, 0.30, 0.25, 0.15, 0.40, False, None, False, 0, 0, 0, 100, None)
c_mccollum = BasketballPlayer("CJ McCollum", "Shooting Guard", 2, "New Orleans Pelicans", .400, 0.75, 0.68, 0.10, 0.30, 0.20, 0.12, 0.35, False, None, False, 0, 0, 0, 100, ["C.J"])
b_ingram = BasketballPlayer("Brandon Ingram", "Small Forward", 3, "New Orleans Pelicans", .380, 0.65, 0.70, 0.11, 0.28, 0.25, 0.12, 0.40, False, None, False, 0, 0, 0, 100, ["B.I", "The Sleepy Reaper"])
z_williamson = BasketballPlayer("Zion Williamson", "Power Forward", 4, "New Orleans Pelicans", .370, 0.40, 0.75, 0.10, 0.35, 0.30, 0.15, 0.30, False, None, False, 0, 0, 0, 100, None)
y_missi = BasketballPlayer("Yves Missi", "Center", 5, "New Orleans Pelicans", 0.350, 0.45, 0.60, 0.12, 0.25, 0.22, 0.14, 0.32, False, None, False, 0, 0, 0, 100, None)


# PELICANS BENCH UNIT
j_hawkins = BasketballPlayer("Jordan Hawkins", "Point Guard", 1, "New Orleans Pelicans", 0.400, 0.65, 0.70, 0.10, 0.25, 0.20, 0.12, 0.30, False, None, False, 0, 0, 0, 100, None)
t_murphy_iii = BasketballPlayer("Trey Murphy III", "Shooting Guard", 2, "New Orleans Pelicans", 0.450, 0.65, 0.75, 0.10, 0.25, 0.22, 0.12, 0.35, False, None, False, 0, 0, 0, 100, None)
b_boston_jr = BasketballPlayer("Brandon Boston Jr.", "Small Forward", 3, "New Orleans Pelicans", 0.390, 0.60, 0.65, 0.11, 0.22, 0.18, 0.10, 0.30, False, None, False, 0, 0, 0, 100, None)
jav_green = BasketballPlayer("Javonte Green", "Power Forward", 4, "New Orleans Pelicans", 0.400, 0.55, 0.68, 0.12, 0.25, 0.20, 0.12, 0.32, False, None, False, 0, 0, 0, 100, None)
j_robinson_earl = BasketballPlayer("Jeremiah Robinson-Earl", "Center", 5, "New Orleans Pelicans", 0.370, 0.50, 0.62, 0.12, 0.22, 0.20, 0.12, 0.30, False, None, False, 0, 0, 0, 100, None)


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
d_jordan_den = BasketballPlayer("DeAndre Jordan", "Center", 5, "Denver Nuggets", 0.000, 0.20, 0.60, 0.12, 0.18, 0.22, 0.14, 0.30, False, None, False, 0, 0, 0, 100, ["DJ"])


# MAVERICKS STARTING UNIT
d_russell = BasketballPlayer("D'Angelo Russell", "Point Guard", 1, "Dallas Mavericks", .382, 0.87, 0.72, 0.15, 0.32, 0.28, 0.14, 0.50, False, None, False, 0, 0, 0, 100, ["D'Lo"])
k_irving = BasketballPlayer("Kyrie Irving", "Shooting Guard", 2, "Dallas Mavericks", .395, 0.80, 0.70, 0.12, 0.28, 0.22, 0.12, 0.45, False, None, False, 0, 0, 0, 100, ["Kai", "Kyrie"])
k_thompson = BasketballPlayer("Klay Thompson", "Small Forward", 3, "Dallas Mavericks", .413, 0.65, 0.60, 0.10, 0.25, 0.20, 0.10, 0.40, False, None, False, 0, 0, 0, 100, None)
a_davis = BasketballPlayer("Anthony Davis", "Power Forward", 4, "Los Angeles Lakers", .350, 0.30, 0.72, 0.12, 0.25, 0.28, 0.15, 0.3, False, None, False, 0, 0, 0, 100, ["AD"])
d_lively = BasketballPlayer("Dereck Lively II", "Center", 5, "Dallas Mavericks", 0.330, 0.40, 0.60, 0.12, 0.25, 0.22, 0.12, 0.30, False, None, False, 0, 0, 0, 100, None)


# MAVERICKS BENCH UNIT
s_dinwiddie = BasketballPlayer("Spencer Dinwiddie", "Point Guard", 1, "Dallas Mavericks", 0.450, 0.80, 0.70, 0.12, 0.25, 0.20, 0.10, 0.35, False, None, False, 0, 0, 0, 100, None)
m_christie = BasketballPlayer("Max Christie", "Shooting Guard", 2, "Dallas Mavericks", 0.390, 0.70, 0.68, 0.10, 0.25, 0.20, 0.10, 0.30, False, None, False, 0, 0, 0, 100, None)
d_exum = BasketballPlayer("Dante Exum", "Small Forward", 3, "Dallas Mavericks", 0.370, 0.60, 0.60, 0.10, 0.22, 0.18, 0.10, 0.30, False, None, False, 0, 0, 0, 100, None)
p_washington = BasketballPlayer("P.J. Washington", "Power Forward", 4, "Dallas Mavericks", .370, 0.60, 0.65, 0.11, 0.22, 0.20, 0.11, 0.35, False, None, False, 0, 0, 0, 100, None)
d_gafford = BasketballPlayer("Daniel Gafford", "Center", 5, "Dallas Mavericks", 0.000, 0.50, 0.60, 0.12, 0.20, 0.22, 0.12, 0.30, False, None, False, 0, 0, 0, 100, None)


# MAGIC STARTING UNIT
j_suggs = BasketballPlayer("Jalen Suggs", "Point Guard", 1, "Orlando Magic", .330, 0.60, 0.65, 0.14, 0.20, 0.18, 0.13, 0.35, False, None, False, 0, 0, 0, 100, None)
d_bane = BasketballPlayer("Desmond Bane", "Shooting Guard", 2, "Memphis Grizzlies", 0.430, 0.80, 0.70, 0.10, 0.22, 0.18, 0.11, 0.40, False, None, False, 0, 0, 0, 100, None)
f_wagner = BasketballPlayer("Franz Wagner", "Small Forward", 3, "Orlando Magic", .360, 0.65, 0.70, 0.11, 0.25, 0.18, 0.12, 0.35, False, None, False, 0, 0, 0, 100, None)
p_banchero = BasketballPlayer("Paolo Banchero", "Power Forward", 4, "Orlando Magic", .340, 0.70, 0.75, 0.13, 0.28, 0.20, 0.10, 0.40, False, None, False, 0, 0, 0, 100, None)
w_carter_jr = BasketballPlayer("Wendell Carter Jr.", "Center", 5, "Orlando Magic", .320, 0.60, 0.68, 0.12, 0.22, 0.20, 0.14, 0.30, False, None, False, 0, 0, 0, 100, None)


# MAGIC BENCH UNIT
a_black = BasketballPlayer("Anthony Black", "Point Guard", 1, "Orlando Magic", 0.400, 0.70, 0.68, 0.12, 0.25, 0.20, 0.12, 0.30, False, None, False, 0, 0, 0, 100, None)
c_anthony = BasketballPlayer("Cole Anthony", "Shooting Guard", 2, "Orlando Magic", 0.420, 0.65, 0.70, 0.10, 0.25, 0.22, 0.12, 0.32, False, None, False, 0, 0, 0, 100, None)
g_harris = BasketballPlayer("Gary Harris", "Small Forward", 3, "Orlando Magic", 0.410, 0.60, 0.65, 0.11, 0.22, 0.20, 0.12, 0.35, False, None, False, 0, 0, 0, 100, None)
j_isaac = BasketballPlayer("Jonathan Isaac", "Power Forward", 4, "Orlando Magic", 0.390, 0.55, 0.62, 0.12, 0.25, 0.22, 0.14, 0.35, False, None, False, 0, 0, 0, 100, None)
g_bitadze = BasketballPlayer("Goga Bitadze", "Center", 5, "Orlando Magic", 0.350, 0.50, 0.60, 0.12, 0.18, 0.22, 0.14, 0.30, False, None, False, 0, 0, 0, 100, None)


# WARRIORS STARTING UNIT
s_curry = BasketballPlayer("Stephen Curry", "Point Guard", 1, "Golden State Warriors", .428, 0.85, 0.70, 0.12, 0.30, 0.25, 0.15, 0.50, False, None, False, 0, 0, 0, 100, ["Chef Curry"])
b_hield = BasketballPlayer("Buddy Hield", "Shooting Guard", 2, "Golden State Warriors", .400, 0.70, 0.65, 0.10, 0.25, 0.20, 0.12, 0.45, False, None, False, 0, 0, 0, 100, None)
an_wiggins = BasketballPlayer("Andrew Wiggins", "Small Forward", 3, "Golden State Warriors", .420, 0.55, 0.62, 0.10, 0.22, 0.18, 0.14, 0.35, False, None, False, 0, 0, 0, 100, None)
j_kuminga = BasketballPlayer("Jonathan Kuminga", "Power Forward", 4, "Golden State Warriors", 0.420, 0.55, 0.65, 0.12, 0.25, 0.22, 0.12, 0.35, False, None, False, 0, 0, 0, 100, None)
d_green = BasketballPlayer("Draymond Green", "Center", 5, "Golden State Warriors", .320, 0.70, 0.55, 0.15, 0.40, 0.30, 0.18, 0.35, False, None, False, 0, 0, 0, 100, None)


# WARRIORS BENCH UNIT
b_podziemski = BasketballPlayer("Brandin Podziemski", "Point Guard", 1, "Golden State Warriors", 0.410, 0.65, 0.68, 0.12, 0.22, 0.20, 0.12, 0.30, False, None, False, 0, 0, 0, 100, ["Podz", "Airpodz"])
m_moody = BasketballPlayer("Moses Moody", "Shooting Guard", 2, "Golden State Warriors", 0.390, 0.60, 0.65, 0.10, 0.25, 0.22, 0.10, 0.30, False, None, False, 0, 0, 0, 100, None)
g_payton_ii = BasketballPlayer("Gary Payton-II", "Small Forward", 3, "Golden State Warriors", 0.420, 0.60, 0.65, 0.10, 0.22, 0.20, 0.12, 0.32, False, None, False, 0, 0, 0, 100, ["GP2"])
k_anderson = BasketballPlayer("Kyle Anderson", "Power Forward", 4, "Golden State Warriors", 0.380, 0.55, 0.60, 0.12, 0.25, 0.22, 0.12, 0.35, False, None, False, 0, 0, 0, 100, None)
k_looney = BasketballPlayer("Kevon Looney", "Center", 5, "Golden State Warriors", .300, 0.25, 0.60, 0.10, 0.20, 0.20, 0.10, 0.25, False, None, False, 0, 0, 0, 100, ["Loon"])


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


# SUNS STARTING UNIT
d_booker = BasketballPlayer("Devin Booker", "Point Guard", 1, "Phoenix Suns", .470, 0.75, 0.70, 0.10, 0.28, 0.22, 0.12, 0.30, False, None, False, 0, 0, 0, 100, ["D-Book", "Book"])
j_green = BasketballPlayer("Jalen Green", "Shooting Guard", 2, "Houston Rockets", 0.340, 0.70, 0.65, 0.12, 0.22, 0.18, 0.12, 0.40, False, None, False, 0, 0, 0, 100, None)
d_brooks = BasketballPlayer("Dillon Brooks", "Small Forward", 3, "Phoenix Suns", .450, 0.70, 0.68, 0.12, 0.28, 0.18, 0.10, 0.30, False, None, False, 0, 0, 0, 100, None)
n_hayes_davis = BasketballPlayer("Nigel Hayes-Davis", "Power Forward", 4, "Phoenix Suns", .490, 0.80, 0.72, 0.08, 0.35, 0.30, 0.18, 0.40, False, None, False, 0, 0, 0, 100, None)
j_nurkic = BasketballPlayer("Jusuf Nurkic", "Center", 5, "Phoenix Suns", .380, 0.25, 0.65, 0.10, 0.20, 0.18, 0.14, 0.30, False, None, False, 0, 0, 0, 100, None)


# SUNS BENCH UNIT
m_morris = BasketballPlayer("Monte Morris", "Point Guard", 1, "Phoenix Suns", 0.400, 0.70, 0.65, 0.11, 0.22, 0.20, 0.12, 0.30, False, None, False, 0, 0, 0, 100, None)
g_allen = BasketballPlayer("Grayson Allen", "Shooting Guard", 2, "Phoenix Suns", 0.400, 0.65, 0.68, 0.12, 0.25, 0.20, 0.12, 0.30, False, None, False, 0, 0, 0, 100, None)
r_oneale = BasketballPlayer("Royce O'Neale", "Small Forward", 3, "Phoenix Suns", 0.380, 0.60, 0.65, 0.11, 0.22, 0.18, 0.10, 0.32, False, None, False, 0, 0, 0, 100, None)
r_dunn = BasketballPlayer("Ryan Dunn", "Power Forward", 4, "Phoenix Suns", 0.370, 0.55, 0.62, 0.10, 0.20, 0.18, 0.10, 0.30, False, None, False, 0, 0, 0, 100, None)
m_plumlee = BasketballPlayer("Mason Plumlee", "Center", 5, "Phoenix Suns", 0.000, 0.50, 0.60, 0.12, 0.25, 0.22, 0.14, 0.35, False, None, False, 0, 0, 0, 100, ["Plumdog Millionaire"])

# KNICKS STARTING UNIT
j_brunson = BasketballPlayer("Jalen Brunson", "Point Guard", 1, "New York Knicks", 0.470, 0.75, 0.70, 0.09, 0.28, 0.22, 0.12, 0.40, False, None, False, 0, 0, 0, 100, None)
m_bridges = BasketballPlayer("Mikal Bridges", "Shooting Guard", 2, "New York Knicks", 0.410, 0.65, 0.68, 0.11, 0.22, 0.18, 0.10, 0.30, False, None, False, 0, 0, 0, 100, None)
o_anunoby = BasketballPlayer("OG Anunoby", "Small Forward", 3, "New York Knicks", 0.450, 0.60, 0.65, 0.12, 0.24, 0.20, 0.14, 0.35, False, None, False, 0, 0, 0, 100, None)
p_achiuwa = BasketballPlayer("Precious Achiuwa", "Power Forward", 4, "New York Knicks", 0.460, 0.45, 0.70, 0.10, 0.30, 0.32, 0.15, 0.40, False, None, False, 0, 0, 0, 100, None)
k_towns = BasketballPlayer("Karl-Anthony Towns", "Center", 5, "New York Knicks", 0.370, 0.15, 0.75, 0.08, 0.18, 0.28, 0.20, 0.30, False, None, False, 0, 0, 0, 100, ["KAT"])


# KNICKS BENCH UNIT
c_payne = BasketballPlayer("Cameron Payne", "Point Guard", 1, "New York Knicks", 0.390, 0.65, 0.65, 0.12, 0.25, 0.20, 0.12, 0.32, False, None, False, 0, 0, 0, 100, None)
j_clarkson = BasketballPlayer("Jordan Clarkson", "Shooting Guard", 2, "Utah Jazz", 0.330, 0.65, 0.68, 0.12, 0.28, 0.22, 0.13, 0.40, False, None, False, 0, 0, 0, 100, None)
j_hart = BasketballPlayer("Josh Hart", "Small Forward", 3, "New York Knicks", 0.400, 0.70, 0.68, 0.11, 0.22, 0.20, 0.12, 0.35, False, None, False, 0, 0, 0, 100, None)
j_sims = BasketballPlayer("Jericho Sims", "Power Forward", 4, "New York Knicks", 0.350, 0.50, 0.62, 0.12, 0.25, 0.22, 0.12, 0.30, False, None, False, 0, 0, 0, 100, None)
m_robinson = BasketballPlayer("Mitchell Robinson", "Center", 5, "New York Knicks", 0.000, 0.40, 0.65, 0.10, 0.22, 0.20, 0.14, 0.30, False, None, False, 0, 0, 0, 100, None)


# CELTICS STARTING UNIT
j_holiday = BasketballPlayer("Jrue Holiday", "Point Guard", 1, "Boston Celtics", .480, .429, .833, .120, .180, .080, .090, .160, False, None, False, 0, 0, 0, 100, None)
d_white = BasketballPlayer("Derrick White", "Shooting Guard", 2, "Boston Celtics", 0.396, 0.75, 0.70, 0.12, 0.25, 0.20, 0.12, 0.40, False, None, False, 0, 0, 0, 100, None)
j_brown = BasketballPlayer("Jaylen Brown", "Small Forward", 3, "Boston Celtics", .480, .335, .765, .120, .180, .050, .060, .200, False, None, False, 0, 0, 0, 100, None)
j_tatum = BasketballPlayer("Jayson Tatum", "Power Forward", 4, "Boston Celtics", .473, .354, .854, .091, .200, .100, .060, .250, False, None, False, 0, 0, 0, 100, None)
k_porzingis = BasketballPlayer("Kristaps Porzingis", "Center", 5, "Boston Celtics", .498, .385, .850, .120, .180, .190, .070, .220, False, None, False, 0, 0, 0, 100, None)

# CELTICS BENCH UNIT
p_pritchard = BasketballPlayer("Payton Pritchard", "Point Guard", 1, "Boston Celtics", 0.375, 0.70, 0.65, 0.10, 0.20, 0.15, 0.10, 0.50, False, None, False, 0, 0, 0, 100, None)
b_scheierman = BasketballPlayer("Baylor Scheierman", "Shooting Guard", 2, "Boston Celtics", 0.218, 0.60, 0.65, 0.10, 0.20, 0.15, 0.10, 0.40, False, None, False, 0, 0, 0, 100, None)
s_hauser = BasketballPlayer("Sam Hauser", "Small Forward", 3, "Boston Celtics", 0.400, 0.60, 0.55, 0.09, 0.20, 0.12, 0.10, 0.40, False, None, False, 0, 0, 0, 100, None)
a_horford = BasketballPlayer("Al Horford", "Power Forward", 4, "Boston Celtics", .470, .380, .820, .130, .180, .100, .060, .140, False, None, False, 0, 0, 0, 100, None)
l_kornet = BasketballPlayer("Luke Kornet", "Center", 5, "Boston Celtics", 0.000, 0.50, 0.60, 0.12, 0.18, 0.22, 0.10, 0.30, False, None, False, 0, 0, 0, 100, None)


# LAKERS STARTING UNIT
l_doncic = BasketballPlayer("Luka Doncic", "Point Guard", 1, "Los Angeles Lakers", .390, 0.75, 0.60, 0.09, 0.20, 0.18, 0.09, 0.4, False, None, False, 0, 0, 0, 100, ["Luka"])
a_reaves = BasketballPlayer("Austin Reaves", "Shooting Guard", 2, "Los Angeles Lakers", .390, 0.75, 0.60, 0.09, 0.20, 0.18, 0.09, 0.4, False, None, False, 0, 0, 0, 100, ["AR15"])
l_james = BasketballPlayer("LeBron James", "Small Forward", 3, "Los Angeles Lakers", .450, 0.80, 0.70, 0.12, 0.50, 0.50, 0.20, 0.5, False, None, False, 0, 0, 0, 100, ["King James"])
r_hachimura = BasketballPlayer("Rui Hachimura", "Power Forward", 4, "Los Angeles Lakers", .370, 0.35, 0.60, 0.10, 0.22, 0.20, 0.10, 0.3, False, None, False, 0, 0, 0, 100, None)
d_ayton = BasketballPlayer("DeAndre Ayton", "Center", 5, "Los Angeles Lakers", .350, 0.30, 0.72, 0.12, 0.25, 0.28, 0.15, 0.3, False, None, False, 0, 0, 0, 100, None)


# LAKERS BENCH UNIT
g_vincent = BasketballPlayer("Gabe Vincent", "Point Guard", 1, "Los Angeles Lakers", 0.380, 0.80, 0.70, 0.10, 0.25, 0.20, 0.12, 0.35, False, None, False, 0, 0, 0, 100, None)
m_smart = BasketballPlayer("Marcus Smart", "Shooting Guard", 2, "Los Angeles Lakers", .481, 0.25, 0.521, 0.143, 0.25, 0.1, 0.04, 0.2, False, None, False, 0, 0, 0, 100, None)
j_laravia = BasketballPlayer("Jake LaRavia", "Small Forward", 3, "Los Angeles Lakers", 0.400, 0.65, 0.68, 0.12, 0.22, 0.20, 0.11, 0.32, False, None, False, 0, 0, 0, 100, None)
j_vanderbilt = BasketballPlayer("Jarred Vanderbilt", "Power Forward", 4, "Los Angeles Lakers", 0.400, 0.65, 0.68, 0.12, 0.22, 0.20, 0.11, 0.32, False, None, False, 0, 0, 0, 100, ['Vando'])
j_hayes = BasketballPlayer("Jaxson Hayes", "Center", 5, "Los Angeles Lakers", 0.350, 0.50, 0.70, 0.10, 0.25, 0.22, 0.12, 0.30, False, None, False, 0, 0, 0, 100, None)


# CLIPPERS STARTING UNIT
j_harden = BasketballPlayer("James Harden", "Point Guard", 1, "LA Clippers", .400, 0.85, 0.65, 0.15, 0.30, 0.25, 0.12, 0.6, False, None, False, 0, 0, 0, 100, ["Uno"])
b_beal = BasketballPlayer("Bradley Beal", "Shooting Guard", 2, "LA Clippers", .381, 0.25, 0.554, 0.071, 0, 0, 0.086, 0.25, False, None, False, 0, 0, 0, 100, ["the Big Panda"])
k_leonard = BasketballPlayer("Kawhi Leonard", "Small Forward", 3, "LA Clippers", .420, 0.45, 0.64, 0.08, 0.35, 0.45, 0.18, 0.35, False, None, False, 0, 0, 0, 100, ["the Klaw"])
j_collins = BasketballPlayer("John Collins", "Power Forward", 4, "LA Clippers", .380, 0.40, 0.66, 0.10, 0.20, 0.18, 0.12, 0.3, False, None, False, 0, 0, 0, 100, None)
i_zubac = BasketballPlayer("Ivica Zubac", "Center", 5, "LA Clippers", 0.000, 0.20, 0.60, 0.10, 0.18, 0.22, 0.14, 0.25, False, None, False, 0, 0, 0, 100, ["Zu"])


# CLIPPERS BENCH UNIT 
c_paul = BasketballPlayer("Chris Paul", "Point Guard", 1, "LA Clippers", 0.390, 0.65, 0.70, 0.11, 0.25, 0.18, 0.12, 0.35, False, None, False, 0, 0, 0, 100, ["CP3"])
k_dunn = BasketballPlayer("Kris Dunn", "Shooting Guard", 2, "LA Clippers", 0.410, 0.60, 0.68, 0.10, 0.22, 0.18, 0.11, 0.30, False, None, False, 0, 0, 0, 100, ["the Dunngeon"])
n_batum = BasketballPlayer("Nico Batum", "Small Forward", 3, "LA Clippers", 0.400, 0.55, 0.65, 0.10, 0.20, 0.18, 0.10, 0.30, False, None, False, 0, 0, 0, 100, None)
d_jones_jr = BasketballPlayer("Derrick Jones Jr.", "Power Forward", 4, "LA Clippers", 0.350, 0.45, 0.62, 0.10, 0.22, 0.18, 0.12, 0.30, False, None, False, 0, 0, 0, 100, None)
b_lopez = BasketballPlayer("Brook Lopez", "Center", 5, "LA Clippers", 0.320, 0.40, 0.65, 0.10, 0.22, 0.20, 0.14, 0.30, False, None, False, 0, 0, 0, 100, None)


# '13-'14 CLIPPERS STARTING UNIT
ch_paul = BasketballPlayer("Chris Paul", "Point Guard", 1, "'13-'14 LA Clippers", 0.368, 0.90, 0.70, 0.11, 0.25, 0.20, 0.15, 0.50, False, None, False, 0, 0, 0, 100, ["CP3"])
j_redick = BasketballPlayer("JJ Redick", "Shooting Guard", 2, "'13-'14 LA Clippers", 0.395, 0.65, 0.60, 0.10, 0.20, 0.15, 0.10, 0.40, False, None, False, 0, 0, 0, 100, None)
j_dudley = BasketballPlayer("Jared Dudley", "Small Forward", 3, "'13-'14 LA Clippers", 0.360, 0.60, 0.55, 0.10, 0.20, 0.15, 0.12, 0.35, False, None, False, 0, 0, 0, 100, None)
b_griffin = BasketballPlayer("Blake Griffin", "Power Forward", 4, "'13-'14 LA Clippers", 0.276, 0.55, 0.75, 0.12, 0.30, 0.25, 0.10, 0.40, False, None, False, 0, 0, 0, 100, None)
d_jordan_lac = BasketballPlayer("DeAndre Jordan", "Center", 5, "'13-'14 LA Clippers", 0.000, 0.40, 0.80, 0.15, 0.35, 0.45, 0.15, 0.30, False, None, False, 0, 0, 0, 100, ["DJ"])


# '13-'14 CLIPPERS BENCH UNIT
d_collison = BasketballPlayer("Darren Collison", "Point Guard", 1, "'13-'14 LA Clippers", 0.375, 0.75, 0.65, 0.10, 0.22, 0.18, 0.12, 0.40, False, None, False, 0, 0, 0, 100, None)
j_crawford = BasketballPlayer("Jamal Crawford", "Shooting Guard", 2, "'13-'14 LA Clippers", 0.360, 0.65, 0.70, 0.12, 0.20, 0.15, 0.10, 0.35, False, None, False, 0, 0, 0, 100, ["J-Crossover"])
m_barnes = BasketballPlayer("Matt Barnes", "Small Forward", 3, "'13-'14 LA Clippers", 0.340, 0.55, 0.60, 0.11, 0.25, 0.20, 0.12, 0.35, False, None, False, 0, 0, 0, 100, None)
h_turkoglu = BasketballPlayer("Hedo Turkoglu", "Power Forward", 4, "'13-'14 LA Clippers", 0.380, 0.60, 0.55, 0.10, 0.20, 0.15, 0.10, 0.30, False, None, False, 0, 0, 0, 100, None)
r_hollins = BasketballPlayer("Ryan Hollins", "Center", 5, "'13-'14 LA Clippers", 0.000, 0.40, 0.65, 0.12, 0.18, 0.20, 0.12, 0.25, False, None, False, 0, 0, 0, 100, None)


# OKLAHOMA CITY THUNDER STARTING UNIT
s_gilgeous_alexander = BasketballPlayer("Shai Gilgeous-Alexander", "Point Guard", 1, "Oklahoma City Thunder", 0.375, 0.85, 0.80, 0.12, 0.28, 0.25, 0.15, 0.45, False, None, False, 0, 0, 0, 100, ["SGA"])
c_wallace = BasketballPlayer("Cason Wallace", "Shooting Guard", 2, "Oklahoma City Thunder", 0.350, 0.70, 0.65, 0.10, 0.22, 0.18, 0.12, 0.40, False, None, False, 0, 0, 0, 100, None)
l_dort = BasketballPlayer("Luguentz Dort", "Small Forward", 3, "Oklahoma City Thunder", 0.330, 0.60, 0.65, 0.12, 0.25, 0.22, 0.14, 0.35, False, None, False, 0, 0, 0, 100, ["the Dorture Chamber", "Dortress"])
j_williams = BasketballPlayer("Jalen Williams", "Power Forward", 4, "Oklahoma City Thunder", 0.400, 0.75, 0.70, 0.10, 0.28, 0.22, 0.14, 0.40, False, None, False, 0, 0, 0, 100, ["J-Dub"])
c_holmgren = BasketballPlayer("Chet Holmgren", "Center", 5, "Oklahoma City Thunder", 0.380, 0.60, 0.70, 0.11, 0.30, 0.25, 0.15, 0.40, False, None, False, 0, 0, 0, 100, None)


# OKLAHOMA CITY THUNDER BENCH UNIT
a_mitchell = BasketballPlayer("Ajay Mitchell", "Point Guard", 1, "Oklahoma City Thunder", 0.330, 0.65, 0.60, 0.11, 0.20, 0.15, 0.10, 0.35, False, None, False, 0, 0, 0, 100, None)
i_joe = BasketballPlayer("Isaiah Joe", "Shooting Guard", 2, "Oklahoma City Thunder", 0.410, 0.70, 0.65, 0.10, 0.22, 0.18, 0.12, 0.40, False, None, False, 0, 0, 0, 100, None)
a_caruso = BasketballPlayer("Alex Caruso", "Small Forward", 3, "Oklahoma City Thunder", 0.365, 0.75, 0.65, 0.10, 0.25, 0.22, 0.15, 0.40, False, None, False, 0, 0, 0, 100, None)
aa_wiggins = BasketballPlayer("Aaron Wiggins", "Power Forward", 4, "Oklahoma City Thunder", 0.340, 0.65, 0.62, 0.12, 0.22, 0.20, 0.12, 0.35, False, None, False, 0, 0, 0, 100, None)
i_hartenstein = BasketballPlayer("Isaiah Hartenstein", "Center", 5, "Oklahoma City Thunder", 0.310, 0.55, 0.65, 0.12, 0.20, 0.22, 0.14, 0.35, False, None, False, 0, 0, 0, 100, ["iHart"])


# MEMPHIS GRIZZLIES STARTING UNIT
j_morant = BasketballPlayer("Ja Morant", "Point Guard", 1, "Memphis Grizzlies", 0.320, 0.85, 0.80, 0.13, 0.25, 0.20, 0.12, 0.45, False, None, False, 0, 0, 0, 100, None)
k_caldwell_pope = BasketballPlayer("Kentavious Caldwell-Pope", "Shooting Guard", 2, "Orlando Magic", 0.400, 0.60, 0.65, 0.10, 0.22, 0.20, 0.12, 0.35, False, None, False, 0, 0, 0, 100, ["KCP"])
j_jackson_jr = BasketballPlayer("Jaren Jackson Jr.", "Small Forward", 3, "Memphis Grizzlies", 0.350, 0.65, 0.65, 0.12, 0.28, 0.25, 0.14, 0.35, False, None, False, 0, 0, 0, 100, ["JJJ"])
b_clarke = BasketballPlayer("Brandon Clarke", "Power Forward", 4, "Memphis Grizzlies", 0.200, 0.55, 0.70, 0.11, 0.22, 0.20, 0.12, 0.30, False, None, False, 0, 0, 0, 100, None)
z_edey = BasketballPlayer("Zach Edey", "Center", 5, "Memphis Grizzlies", 0.000, 0.50, 0.75, 0.12, 0.30, 0.28, 0.15, 0.35, False, None, False, 0, 0, 0, 100, None)


# MEMPHIS GRIZZLIES BENCH UNIT
t_jerome = BasketballPlayer("Ty Jerome", "Point Guard", 1, "Memphis Grizzlies", 0.320, 0.70, 0.65, 0.12, 0.25, 0.22, 0.14, 0.40, False, None, False, 0, 0, 0, 100, None)
l_kennard = BasketballPlayer("Luke Kennard", "Shooting Guard", 2, "Memphis Grizzlies", 0.420, 0.65, 0.60, 0.10, 0.20, 0.15, 0.10, 0.35, False, None, False, 0, 0, 0, 100, None)
s_aldama = BasketballPlayer("Santi Aldama", "Small Forward", 3, "Memphis Grizzlies", 0.350, 0.60, 0.65, 0.11, 0.22, 0.20, 0.12, 0.30, False, None, False, 0, 0, 0, 100, None)
d_roddy = BasketballPlayer("David Roddy", "Power Forward", 4, "Memphis Grizzlies", 0.300, 0.55, 0.60, 0.10, 0.22, 0.18, 0.11, 0.30, False, None, False, 0, 0, 0, 100, None)
j_huff = BasketballPlayer("Jay Huff", "Center", 5, "Memphis Grizzlies", 0.300, 0.55, 0.65, 0.12, 0.22, 0.20, 0.14, 0.30, False, None, False, 0, 0, 0, 100, None)


# HOUSTON ROCKETS STARTING UNIT 
f_vanvleet = BasketballPlayer("Fred VanVleet", "Point Guard", 1, "Houston Rockets", 0.370, 0.85, 0.70, 0.10, 0.25, 0.22, 0.14, 0.45, False, None, False, 0, 0, 0, 100, None)
a_thompson = BasketballPlayer("Amen Thompson", "Shooting Guard", 2, "Houston Rockets", 0.340, 0.70, 0.65, 0.12, 0.22, 0.18, 0.12, 0.40, False, None, False, 0, 0, 0, 100, None)
k_durant = BasketballPlayer("Kevin Durant", "Small Forward", 3, "Houston Rockets", 0.320, 0.60, 0.65, 0.12, 0.25, 0.22, 0.13, 0.35, False, None, False, 0, 0, 0, 100, ["Slim Reaper", "KD", "Durantula"])
j_smith_jr = BasketballPlayer("Jabari Smith Jr.", "Power Forward", 4, "Houston Rockets", 0.310, 0.55, 0.70, 0.11, 0.28, 0.25, 0.14, 0.40, False, None, False, 0, 0, 0, 100, None)
a_sengun = BasketballPlayer("Alperen Sengun", "Center", 5, "Houston Rockets", 0.300, 0.60, 0.75, 0.13, 0.30, 0.28, 0.15, 0.40, False, None, False, 0, 0, 0, 100, None)


# HOUSTON ROCKETS BENCH UNIT
a_holiday = BasketballPlayer("Aaron Holiday", "Point Guard", 1, "Houston Rockets", 0.360, 0.65, 0.60, 0.11, 0.20, 0.18, 0.12, 0.35, False, None, False, 0, 0, 0, 100, None)
c_whitmore = BasketballPlayer("Cam Whitmore", "Shooting Guard", 2, "Houston Rockets", 0.340, 0.65, 0.65, 0.12, 0.22, 0.18, 0.11, 0.35, False, None, False, 0, 0, 0, 100, None)
d_finney_smith = BasketballPlayer("Dorian Finney-Smith", "Small Forward", 3, "Houston Rockets", 0.400, 0.65, 0.68, 0.12, 0.22, 0.20, 0.11, 0.32, False, None, False, 0, 0, 0, 100, ['DFS', 'Dodo'])
t_eason = BasketballPlayer("Tari Eason", "Power Forward", 4, "Houston Rockets", 0.300, 0.55, 0.65, 0.12, 0.28, 0.22, 0.14, 0.35, False, None, False, 0, 0, 0, 100, None)
s_adams = BasketballPlayer("Steven Adams", "Center", 5, "Houston Rockets", 0.000, 0.40, 0.70, 0.13, 0.25, 0.28, 0.14, 0.30, False, None, False, 0, 0, 0, 100, None)


# WASHINGTON WIZARDS STARTING UNIT
j_poole = BasketballPlayer("Jordan Poole", "Point Guard", 1, "Washington Wizards", 0.330, 0.75, 0.70, 0.12, 0.25, 0.20, 0.12, 0.40, False, None, False, 0, 0, 0, 100, None)
b_carrington = BasketballPlayer("Bub Carrington", "Shooting Guard", 2, "Washington Wizards", 0.310, 0.60, 0.65, 0.11, 0.22, 0.18, 0.12, 0.35, False, None, False, 0, 0, 0, 100, ["Bub"])
b_coulibaly = BasketballPlayer("Bilal Coulibaly", "Small Forward", 3, "Washington Wizards", 0.340, 0.65, 0.65, 0.12, 0.25, 0.22, 0.14, 0.35, False, None, False, 0, 0, 0, 100, None)
k_kuzma = BasketballPlayer("Kyle Kuzma", "Power Forward", 4, "Washington Wizards", 0.320, 0.60, 0.70, 0.12, 0.28, 0.25, 0.14, 0.40, False, None, False, 0, 0, 0, 100, ["Kuz"])
a_sarr = BasketballPlayer("Alex Sarr", "Center", 5, "Washington Wizards", 0.300, 0.55, 0.70, 0.13, 0.30, 0.28, 0.15, 0.40, False, None, False, 0, 0, 0, 100, None)

# WASHINGTON WIZARDS BENCH UNIT
m_brogdon = BasketballPlayer("Malcolm Brogdon", "Point Guard", 1, "Washington Wizards", 0.380, 0.80, 0.70, 0.11, 0.25, 0.20, 0.12, 0.40, False, None, False, 0, 0, 0, 100, None)
c_kispert = BasketballPlayer("Corey Kispert", "Shooting Guard", 2, "Washington Wizards", 0.420, 0.65, 0.65, 0.10, 0.22, 0.18, 0.11, 0.40, False, None, False, 0, 0, 0, 100, None)
k_george = BasketballPlayer("Kyshawn George", "Small Forward", 3, "Washington Wizards", 0.340, 0.60, 0.65, 0.12, 0.25, 0.20, 0.12, 0.35, False, None, False, 0, 0, 0, 100, None)
j_champagnie = BasketballPlayer("Justin Champagnie", "Power Forward", 4, "Washington Wizards", 0.310, 0.55, 0.65, 0.12, 0.28, 0.22, 0.14, 0.35, False, None, False, 0, 0, 0, 100, None)
j_valanciunas = BasketballPlayer("Jonas Valanciunas", "Center", 5, "Washington Wizards", 0.300, 0.60, 0.75, 0.13, 0.30, 0.28, 0.15, 0.40, False, None, False, 0, 0, 0, 100, None)

# INDIANA PACERS STARTING UNIT
t_haliburton = BasketballPlayer("Tyrese Haliburton", "Point Guard", 1, "Indiana Pacers", 0.400, 0.85, 0.70, 0.12, 0.30, 0.25, 0.14, 0.45, False, None, False, 0, 0, 0, 100, None)
a_nembhard = BasketballPlayer("Andrew Nembhard", "Shooting Guard", 2, "Indiana Pacers", 0.350, 0.75, 0.65, 0.11, 0.25, 0.20, 0.12, 0.40, False, None, False, 0, 0, 0, 100, None)
a_nesmith = BasketballPlayer("Aaron Nesmith", "Small Forward", 3, "Indiana Pacers", 0.350, 0.65, 0.68, 0.12, 0.28, 0.22, 0.13, 0.35, False, None, False, 0, 0, 0, 100, None)
p_siakam = BasketballPlayer("Pascal Siakam", "Power Forward", 4, "Indiana Pacers", 0.360, 0.65, 0.70, 0.12, 0.30, 0.25, 0.14, 0.45, False, None, False, 0, 0, 0, 100, ["Spicy P"])
m_turner = BasketballPlayer("Myles Turner", "Center", 5, "Indiana Pacers", 0.320, 0.60, 0.75, 0.13, 0.28, 0.28, 0.15, 0.50, False, None, False, 0, 0, 0, 100, None)

# INDIANA PACERS BENCH UNIT
t_mcconnell = BasketballPlayer("T.J. McConnell", "Point Guard", 1, "Indiana Pacers", 0.360, 0.75, 0.70, 0.11, 0.25, 0.22, 0.12, 0.40, False, None, False, 0, 0, 0, 100, None)
b_sheppard = BasketballPlayer("Ben Sheppard", "Shooting Guard", 2, "Indiana Pacers", 0.340, 0.65, 0.65, 0.12, 0.25, 0.20, 0.12, 0.35, False, None, False, 0, 0, 0, 100, None)
b_mathurin = BasketballPlayer("Bennedict Mathurin", "Small Forward", 3, "Indiana Pacers", 0.370, 0.70, 0.68, 0.12, 0.28, 0.22, 0.13, 0.40, False, None, False, 0, 0, 0, 100, None)
o_toppin = BasketballPlayer("Obi Toppin", "Power Forward", 4, "Indiana Pacers", 0.360, 0.65, 0.70, 0.12, 0.28, 0.25, 0.14, 0.40, False, None, False, 0, 0, 0, 100, None)
t_bryant = BasketballPlayer("Thomas Bryant", "Center", 5, "Indiana Pacers", 0.350, 0.60, 0.70, 0.12, 0.25, 0.22, 0.14, 0.35, False, None, False, 0, 0, 0, 100, None)

# CLEVELAND CAVALIERS STARTING UNIT
d_garland = BasketballPlayer("Darius Garland", "Point Guard", 1, "Cleveland Cavaliers", 0.418, 0.85, 0.70, 0.12, 0.30, 0.25, 0.14, 0.45, False, None, False, 0, 0, 0, 100, ["Boog"])
d_mitchell = BasketballPlayer("Donovan Mitchell", "Shooting Guard", 2, "Cleveland Cavaliers", 0.404, 0.80, 0.70, 0.12, 0.28, 0.22, 0.13, 0.40, False, None, False, 0, 0, 0, 100, ["Spida"])
m_strus = BasketballPlayer("Max Strus", "Small Forward", 3, "Cleveland Cavaliers", 0.000, 0.65, 0.70, 0.12, 0.28, 0.22, 0.14, 0.35, False, None, False, 0, 0, 0, 100, None)
e_mobley = BasketballPlayer("Evan Mobley", "Power Forward", 4, "Cleveland Cavaliers", 0.411, 0.70, 0.75, 0.12, 0.30, 0.25, 0.14, 0.45, False, None, False, 0, 0, 0, 100, None)
j_allen = BasketballPlayer("Jarrett Allen", "Center", 5, "Cleveland Cavaliers", 0.000, 0.60, 0.73, 0.13, 0.28, 0.28, 0.15, 0.50, False, None, False, 0, 0, 0, 100, None)

# CLEVELAND CAVALIERS BENCH UNIT
l_ball = BasketballPlayer("Lonzo Ball", "Point Guard", 1, "Cleveland Cavaliers", 0.447, 0.75, 0.65, 0.11, 0.25, 0.20, 0.12, 0.35, False, None, False, 0, 0, 0, 100, ["Zo"])
s_merrill = BasketballPlayer("Sam Merrill", "Shooting Guard", 2, "Cleveland Cavaliers", 0.333, 0.65, 0.65, 0.10, 0.25, 0.20, 0.12, 0.35, False, None, False, 0, 0, 0, 100, None)
d_hunter = BasketballPlayer("De'Andre Hunter", "Small Forward", 3, "Cleveland Cavaliers", 0.350, 0.65, 0.68, 0.12, 0.28, 0.22, 0.13, 0.35, False, None, False, 0, 0, 0, 100, None)
d_wade = BasketballPlayer("Dean Wade", "Power Forward", 4, "Cleveland Cavaliers", 0.305, 0.60, 0.40, 0.12, 0.28, 0.22, 0.14, 0.35, False, None, False, 0, 0, 0, 100, None)
g_niang = BasketballPlayer("Georges Niang", "Center", 5, "Cleveland Cavaliers", 0.363, 0.65, 0.78, 0.12, 0.28, 0.22, 0.14, 0.35, False, None, False, 0, 0, 0, 100, None)

# TORONTO RAPTORS STARTING UNIT
i_quickley = BasketballPlayer("Immanuel Quickley", "Point Guard", 1, "Toronto Raptors", 0.370, 0.80, 0.70, 0.11, 0.25, 0.22, 0.12, 0.40, False, None, False, 0, 0, 0, 100, ["IQ"])
g_dick = BasketballPlayer("Gradey Dick", "Shooting Guard", 2, "Toronto Raptors", 0.350, 0.70, 0.65, 0.12, 0.22, 0.18, 0.11, 0.35, False, None, False, 0, 0, 0, 100, None)
r_barrett = BasketballPlayer("RJ Barrett", "Small Forward", 3, "Toronto Raptors", 0.340, 0.65, 0.68, 0.12, 0.25, 0.22, 0.13, 0.35, False, None, False, 0, 0, 0, 100, None)
s_barnes = BasketballPlayer("Scottie Barnes", "Power Forward", 4, "Toronto Raptors", 0.360, 0.75, 0.72, 0.12, 0.30, 0.25, 0.14, 0.40, False, None, False, 0, 0, 0, 100, None)
j_poeltl = BasketballPlayer("Jakob Poeltl", "Center", 5, "Toronto Raptors", 0.000, 0.60, 0.75, 0.13, 0.30, 0.28, 0.15, 0.40, False, None, False, 0, 0, 0, 100, None)

# TORONTO RAPTORS BENCH UNIT
j_shead = BasketballPlayer("Jamal Shead", "Point Guard", 1, "Toronto Raptors", 0.340, 0.70, 0.68, 0.11, 0.25, 0.22, 0.12, 0.35, False, None, False, 0, 0, 0, 100, None)
j_walter = BasketballPlayer("Ja'Kobe Walter", "Shooting Guard", 2, "Toronto Raptors", 0.330, 0.65, 0.65, 0.12, 0.22, 0.18, 0.11, 0.35, False, None, False, 0, 0, 0, 100, None)
o_agbaji = BasketballPlayer("Ochai Agbaji", "Small Forward", 3, "Toronto Raptors", 0.350, 0.65, 0.68, 0.12, 0.25, 0.22, 0.13, 0.35, False, None, False, 0, 0, 0, 100, None)
j_mogbo = BasketballPlayer("Jonathan Mogbo", "Power Forward", 4, "Toronto Raptors", 0.320, 0.60, 0.70, 0.12, 0.28, 0.25, 0.14, 0.35, False, None, False, 0, 0, 0, 100, None)
o_robinson = BasketballPlayer("Orlando Robinson", "Center", 5, "Toronto Raptors", 0.310, 0.55, 0.72, 0.13, 0.28, 0.28, 0.15, 0.35, False, None, False, 0, 0, 0, 100, None)

# UTAH JAZZ STARTING UNIT
i_collier = BasketballPlayer("Isaiah Collier", "Point Guard", 1, "Utah Jazz", 0.249, 0.63, 0.42, 0.12, 0.25, 0.22, 0.12, 0.35, False, None, False, 0, 0, 0, 100, None)
c_sexton = BasketballPlayer("Collin Sexton", "Shooting Guard", 2, "Utah Jazz", 0.406, 0.42, 0.48, 0.12, 0.28, 0.22, 0.12, 0.35, False, None, False, 0, 0, 0, 100, None)
l_markkanen = BasketballPlayer("Lauri Markkanen", "Small Forward", 3, "Utah Jazz", 0.346, 0.35, 0.42, 0.12, 0.28, 0.22, 0.12, 0.35, False, None, False, 0, 0, 0, 100, ["the Finnisher"])
t_hendricks = BasketballPlayer("Taylor Hendricks", "Power Forward", 4, "Utah Jazz", 0.399, 0.20, 0.52, 0.12, 0.28, 0.22, 0.12, 0.35, False, None, False, 0, 0, 0 , 100, None)
w_kessler = BasketballPlayer("Walker Kessler", "Center", 5, "Utah Jazz", 0.176, 0.17, 0.66, 0.12, 0.28, 0.22, 0.12, 0.35, False, None, False, 0, 0, 0, 100, None)

# UTAH JAZZ BENCH UNIT
k_george = BasketballPlayer("Keyonte George", "Point Guard", 1, "Utah Jazz", 0.350, 0.70, 0.68, 0.12, 0.28, 0.22, 0.13, 0.40, False, None, False, 0, 0, 0, 100, None)
j_springer = BasketballPlayer("Jaden Springer", "Shooting Guard", 2, "Utah Jazz", 0.330, 0.65, 0.68, 0.12, 0.28, 0.22, 0.13, 0.40, False, None, False, 0, 0, 0, 100, None)
c_williams = BasketballPlayer("Cody Williams", "Small Forward", 3, "Utah Jazz", 0.259, 0.32, 0.65, 0.19, 0.25, 0.22, 0.12, 0.35, False, None, False, 0, 0, 0, 100, None)
t_brown = BasketballPlayer("Trevor Brown", "Power Forward", 4, "Utah Jazz", 0.310, 0.55, 0.65, 0.12, 0.24, 0.22, 0.11, 0.32, False, None, False, 0, 0, 0, 100, None)
k_filipowski = BasketballPlayer("Kyle Filipowski", "Center", 5, "Utah Jazz", 0.350, 0.65, 0.65, 0.14, 0.28, 0.22, 0.13, 0.35, False, None, False, 0, 0, 0, 100, None)


clippers_list = [j_harden, b_beal, k_leonard, j_collins, i_zubac]
clippers_bench_list = [c_paul, k_dunn, n_batum, d_jones_jr, b_lopez]

lakers_list = [l_doncic, a_reaves, l_james, r_hachimura, d_ayton]
lakers_bench_list = [g_vincent, m_smart, j_laravia, j_vanderbilt, j_hayes]

celtics_list = [j_holiday, d_white, j_brown, j_tatum, k_porzingis]
celtics_bench_list = [p_pritchard, b_scheierman, s_hauser, a_horford, l_kornet]

knicks_list = [j_brunson, m_bridges, o_anunoby, p_achiuwa, k_towns]
knicks_bench_list = [c_payne, j_clarkson, j_hart, j_sims, m_robinson]

suns_list = [d_booker, j_green, d_brooks, n_hayes_davis, j_nurkic]
suns_bench_list = [m_morris, g_allen, r_oneale, r_dunn, m_plumlee]

sixers_list = [t_maxey, k_oubre, p_george, g_yabusele, j_embiid]
sixers_bench_list = [r_jackson, k_lowry, c_martin, p_nance, a_drummond]

warriors_list = [s_curry, b_hield, an_wiggins, j_kuminga, d_green]
warriors_bench_list = [b_podziemski, m_moody, g_payton_ii, k_anderson, k_looney]

magic_list = [j_suggs, d_bane, f_wagner, p_banchero, w_carter_jr]
magic_bench_list = [a_black, c_anthony, g_harris, j_isaac, g_bitadze]

mavericks_list = [d_russell, k_irving, k_thompson, a_davis, d_lively]
mavericks_bench_list = [s_dinwiddie, m_christie, d_exum, p_washington, d_gafford]

pelicans_list = [d_murray, c_mccollum, b_ingram, z_williamson, y_missi]
pelicans_bench_list = [j_hawkins, t_murphy_iii, b_boston_jr, jav_green, j_robinson_earl]

nuggets_list = [j_murray, c_braun, m_porter_jr, a_gordon, n_jokic]
nuggets_bench_list = [r_westbrook, j_strawther, h_tyson , p_watson, d_jordan_den]

retro_clippers_list = [ch_paul, j_redick, j_dudley, b_griffin, d_jordan_lac]
retro_clippers_bench_list = [d_collison, j_crawford, m_barnes, h_turkoglu, r_hollins]

thunder_list = [s_gilgeous_alexander, c_wallace, l_dort, j_williams, c_holmgren]
thunder_bench_list = [a_mitchell, i_joe, a_caruso, aa_wiggins, i_hartenstein]

grizzlies_list = [j_morant, k_caldwell_pope, j_jackson_jr, b_clarke, z_edey]
grizzlies_bench_list = [t_jerome, l_kennard, s_aldama, d_roddy, j_huff]

rockets_list = [f_vanvleet, a_thompson, k_durant, j_smith_jr, a_sengun]
rockets_bench_list = [a_holiday, c_whitmore, d_finney_smith, t_eason, s_adams]


wizards_list = [j_poole, b_carrington, b_coulibaly, k_kuzma, a_sarr]
wizards_bench_list = [m_brogdon, c_kispert, k_george, j_champagnie, j_valanciunas]

pacers_list = [t_haliburton, a_nembhard, a_nesmith, p_siakam, m_turner]
pacers_bench_list = [t_mcconnell, b_sheppard, b_mathurin, o_toppin, t_bryant]

cavaliers_list = [d_garland, d_mitchell, m_strus, e_mobley, j_allen]
cavaliers_bench_list = [l_ball, s_merrill, d_hunter, d_wade, g_niang]

raptors_list = [i_quickley, g_dick, r_barrett, s_barnes, j_poeltl]
raptors_bench_list = [j_shead, j_walter, o_agbaji, j_mogbo, o_robinson]

jazz_list = [i_collier, c_sexton, l_markkanen, t_hendricks, w_kessler]
jazz_bench_list = [k_george, j_springer, c_williams, t_brown, k_filipowski]

teams_names = ['LA Clippers', 'Los Angeles Lakers', 'Boston Celtics', 'New York Knicks', 'Phoenix Suns', 'Philadelphia 76ers', 'Golden State Warriors', 'Orlando Magic', 'Dallas Mavericks', 'Denver Nuggets', 'New Orleans Pelicans', "'13-'14 LA Clippers", "Oklahoma City Thunder", "Memphis Grizzlies", "Houston Rockets", "Washington Wizards", "Indiana Pacers", "Cleveland Cavaliers", "Toronto Raptors", "Utah Jazz"]

clippers_team = Team("LA Clippers", clippers_list, clippers_bench_list, clippers_logo, 'Tyronn Lue')
lakers_team = Team("Los Angeles Lakers", lakers_list, lakers_bench_list, lakers_logo, 'JJ Redick')
celtics_team = Team("Boston Celtics", celtics_list, celtics_bench_list, celtics_logo, 'Joe Mazzulla')
knicks_team = Team("New York Knicks", knicks_list, knicks_bench_list, knicks_logo, 'Tom Thibodeau')
suns_team = Team("Phoenix Suns", suns_list, suns_bench_list, suns_logo, 'Mike Budenholzer')
sixers_team = Team("Philadelphia 76ers", sixers_list, sixers_bench_list, sixers_logo, 'Nick Nurse')
warriors_team = Team("Golden State Warriors", warriors_list, warriors_bench_list, warriors_logo, 'Steve Kerr')
magic_team = Team("Orlando Magic", magic_list, magic_bench_list, magic_logo, 'Jamahl Mosley')
mavericks_team = Team("Dallas Mavericks", mavericks_list, mavericks_bench_list, mavericks_logo, 'Jason Kidd')
pelicans_team = Team("New Orleans Pelicans", pelicans_list, pelicans_bench_list, pelicans_logo, 'Willie Green')
nuggets_team = Team("Denver Nuggets", nuggets_list, nuggets_bench_list, nuggets_logo, 'Mike Malone')
retro_clippers_team = Team("'13-'14 LA Clippers", retro_clippers_list, retro_clippers_bench_list, retro_clippers_logo, 'Doc Rivers')
thunder_team = Team("Oklahoma City Thunder", thunder_list, thunder_bench_list, thunder_logo, 'Mark Daigneault')
grizzlies_team = Team("Memphis Grizzlies", grizzlies_list, grizzlies_bench_list, grizzlies_logo, 'Taylor Jenkins')
rockets_team = Team("Houston Rockets", rockets_list, rockets_bench_list, rockets_logo, 'Ime Udoka')
wizards_team = Team("Washington Wizards", wizards_list, wizards_bench_list, wizards_logo, 'Brian Keefe')
pacers_team = Team("Indiana Pacers", pacers_list, pacers_bench_list, pacers_logo, 'Rick Carlisle')
cavaliers_team = Team("Cleveland Cavaliers", cavaliers_list, cavaliers_bench_list, cavaliers_logo, 'Kenny Atkinson')
raptors_team = Team("Toronto Raptors", raptors_list, raptors_bench_list, raptors_logo, 'Darko Rajakovic')
jazz_team = Team("Utah Jazz", jazz_list, jazz_bench_list, jazz_logo, 'Will Hardy')

list_of_team_objects = [clippers_team, lakers_team, celtics_team, knicks_team, suns_team, sixers_team, warriors_team, magic_team, mavericks_team, pelicans_team, nuggets_team, retro_clippers_team, thunder_team, grizzlies_team, rockets_team, wizards_team, pacers_team, cavaliers_team, raptors_team, jazz_team]







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
        user_team_object = clippers_team
    case 2:
        user_team_object = lakers_team
    case 3:
        user_team_object = celtics_team
    case 4:
        user_team_object = knicks_team
    case 5:
        user_team_object = suns_team
    case 6:
        user_team_object = sixers_team
    case 7:
        user_team_object = warriors_team
    case 8:
        user_team_object = magic_team
    case 9:
        user_team_object = mavericks_team
    case 10:
        user_team_object = nuggets_team
    case 11:
        user_team_object = pelicans_team
    case 12:
        user_team_object = retro_clippers_team
    case 13:
        user_team_object = thunder_team
    case 14:
        user_team_object = grizzlies_team
    case 15:
        user_team_object = rockets_team
    case 16:
        user_team_object = wizards_team
    case 17:
        user_team_object = pacers_team
    case 18:
        user_team_object = cavaliers_team
    case 19:
        user_team_object = raptors_team
    case 20:
        user_team_object = jazz_team

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

if opposing_team == 'LA Clippers':
    opposing_team_object = clippers_team
elif opposing_team == 'Los Angeles Lakers':
    opposing_team_object = lakers_team
elif opposing_team == 'Boston Celtics':
    opposing_team_object = celtics_team
elif opposing_team == 'New York Knicks':
    opposing_team_object = knicks_team
elif opposing_team == 'Phoenix Suns':
    opposing_team_object = suns_team
elif opposing_team == 'Philadelphia 76ers':
    opposing_team_object = sixers_team
elif opposing_team == 'Golden State Warriors':
    opposing_team_object = warriors_team
elif opposing_team == 'Orlando Magic':
    opposing_team_object = magic_team
elif opposing_team == 'Dallas Mavericks':
    opposing_team_object = mavericks_team
elif opposing_team == 'Denver Nuggets':
    opposing_team_object = nuggets_team
elif opposing_team == 'New Orleans Pelicans':
    opposing_team_object = pelicans_team
elif opposing_team == "'13-'14 LA Clippers":
    opposing_team_object = retro_clippers_team
elif opposing_team == "Oklahoma City Thunder":
    opposing_team_object = thunder_team
elif opposing_team == "Memphis Grizzlies":
    opposing_team_object = grizzlies_team
elif opposing_team == "Houston Rockets":
    opposing_team_object = rockets_team
elif opposing_team == "Washington Wizards":
    opposing_team_object = wizards_team
elif opposing_team == "Indiana Pacers":
    opposing_team_object = pacers_team
elif opposing_team == "Cleveland Cavaliers":
    opposing_team_object = cavaliers_team
elif opposing_team == "Toronto Raptors":
    opposing_team_object = raptors_team
elif opposing_team == "Utah Jazz":
    opposing_team_object = jazz_team

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
    defender = KermLib.object_matcher(player, opposing_team_list, 'positionnumber')
    player.defender = defender
    defender.defender = player

time.sleep(2)

print('\n' + '\n')

if auto_or_manual in ['m', "M"]:
    for player in user_team_list:
        if player.positionnumber == player_decision:
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
            if last_event is not 'pass':
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
                        if player_decision not in ['1', '2', '3', '4', '5'] or player_decision == str(current_player.positionnumber):
                            print('Decision not recognized. Please try again')
                            continue
                        else:
                            player_decision = int(player_decision)
                            break



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

