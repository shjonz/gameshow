#============================================Stage 1 =================================================####
import random
import time
import csv
import os


class Player:
    def __init__(self,name):
        self.name=name
        self.stage_1_2_Points= 500
        self.stage_3_Points = 0
        self.lives = 6
        
    def add_points(self,amt, stage):
        if stage == 1 or stage==2:
            self.stage_1_2_Points+=amt
        else:
            self.stage_3_Points+=amt
        
    def loselife(self):
        self.lives-= 1

    def __str__(self):
        return '{}'.format(self.name)

#set up -
# stage 1 spin wheel for random questions of a selected topic 
# 3 topics, HASS, geography, history

def create_players(num):
    new = []
    for i in range(num):
        name = input('What is your name player {}? '.format(i+1) )
        player_instance = Player(name)
        new.append(player_instance)
        print(new)
    return new

def turn_stage_1_wheel_to_pick_question(topic, lis_of_questions):
    if topic == 'HASS':
        dic = random.choice( lis_of_questions )
        qn = dic['Question']
        return qn, dic

    elif topic == 'Geography':
        dic = random.choice( lis_of_questions )
        qn = dic['Question']
        return qn, dic
    
    elif topic == 'History':
        dic = random.choice( lis_of_questions )
        qn = dic['Question']
        return qn, dic
    else:
        return 'Invalid topic'


def convert_to_list(topic):
    while True:
        questions_list = []
        with open("stage1.csv", newline='') as csvfile: 
        
            dict_reader = csv.DictReader(csvfile) 
         
            for line in dict_reader: 
                if line['Topic'] == topic:
                    questions_list.append(line)
            return questions_list

def Topic_game(topic):

    if topic == 'Geography':
        questions = 6
        stage_1_question_list = convert_to_list(topic)

        while questions > 0:

            players_who_havent_answered = lis_of_players[:]
            while len(players_who_havent_answered) > 0 and questions > 0:
            
                qn, dic = turn_stage_1_wheel_to_pick_question(topic, stage_1_question_list)
                
                question_prompt = '''
                ======================================
                Here is Question:
                {}
                Option A:{}
                Option B:{}
                Option C:{}
                Option D:{} 
                ======================================
                '''.format(qn, dic["A"], dic["B"], dic["C"], dic["D"])
                
                print(question_prompt)

                player = random.choice(players_who_havent_answered)
                
                answer = input('100 points, what option do you choose {}? '.format( player ) )
                if answer == dic['Correct Option']:
                    print('Correct +100')
                    players_who_havent_answered.remove(player)    
                    questions -= 1

                    for i in lis_of_players:
                        if i == player:
                            i.add_points( 100 , stage_level)
                            print(i.stage_1_2_Points)
                            if i.stage_1_2_Points > 2000:
                                print('{} has reached 2000 points, stage 1 has ended'.format(i))
                                questions = 0
                                players_who_havent_answered.clear()
                                
                    stage_1_question_list.remove(dic)
                    continue

                else:
                    print('Wrong answer, opening question up to next player...')
                    lis_no_wrong = lis_of_players[:]
                    lis_no_wrong.remove(player)
                    players_who_havent_answered.remove(player)
                    for i in lis_no_wrong:

                        print(question_prompt)
                        answer = input('100 points, what is ur answer {}? '.format(i))
                        
                        if answer == dic['Correct Option']:
                            print('Correct +100 points')
                            for n in lis_of_players:
                                if n == i:
                                    n.add_points( 100 , stage_level)
                                    print(n.stage_1_2_Points)
                                    if n.stage_1_2_Points > 2000:
                                        print('{} has reached 2000 points, stage 1 has ended'.format(n))
                                        questions = 0
                                        players_who_havent_answered.clear()
                                        break
                            
                            break
                        else:
                            print('Wrong, next player ....')
                            
                            continue
                             
                    stage_1_question_list.remove(dic)
                    questions -= 1
                    continue
                #geography_questions_list.remove(dic)
                #questions -= 1
            continue
        
        print( 'Geog round ended')

    #topic is history
    if topic == 'History':
        questions = 6
        stage_1_question_list = convert_to_list(topic)

        while questions > 0:

            players_who_havent_answered = lis_of_players[:]
            while len(players_who_havent_answered) > 0 and questions > 0:
            
                qn, dic = turn_stage_1_wheel_to_pick_question(topic, stage_1_question_list)
                question_prompt = '''
                ======================================
                Here is Question:
                {}
                Option A:{}
                Option B:{}
                Option C:{}
                Option D:{} 
                ======================================
                '''.format(qn, dic["A"], dic["B"], dic["C"], dic["D"])
                print(question_prompt)
                
                player = random.choice(players_who_havent_answered)
                
                answer = input('200 points, what option do you choose {}? '.format( player ) )
                if answer == dic['Correct Option']:
                    print('correct +200')
                    players_who_havent_answered.remove(player)    
                    questions -= 1
                    #add points to player
                    for i in lis_of_players:
                        if i == player:
                            i.add_points( 200 , stage_level)
                            print(i.stage_1_2_Points)
                            if i.stage_1_2_Points > 2000:
                                print('{} has reached 2000 points, stage 1 has ended'.format(i))
                                questions = 0
                                players_who_havent_answered.clear()
                    stage_1_question_list.remove(dic)
                    continue

                else:
                    print('Wrong answer, opening question up to next player...')
                    lis_no_wrong = lis_of_players[:]
                    lis_no_wrong.remove(player)
                    players_who_havent_answered.remove(player)
                    for i in lis_no_wrong:
                        print(question_prompt)
                        answer = input('200 points, what is ur answer {}? '.format(i))
                        
                        if answer == dic['Correct Option']:
                            print('Correct +200')
                            for n in lis_of_players:
                                if n == i:
                                    n.add_points( 200 , stage_level)
                                    print(n.stage_1_2_Points)
                                    if i.stage_1_2_Points > 2000:
                                        print('{} has reached 2000 points, stage 1 has ended'.format(i))
                                        questions = 0
                                        players_who_havent_answered.clear()
                            
                            break
                        else:
                            print('Wrong, next')
                            continue
                             
                    stage_1_question_list.remove(dic)
                    questions -= 1
                    continue
                #history_questions_list.remove(dic)
                #questions -= 1
            continue
        
        print( 'History round ended')

    if topic == 'HASS':
        questions = 6
        stage_1_question_list = convert_to_list(topic)
        while questions > 0:

            players_who_havent_answered = lis_of_players[:]
            while len(players_who_havent_answered) > 0 and questions > 0:
                #time.sleep(2)
                qn, dic = turn_stage_1_wheel_to_pick_question( topic, stage_1_question_list )
                question_prompt = '''
                ======================================
                Here is Question:
                {}
                Option A:{}
                Option B:{}
                Option C:{}
                Option D:{} 
                ======================================
                '''.format(qn, dic["A"], dic["B"], dic["C"], dic["D"])
                print(question_prompt)
                
                player = random.choice(players_who_havent_answered)
                
                answer = input('400 points, what option do you choose {}? '.format( player ) )
                if answer == dic['Correct Option']:
                    print('correct +400')
                    players_who_havent_answered.remove(player)    
                    questions -= 1
                    #add points to player
                    for i in lis_of_players:
                        if i == player:
                            i.add_points( 400 , stage_level)
                            print(i.stage_1_2_Points)
                            if i.stage_1_2_Points > 2000:
                                print('{} has reached 2000 points, stage 1 has ended'.format(i))
                                questions = 0
                                players_who_havent_answered.clear()
                    stage_1_question_list.remove(dic)
                    continue

                else:
                    print('Wrong answer, opening question up to next player...')
                    lis_no_wrong = lis_of_players[:]
                    lis_no_wrong.remove(player)
                    players_who_havent_answered.remove(player)
                    for i in lis_no_wrong:
                        print(question_prompt)
                        answer = input('400 points, what is ur answer {}? '.format(i))
                        
                        if answer == dic['Correct Option']:
                            print('Correct 400')
                            for n in lis_of_players:
                                if n == i:
                                    n.add_points( 400 , stage_level)
                                    print(n.stage_1_2_Points)
                                    if i.stage_1_2_Points > 2000:
                                        print('{} has reached 2000 points, stage 1 has ended'.format(i))
                                        questions = 0
                                        players_who_havent_answered.clear()
                            break
                        else:
                            print('Wrong, next')
                            continue
                              
                    stage_1_question_list.remove(dic)
                    questions -= 1
                    continue
                #hass_questions_list.remove(dic)
                #questions -= 1
            continue
        
        print( 'HASS round ended')

def start_stage1(list_of_players):
    start_loop = True
    
    while start_loop:
        print('First Round of questions')
        time.sleep(1)
        print('Each correct answer will award 100 points, wrong answer will award 0 points')
        time.sleep(1)
        print('A wrong answer will open up the question to other players to answer')
        time.sleep(1)
        print('First Round topic is Geography')
        time.sleep(1)
        print('Are you ready???')
        time.sleep(1)
        print('Starting Stage 1....')
        Topic_game('Geography')
        #Topic_game('History')
        #Topic_game('HASS')
        start_loop = False
        continue


###########===========================================================STAGE 2==================================################

def csvFiletoListDic(filename):
    list_of_words_to_guess = []
    with open(filename, newline='') as csvfile: 
        dict_reader = csv.DictReader(csvfile)
    
        for line in dict_reader:
            list_of_words_to_guess.append(line)
    return list_of_words_to_guess

def descending_player_index_sort(list_of_players):
    for i in range(1,len(list_of_players)):
        for j in range(i,0,-1):
            if list_of_players[j].stage_1_2_Points > list_of_players[j-1].stage_1_2_Points:
                list_of_players[j],list_of_players[j-1] = list_of_players[j-1],list_of_players[j]

def obscurePhrase(phrase, letters_guessed_correctly,replaced_chars_per_blank):
    LETTERS ='abcdefghijklmnopqrstuvwxyz'
    rv = ''
    for s in phrase:
        if (s in LETTERS) and (s not in letters_guessed_correctly):
            rv = rv+replaced_chars_per_blank
        else:
            rv = rv+s
    return rv

def eliminate_check(player,lis_of_players):
    print("Player {0}, you have {1} lives left and {2} points.".format(player.name,player.lives,player.stage_1_2_Points))
    if player.stage_1_2_Points<= 0 or player.lives ==0:
        print("Player {0}, you have been eliminated".format(player))
        lis_of_players.remove(player)

def start_stage2(lis_of_players):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    vowels  = 'aeiou'
    vowel_cost  = 150
    Letter_price = 100
    reward_price_per_char = 200

    list_of_words_to_guess = csvFiletoListDic('stage2lesser.csv')
    
    descending_player_index_sort(lis_of_players)

    attempt_Num = 0 

    for question in list_of_words_to_guess:

        letters_remain = list(letters)
        letters_guessed_correctly = []

        question_word = question['Question'].lower()

        covered_word = obscurePhrase(question_word, letters_guessed_correctly,"_")

        while covered_word!=question_word:

            display_covered_word =  obscurePhrase(question_word, letters_guessed_correctly,"_ ")
            print("\nPhysics the word to guess is... {}. \n The hint is: {}".format(display_covered_word, question['Hint']))

            player_index = attempt_Num %len(lis_of_players)
            player = lis_of_players[player_index]

            print("Player {0}, you have {1} lives left and {2} points.".format(player,player.lives,player.stage_1_2_Points))

            letter = ""
            while True:
                letter = str(input('A vowel costs {1} while a letter costs {2}.\nPlayer {0}, what letter do you guess? '.format(player,vowel_cost,Letter_price)))
                letter = letter.lower()
                if len(letter) > 1 or letter not in letters_remain:
                    print('Either you typed more than 1 letter or a letter than has already been used')  
                else:
                    break 
            
            letters_remain.remove(letter)

            if letter in vowels:
                player.add_points(-vowel_cost, 2)
            else:
                player.add_points(-Letter_price, 2)          
        
            
            if letter not in question_word:
                print('letter is not in the word')
                player.loselife()
            else:
                number_of_occurences = question_word.count(letter)
                points_rewarded = reward_price_per_char*number_of_occurences
                player.add_points(points_rewarded, 2)
                print("Congrats Player {0}, you have been rewarded with {1} points".format(player,points_rewarded))

                letters_guessed_correctly.append(letter)
                covered_word = obscurePhrase(question_word, letters_guessed_correctly,"_")

            eliminate_check(player,lis_of_players)

            attempt_Num+=1
        print(question_word)

def filter_top_players(lis_of_players,number_of_top_players):
    descending_player_index_sort(lis_of_players)
    print(lis_of_players)
    while len(lis_of_players) > number_of_top_players:
        lis_of_players.pop()


#=====================================================stage 3 ===========================================###
def start_stage3(list_of_players):
    stage_level=3
    ls_questions = csvFiletoListDic('stage3lesser.csv')

    for count, question in enumerate(ls_questions):
        best_player = None
        best_time = None
        
        for player in list_of_players:
            input('Player {0}, press enter key to begin... '.format(player))

            correct = False
            question_prompt = '''
            ==========================
            Here is Question {0}/{1} :
            {2}
            Option A:{3}
            Option B:{4}
            Option C:{5}
            Option D:{6}
            ==========================
            '''.format(count+1, len(ls_questions),question["qn"],question["A"],question["B"],question["C"],question["D"])
            print(question_prompt)
            start = time.time()
            answer = ""
            while True:
                answer = input("What is ur answer (A,B,C or D)?  ")
                answer = answer.upper()
                if len(answer) > 1 or answer not in "ABCD":
                    print('Either you typed more than 1 letter or not a valid option')  
                else:
                    break                 
            end = time.time()
            if answer == question["ans"]:
                correct = True
            
            time_taken = round(end-start,5)

            os.system("cls")
            if correct:
                print("You are RIGHT, time elapsed = {0}".format(time_taken))
                if best_time == None or time_taken<best_time:
                    best_time = time_taken
                    best_player = player
            else:
                print("You are WRONG")
        if best_player:
            best_player.add_points(1, stage_level)
        
        
        updated_score_msg = "Updated Scores are as follows:"
        for player in list_of_players:
            updated_score_msg += "\n Player {0}: {1} points".format(player,player.stage_3_Points)
        print(updated_score_msg+"\n")

def determine_winning_player(list_of_players):
    list_final_scores = [player.stage_3_Points for player in list_of_players]
    max_score = max(list_final_scores)
    list_winners = [player.name for player in list_of_players if player.stage_3_Points ==max_score]
    if len(list_winners)>1:
        print("Winners are {0}".format(list_winners))
    else:
        print("The winner is {0}".format(list_winners[0]))
    







#======================================================================game logic======================================########

lis_of_players = []
player_current_index = 0 
stage_level = 1

print('Welcome, this is a 3 player game, Enter your names... ')
time.sleep(1)
newlist = create_players(3)
lis_of_players = lis_of_players + newlist
start_stage1(lis_of_players)

#start stage 2
stage_level = 2
start_stage2(lis_of_players)


#start stage 3
filter_top_players(lis_of_players, 2)
start_stage3(lis_of_players)#make sure player list passed here is the new list
determine_winning_player(lis_of_players)