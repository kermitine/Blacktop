import random
import time
from KermLib.KermLib import *
from basketball_ascii import *

version = '2024.12.1.1700.stable'

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
        if 81 > modified_probability >= 33.3:
            return 'pass'
        elif 150 >= modified_probability >= 81:
            return '3pt'
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
            
            # RE-INITIALIZE DEFENDERS
            for player in opposing_team_list:
                defender = KermLib.object_matcher(player, user_team_list, 'positionnumber')
                player.defender = defender
                defender.defender = player

        #update list
        combined_list = user_team_list + opposing_team_list
        print('\n')
        return combined_list
        


# PELICANS STARTING UNIT
d_murray = BasketballPlayer("Dejounte Murray", "Point Guard", 1, "New Orleans Pelicans", .450, 0.80, 0.72, 0.12, 0.30, 0.25, 0.15, 0.40, False, None, False, 0, 0, 0, 100)
c_mccollum = BasketballPlayer("CJ McCollum", "Shooting Guard", 2, "New Orleans Pelicans", .400, 0.75, 0.68, 0.10, 0.30, 0.20, 0.12, 0.35, False, None, False, 0, 0, 0, 100)
b_ingram = BasketballPlayer("Brandon Ingram", "Small Forward", 3, "New Orleans Pelicans", .380, 0.65, 0.70, 0.11, 0.28, 0.25, 0.12, 0.40, False, None, False, 0, 0, 0, 100)
z_williamson = BasketballPlayer("Zion Williamson", "Power Forward", 4, "New Orleans Pelicans", .370, 0.40, 0.75, 0.10, 0.35, 0.30, 0.15, 0.30, False, None, False, 0, 0, 0, 100)
d_theis = BasketballPlayer("Daniel Theis", "Center", 5, "New Orleans Pelicans", .320, 0.50, 0.60, 0.10, 0.25, 0.20, 0.12, 0.30, False, None, False, 0, 0, 0, 100)


# NUGGETS STARTING UNIT
j_murray = BasketballPlayer("Jamal Murray", "Point Guard", 1, "Denver Nuggets", .400, 0.85, 0.70, 0.12, 0.28, 0.22, 0.12, 0.40, False, None, False, 0, 0, 0, 100)
c_braun = BasketballPlayer("Christian Braun", "Shooting Guard", 2, "Denver Nuggets", .370, 0.50, 0.65, 0.11, 0.22, 0.20, 0.10, 0.30, False, None, False, 0, 0, 0, 100)
m_porter_jr = BasketballPlayer("Michael Porter-Jr", "Small Forward", 3, "Denver Nuggets", .430, 0.60, 0.65, 0.10, 0.25, 0.22, 0.10, 0.35, False, None, False, 0, 0, 0, 100)
a_gordon = BasketballPlayer("Aaron Gordon", "Power Forward", 4, "Denver Nuggets", .350, 0.50, 0.70, 0.12, 0.30, 0.25, 0.15, 0.30, False, None, False, 0, 0, 0, 100)
n_jokic = BasketballPlayer("Nikola Jokic", "Center", 5, "Denver Nuggets", .500, 0.90, 0.75, 0.12, 0.40, 0.30, 0.15, 0.50, False, None, False, 0, 0, 0, 100)


# MAVERICKS STARTING UNIT
l_doncic = BasketballPlayer("Luka Doncic", "Point Guard", 1, "Dallas Mavericks", .382, 0.87, 0.72, 0.15, 0.32, 0.28, 0.14, 0.50, False, None, False, 0, 0, 0, 100)
k_irving = BasketballPlayer("Kyrie Irving", "Shooting Guard", 2, "Dallas Mavericks", .395, 0.80, 0.70, 0.12, 0.28, 0.22, 0.12, 0.45, False, None, False, 0, 0, 0, 100)
k_thompson = BasketballPlayer("Klay Thompson", "Small Forward", 3, "Dallas Mavericks", .413, 0.65, 0.60, 0.10, 0.25, 0.20, 0.10, 0.40, False, None, False, 0, 0, 0, 100)
p_washington = BasketballPlayer("P.J. Washington", "Power Forward", 4, "Dallas Mavericks", .370, 0.60, 0.65, 0.11, 0.22, 0.20, 0.11, 0.35, False, None, False, 0, 0, 0, 100)
d_lively = BasketballPlayer("Dereck Lively-II", "Center", 5, "Dallas Mavericks", 0.330, 0.40, 0.60, 0.12, 0.25, 0.22, 0.12, 0.30, False, None, False, 0, 0, 0, 100)


# MAVERICKS BENCH UNIT
s_dinwiddie = BasketballPlayer("Spencer Dinwiddie", "Point Guard", 1, "Dallas Mavericks", 0.450, 0.80, 0.70, 0.12, 0.25, 0.20, 0.10, 0.35, False, None, False, 0, 0, 0, 100)
q_grimes = BasketballPlayer("Quentin Grimes", "Shooting Guard", 2, "Dallas Mavericks", 0.390, 0.70, 0.68, 0.10, 0.25, 0.20, 0.10, 0.30, False, None, False, 0, 0, 0, 100)
d_exum = BasketballPlayer("Dante Exum", "Small Forward", 3, "Dallas Mavericks", 0.370, 0.60, 0.60, 0.10, 0.22, 0.18, 0.10, 0.30, False, None, False, 0, 0, 0, 100)
m_kleber = BasketballPlayer("Maxi Kleber", "Power Forward", 4, "Dallas Mavericks", 0.390, 0.65, 0.70, 0.11, 0.22, 0.20, 0.11, 0.32, False, None, False, 0, 0, 0, 100)
d_gafford = BasketballPlayer("Daniel Gafford", "Center", 5, "Dallas Mavericks", .310, 0.50, 0.60, 0.12, 0.20, 0.22, 0.12, 0.30, False, None, False, 0, 0, 0, 100)


# MAGIC STARTING UNIT
j_suggs = BasketballPlayer("Jalen Suggs", "Point Guard", 1, "Orlando Magic", .330, 0.60, 0.65, 0.14, 0.20, 0.18, 0.13, 0.35, False, None, False, 0, 0, 0, 100)
k_caldwell_pope = BasketballPlayer("Kentavious Caldwell-Pope", "Shooting Guard", 2, "Orlando Magic", 0.400, 0.60, 0.65, 0.10, 0.22, 0.20, 0.12, 0.35, False, None, False, 0, 0, 0, 100)
f_wagner = BasketballPlayer("Franz Wagner", "Small Forward", 3, "Orlando Magic", .360, 0.65, 0.70, 0.11, 0.25, 0.18, 0.12, 0.35, False, None, False, 0, 0, 0, 100)
p_banchero = BasketballPlayer("Paolo Banchero", "Power Forward", 4, "Orlando Magic", .340, 0.70, 0.75, 0.13, 0.28, 0.20, 0.10, 0.40, False, None, False, 0, 0, 0, 100)
w_carter_jr = BasketballPlayer("Wendell Carter-Jr", "Center", 5, "Orlando Magic", .320, 0.60, 0.68, 0.12, 0.22, 0.20, 0.14, 0.30, False, None, False, 0, 0, 0, 100)


# WARRIORS STARTING UNIT
s_curry = BasketballPlayer("Stephen Curry", "Point Guard", 1, "Golden State Warriors", .428, 0.85, 0.70, 0.12, 0.30, 0.25, 0.15, 0.50, False, None, False, 0, 0, 0, 100)
b_hield = BasketballPlayer("Buddy Hield", "Shooting Guard", 2, "Golden State Warriors", .400, 0.70, 0.65, 0.10, 0.25, 0.20, 0.12, 0.45, False, None, False, 0, 0, 0, 100)
a_wiggins = BasketballPlayer("Andrew Wiggins", "Small Forward", 3, "Golden State Warriors", .420, 0.55, 0.62, 0.10, 0.22, 0.18, 0.14, 0.35, False, None, False, 0, 0, 0, 100)
d_green = BasketballPlayer("Draymond Green", "Power Forward", 4, "Golden State Warriors", .320, 0.70, 0.55, 0.15, 0.40, 0.30, 0.18, 0.35, False, None, False, 0, 0, 0, 100)
k_looney = BasketballPlayer("Kevon Looney", "Center", 5, "Golden State Warriors", .300, 0.25, 0.60, 0.10, 0.20, 0.20, 0.10, 0.25, False, None, False, 0, 0, 0, 100)


# 76ers STARTING UNIT
t_maxey = BasketballPlayer("Tyrese Maxey", "Point Guard", 1, "Philadelphia 76ers", 0.420, 0.75, 0.70, 0.10, 0.25, 0.22, 0.10, 0.35, False, None, False, 0, 0, 0, 100)
k_oubre = BasketballPlayer("Kelly Oubre-Jr", "Shooting Guard", 2, "Philadelphia 76ers", 0.430, 0.55, 0.70, 0.12, 0.25, 0.22, 0.12, 0.35, False, None, False, 0, 0, 0, 100)
p_george = BasketballPlayer("Paul George", "Small Forward", 3, "Philadelphia 76ers", 0.380, 0.65, 0.68, 0.11, 0.28, 0.25, 0.13, 0.35, False, None, False, 0, 0, 0, 100)
g_yabusele = BasketballPlayer("Guerschon Yabusele", "Power Forward", 4, "Philadelphia 76ers", 0.380, 0.50, 0.60, 0.12, 0.22, 0.20, 0.10, 0.30, False, None, False, 0, 0, 0, 100)
j_embiid = BasketballPlayer("Joel Embiid", "Center", 5, "Philadelphia 76ers", 0.370, 0.60, 0.75, 0.13, 0.30, 0.25, 0.15, 0.40, False, None, False, 0, 0, 0, 100)


# 76ers BENCH UNIT
j_mccain = BasketballPlayer("Jared McCain", "Point Guard", 1, "Philadelphia 76ers", 0.374, 0.60, 0.70, 0.12, 0.20, 0.18, 0.10, 0.30, False, None, False, 0, 0, 0, 100)
k_lowry = BasketballPlayer("Kyle Lowry", "Shooting Guard", 2, "Philadelphia 76ers", 0.400, 0.80, 0.70, 0.10, 0.30, 0.25, 0.12, 0.40, False, None, False, 0, 0, 0, 100)
c_martin = BasketballPlayer("Caleb Martin", "Small Forward", 3, "Philadelphia 76ers", 0.370, 0.55, 0.65, 0.09, 0.22, 0.20, 0.12, 0.30, False, None, False, 0, 0, 0, 100)
p_nance = BasketballPlayer("Pete Nance", "Power Forward", 4, "Philadelphia 76ers", 0.380, 0.60, 0.65, 0.12, 0.22, 0.20, 0.12, 0.30, False, None, False, 0, 0, 0, 100)
a_drummond = BasketballPlayer("Andre Drummond", "Center", 5, "Philadelphia 76ers", 0.520, 0.20, 0.60, 0.15, 0.18, 0.30, 0.15, 0.30, False, None, False, 0, 0, 0, 100)


# SUNS STARTING UNIT
t_jones = BasketballPlayer("Tyus Jones", "Point Guard", 1, "Phoenix Suns", .360, 0.85, 0.65, 0.09, 0.28, 0.22, 0.10, 0.30, False, None, False, 0, 0, 0, 100)
d_booker = BasketballPlayer("Devin Booker", "Shooting Guard", 2, "Phoenix Suns", .470, 0.75, 0.70, 0.10, 0.28, 0.22, 0.12, 0.30, False, None, False, 0, 0, 0, 100)
b_beal = BasketballPlayer("Bradley Beal", "Small Forward", 3, "Phoenix Suns", .450, 0.70, 0.68, 0.12, 0.28, 0.18, 0.10, 0.30, False, None, False, 0, 0, 0, 100)
k_durant = BasketballPlayer("Kevin Durant", "Power Forward", 4, "Phoenix Suns", .490, 0.80, 0.72, 0.08, 0.35, 0.30, 0.18, 0.40, False, None, False, 0, 0, 0, 100)
y_nurkic = BasketballPlayer("Jusuf Nurkic", "Center", 5, "Phoenix Suns", .380, 0.25, 0.65, 0.10, 0.20, 0.18, 0.14, 0.30, False, None, False, 0, 0, 0, 100)


# SUNS BENCH UNIT
m_morris = BasketballPlayer("Monte Morris", "Point Guard", 1, "Phoenix Suns", 0.400, 0.70, 0.65, 0.11, 0.22, 0.20, 0.12, 0.30, False, None, False, 0, 0, 0 , 100)
g_allen = BasketballPlayer("Grayson Allen", "Shooting Guard", 2, "Phoenix Suns", 0.400, 0.65, 0.68, 0.12, 0.25, 0.20, 0.12, 0.30, False, None, False, 0, 0, 0, 100)
r_oneale = BasketballPlayer("Royce O'Neale", "Small Forward", 3, "Phoenix Suns", 0.380, 0.60, 0.65, 0.11, 0.22, 0.18, 0.10, 0.32, False, None, False, 0, 0, 0, 100)
r_dunn = BasketballPlayer("Ryan Dunn", "Power Forward", 4, "Phoenix Suns", 0.370, 0.55, 0.62, 0.10, 0.20, 0.18, 0.10, 0.30, False, None, False, 0, 0, 0, 100)
m_plumlee = BasketballPlayer("Mason Plumlee", "Center", 5, "Phoenix Suns", 0.350, 0.50, 0.60, 0.12, 0.25, 0.22, 0.14, 0.35, False, None, False, 0, 0, 0, 100)


# KNICKS STARTING UNIT
j_brunson = BasketballPlayer("Jalen Brunson", "Point Guard", 1, "New York Knicks", 0.470, 0.75, 0.70, 0.09, 0.28, 0.22, 0.12, 0.40, False, None, False, 0, 0, 0, 100)
m_bridges = BasketballPlayer("Mikal Bridges", "Shooting Guard", 2, "New York Knicks", 0.410, 0.65, 0.68, 0.11, 0.22, 0.18, 0.10, 0.30, False, None, False, 0, 0, 0, 100)
o_anunoby = BasketballPlayer("OG Anunoby", "Small Forward", 3, "New York Knicks", 0.450, 0.60, 0.65, 0.12, 0.24, 0.20, 0.14, 0.35, False, None, False, 0, 0, 0, 100)
p_achiuwa = BasketballPlayer("Precious Achiuwa", "Power Forward", 4, "New York Knicks", 0.460, 0.45, 0.70, 0.10, 0.30, 0.32, 0.15, 0.40, False, None, False, 0, 0, 0, 100)
k_towns = BasketballPlayer("Karl-Anthony Towns", "Center", 5, "New York Knicks", 0.370, 0.15, 0.75, 0.08, 0.18, 0.28, 0.20, 0.30, False, None, False, 0, 0, 0, 100)


# KNICKS BENCH UNIT
c_payne = BasketballPlayer("Cameron Payne", "Point Guard", 1, "New York Knicks", 0.390, 0.65, 0.65, 0.12, 0.25, 0.20, 0.12, 0.32, False, None, False, 0, 0, 0, 100)
m_mcbride = BasketballPlayer("Miles McBride", "Shooting Guard", 2, "New York Knicks", 0.370, 0.60, 0.60, 0.10, 0.22, 0.18, 0.10, 0.30, False, None, False, 0, 0, 0, 100)
j_hart = BasketballPlayer("Josh Hart", "Small Forward", 3, "New York Knicks", 0.400, 0.70, 0.68, 0.11, 0.22, 0.20, 0.12, 0.35, False, None, False, 0, 0, 0, 100)
j_sims = BasketballPlayer("Jericho Sims", "Power Forward", 4, "New York Knicks", 0.350, 0.50, 0.62, 0.12, 0.25, 0.22, 0.12, 0.30, False, None, False, 0, 0, 0, 100)
m_robinson = BasketballPlayer("Mitchell Robinson", "Center", 5, "New York Knicks", 0.320, 0.40, 0.65, 0.10, 0.22, 0.20, 0.14, 0.30, False, None, False, 0, 0, 0, 100)


# CELTICS STARTING UNIT
j_holiday = BasketballPlayer("Jrue Holiday", "Point Guard", 1, "Boston Celtics", .480, .429, .833, .120, .180, .080, .090, .160, False, None, False, 0, 0, 0, 100)
d_white = BasketballPlayer("Derrick White", "Shooting Guard", 2, "Boston Celtics", 0.396, 0.75, 0.70, 0.12, 0.25, 0.20, 0.12, 0.40, False, None, False, 0, 0, 0, 100)
j_brown = BasketballPlayer("Jaylen Brown", "Small Forward", 3, "Boston Celtics", .480, .335, .765, .120, .180, .050, .060, .200, False, None, False, 0, 0, 0, 100)
j_tatum = BasketballPlayer("Jayson Tatum", "Power Forward", 4, "Boston Celtics", .473, .354, .854, .091, .200, .100, .060, .250, False, None, False, 0, 0, 0, 100)
k_porzingis = BasketballPlayer("Kristaps Porzingis", "Center", 5, "Boston Celtics", .498, .385, .850, .120, .180, .190, .070, .220, False, None, False, 0, 0, 0, 100)

# CELTICS BENCH UNIT
p_pritchard = BasketballPlayer("Payton Pritchard", "Point Guard", 1, "Boston Celtics", 0.375, 0.70, 0.65, 0.10, 0.20, 0.15, 0.10, 0.50, False, None, False, 0, 0, 0, 100)
j_springer = BasketballPlayer("Jaden Springer", "Shooting Guard", 2, "Boston Celtics", 0.218, 0.60, 0.65, 0.10, 0.20, 0.15, 0.10, 0.40, False, None, False, 0, 0, 0, 100)
s_hauser = BasketballPlayer("Sam Hauser", "Small Forward", 3, "Boston Celtics", 0.400, 0.60, 0.55, 0.09, 0.20, 0.12, 0.10, 0.40, False, None, False, 0, 0, 0, 100)
a_horford = BasketballPlayer("Al Horford", "Power Forward", 4, "Boston Celtics", .470, .380, .820, .130, .180, .100, .060, .140, False, None, False, 0, 0, 0, 100)
l_kornet = BasketballPlayer("Luke Kornet", "Center", 5, "Boston Celtics", 0.300, 0.50, 0.60, 0.12, 0.18, 0.22, 0.10, 0.30, False, None, False, 0, 0, 0, 100)


# LAKERS STARTING UNIT
a_reaves = BasketballPlayer("Austin Reaves", "Point Guard", 1, "Los Angeles Lakers", .390, 0.75, 0.60, 0.09, 0.20, 0.18, 0.09, 0.4, False, None, False, 0, 0, 0, 100)
d_knecht = BasketballPlayer("Dalton Knecht", "Shooting Guard", 2, "Los Angeles Lakers", .481, 0.25, 0.521, 0.143, 0.25, 0.1, 0.04, 0.2, False, None, False, 0, 0, 0, 100)
l_james = BasketballPlayer("LeBron James", "Small Forward", 3, "Los Angeles Lakers", .450, 0.80, 0.70, 0.12, 0.50, 0.50, 0.20, 0.5, False, None, False, 0, 0, 0, 100)
r_hachimura = BasketballPlayer("Rui Hachimura", "Power Forward", 4, "Los Angeles Lakers", .370, 0.35, 0.60, 0.10, 0.22, 0.20, 0.10, 0.3, False, None, False, 0, 0, 0, 100)
a_davis = BasketballPlayer("Anthony Davis", "Center", 5, "Los Angeles Lakers", .350, 0.30, 0.72, 0.12, 0.25, 0.28, 0.15, 0.3, False, None, False, 0, 0, 0, 100)


# LAKERS BENCH UNIT
d_russell = BasketballPlayer("D'Angelo Russell", "Point Guard", 1, "Los Angeles Lakers", 0.450, 0.80, 0.75, 0.12, 0.28, 0.22, 0.11, 0.40, False, None, False, 0, 0, 0, 100)
g_vincent = BasketballPlayer("Gabe Vincent", "Shooting Guard", 2, "Los Angeles Lakers", 0.380, 0.80, 0.70, 0.10, 0.25, 0.20, 0.12, 0.35, False, None, False, 0, 0, 0, 100)
m_christie = BasketballPlayer("Max Christie", "Small Forward", 3, "Los Angeles Lakers", 0.370, 0.60, 0.65, 0.09, 0.20, 0.18, 0.10, 0.30, False, None, False, 0, 0, 0, 100)
c_reddish = BasketballPlayer("Cam Reddish", "Power Forward", 4, "Los Angeles Lakers", 0.400, 0.65, 0.68, 0.12, 0.22, 0.20, 0.11, 0.32, False, None, False, 0, 0, 0, 100)
j_hayes = BasketballPlayer("Jaxson Hayes", "Center", 5, "Los Angeles Lakers", 0.350, 0.50, 0.70, 0.10, 0.25, 0.22, 0.12, 0.30, False, None, False, 0, 0, 0, 100)


# CLIPPERS STARTING UNIT
j_harden = BasketballPlayer("James Harden", "Point Guard", 1, "LA Clippers", .400, 0.85, 0.65, 0.15, 0.30, 0.25, 0.12, 0.6, False, None, False, 0, 0, 0, 100)
a_coffey = BasketballPlayer("Amir Coffey", "Shooting Guard", 2, "LA Clippers", .381, 0.25, 0.554, 0.071, 0, 0, 0.086, 0.25, False, None, False, 0, 0, 0, 100)
n_powell = BasketballPlayer("Norman Powell", "Small Forward", 3, "LA Clippers", .380, 0.40, 0.66, 0.10, 0.20, 0.18, 0.12, 0.3, False, None, False, 0, 0, 0, 100)
k_leonard = BasketballPlayer("Kawhi Leonard", "Power Forward", 4, "LA Clippers", .420, 0.45, 0.64, 0.08, 0.35, 0.45, 0.18, 0.35, False, None, False, 0, 0, 0, 100)
i_zubac = BasketballPlayer("Ivica Zubac", "Center", 5, "LA Clippers", .310, 0.20, 0.60, 0.10, 0.18, 0.22, 0.14, 0.25, False, None, False, 0, 0, 0, 100)


 # CLIPPERS BENCH UNIT 
k_porter_jr = BasketballPlayer("Kevin Porter-Jr", "Point Guard", 1, "LA Clippers", 0.390, 0.65, 0.70, 0.11, 0.25, 0.18, 0.12, 0.35, False, None, False, 0, 0, 0, 100)
b_hyland = BasketballPlayer("Bones Hyland", "Shooting Guard", 2, "LA Clippers", 0.410, 0.60, 0.68, 0.10, 0.22, 0.18, 0.11, 0.30, False, None, False, 0, 0, 0, 100)
t_mann = BasketballPlayer("Terance Mann", "Small Forward", 3, "LA Clippers", 0.400, 0.55, 0.65, 0.10, 0.20, 0.18, 0.10, 0.30, False, None, False, 0, 0, 0, 100)
d_jones_jr = BasketballPlayer("Derrick Jones-Jr", "Power Forward", 4, "LA Clippers", 0.350, 0.45, 0.62, 0.10, 0.22, 0.18, 0.12, 0.30, False, None, False, 0, 0, 0, 100)
m_bamba = BasketballPlayer("Mo Bamba", "Center", 5, "LA Clippers", 0.320, 0.40, 0.65, 0.10, 0.22, 0.20, 0.14, 0.30, False, None, False, 0, 0, 0, 100)



clippers_list = [j_harden, a_coffey, n_powell, k_leonard, i_zubac]
clippers_bench_list = [k_porter_jr, b_hyland, t_mann, d_jones_jr, m_bamba]

lakers_list = [a_reaves, d_knecht, l_james, r_hachimura, a_davis]
lakers_bench_list = [d_russell, g_vincent, m_christie, c_reddish, j_hayes]

celtics_list = [j_holiday, d_white, j_brown, j_tatum, k_porzingis]
celtics_bench_list = [p_pritchard, j_springer, s_hauser, a_horford, l_kornet]

knicks_list = [j_brunson, m_bridges, o_anunoby, p_achiuwa, k_towns]
knicks_bench_list = [c_payne, m_mcbride,j_hart, j_sims, m_robinson]

suns_list = [t_jones, d_booker, b_beal, k_durant, y_nurkic]
suns_bench_list = [m_morris, g_allen, r_oneale, r_dunn, m_plumlee]

sixers_list = [t_maxey, k_oubre, p_george, g_yabusele, j_embiid]
sixers_bench_list = [j_mccain, k_lowry, c_martin, p_nance, a_drummond]

warriors_list = [s_curry, b_hield, a_wiggins, d_green, k_looney]
magic_list = [j_suggs, k_caldwell_pope, f_wagner, p_banchero, w_carter_jr]

mavericks_list = [l_doncic, k_irving, k_thompson, p_washington, d_lively]
mavericks_bench_list = [s_dinwiddie, q_grimes, d_exum, m_kleber, d_gafford]


nuggets_list = [j_murray, c_braun, m_porter_jr, a_gordon, n_jokic]
pelicans_list = [d_murray, c_mccollum, b_ingram, z_williamson, d_theis]

teams_names = ['LA Clippers', 'Los Angeles Lakers', 'Boston Celtics', 'New York Knicks', 'Phoenix Suns', 'Philadelphia 76ers', 'Golden State Warriors', 'Orlando Magic', 'Dallas Mavericks', 'Denver Nuggets', 'New Orleans Pelicans']

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
elif user_team_input == '8':
    user_team = 'Orlando Magic'
    user_team_list = magic_list
    user_team_logo = magic_logo
elif user_team_input == '9':
    user_team = 'Dallas Mavericks'
    user_team_list = mavericks_list
    user_team_logo = mavericks_logo
    user_team_list_bench = mavericks_bench_list
elif user_team_input == '10':
    user_team = 'Denver Nuggets'
    user_team_list = nuggets_list
    user_team_logo = nuggets_logo
elif user_team_input == '11':
    user_team = 'New Orleans Pelicans'
    user_team_list = pelicans_list
    user_team_logo = pelicans_logo


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
elif opposing_team == 'Orlando Magic':
    opposing_team_list = magic_list
    opposing_team_logo = magic_logo
elif opposing_team == 'Dallas Mavericks':
    opposing_team_list = mavericks_list
    opposing_team_logo = mavericks_logo
    opposing_team_list_bench = mavericks_bench_list
elif opposing_team == 'Denver Nuggets':
    opposing_team_list = nuggets_list
    opposing_team_logo = nuggets_logo
elif opposing_team == 'New Orleans Pelicans':
    opposing_team_list = pelicans_list
    opposing_team_logo = pelicans_logo



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

