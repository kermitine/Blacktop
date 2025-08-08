"""
Copyright (C) 2025 Ayrik Nabirahni. This file
is apart of the Blacktop project, and licensed under
the GNU AGPL-3.0-or-later. See LICENSE and README for more details.
"""

import random
last_used_commentary_3ptshot = None
last_used_commentary_3ptmake = None
last_used_commentary_3ptmiss = None
last_used_commentary_drive = None
last_used_commentary_drivemake = None
last_used_commentary_drivemakefoul = None
last_used_commentary_drivemiss = None
last_used_commentary_drivemissfoul = None
last_used_commentary_firstfreethrowmake = None
last_used_commentary_firstfreethrowmiss = None
last_used_commentary_secondfreethrowmake = None
last_used_commentary_secondfreethrowmiss = None
last_used_commentary_pass = None
last_used_commentary_stolen = None
last_used_commentary_substitution_initial = None
last_used_commentary_substitution_final = None
last_used_commentary_haspossession = None
class CommentaryEngine():
    def commentator(principal_player, event, secondary_player):
            global last_used_commentary_3ptshot
            global last_used_commentary_3ptmake
            global last_used_commentary_3ptmiss
            global last_used_commentary_drive
            global last_used_commentary_drivemake
            global last_used_commentary_drivemakefoul
            global last_used_commentary_drivemiss
            global last_used_commentary_drivemissfoul
            global last_used_commentary_firstfreethrowmake
            global last_used_commentary_firstfreethrowmiss
            global last_used_commentary_secondfreethrowmake
            global last_used_commentary_secondfreethrowmiss
            global last_used_commentary_pass
            global last_used_commentary_stolen
            global last_used_commentary_substitution_initial
            global last_used_commentary_substitution_final
            global last_used_commentary_haspossession

            # RANDOMIZES USAGE OF FULL NAME, LAST NAME, OR NICKNAME
            num = random.randint(1, 8) # 50% to use last name (if nickname exists, otherwise 75%), 25% for full name, 25% for nickname
            if num in [1, 2, 3, 4, 5]:
                primary_name = principal_player.name.split(" ")[1]
            elif num in [6, 7] and principal_player.nicknames:
                nicknames_index = random.randint(0, (len(principal_player.nicknames)-1))
                primary_name = principal_player.nicknames[nicknames_index]
            else:
                primary_name = principal_player.name
            
            if principal_player.defender:
                num = random.randint(1, 8)
                if num in [1, 2, 3, 4, 5]:
                    defender_name = principal_player.defender.name.split(" ")[1]
                elif num in [6, 7] and principal_player.defender.nicknames:
                    nicknames_index = random.randint(0, (len(principal_player.defender.nicknames)-1))
                    defender_name = principal_player.defender.nicknames[nicknames_index]
                else:
                    defender_name = principal_player.defender.name

            if secondary_player:
                num = random.randint(1, 8)
                if num in [1, 2, 3, 4, 5]:
                    secondary_player_name = secondary_player.name.split(" ")[1]
                elif num in [6, 7] and secondary_player.nicknames:
                    nicknames_index = random.randint(0, (len(secondary_player.nicknames)-1))
                    secondary_player_name = secondary_player.nicknames[nicknames_index]
                else:
                    secondary_player_name = secondary_player.name

                if secondary_player.defender:
                    num = random.randint(1, 8)
                    if num in [1, 2 ,3, 4, 5]:
                        secondary_player_defender_name = secondary_player.defender.name.split(" ")[1]
                    elif num in [6, 7] and secondary_player.defender.nicknames:
                        nicknames_index = random.randint(0, (len(secondary_player.defender.nicknames)-1))
                        secondary_player_defender_name = secondary_player.defender.nicknames[nicknames_index]
                    else:
                        secondary_player_defender_name = secondary_player.defender.name
                





            if event == '3ptshot':
                cases = 15 # number of commentary variations
                commentary_variation = random.randint(1, cases)

                while True: # PREVENTS USING SAME COMMENTARY VARIATION TWICE IN A ROW
                    if last_used_commentary_3ptshot and last_used_commentary_3ptshot == commentary_variation:
                        commentary_variation = random.randint(1, cases)
                    else:
                        last_used_commentary_3ptshot = commentary_variation
                        break

                match commentary_variation:
                    case 1:
                        print('A confident three from', primary_name + '!')
                    case 2:
                        print(primary_name, 'lets it fly!')
                    case 3:
                        print(primary_name, 'from downtown!')
                    case 4:
                        print(primary_name, 'steps back and fires a three!')
                    case 5:
                        print('A corner three from', primary_name + '!')
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
                    case 14:
                        print(primary_name + ', a three!')
                    case 15:
                        print(primary_name + ', corner three!')

            elif event == '3ptmake':
                cases = 14 # number of commentary variations
                commentary_variation = random.randint(1, cases)  # Increased range for more variations

                while True: # PREVENTS USING SAME COMMENTARY VARIATION TWICE IN A ROW
                    if last_used_commentary_3ptmake and last_used_commentary_3ptmake == commentary_variation:
                        commentary_variation = random.randint(1, cases)
                    else:
                        last_used_commentary_3ptmake = commentary_variation
                        break

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
                cases = 11 # number of commentary variations
                commentary_variation = random.randint(1, cases)  # Increased range for more variations

                while True: # PREVENTS USING SAME COMMENTARY VARIATION TWICE IN A ROW
                    if last_used_commentary_3ptmiss and last_used_commentary_3ptmiss == commentary_variation:
                        commentary_variation = random.randint(1, cases)
                    else:
                        last_used_commentary_3ptmiss = commentary_variation
                        break
                
                match commentary_variation:
                    case 1:
                        print('And airballs!', defender_name, 'gathers it up.')
                    case 2:
                        print('And the shot is off the mark.')
                    case 3:
                        print('And he misfires.', defender_name, 'with the rebound.')
                    case 4:
                        print('SMOTHERED BY', defender_name.upper() + '!')
                    case 5:
                        print('The three-point attempt rattles out. Tough luck for', primary_name + '.')
                    case 6:
                        print('It’s no good from downtown!', defender_name, 'picks it up for the', principal_player.defender.team + '.')
                    case 7:
                        print('Way off target from beyond the arc.')
                    case 8:
                        print('And it’s just short! A strong defensive effort by', defender_name + '.')
                    case 9:
                        print('Off the back iron!', defender_name, 'secures the rebound.')
                    case 10:
                        print('Off the rim, recovered by', defender_name + '!')
                    case 11:
                        print('And that one clanks off the rim, rebounded by', defender_name + '.')


            elif event == 'drive':
                cases = 13 # number of commentary variations
                commentary_variation = random.randint(1, cases)  # Increased range for more variations

                while True: # PREVENTS USING SAME COMMENTARY VARIATION TWICE IN A ROW
                    if last_used_commentary_drive and last_used_commentary_drive == commentary_variation:
                        commentary_variation = random.randint(1, cases)
                    else:
                        last_used_commentary_drive = commentary_variation
                        break

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
                        print(principal_player.name, 'weaves through traffic and heads to the rack!')
                    case 10:
                        print('Explosive drive by ' + primary_name + '!')
                    case 11:
                        print(primary_name, 'cuts inside and challenges', defender_name + '!')
                    case 12:
                        print('Here we go!')
                    case 13:
                        print(primary_name, 'to the basket!')

            
            elif event == 'drivemake':
                cases = 13 # number of commentary variations
                commentary_variation = random.randint(1, cases)  # Increased range for more variations

                while True: # PREVENTS USING SAME COMMENTARY VARIATION TWICE IN A ROW
                    if last_used_commentary_drivemake and last_used_commentary_drivemake == commentary_variation:
                        commentary_variation = random.randint(1, cases)
                    else:
                        last_used_commentary_drivemake = commentary_variation
                        break

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
                    case 12:
                        print('And the smooth up-and-under layup is good!')
                    case 13:
                        print('And that high-arcing layup is good!')


            elif event == 'drivemiss':
                cases = 11 # number of commentary variations
                commentary_variation = random.randint(1, cases)

                while True: # PREVENTS USING SAME COMMENTARY VARIATION TWICE IN A ROW
                    if last_used_commentary_drivemiss and last_used_commentary_drivemiss == commentary_variation:
                        commentary_variation = random.randint(1, cases)
                    else:
                        last_used_commentary_drivemiss = commentary_variation
                        break 

                match commentary_variation:
                    case 1:
                        print('And the ball rims out!', defender_name, 'recovers it.')
                    case 2:
                        print('A BACKBOARD BLOCK BY', defender_name.upper() + '!')
                    case 3:
                        print('And he bricks it!', defender_name, 'brings it back up for the', principal_player.defender.team + '.')
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
                    case 11:
                        print('Rattles out, recovered by', defender_name + '!')
            

            elif event == 'pass': # UNSPAGHETTIFY
                cases = 15 # number of commentary variations
                commentary_variation = random.randint(1, cases)  # Increased range for more variations

                while True: # PREVENTS USING SAME COMMENTARY VARIATION TWICE IN A ROW
                    if last_used_commentary_pass and last_used_commentary_pass == commentary_variation:
                        commentary_variation = random.randint(1, cases)
                    else:
                        last_used_commentary_pass = commentary_variation
                        break

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


            elif event == 'drivemakefoul': 
                cases = 2 # number of commentary variations
                commentary_variation = random.randint(1, cases) 

                while True: # PREVENTS USING SAME COMMENTARY VARIATION TWICE IN A ROW
                    if last_used_commentary_drivemakefoul and last_used_commentary_drivemakefoul == commentary_variation:
                        commentary_variation = random.randint(1, cases)
                    else:
                        last_used_commentary_drivemakefoul = commentary_variation
                        break

                match commentary_variation:
                    case 1:
                        print('Count it and a foul!')
                    case 2:
                        print('And he’s fouled! Count the basket! One free throw coming up!')


            elif event == 'drivemissfoul': 
                cases = 2 # number of commentary variations
                commentary_variation = random.randint(1, cases) 

                while True: # PREVENTS USING SAME COMMENTARY VARIATION TWICE IN A ROW
                    if last_used_commentary_drivemissfoul and last_used_commentary_drivemissfoul == commentary_variation:
                        commentary_variation = random.randint(1, cases)
                    else:
                        last_used_commentary_drivemissfoul = commentary_variation
                        break

                match commentary_variation:
                    case 1:
                        print('Fouled on the way up, two free throws coming!')
                    case 2:
                        print('And he’s fouled! Two free throws coming up!')
            

            elif event == 'firstfreethrowmake':
                cases = 3 # number of commentary variations
                commentary_variation = random.randint(1, cases) 

                while True: # PREVENTS USING SAME COMMENTARY VARIATION TWICE IN A ROW
                    if last_used_commentary_firstfreethrowmake and last_used_commentary_firstfreethrowmake == commentary_variation:
                        commentary_variation = random.randint(1, cases)
                    else:
                        last_used_commentary_firstfreethrowmake = commentary_variation
                        break

                match commentary_variation:
                    case 1:
                        print('Makes the first!')
                    case 2:
                        print('Drains the first!')
                    case 3:
                        print('Bounces in the first.')


            elif event == 'firstfreethrowmiss': 
                cases = 3   # number of commentary variations
                commentary_variation = random.randint(1, cases) 

                while True: # PREVENTS USING SAME COMMENTARY VARIATION TWICE IN A ROW
                    if last_used_commentary_firstfreethrowmiss and last_used_commentary_firstfreethrowmiss == commentary_variation:
                        commentary_variation = random.randint(1, cases)
                    else:
                        last_used_commentary_firstfreethrowmiss = commentary_variation
                        break

                match commentary_variation:
                    case 1:
                        print('Misses the first!')
                    case 2:
                        print("First one's off!")
                    case 3:
                        print('The first one rattles out.')


            elif event == 'secondfreethrowmake': 
                cases = 3 # number of commentary variations
                commentary_variation = random.randint(1, cases) 

                while True: # PREVENTS USING SAME COMMENTARY VARIATION TWICE IN A ROW
                    if last_used_commentary_secondfreethrowmake and last_used_commentary_secondfreethrowmake == commentary_variation:
                        commentary_variation = random.randint(1, cases)
                    else:
                        last_used_commentary_secondfreethrowmake = commentary_variation
                        break

                match commentary_variation:
                    case 1:
                        print('Makes the second!')
                    case 2:
                        print('Drains the second!')
                    case 3:
                        print('Bounces in the second.')


            elif event == 'secondfreethrowmiss': 
                cases = 3 # number of commentary variations
                commentary_variation = random.randint(1, cases) 

                while True: # PREVENTS USING SAME COMMENTARY VARIATION TWICE IN A ROW
                    if last_used_commentary_secondfreethrowmiss and last_used_commentary_secondfreethrowmiss == commentary_variation:
                        commentary_variation = random.randint(1, cases)
                    else:
                        last_used_commentary_secondfreethrowmiss = commentary_variation
                        break

                match commentary_variation:
                    case 1:
                        print('Misses the second!')
                    case 2:
                        print("Second one's off!")
                    case 3:
                        print('The second one rattles out.')
            

            elif event == 'stolen':
                cases = 10 # number of commentary variations
                commentary_variation = random.randint(1, cases)  # Increased range for more variations

                while True: # PREVENTS USING SAME COMMENTARY VARIATION TWICE IN A ROW
                    if last_used_commentary_stolen and last_used_commentary_stolen == commentary_variation:
                        commentary_variation = random.randint(1, cases)
                    else:
                        last_used_commentary_stolen = commentary_variation
                        break

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
                        print(primary_name, 'turns it over!', secondary_player_defender_name, 'brings it back up the court!')
                    case 6:
                        print('Pickpocketed by ' + secondary_player_defender_name + '!')
                    case 7:
                        print('And a clean steal by ' + secondary_player_defender_name + '!')
                    case 8:
                        print('Fantastic anticipation by ' + secondary_player_defender_name + ', and he takes it away!')
                    case 9:
                        print('A quick swipe by ' + secondary_player_defender_name + '! Possession changes hands.')
                    case 10:
                        print('And ' + primary_name + "'s pass is intercepted by " + secondary_player_defender_name + '!')
            

            elif event == 'substitution_initial':
                cases = 4 # number of commentary variations
                commentary_variation = random.randint(1, cases)

                while True: # PREVENTS USING SAME COMMENTARY VARIATION TWICE IN A ROW
                    if last_used_commentary_substitution_initial and last_used_commentary_substitution_initial == commentary_variation:
                        commentary_variation = random.randint(1, cases)
                    else:
                        last_used_commentary_substitution_initial = commentary_variation
                        break

                match commentary_variation:
                    case 1:
                        print('Seems like we got a substitution coming up for the ' + principal_player.team + '!')
                    case 2:
                        print('Seems like the coach is making a change for the ' + principal_player.team + '!')
                    case 3:
                        print('And we have a substitution for the ' + principal_player.team + '!')
                    case 4:
                        print('Another change for the ' + principal_player.team + '.')


            elif event == 'substitution_final':
                cases = 2 # number of commentary variations
                commentary_variation = random.randint(1, cases)

                while True: # PREVENTS USING SAME COMMENTARY VARIATION TWICE IN A ROW
                    if last_used_commentary_substitution_final and last_used_commentary_substitution_final == commentary_variation:
                        commentary_variation = random.randint(1, cases)
                    else:
                        last_used_commentary_substitution_final = commentary_variation
                        break

                match commentary_variation:
                    case 1:
                        print('So ' + primary_name + ' will come in for ' + secondary_player_name + '.')
                    case 2:
                        print('And ' + primary_name + ' will take the place of ' + secondary_player_name + '.')


            elif event == 'tipoff':
                cases = 2 # number of commentary variations
                commentary_variation = random.randint(1, cases)

                match commentary_variation:
                    case 1:
                        print('So we have ' +  primary_name + ' taking the tip for the ' + principal_player.team + ', against ' + secondary_player_name + ' for the ' + secondary_player.team + '.')
                    case 2:
                        print(primary_name + ' will take it for the ' + principal_player.team + ', while ' + secondary_player_name + "'s up for the " + secondary_player.team + '.')


            elif event == 'tipoffoutcome':
                cases = 3 # number of commentary variations
                commentary_variation = random.randint(1, cases)

                match commentary_variation:
                    case 1:
                        print(primary_name, 'wins the jump! Tipped to ' + secondary_player_name + '!')
                    case 2:
                        print("And it's tipped to " + secondary_player_name + '!')
                    case 3:
                        print('The ' + principal_player.team + ' win the tip! ' + secondary_player_name + "'s got it!")
            
            elif event == 'haspossession':
                cases = 7 # number of commentary variations
                commentary_variation = random.randint(1, cases)

                while True: # PREVENTS USING SAME COMMENTARY VARIATION TWICE IN A ROW
                    if last_used_commentary_haspossession and last_used_commentary_haspossession == commentary_variation:
                        commentary_variation = random.randint(1, cases)
                    else:
                        last_used_commentary_haspossession = commentary_variation
                        break
                match commentary_variation:
                    case 1:
                        print(primary_name, 'breaks the press!')
                    case 2:
                        print(primary_name, 'brings it up!')
                    case 3:
                        print(primary_name, 'has it!')
                    case 4:
                        print(primary_name, 'brings it up the court!')
                    case 5:
                        print(primary_name, 'brings it up the floor!')
                    case 6:
                        print(primary_name, 'brings it up the floor for the', principal_player.team + '!')
                    case 7:
                        print(primary_name, 'brings it up the court for the', principal_player.team + '!')

            return event

                    
