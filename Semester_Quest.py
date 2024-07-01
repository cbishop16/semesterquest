import sys 
import time
import random as rand
import math 
class college_player: #functions for the player
    #Essentially contains functions that would affect a players stats
    def __init__(self, name,age=18): #defines the players stats
        self.name = name #player will input a name
        self.age = age #age is 18
        self.money = rand.randint(0,100) #the player will start with a random amount of money (0-100) and will change depeneding on how much they work
        self.health = rand.randint(75,90) #the player will start with a random amount of health (50,100) and will change depending on their decisions
        self.happiness = rand.randint(0,100) #the player will start with a random happiness level that will change as they play the game
        self.gpa = float(4) #the player starts off with a 4.0 gpa
        self.classes = rand.randint(4,6) #a random number of classes 
    
    def bar(self): #senario for when the player choses to go to the bar
        gg.slow_print("\nTHE BARS!!!",0.06)
        gg.slow_print(f"You currently have ${self.money} to your name.",0.04) #show how much money the player has

        if self.money <= 50: #if money is less than or equal to $50 
            gg.slow_print("You might have to get a job after tonight.",0.04) #recommend to the player that they mihgt want to get a job
            yes = gg.slow_input("You sure you wanna go? ",0.04) #make sure they definetly want to go
            gg.check_yes_no(yes) #calls check_yes_no function
            if yes == 'n': #back out of going to the bar, give other choices
                options = ['hangout with friends','sleep','play video games','read a book'] #options
                gg.print_list(options) #calls print list function 
                what = gg.slow_input('What do you wanna do instead?',0.04)#user input what they want to do
                what = gg.check_number_answer(what,options) #calls the check_number_answer function

                if what == '0': 
                    gg.endgame() #calls endgame function
                elif what == '1':   
                    cp.hangout_night(self) #calls hangout function
                elif what == '2':
                    cp.video_games(self) #calls video_games function
                elif what == '3': 
                    cp.sleep(self) #calls sleep function
                else:
                    cp.read_book(self) #calls read_book function
            else: #if yes continues code
                pass
        elif self.money > 50: #if money is greater than $50
            gg.slow_print("You'll be fine for the night!",0.04)
        
        options = ['room','bars'] #option for where to drink
        gg.slow_print('\nYou are deciding whether or not you should drink at the bar or in your room.',0.04)
        gg.print_list(options) #calls print_list function
        ans = gg.slow_input('What are you going to do? ',0.04) #user input
        ans = gg.check_number_answer(ans,options) #calls function
        if ans == '0':
            gg.endgame() #calls function
        elif ans == '1': #drink in room
            gg.slow_print("\nSmart decision!",0.04)
            gg.slow_print('Drinks are overpriced at the bars!',0.04)
            gg.slow_print('\nYou get a small group of friends to drink with.',0.04)
            lots = rand.randint(1,2)
            if lots == 1: #early start to the night
                gg.slow_print('The night has only begun!',0.04)
                gg.slow_print('Why not play a few drinking games?',0.04)
                luck = rand.randint(1,2)
                positive = ['You did not lose a single game!','You won the most games!']
                negative = ['You lost every single game!','You finished a whole handle!!!'] 
                if luck == 1: #negative senario
                    gg.slow_print(rand.choice(negative),0.04) #random negative line
                    self.health += rand.randint(-45,0) #stat change
                else: #postitve senario
                    gg.slow_print(rand.choice(positive),0.04) #random positive line
                    self.health += rand.randint(-25,0) #stat change
            else: #late start to the night
                gg.slow_print("Since you guys started late, theres not time for games!",0.04)
                gg.slow_print("Get to chuggin' so you guys can get to the bars!",0.04)
                senario = ['You took those shots like a champ!','Those drinks are melting your insides!','Was that water you were drinking?','What did they mix to make that awful drink?!?!'] #list of senarios
                gg.slow_print(rand.choice(senario),0.04) # print random senaro
            
            gg.slow_print('\nYour group decides to walk to the bars.',0.04)

            a = rand.randint(1,2) 
            if a == 1: #problem on the walk
                problems = ['You left your keys!','You forgot your wallet!','You left your phone!'] #list of problems 
                gg.slow_print(rand.choice(problems),0.04) #print random problem
                self.happiness += rand.randint(-30,0) #stat change
                #choice to turn back or still go to the bars
                options = ['turn back','go to the bars']
                gg.print_list(options) #calls function
                do = gg.slow_input('What are you going to do? ',0.04) #user input
                do = gg.check_number_answer(do,options) #calls function
                if do == '0':
                    gg.endgame()
                elif do == '1': #go back to dorm
                    gg.slow_print("\nYou turn back.",0.04)
                    gg.slow_print("You get back to your dorm to grab what you forgot.",0.04)
                    
                    feel = ['like s%#t','energized',]
                    gg.slow_print(f'You feel {rand.choice(feel)}!',0.04) #how player feels
                    #choice to go back to the bars
                    yes = ['stay','go back out']
                    gg.print_list(yes)
                    what = gg.slow_input('What are you going to do? ',0.04)
                    what = gg.check_number_answer(what, yes)
                    if what == '0':
                        gg.endgame() #calls function
                    elif what == '1': #don't go back 
                        gg.slow_print('You decide it is not worth going back out.',0.04)
                        gg.slow_print('Good on you, cause the bars are so overrated!',0.04)
                        options = ['sleep','video games','go on a walk'] #other options
                        gg.print_list(options)
                        where = gg.slow_input('What are you going to do? ',0.04)
                        what = gg.check_number_answer(where,options)
                        if where == '0':
                            gg.endgame()
                        elif where == '1':
                            cp.video_games(self)
                        else:
                            cp.walk(self)
                    else: #go back to the bars
                        gg.slow_print('You make your way back to the bars!',0.04)
                        cp.bar2(self)        
                else:
                    gg.slow_print("F@%k it, you don't need it!",0.04)
                    cp.bar2(self)
            else: #no problem on the walk
                pos = ['You guys made it to the bars in one piece!','Someone complemented on your walk to the bars!','On the way your friend walked straight into a pole!']
                gg.slow_print(rand.choice(pos),0.04)
                self.happiness += rand.randint(0,20)#stat change
                #line is long or short
                a = ['shorter than attention span','longer than your patience']
                length = rand.choice(a)
                gg.slow_print(f"You get to the line and see that it's {length}!",0.04)
                if length == 'longer than your patience': #line is too long
                    gg.slow_print('\nYou decided that the line is way too long!',0.04)
                    gg.slow_print('You go back to your dorm.',0.04)
                    self.happiness += rand.randint(-35,0)
                    self.health += rand.randint(-30,0)
                else: #line is short go to the bar
                    gg.slow_print('You and your friends get into the bar.',0.04)
                    cp.bar2(self)
        else: #drink at the bars  
            gg.slow_print('\nYou must be made of money or something!',0.04)
            gg.slow_print('Drinks are overpriced at the bars!',0.04)
            gg.slow_print('\nYou get to the bars!',0.04)
            cp.bar2(self)
            
    def bar2(self): #continue bar function
        gg.slow_print('You go up to the bartender and order some drinks!',0.04)
        if self.money > 0: #options to buy drinks if player wants
            gg.slow_print(f'\nYou have ${self.money} and each drink costs $4.',0.04)
            drinks = gg.slow_input('How many drinks would you like to get for the night? ',0.04)
            drinks = gg.check_number(drinks)
            drinks = int(drinks)
                    
            q = math.floor(self.money/4)
            #conditions for amount of drinks
            if drinks == q:
                gg.slow_print("YOURE CRAZYYYYYY!!",0.04)
                gg.slow_print('YOU HAVE ZERO MONEY NOW!',0.04)
                gg.slow_print("Lets forget about that though...",0.05)
                gg.slow_print('YOU CAME TO GET CRUNK!',0.04)
                self.happiness += 1000000
                self.health -= 100000
                cp.instant_win(self)
            elif 0 < drinks <= q:
                gg.slow_print('You got your drinks for the night!',0.04)      
            elif drinks == 0:
                gg.slow_print("You didn't get any!",0.04)
                gg.slow_print('You are a soldier for being around drunk people SOBER!',0.04)
            elif drinks > q:
                while drinks > q:
                    gg.slow_print("You can't afford that many drinks!",0.04)
                    drinks = int(gg.slow_input('Pick a smaller amount: ',0.04)) 
                gg.slow_print('You got your drinks for the night!',0.04)      
            else:
                drinks = int(gg.slow_input(f'Please enter a valid number (0-{q}): ',0.04))      
            self.money -= 4*drinks 
        elif self.money <= 0: #can't afford drinks
                gg.slow_print("You can't afford drinks!",0.04)
        #stuff to do at the bars
        gg.slow_print("\nYou and your friends find a place to sit.",0.04)
        actions = ['dance','drink','talk']
        gg.print_list(actions)
        what = gg.slow_input('What are you gonna do? ',0.04)
        what = gg.check_number_answer(what,actions)

        if what == "0":
            gg.endgame()
        elif what == '1':
            cp.dance(self)
        elif what == '2':
            cp.drink(self,drinks)
        else:
            cp.talk(self)
            gg.slow_print('You feel super akward after that conversation, so you decide to go dance.',0.04)
            cp.dance(self)

    def calc_gpa(self,factor): #calculates gpa based on # of classes and the factor
        self.gpa += factor*1/2*self.classes
        return self.gpa 

    def check_health(self): #makes sure player is alive
        if self.health <= 0: 
            gg.slow_print('You died.',0.06)
            gg.endgame()
        else:
            pass
            
    def check_money(self,floor,general): #check to see if player has enough money to afford concert tickets
        if self.money < floor and self.money < general:
            gg.slow_print('You have no money to buy the ticket!',0.04)
        if self.money > floor and self.money > general: 
            gg.slow_print("You can purchase the tickets!",0.04)   
        if self.money < floor and self.money > general: 
            gg.slow_print("You can only afford the general ticket.",0.04)
        if self.money > floor and self.money < general: 
            gg.slow_print("You can only afford the floor tickets.",0.04)

    def check_tired(self): #warning for player to get rest because health is low
        if self.health < 20:
            gg.slow_print("You should get some REST!!",0.04)
            gg.slow_print(f"You aren't feeling that great! (health = {self.health})",0.04)
        elif self.health == 0:
            gg.slow_print("You are so exhuasted.",0.04)
            gg.slow_print("Everything gets blurry and your insides start melting.",0.04)
            senarios = ['A bus ran you over as you tried to cross the street!',
                        'A wild baseball cracked your head open!',
                        'A meteor is flying straight at you!',
                        'You tripped down the stairs!']
            gg.slow_print(rand.choice(senarios),0.04)
            gg.slow_print('You died!',0.04)
            gg.endgame()
        else:
            pass

    def check_wol_conditions(self): #win/lose conditions
        if self.gpa < 2.75:
            gg.slow_print(f"Unfortunately, you did not pass this semester. Better luck next time!",0.03)
        elif 3 > self.gpa >= 2.75:
            gg.slow_print('You passed the semester!',0.04)
            gg.slow_print("You know you could've done better.",0.04)
            gg.slow_print("But for your first semester in college, I guess it's not too bad.",0.04)
        elif 4 > self.gpa >= 3:
            gg.slow_print(f"Congratulations! You passed the semester with a gpa of {self.gpa}.",0.04)
        
        if self.happiness > 50:
            gg.slow_print('You are very happy with how your semester ended!',0.04)
        elif 30 <= self.happiness <= 50:
            gg.slow_print('You ended the semester semi-happy.',0.04)
        else:
            gg.slow_print('You ended your semester very depressed.',0.04)

        if self.health <= 0:
            gg.slow_print('You did not survive the semester.',0.04)
            var = ['You died to exhuastion.','You died to the common cold']
            gg.slow_print(rand.choice(var),0.04)
        elif 0 < self.health <= 50:
            gg.slow_print('You ended the semester some what sick!',0.04)  
        elif self.health > 50:
            gg.slow_print('You kept yourself healthy this semester!',0.04)
        gg.endgame()

    def concert(self): #senario for when palyer goes to a concert
        gg.slow_print("\nTHERES A CONCERT TONIGHT",0.04)
        artists = ['Dominic Fike','Bennett Coast','Tame Impala', 'Joji','Playboy Carti','Tyler the Creator','Bakar','Taylor Swift','Green Day','Fall Out Boys','Imagine Dragons','Coldplay','Frank Ocean','Childish Gambino', 'Jaden','Steve Lacy','Daniel Caesar','Still Woozy','Clairo','Bring Me the Horizon']
        random_artist = rand.sample(artists,6)
        gg.print_list(random_artist)
        which = gg.slow_input('Which artist would you like to go see? ',0.04)
        which = gg.check_number_answer(which,random_artist)

        if which == '0':
            gg.endgame()
        else:
            gg.slow_print(f'\nYou decided to go and see {random_artist[int(which)-1]}!',0.04)

            prices = rand.randint(1,3) #different prices for the tickets
            if prices == 1:
                floor = rand.randint(50,75)
                general = rand.randint(30,65)  
            elif prices == 2:
                floor = rand.randint(75,105)
                general = rand.randint(65,85)
            else:
                floor = rand.randint(110,200)
                general = rand.randint(90,120)

            if self.money >= floor and self.money >= general: #makes sure player can afford the tickets

                gg.slow_print(f'The floor tickets cost ${floor} and the seat tickets cost ${general}!',0.04)
                cp.check_money(self,floor,general)

                get_ticket = ['off a sketchy website?','through a reliable website?','off a friend?']
                gg.print_list(get_ticket)
                how = gg.slow_input('How are you going to buy the ticket(s)? ',0.04)
                how = gg.check_number_answer(how,get_ticket)
                #different methods to get the tickets
                if how == '0':
                    gg.endgame()
                elif how == '1':
                    cp.website_scam(self,floor,general)
                elif how == '2':
                    cp.website_reliable(self,floor,general)
                else: 
                    cp.website_friend(self,floor,general)
            
                cg.concert_day(self,random_artist[int(which)-1]) #continue concert sernario
            else: #no money, so can't go to the concert
                gg.slow_print("You don't have enough money to go the concert.",0.04)

    def dance(self): #dancing at the bar
        gg.slow_print('\nYou get on that dance floor and dance your heart out.',0.04)
        luck = rand.randint(1,2)
        if luck == 1: #bad dancing that affects stats 
            negatives = ['You danced like a robot!!!','You are a terrible dancer!','Did you pull your hamstring??','You ate s$%t!']
            gg.slow_print(f'\n{rand.choice(negatives)}',0.04)
            gg.slow_print('You leave with the whole bar laughing at you!',0.04)
            self.happiness += rand.randint(-40,0)
            self.health += rand.randint(-30,0)
        else: #good dancing that affects stats
            positives = ['Since when could you dance?!?!','WOW! YOU CAN DANCE!','MICHEAL JACKSON!','You whole bar impressed!']
            gg.slow_print(f'\n{rand.choice(positives)}',0.04)
            gg.slow_print('You leave the bar feeling like the main character!',0.04)
            self.happiness += rand.randint(0,40)
            self.health += rand.randint(0,30)
    
    def display_college_info(self): #function that shows a players stats
        gg.slow_print(f'Name: {self.name}',0.04)
        gg.slow_print(f'Age: {self.age}',0.04)
        gg.slow_print(f'Money: ${self.money}',0.04)
        gg.slow_print(f'Health: {self.health}',0.04)
        gg.slow_print(f'Happiness: {self.health}',0.04)
        gg.slow_print(f'Gpa: {round(self.gpa,2)}',0.04)

    def dininghall(self): #dining hall senario
        gg.slow_print('\nFood has to be the greatest idea ever!',0.04)
        gg.slow_print('You get to eat, and get talk to new people!',0.04)
        gg.slow_print('Its like killing 2 birds with one stone!',0.04)
            
        factor = rand.randint(-40,40)   
        if factor < 0: #bad expirence that affects players stats
            negatives = ['You think you got a stomach bug!',
                        'The food quality was terrible!',
                        'You found a bandaid in your sandwhich!',
                        "You didn't get to meet anyone!"]
            gg.slow_print(f'\n{rand.choice(negatives)}',0.04)                   
        elif factor > 0: #good expirence that affects players stats
            positives = ['You ate so much good food!',
                        'You met some great people!']
            gg.slow_print(f'\n{rand.choice(positives)}',0.04)
        else: #neutral outcome
            gg.slow_print('\nNothing out of the ordinary happened!',0.04)    
        #stat changes
        self.happiness += factor
        self.health += factor 

        if self.health <= 0: #player dies (death condition) 
            gg.slow_print("\nYou did not know you were deathly allergic to something you ate!",0.04)
            gg.slow_print('The paramedics did not arrive in time!',0.04)
            gg.slow_print('You died.',0.04)
            gg.endgame()

    def do_hw(self): #player does homework
        digit = rand.randint(1,3)
        if digit == '1': #no hw done
            gg.slow_print('\nYou were not on task and easily distracted.',0.04)
            gg.slow_print('You got no work done.',0.04)
            self.health += rand.randint(-45,0)
            self.happiness += rand.randint(-35,0)
            self.gpa = cp.calc_gpa(self,rand.uniform(-0.25,0))
        elif digit == '2': #some hw done
            gg.slow_print('\nYou got some work done.',0.04)
            gg.slow_print('There is still much more that needs to be done!',0.04)
            self.health += rand.randint(-35,0)
            self.happiness += rand.randint(-35,0)
            self.gpa = cp.calc_gpa(self,rand.uniform(-0.2,0.2))
        else: #a lot of hw done
            gg.slow_print('\nYou got a lot of work done today!',0.04)
            self.health += rand.randint(-20,0)
            self.happiness += rand.randint(0,20)
            self.gpa = cp.calc_gpa(self,rand.uniform(0,0.35))          

    def drink(self,drinks): #drinking at the bar
        if drinks > 1: #multiple drinks
            #How they drink (fast, slow)
            gg.slow_print("I know you didn't forget about the drinks you got!",0.04)
            option = ['chug','sip']
            gg.print_list(option)
            patience = gg.slow_input('How are you gonna face your drinks? ',0.04)
            patience = gg.check_number_answer(patience,option)

            if patience == '0':
                gg.endgame()
            elif patience == '1': #player chugs drinks (instant lose)
                gg.slow_print('You chug your drinks like a MADMAN!!',0.04)
                self.happiness += rand.randint(-20,20)
                self.health += rand.randint(-25,5)
                gg.slow_print("\nYou are experiencing a feeling you can't describe!",0.04)
                gg.slow_print("Its unbelievable!",0.04)
                gg.slow_print('What is this feeling?',0.04)
                gg.slow_print('NEWS FLASH!!',0.04)
                gg.slow_print('You some how teleported to the bathroom.',0.04)
                gg.slow_print('There is yak everywhere',0.04)
                gg.slow_print('After realizing you did that.',0.04)
                gg.slow_print('You get yourself together and bolt for the exit.',0.04)
                self.happiness -= 10000
                if self.health < 1000:
                    gg.slow_print('You left feeling embarassed and decide that you will never go to the bars again.',0.04)
                    gg.slow_print('After some time a you come across a video online of your puke and run incident.',0.04)
                    gg.slow_print("People start to recognize you and you can't handle staring and whispers.",0.04)
                    gg.slow_print("ITS MAKING YOU GO BONKERS.",0.04)
                    gg.slow_print('SO YOU DROP OUT!',0.04)
                    gg.slow_print('You lose.',0.04)
                gg.endgame()

            else: #player chooses to sip their drinks
                gg.slow_print('You sip on your drinks like any responsible person would.',0.04)
                gg.slow_print('Your drinks taste like candy!',0.04)
                gg.slow_print('You went through them much quicker than you expected.',0.04)
                gg.slow_print('You feel like dancing!',0.04)
                cp.dance(self)

        elif drinks == 1: #player only got 1 drink same thing just singular sentences
            gg.slow_print("I know you didn't forget about the drinks you got.",0.04)
            option = ['chug','sip']
            gg.print_list(option)
            patience = gg.slow_input('How are you gonna face your drink?',0.04)
            patience = gg.check_number_answer(patience,option)

            if patience == '0':
                gg.endgame()
            elif patience == '1': #chug
                gg.slow_print('You chug your drink like a MADMAN!!',0.04)
                self.happiness += rand.randint(-20,20)
                self.health += rand.randint(-25,5)
                luck = rand.randint(1,4)
                if luck == 1:
                    gg.slow_print("You are experiencing a feeling you can't describe!",0.04)
                    gg.slow_print("Its unbelievable!",0.04)
                    gg.slow_print('What is this feeling?',0.04)
                    gg.slow_print('NEWS FLASH!!',0.04)
                    gg.slow_print('You somehow teleported to the bathroom.',0.04)
                    gg.slow_print('There is yak everywhere',0.04)
                    gg.slow_print('After realizing you did that.',0.04)
                    gg.slow_print('You get yourself together and bolt for the exit.',0.04)
                    self.happiness -= 10000
                    if self.health < 1000:
                        gg.slow_print('You left feeling embarassed and decide that you will never go to the bars again.',0.04)
                        gg.slow_print('After some time a you come across a video online of your puke and run incident.',0.04)
                        gg.slow_print("People start to recognize you and you can't handle staring and whispers.",0.04)
                        gg.slow_print("ITS MAKING YOU GO BONKERS.",0.04)
                        gg.slow_print('SO YOU DROP OUT!',0.04)
                        gg.slow_print('You lose.',0.04)
                        gg.endgame()
                else:
                    gg.slow_print('You finish your drink!',0.04)
                    gg.slow_print('You feel like dancing!',0.04)
                    cp.dance(self)
            else: 
                gg.slow_print('You sip on your drink like any responsible person would.',0.04)
                gg.slow_print('Your drink tasted like candy!',0.04)
                gg.slow_print('You feel like dancing!',0.04)
                cp.dance(self)

        elif drinks == 0: #no drinks
            gg.slow_print("You did not buy a drink, so you can't drink anything.",0.04)
            gg.slow_print("I can't tell if your drunk asf or just plain stupid!",0.04)
            gg.slow_print('You decide to go dance instead.',0.04)
            cp.dance(self)

    def extra_time(self): #see if player has extra time
        digit = rand.randint(1,2)
        if digit == 1: #extra time
            gg.slow_print('\nYou still have some time in the day!',0.04)
            options = ['do homework','study','hangout with friends']
            gg.print_list(options)
            what = gg.slow_input("What are you trying to do before the day is over? ",0.04)
            what = gg.check_number_answer(what,options)
            if what == '0':
                gg.endgame()
            elif what == '1':
                cp.do_hw(self)
            elif what == '2':
                cp.study(self)
            else:
                cp.hangout_night(self)
        else: #no extra time
            gg.slow_print('\nYou decide that its best to sleep, since your bed is calling your name.',0.04)

    def find_classes(self): #find classes, but buildings are locked
        gg.slow_print('\nLets go and find where your classes will be!',0.04)
        gg.slow_print('You get to your first building and open the door.',0.04)
        gg.slow_print("The door doesn't open.",0.04)
        gg.slow_print("You try other buildings and no door will open.",0.04)
        gg.slow_print('Looks like the buildings are closed today.',0.04)
        gg.slow_print('You just wasted your time. Unlucky.',0.04)
        self.happiness += rand.randint(-40,0)

    def go_class(self): #player goes to class
        gg.slow_print("\nToday wasn't too bad!",0.04)
        sayings = ["You almost fell asleep in that one class though!",
                   "You should've payed more attention in class!",
                   "The lectures were actually interesting!",
                   "Your professor made the best dad joke you have ever heard of!",
                   "You got let out early today!"]
        gg.slow_print(rand.choice(sayings),0.04)

        self.gpa = cp.calc_gpa(self,rand.uniform(0,0.25))
        self.health += rand.randint(-35,0)
        self.happiness += rand.randint(-30,20)

    def gym(self): #player goes to the gym 
        gg.slow_print('ITS TIME TO GET ACTIVE!',0.04)
        
        activities = ['Lift','Basketball','Swim','Volleyball']
        gg.print_list(activities)
        activity = gg.slow_input('What would you like to do? ',0.04)

        if activity == '0':
            gg.endgame()
        if activity == '1': #weight room 
            gg.slow_print("\nYou head to the weight room.",0.04)
            gg.slow_print('There are so many machines to chose from!',0.04)
            
            factor = rand.randint(-40,40)
            if factor < 0: #bad day
                negatives = ['You pulled a muscle on the stair master!',
                             'You dropped a dumbell on your toe!',
                             'You realize that working out is not for you.',]
                gg.slow_print(f'\n{rand.choice(negatives)}',0.04)
                self.health += factor
                self.happiness += factor
            elif factor > 0: #good day
                positives = ["You've met your match! You gotta be consistent, so that you have bragging rights!",
                             "You set so many personal records.",
                             "The pump felt amazing!"]
                gg.slow_print(f'\n{rand.choice(positives)}',0.04)
                self.health += rand.randint(-20,0)
                self.happiness += factor
            else:
                gg.slow_print('\nLifting was meh.',0.04)

            if self.health <= 0: #potential death
                gg.slow_print('\nThere was a freak accident!',0.04)
                gg.slow_print('Someone dropped a 45 pound weight on your head!',0.04)
                gg.slow_print('You died.',0.04)
                gg.endgame()           
        if activity == '2': #Basketball
            gg.slow_print('\nYou find the basketball courts',0.04)
            gg.slow_print('Wow there are a lot of people!',0.04)
            gg.slow_print('You see a group of 4 you can join!',0.04)
            gg.slow_print('You go up to them and ask if you can play.',0.04)
            gg.slow_print('They said yes!',0.04)
            gg.slow_print('Now you gotta wait until the current game finishes.',0.04)

            factor = rand.randint(-40,40)
            if factor < 0: #bad senario
                negatives = ['The other players were jerks.',
                            "You didn't make a single shot.",
                            'You rolled your ankle.']
                gg.slow_print(f'\n{rand.choice(negatives)}',0.04)
                self.health += factor
                self.happiness += factor 
            elif factor > 0: #good senario
                positives = ["You didn't miss a single shot!",
                            'You made the game winning shot!',
                            'You won a game of Knock Out!']
                gg.slow_print(f'\n{rand.choice(positives)}',0.04)
                self.health += rand.randint(-20,0)
                self.happiness += factor   
            else: 
                gg.slow_print('\nPlaying basketball was meh.',0.04)
            if self.health <= 0: #potential death
                gg.slow_print('\nThere was a freak accident!',0.04)
                gg.slow_print('The basketball hoop fell on you!',0.04)
                gg.slow_print('You died.',0.04)
                gg.endgame()
        if activity == '3': #Swimming
            gg.slow_print('\nYou put your stuff away in the locker room.',0.04)
            gg.slow_print('You gotta hurry that water is calling your name!',0.04)
            
            choice = ['indoor','outdoor']
            gg.print_list(choice)
            where = gg.slow_input('Which pool do you want to go to? ',0.04)
            where = gg.check_number_answer(where,choice)

            if where == '1': #indoor
                gg.slow_print('\nYou see the indoor pool is huge, but students are only allowed to use one section of it.',0.04)
                factor = rand.randint(0,30)
                if factor > 0: #good swim
                    positives = ["You swam 1600 meters!",
                                "Swimming was so theraputic!",
                                "You were the last one standing in sharks and minows!"]
                    gg.slow_print(f'\n{rand.choice(positives)}',0.04)
                    self.health += rand.randint(-20,0)
                    self.happiness += factor
                else: #neutral
                    gg.slow_print('\nJust a normal day at the pool.',0.04)
                    self.health += rand.randint(-25,0)
                    self.happiness += factor  
            else: #outdoor
                gg.slow_print('\nThe outdoor pool is so small!',0.04)
                gg.slow_print('There are way too many people.',0.04)

                factor = rand.randint(-30,0)
                if factor < 0: #bad swim
                    negatives = ['Someone pooped in the pool!',
                                 'You suck at Marco Polo!']
                    gg.slow_print(f'\n{rand.choice(negatives)}',0.04)
                    self.health += rand.randint(-35,0)
                    self.happiness += factor
                else: #netural
                    gg.slow_print('\nNothing exciting happened at the pool.',0.04)
                    self.health += rand.randint(-20,0)
                    self.happiness += factor
             
            if self.health == 0: #potential death
                gg.slow_print('\nYou got cramps in your legs and arms.',0.04)
                gg.slow_print('The life gaurds did not notice you struggling',0.04)
                gg.slow_print('You drowned.',0.04)
                gg.endgame()     
        else: #volleyball
            gg.slow_print('\nYou head to the volleyball courts.',0.04)
            gg.slow_print('You see that there is a team of 5 and ask to join them.',0.04)
            gg.slow_print('They said yes!',0.04)
            gg.slow_print('Perfect timing too! They are about to play against another team.',0.04)

            factor = rand.randint(-30,30)

            if factor < 0: #bad day
                negatives = ['The other players were jerks.',
                             "All your serves went out of bounds.",
                             'You rolled your ankle.']
                gg.slow_print(f'\n{rand.choice(negatives)}',0.04)
                self.health += rand.randint(-30,0)
                self.happiness += factor  
            elif factor > 0: #good day
                positives = ["You didn't miss a single serve!",
                             'You made the game winning serve! NiCE ACE!',
                             'You won the match!']
                gg.slow_print(f'\n{rand.choice(positives)}',0.04)
                self.health += rand.randint(-20,0)
                self.happiness += factor
            else:
                gg.slow_print('\nNothing crazy happened at volleyball.',0.04)

            if self.health == 0: #potential death
                gg.slow_print('\nYou had a heart attack mid game!',0.04)
                gg.slow_print('Paramedics were not able to save you.',0.04)
                gg.slow_print('You died.',0.04)
                gg.endgame()

    def hangout_day(self): #senario for when the player chooses to hangout during the day
        gg.slow_print("\nYou meet with your friends later in the day.",0.04) 
        options = ['play board games','play soccer','go on a hike','do a puzzle'] #options
        gg.print_list(options) #calls print_list function
        what = gg.slow_input('What all of you do? ',0.04) #user input
        what = gg.check_number_answer(what,options) #calls check_number_answer function

        if what == '0':
            gg.endgame() #calls endgame function
        elif what == '1': #board game 
            gg.slow_print('Board games are so much fun!',0.04)
            factor = rand.randint(-20,20) #random number that will determine the following
            if factor < 0: #unlucky board games
                negatives = ['You went bankrupt in Monopoly!',
                            'You ended up drawing 60 cards in uno and lost!',
                            'You guess the wrong person, weapon, and place in Clue.',
                            'You got bored of the board game and gave up.'] #negative responses
                gg.slow_print(f"\n{rand.choice(negatives)}",0.04) #prints a random negative response
                self.happiness += factor #happiness changes by the factor
                self.health += rand.randint(-30,0) #health changes by a random number (negative since negative effect)
                self.gpa = cp.calc_gpa(self,rand.uniform(-0.35,0)) #calls the calc_gpa function
            elif factor > 0: #lucky board games 
                positives = ["You're a billionaire in Monopoly!",
                            'You guessed the right person, weapon, and place in Clue!',
                            'You won every UNO game!'] #positive responses
                gg.slow_print(f"\n{rand.choice(positives)}",0.04) #print a random positive response
                self.happiness += factor #happiness changes by the factor
                self.health += rand.randint(-20,0) #health changes by a random number (negative because board games don't make people healthier)
                self.gpa = cp.calc_gpa(self,rand.uniform(-0.25,0)) #calls the calc_gpa function
            else: #neutral
                gg.slow_print('\nNothing extraodinary happened when you played.',0.04)
        elif what == '2': #soccer
            gg.slow_print('SOCCER!!!!!!',0.04)
            gg.slow_print("THE GREATEST SPORT IN THE WORLD!!!!",0.04)
            gg.slow_print("You and your friends head to the soccer fields.",0.04)
            factor = rand.randint(-30,30) #random number that will determine the following
            if factor < 0: #bad soccer day 
                negatives = ['You rolled your ankle playing!',
                            "You didn't score a single goal!",
                            "You hit someone in the head, they are now concussed!",
                            'You stepped on someones foot and broke it!'] #negative responses
                gg.slow_print(f"\n{rand.choice(negatives)}",0.04) #print a negative response
                self.happiness += factor #happiness changes by the factor
                self.health += factor #health changes by the factor
                self.gpa = cp.calc_gpa(self,rand.uniform(-0.30,0)) #calls calc_gpa function
            elif factor > 0: #good soccer day
                positives = ["You didn't miss a single shot!",
                            "Your team was unstoppable!",
                            "You managed to do a rainbow flick during a game!"] #positive responses 
                gg.slow_print(f"\n{rand.choice(positives)}",0.04) #print a random positive response
                self.happiness += factor #happiness changes by the factor
                self.health += rand.randint(-15,0) #health won't decrease too much in positive, but will still decrease
                self.gpa = cp.calc_gpa(self,rand.uniform(-0.20,0)) #calls calc_gpa function
            else: 
                gg.slow_print('\nNothing extraodinary happened when you played.',0.04) #neutral response
        elif what == '3': #hike
            gg.slow_print('You go to a near by trail and hike it!',0.04)
            factor = rand.randint(-30,30) #random number that will determine the following
            if factor < 0: #bad hikes
                negatives = ["You go swarmed by bugs!",
                            "You fell and rolled down the trail! OUCH!",
                            'You tried to climb a tree and fell!',
                            'The trail was so boring!',
                            "You stepped in deer poop!"] #bad responses
                gg.slow_print(f"\n{rand.choice(negatives)}",0.04) #print a random bad response
                self.happiness += factor #stat change by the factor
                self.health += factor #stat change by the factor
                self.gpa = cp.calc_gpa(self,rand.uniform(-0.30,0)) #calls calc_gpa function
            if factor > 0: #good hikes
                positives = ["You saw a fox, coyote, and a bear! Your luck is crazy!",
                            "You got to the top and the view was amazing!",
                            'You won the tree climbimg competition!',
                            'You found a hidden lake!'] #good responses
                gg.slow_print(f"\n{rand.choice(positives)}",0.04) #print a random good response
                self.happiness += factor #stat changes by the factor
                self.health += rand.randint(-17,0) #stat changes by a random number
                self.gpa = cp.calc_gpa(self,rand.uniform(-0.20,0)) #calls calc_gpa function
            else: 
                gg.slow_print('\nNothing extraodinary happened when you went hiking.',0.04) #neutral response
        else: #puzzle
            gg.slow_print('It took you all day to finish that puzzle!',0.04)
            gg.slow_print("That must've been one challenging puzzle!",0.04)
            self.happiness += rand.randint(-20,10) #stat change
            self.gpa = cp.calc_gpa(self,rand.uniform(-0.20,0)) #calls calc_gpa function
            self.health = rand.randint(-27,0) #stat change 

    def hangout_night(self): #hanout during the evening/night 
        options = ['play board games','play soccer','go out to eat','go to the movies'] #options
        gg.print_list(options) #calls print_list function
        what = gg.slow_input('What will you and your friends do? ',0.04) #user input
        what = gg.check_number_answer(what,options) #calls check_number_answer function

        if what == '0':
            gg.endgame() #calls endgame function
        elif what == '1': #board game 
            gg.slow_print('\nBoard games are so much fun!',0.04)
            factor = rand.randint(-20,20) #random number that will determine the following
            if factor < 0: #unlucky board games
                negatives = ['You went bankrupt in Monopoly!',
                            'You ended up drawing 60 cards in uno and lost!',
                            'You guess the wrong person, weapon, and place in Clue.',
                            'You got bored of the board game and gave up.'] #negative responses
                gg.slow_print(f"\n{rand.choice(negatives)}",0.04) #prints a random negative response
                self.happiness += factor #happiness changes by the factor
                self.health += rand.randint(-30,0) #health changes by a random number (negative since negative effect)
            elif factor > 0: #lucky board games 
                positives = ["You're a billionaire in Monopoly!",
                            'You guessed the right person, weapon, and place in Clue!',
                            'You won every UNO game!'] #positive responses
                gg.slow_print(f"\n{rand.choice(positives)}",0.04) #print a random positive response
                self.happiness += factor #happiness changes by the factor
                self.health += rand.randint(-20,0) #health changes by a random number (negative because board games don't make people healthier)
            else: 
                gg.slow_print('\nNothing extraodinary happened when you played.',0.04) #neutral response
        elif what == '2': #soccer
            gg.slow_print('\nSOCCER!!!!!!',0.04)
            gg.slow_print("THE GREATEST SPORT IN THE WORLD!!!!",0.04)

            factor = rand.randint(-30,30) #random number that will determine the following

            if factor < 0: #bad soccer day 
                negatives = ['You rolled your ankle playing!',
                            "You didn't score a single goal!",
                            "You hit someone in the head, they are now concussed!",
                            'You stepped on someones foot and broke it!'] #negative responses
                gg.slow_print(f"\n{rand.choice(negatives)}",0.04) #print a negative response
                self.happiness += factor #happiness changes by the factor
                self.health += factor #health changes by the factor
                self.gpa = cp.calc_gpa(self,rand.uniform(-0.30,0)) #calls calc_gpa function
            elif factor > 0: #good soccer day
                positives = ["You didn't miss a single shot!",
                            "Your team was unstoppable!",
                            "You managed to do a rainbow flick during a game!"] #positive responses 
                gg.slow_print(f"\n{rand.choice(positives)}",0.04) #print a random positive response
                self.happiness += factor #happiness changes by the factor
                self.health += rand.randint(-15,0) #health won't decrease too much in positive, but will still decrease
                self.gpa = cp.calc_gpa(self,rand.uniform(-0.20,0)) #calls calc_gpa function
            else: 
                gg.slow_print('\nNothing extraodinary happened when you played.',0.04) #neutral response
        elif what == '3': #eat out
            gg.slow_print('\nYou plan to go somewhere to eat with your friends!',0.04)
            price = rand.randint(0,30) #price of meal 
            if self.money >= price: #player has enough money
                gg.slow_print(f'You have ${self.money}.',0.04)
                gg.slow_print(f'It will cost ${price} to eat out tonight.',0.04)
                yes = gg.slow_input(f'Would you like to spend ${price} for the meal? ',0.04)
                gg.check_yes_no(yes)
                if yes == 'y':
                    gg.slow_print('\nYou go out to eat!',0.04)
                    factor = rand.randint(-30,30) #random number that will determine the following
                    if factor < 0: #bad food
                        negatives = ['You think you got a stomach bug!',
                                    'The food quality was terrible!',
                                    'You found a bandaid in your sandwhich!',
                                    'The food was over priced for what you got!'] #bad responses
                        gg.slow_print(f"\n{rand.choice(negatives)}",0.04) #print a random bad response
                        self.happiness += factor #stat change by the factor
                        self.health += factor #stat change by the factor
                    if factor > 0: #good food
                        positives = ['You ate so much good food!',
                                     'You liked the food!',
                                     'Best resturant ever!',
                                     'The food was worth the price!'] #good responses
                        gg.slow_print(f"\n{rand.choice(positives)}",0.04) #print a random good response
                        self.happiness += factor #stat changes by the factor
                        self.health += rand.randint(-17,0) #stat changes by a random number
                    else: 
                        gg.slow_print('\nThe food was average.',0.04) #neutral response
                    self.money -= price
                else: 
                    gg.slow_print('\nYou decided not to go out and eat.',0.04)
                    gg.slow_print('You go to the dining hall instead',0.04)
            else: #not enough money
                gg.slow_print("\nYou can't afford to go out and eat!",0.04)
                self.happiness += rand.randint(-30,0) #stat change by the factor     
        else: #movies
            gg.slow_print('\nYou want to go to the movies!')
            price = rand.randint(0,30) #price of meal 
            if self.money >= price: #player has enough money
                gg.slow_print(f'You have ${self.money}.',0.04)
                gg.slow_print(f'It will cost ${price} to go to the movies.',0.04)
                yes = gg.slow_input(f'Would you like to spend {price}? ',0.04)
                yes = gg.check_yes_no(yes)
                if yes == 'y':
                    movies = ['Barbie','Oppenheimer','Toy Story','Shrek','Kung Fu Panda','Minions','Minions 2',
                              'Minions 3', 'Maze Runner', 'A Silent Voice', 'Your Name', "Mid 90's",'Good Burger'] #list of movies
                    random_movies = rand.sample(movies,5) #randomly choose 5 movies from the list
                    gg.print_list(random_movies) #calls print list function
                    choice = gg.slow_input('What movie would you like to see? ',0.04) #user gg.slow_input
                    choice = gg.check_number_answer(choice) #calls check_number_answer function
                    if choice == '0':
                        gg.endgame() #calls endgame function
                    else:
                        gg.slow_print(f'You went to see {random_movies[int(choice)-1]}!',0.04)
                        factor = rand.randint(-30,30)
                        if factor < 0: #bad movie
                            negatives = ['The movie was boring.',"The movie wasn't worth the money.",'The movie was so bad!',
                                         'Someone threw up on you at the theater!'] #bad responses
                            gg.slow_print(f"\n{rand.choice(negatives)}",0.04) #print a random good response
                            self.happiness += factor #stat changes by the factor
                            self.health += rand.randint(-17,0) #stat changes by a random number
                        elif factor > 0: #good movie
                            positives = ['The movie was amazing!','The movie was worth the money!','You loved the sound track!',
                                         'The story was really good!','You liked the way it ended!'] #good responses
                            gg.slow_print(f"\n{rand.choice(positives)}",0.04) #print a random good response
                            self.happiness += factor #stat changes by the factor
                            self.health += rand.randint(-17,0) #stat changes by a random number
                        else:
                            gg.slow_print('\nThe movie was meh.',0.04)
                        self.money -= price
                else: 
                    gg.slow_print("\nYou decide not to go to the movies.",0.04)
                    gg.slow_print("Instead you decide to stay in and play videogames.",0.04)
                    cp.video_games(self)
                    
    def instant_win(self): #condition for an instant win
        if self.health < -1000 and self.happiness > 1000:
            gg.slow_print('You party like its never gonna end',0.04)
            gg.slow_print('You are extermely happy to be alive.',0.04)
            gg.slow_print('except',0.04)
            gg.slow_print('You kinda died already.',0.04)
            gg.slow_print('Like 1000 years ago.',0.04)
            gg.slow_print('Did I forget to mention?',0.04)
            gg.slow_print('This is just a simulation',0.04)
            gg.slow_print("or",0.04)
            gg.slow_print('Are you living in the simulation?',0.04)
            gg.slow_print('Just kidding!',0.04)
            gg.slow_print('YOU WON THE GAME!!!',0.04)
            gg.endgame()

    def library(self): #player goes to the library
        book = gg.slow_input('\nIs there a book you geek about? ',0.04)
        gg.check_yes_no(book)

        if book == 'y': #player loves a book
            what = gg.slow_input("What is the book's name? ",0.04)
            choices = [f"I've read {what} too! It's a good read.",
                       f"I've never heard of {what}!",
                       f"I might have to give {what} a read!"]
            gg.slow_print(f'\n{rand.choice(choices)}',0.04)
        else: #doesn't like a book
            gg.slow_print("\nStill haven't found one yet?",0.04)
            gg.slow_print("I get it there so many books to be read.",0.04)
            
        factor = rand.randint(-30,30)
        if factor < 0:
            negatives = ["The library only have textbooks and databases!",
                        "The library hasn't opened yet!",
                        "There was no one at the library!"]
            gg.slow_print(f'\n{rand.choice(negatives)}',0.04)
        elif factor > 0:
            positives = ['You met someone that has the same favorite author!',
                        'There were so many books to chose from!',
                        'You found a great spot to do work in the library!']
            gg.slow_print(f'\n{rand.choice(positives)}',0.04)
        else: 
            gg.slow_print('\nNothing happened when you went.',0.04)
            
        self.happiness += factor

    def living_spot(self): #choses # of roomates and affects happiness
        dorm_choices = ['single','double','triple','quad']
        choice = rand.choice(dorm_choices)

        if choice == 'single':
            increase = [-10, -5, 5, 10]
            factor = rand.choice(increase)
            self.happiness += factor   
        elif choice == 'double':
            self.happiness += 20
        else:
            self.happiness -= 45 
        return choice

    def lounge(self): #player goes to the lounge 
        gg.slow_print('\nYou go to the lounge.',0.04)
        senario = rand.randint(1,2)
            
        if senario == 1: #no one in the lounge, prompts user to go somewhere else
            gg.slow_print('\nNo one was there!',0.04)
            gg.slow_print('You go back to your room.',0.04)
            gg.slow_print('\nLets go somewhere else!',0.04)
            self.happiness += rand.randint(-25,0)

            option = ['Dining Hall','Library','Gym']
            gg.print_list(option)

            place = gg.slow_input('\nWhere would you like to go? ',0.04)
            place = gg.check_number_answer(place,option)
            if place =='0':
                gg.endgame()
            elif place == '1':
                cp.dininghall(self)
            elif place == '2':
                cp.library(self)
            else:
                cp.gym(self)
        else: #people are there, end up liking or disliking them
            gg.slow_print('\nYou see a few people from your floor.',0.04)
            choices = ['You actually like your floor mates!',
                       'You are not vibing with your floor mates.']
            which = rand.choice(choices)
            if which == 'You actually like your floor mates!':
                gg.slow_print(which)
                gg.slow_print('You get to know them and exchange numbers!',0.04)
                factor = rand.randint(0,15)
                self.happiness += factor
            else:
                gg.slow_print(which)
                gg.slow_print("You leave the lounge and go back to your room.",0.04)
                factor = rand.randint(-30,0)
                self.happiness += factor  

    def next_day(self): #calls mutiple functions
        cp.sleep(self)
        cp.update_stats(self)
        cp.display_college_info(self)

    def no_labor_day(self): #stats change if player gets labor day off
        self.happiness += -65

    def read_book(self): #player choses to read a book
        factor = rand.randint(0,2)
        if factor == '0': #finish book
            gg.slow_print('\nYou finished the book you have been reading!',0.04)
            self.happiness += rand.randint(0,20)
            self.health += rand.randint(-15,0) 
        if factor == '1': #few pages
            gg.slow_print('\nYou only read a few pages before you got distracted.',0.04)
            self.happiness += rand.randint(-30,10)
            self.health += rand.randint(-25,0)
        else: #1/2 of the book read
            gg.slow_print('\nYou got half way done with your book!',0.04)
            self.happiness += rand.randint(0,10)
            self.health += rand.randint(-20,0)

    def relax(self): #player chooses to relax
        self.happiness += rand.randint(0,25)
        self.health += rand.randint(0,25)
        self.gpa = cp.calc_gpa(self,rand.uniform(-0.15,0))

    def skip(self): #player skips classes
        digit = rand.randint(1,2)
        if digit == '1':
            gg.slow_print('\nSkipping classes is one of the benefits to college!',0.04)
        else:
            gg.slow_print("\nYou know you are paying to go to this school right?",0.04)
        gg.slow_print("You better make the most of your day!",0.04)

        options = ["hang out with friends","do homework & study","take a nap","play video games"]
        gg.print_list(options)
        choice = gg.slow_input("What are your plans for today? ",0.04)
        choice = gg.check_number_answer(choice, options)

        if choice == '0':
            gg.endgame()
        elif choice == '1':
            cp.hangout_day(self)
        elif choice == '2':
            cp.do_hw(self)
            cp.study(self)
        elif choice == '3':
            cp.take_nap(self)
        else:
            cp.video_games(self)

    def skip_class(self): #skipping class alters player stats
        self.happiness += rand.randint(10,30)
        self.gpa = cp.calc_gpa(self,rand.uniform(-0.45,0))

    def skip_week(self): #skip week
        self.happiness += rand.randint(-40,40)

    def sleep(self): #player sleeps (next day)
        self.happiness += rand.randint(-15,20)
        self.health += rand.randint(-5,30)
     
    def socialize(self): #player choses to socialize @ different locations
        gg.slow_print('\nHere are your options.',0.04)
        choice = ['Dining Hall','Library','Lounge','Gym']
        gg.print_list(choice)

        place = gg.slow_input('\nWhere would you like to go? ',0.04)
        place = gg.check_number_answer(place,choice)
        if place == '0':
            gg.endgame()
        elif place == '1':
            cp.dininghall(self)
        elif place == '2':
            cp.library(self)
        elif place == '3':
            cp.lounge(self)
        else:
            cp.gym(self)

    def study(self): #player studies 
        digit = rand.randint(1,3)
        if digit == 1: #good study
            gg.slow_print("\nWhat a great study sesh!",0.04)
            self.gpa = cp.calc_gpa(self,rand.uniform(0,0.45))
            self.happiness += rand.randint(0,45)
            self.health += rand.randint(-15,0)
        elif digit == 2: #bad study
            gg.slow_print("\nThe study shesh was unproductive",0.04)
            choice = ['You were too busy playing Clash of Clans.',
                      'You could not concentrate at all!',
                      'Your study buddies were distracting!',
                      'You got bored of studying!']
            gg.slow_print(rand.choice(choice),0.04)
            self.gpa = cp.calc_gpa(self,rand.uniform(0,0.45))
            self.happiness += rand.randint(-45,0)
            self.health += rand.randint(-25,0)
        else: #less study time but can be good or bad
            gg.slow_print("\nYou studied for less than the time you intended to.",0.04)
            digit = rand.randint(1,2)
            if digit == 1:
                gg.slow_print('You were very productive!',0.04)
                self.gpa = cp.calc_gpa(self,rand.uniform(0,0.25))
                self.happiness += rand.randint(0,20)
                self.health += rand.randint(-25,0)
            else:
                gg.slow_print("You're thinking to yourself right now.",0.04)
                gg.slow_print("'I wish I studied more.'",0.04)
                self.gpa = cp.calc_gpa(self,rand.uniform(-0.25,0))
                self.happiness += rand.randint(-35,0)
                self.health += rand.randint(-25,0)

    def take_exam(self): #player takes exam
        self.gpa = cp.calc_gpa(self,rand.uniform(-0.05,0.35))
        self.happiness += rand.randint(-30,15)
        self.health += rand.randint(-25,10)

    def take_final(self): #player takes final exam
        luck = rand.randint(1,4)
        if luck <= 3:
            gg.slow_print("Your finals today went well!",0.04)
            self.gpa = cp.calc_gpa(rand.uniform(0,0.55))
            self.happiness += rand.randint(0,40)
        else:
            gg.slow_print("Your finals didn't go so well!",0.04)
            self.gpa = cp.calc_gpa(self,rand.uniform(-0.25,0))
            self.happiness += rand.randint(-30,0)
            
    def take_nap(self): #player takes a nap for x amount of hours
        hours = rand.randint(1,10)
        gg.slow_print(f'\nYou ended up sleeping for {hours} hours!',0.04)
        self.health += rand.randint(0,25)
        self.gpa = cp.calc_gpa(self,rand.uniform(-0.05,0))

    def talk(self): #player talks to friend/stranger at the bar
        bnames = ['Joe','Kevin','Edwin','Connor','Steven','Vincent','Danny','Jacob','Ricky','Marvin','Julian','Lukas']
        gnames = ['Carly','Cat','Kaylin','Maddie','Arianna']
        gfeeling = ['amazing','fantastic','radcial','awesome','energentic']
    
        luck = rand.randint(1,2)
        if luck == 1: #talk to man
            pick_name = rand.choice(bnames)
            gg.slow_print(f'\nYou talk to {pick_name}!',0.04)
            luck = rand.randint(1,2)
            if luck == 1:
                gg.slow_print(f'He seems to be feeling {gfeeling}!',0.04)
                gg.slow_print(f'Seem like she is enjoying the bars.',0.04)
            else:
                gg.slow_print(f"Seems like he is not enjoying the bars.",0.04)
                gg.slow_print("He looks like he wants to leave.",0.04)
        else: #talk to woman
            pick_name = rand.choice(gnames)
            gg.slow_print(f'\nYou talk to {pick_name}!',0.04)
            luck = rand.randint(1,2)
            if luck == 1:
                gg.slow_print(f'She seems to be feeling {gfeeling}!',0.04)
                gg.slow_print(f'Seem like she is enjoying the bars.',0.04)
            else:
                gg.slow_print(f"Seems like she is not enjoying the bars.",0.04)
                gg.slow_print("She looks like she wants to leave.",0.04)
        
        gg.slow_print('\nYou have 0 conversational skills.',0.04)
        gg.slow_print('You gotta work on that for next time!',0.04)

    def unpack(self): #player unpacks
        gg.slow_print('\nYou start to unpack your things.',0.04)
        factor = rand.randint(-30,30)
        negatives = ['You found bugs under your bed!',
                     'You have a mold problem!',
                     'Your a/c does not work!',
                     'You hung up a poster, but accidentally ripped it!'] 
        postives = ['You have a big room!',
                    'Your room has no bugs in it!',
                    'Your a/c works!',
                    "YOUR ROOM LOOKS DOPE AS FUCK!!!!!"]
        neutral = ['Room set up complete!']
        if factor < 0:
            gg.slow_print(f'{rand.choice(negatives)}',0.04)
        elif factor > 0:
            gg.slow_print(f'{rand.choice(postives)}',0.04)
        else: 
            gg.slow_print(f'{rand.choice(neutral)}',0.04)
        self.happiness += factor

    def update_stats(self): #updates stats so that they don't go over certain number
        self.health = max(0, min(self.health, 100)) #makes sure that lowest is 0 and the max is 100
        self.happiness = max(0, min(self.happiness, 100))
        self.gpa = max(0, min(self.gpa, 4.0))

        self.health = min(self.health, 100)
        self.happiness = min(self.happiness, 100)
        self.gpa = min(self.gpa, 4.0)

        self.money = max(0, self.money) #money can't be negative

    def walk(self): #player choses to walk
        gg.slow_print('\nYou go on a walk!',0.04)
        gg.slow_print("Can't forget your heaphones! They are essential to every walk!",0.04)
        luck = rand.randint(1,2)
        if luck == 1:
            a = ['\nThe music and fresh air is just so perfect!','You saw a bunch of your friends!','You explored all of campus and made a map!','You saw the campus fox!']
            self.happiness += rand.randint(0,20)
            self.health += rand.randint(0,10)
            gg.slow_print(rand.choice(a),0.04)
        else:
            a = ['\nPeople were bothering you on your walk.','\nA bird pooped on you!','\nYou tripped on air!','\nYou were so bored on your walk!']
            self.happiness += rand.randint(-30,0)
            self.health += rand.randint(-30,0)
            gg.slow_print(rand.choice(a),0.04)

    def website_friend(self,floor,general): #player gets ticket off a friend
        if self.money >= floor or self.money >= general:
            gg.slow_print('\nYou decide to buy your tickets off a friend!',0.04)
            luck = rand.randint(1,3)
            if luck == 1:
                new_floor = rand.randint(0,floor-15)
                new_general = rand.randint(0,general-15)
                gg.slow_print('Your friend cut you a deal!',0.04)
                gg.slow_print(f'Instead of paying ${floor} for floor tickets or ${general} for general tickets.',0.04) 
                gg.slow_print(f'He said ${new_floor} for floor tickets and ${new_general} for general tickets!',0.04)

                purchase = [f'floor ticket: ${new_floor}', f'general tickets: ${new_general}']
                gg.print_list(purchase)
                which = gg.slow_input('Which ticket would you like to buy? ',0.04)
                which = gg.check_number_answer(which,purchase)
                if which == '0':
                    gg.endgame()
                elif which == '1':
                    gg.slow_print(f'You bought the floor ticket for ${new_floor}!',0.04)
                    self.money -= new_floor
                else:
                    gg.slow_print(f'You bought the general ticket for ${new_general}!',0.04)
                    self.money -= new_general

            else: 
                gg.slow_print(f'The price is ${floor} for floor tickets and ${general} for general tickets!',0.04)
             
                purchase = [f'floor ticket: ${floor}', f'general tickets: ${general}']
                gg.print_list(purchase)
                which = gg.slow_input('Which ticket would you like to buy? ',0.04)
                which = gg.check_number_answer(which,purchase)
                if which == '0':
                    gg.endgame()
                elif which == '1':
                    gg.slow_print(f'You bought the floor ticket for ${floor}!',0.04)
                    self.money -= floor
                else:
                    gg.slow_print(f'You bought the general ticket for ${general}!',0.04)
                    self.money -= general
        else:
            gg.slow_print("You can't afford the ticket that you want.",0.04)
    
    def website_reliable(self,floor,general): #player get tickets off a reliable webiste
        if self.money >= floor or self.money >= general:
            gg.slow_print('\nYou search for ticketmaster.com.',0.04)
            gg.slow_print(f'The ticket prices are ${floor} for the floor tickets and ${general} for the general tickets.',0.04)

            purchase = [f'floor ticket: ${floor}', f'general tickets: ${general}']
            gg.print_list(purchase)
            which = gg.slow_input('Which ticket would you like to buy? ',0.04)
            which = gg.check_number_answer(which,purchase)

            if which == '0':
                gg.endgame()
            elif which == '1': #floor ticket
                lucky = rand.randint(1,10)
                if lucky <= 2: #20% chance to get a glitch in the system
                    gg.slow_print("You try to buy the floor ticket.",0.04)
                    gg.slow_print('There was a glitch in the system.',0.04)
                    gg.slow_print('You lost your money and were unable to buy the ticket!',0.04)
                    cp.website_try_again(self,floor,general)
                    self.happiness += rand.randint(-35,0)
                else: #no glitch in the system
                    gg.slow_print('You bought the floor ticket!\n',0.04)
                self.money -= floor

            else: #general ticket
                lucky = rand.randint(1,10)
                if lucky <= 2: #20% chance to get a glitch in the system
                    gg.slow_print("You try to buy the general ticket.",0.04)
                    gg.slow_print('There was a glitch in the system.',0.04)
                    gg.slow_print('You lost your money and were unable to buy the ticket!',0.04)
                    cp.website_try_again(self,floor,general)
                else: #no glitch in the system
                    gg.slow_print('You bought the general ticket!',0.04)
                self.money -= general
        else:
            gg.slow_print("You don't have enough money to buy any ticket.",0.04)

    def website_scam(self,floor,general): #player gets ticket off of a sketchy website
        if self.money >= floor or self.money >= general:
            gg.slow_print('\nYou search for a sketchy website hoping to get some cheap/free tickets.',0.04)
        else: #no money
            gg.slow_print("You don't have enough money to buy a ticket.",0.04)
        
        price = rand.randint(0,25)
        gg.slow_print(f'You managed to find a website that sells floor tickets for ${price}!',0.04)
        luck = 2 #rand.randint(1,2)
        if luck == 1: #scam website worked
            gg.slow_print('You put your credit card information in!',0.04)
            gg.slow_print('It actually worked! You got the ticket!!\n',0.04)
            self.happiness += rand.randint(0,75)
            self.health += rand.randint(-10,0)
            self.money -= price
        else: #you got scammed
            gg.slow_print('You put your credit card information in!',0.04)
            gg.slow_print('IT WAS A SCAM!!!',0.04)
            self.happiness += rand.randint(-75,0)
            self.health += rand.randint(-20,0)
            self.money -= price
            cp.website_try_again(self,floor,general)

    def website_try_again(self,floor,general): #player tries again after getting scammed
        if self.money >= floor or self.money >= general:
            go = gg.slow_input('\nDo you still want to go to the concert? ',0.04)
            go = gg.check_yes_no(go)
            if go == 'y':
                get_ticket = ['through a reliable website?','off a friend?']
                gg.print_list(get_ticket)
                how = gg.slow_input('How are you going to buy the tickets? ',0.04)
                how = gg.check_number_answer(how,get_ticket)
                if how == '0':
                    gg.endgame()
                elif how == '1':
                    cp.website_reliable(self,floor,general)
                else:
                    cp.website_friend(self,floor,general)
            else:
                gg.slow_print("Since you lost money, you're not in the mood to go anymore.",0.04)
                gg.slow_print('Your day is ruined!',0.04)
                self.happiness += rand.randint(-55,0)
                self.health += rand.randint(-35,0)
        else:
            gg.slow_print("Since you got scammed, you can't afford a ticket now.",0.04)

    def will_work(work): #player chooses where they will work if they want to work
        if work == 'y': #does work
            work_choices = ['Mcdonalds',
                            'Target',
                            'CVS',
                            'Library',
                            'Gym']
            gg.print_list(work_choices)

            place = gg.slow_input("\nWhere would you like to work? ",0.04)
            place = gg.check_number_answer(place,work_choices) 
            
            if place == '0':
                gg.endgame()
            elif place == '1' or place == '2' or place == '3':
                place = int(place)
                wages = [15,14,14]
                wage = wages[place - 1]
                gg.slow_print(f'You chose to work at {work_choices[place - 1]} for ${wage} per hour.',0.04)
            else:
                place = int(place)
                wages = [13,14]
                wage = wages[place - 4]
                gg.slow_print(f'You chose to work at the {work_choices[place - 1].lower()} for ${wage} per hour.',0.04)
            return wage
        else: #don't work
            gg.slow_print("\nLets hope you won't need a lot of money in the future",0.04)
            gg.slow_print('Hope you made the right decision!',0.04)
            return 0 #player says no to work then wage = 0 therefore money can't be made 

    def work(self,wage,hours): #player works and earns money
        hours = int(hours)
        if wage == 0: #player has no job, so see if they changed their mind
            gg.slow_print("\nYou chose not to work earlier in the semster dummy!",0.04)
            mind = gg.slow_input('Did you change your mind? ',0.04)
            mind = gg.check_yes_no(mind)
            if mind == 'y':
                work = gg.slow_input('\nWould you like to get a job? ',0.04)
                work = gg.check_yes_no(work)
                cp.will_work(work)
            else:
                gg.slow_print("\nGot it, you don't want to work.",0.04)
        else:
            while hours > 6: #too many hours
                gg.slow_print("\nYou are a college student! You're crazy for trying to work that much!",0.04)
                gg.slow_print('Lets be reasonable here.',0.04)
                hours = int(gg.slow_input('Enter a reasonable amount of hours (1-6): ',0.04))
        
            if hours == 6: #max hours 
                self.happiness += rand.randint(-40,10)
                self.health += rand.randint(-35,10)
                self.gpa = cp.calc_gpa(self,rand.uniform(-0.4,0))
            elif hours == 5:
                self.happiness += rand.randint(-20,10)
                self.health += rand.randint(-15,7)
                self.gpa = cp.calc_gpa(self,rand.uniform(-0.3,0))
            else: #other hours
                self.happiness += rand.randint(-10,10)
                self.health += rand.randint(-10,7)
                factor = rand.uniform(-0.2,0)
                self.gpa = cp.calc_gpa(self,factor)
        
            hours_worked = wage * hours 
            self.money += hours_worked
            gg.slow_print(f'You made ${hours_worked} today!',0.04)

    def video_games(self): #player chooses to play games
        games = ['Minecraft',
                'League of Legends',
                'Stardew Valley',
                'Apex Legend',
                'Clash Royale']
        gg.print_list(games)
        choice = gg.slow_input("So what game is it gonna be? ",0.04)
        choice = gg.check_number_answer(choice, games)

        hours = rand.randint(0,10)

        if choice == '0':
            gg.endgame()
        else:
            choice = int(choice)
            gg.slow_print(f'You ended up playing {games[choice-1]} for {hours} hours!',0.04)
            
            factor = rand.randint(-20,20)

            if factor < 0: #bad game day
                negatives = ["You were not on your game today!",
                             "You were thinking about how you could have used your time better today.",
                             "You didn't have any fun playing today."]
                gg.slow_print(f"{rand.choice(negatives)}",0.04)
                self.gpa = cp.calc_gpa(self,rand.uniform(-0.4,0))
                self.health += rand.randint(-30,0)
                self.happiness += rand.randint(-40,0)  
            elif factor > 0: #good game day
                positives = ['You were on fire today!',
                             'You needed this today day!',
                             f"You just can't get enough of {games[choice-1]}!"]
                gg.slow_print(f"{rand.choice(positives)}",0.04)
                self.gpa = cp.calc_gpa(self,rand.uniform(-0.2,0))
                self.health += rand.randint(-10,0)
                self.happiness += rand.randint(0,40)
            else: #meh game day
                gg.slow_print('The game felt dull today.',0.04)

class college_game: #how the game will be played (the days and weeks of the semester)
    def college_life(): #think of a diff name for this #college game play
        gg.slow_print('\nBefore we start.',0.03)
        name = gg.get_name() #will get players name
        player = cp(name=name) #create player with the players name  

        #applying to college (could have def but already done)(same for the rest)
        gg.slow_print(f"\nYou are planning on going to college and apply your top 2 schools.",0.02)
        college1 = gg.slow_input("What is your first choice? ",0.03)
        college2 = gg.slow_input("Your second choice? ",0.03)
        gg.slow_print(f"Your favorite colleges are {college1} and {college2}?",0.03)
        a = gg.slow_input('Is this correct? ',0.03)
        a = gg.check_yes_no(a)
        college1, college2 = gg.check_college_choice(a,college1,college2)
        
        #picking major
        gg.slow_print('\nWhat do you plan on studying?',0.03)

        major_choices = ['Art', 'Astronomy', 'Biology', 'Business', 'Engineering', 'History', 'Math', 'Physics','Undecided']
        gg.print_list(major_choices)
        major = gg.slow_input("What major would you like to study? ",0.04)
        major = gg.check_number_answer(major, major_choices) # major = '#'
        major = gg.doublecheck_answer(major,major_choices) # major = 'new#'

        if major == '0':
            gg.endgame()
        if major == '9':
            chosen_major = major_choices[8]
            gg.slow_print(f'You are {chosen_major}.',0.05)
        else:
            major = int(major)
            chosen_major = major_choices[major - 1]
            gg.slow_print(f"You want to be a(n) {chosen_major} major.",0.04)

        #transition
        gg.slow_print('\nYou fill out your applications and submit them.',0.03)
        gg.slow_print('\nFast forward a couple months.',0.03)
        gg.slow_print('The emails came back saying BOTH schools wanted you!',0.03)
        gg.slow_print('HOORAY!\n',0.04)

        #picking which college to go to 
        college_choices = [f"{college1}", f"{college2}"] #potentially have a 3rd if strucutre is the same and can tweak a little of the story 
        gg.print_list(college_choices)
        choice = gg.slow_input("Which college will you attend? ",0.03)
        choice = gg.check_number_answer(choice,college_choices)
        choice = gg.doublecheck_answer(choice,college_choices)
        
        if choice == '0': #end game
            gg.endgame()
        elif choice == '1': #college 1
            if chosen_major == 'Undecided':
                gg.slow_print(f'Congrats on getting accepted to {college1}, you are currently {chosen_major.lower}.',0.03)
            else:
                gg.slow_print(f'\nCongrats on getting accepted to {college1} as a(n) {chosen_major} major!',0.03)
        else: #college 2
            if chosen_major == 'Undecided':
                gg.slow_print(f'Congrats on getting accepted to {college2}, you are currently {chosen_major.lower}.',0.03)
            else:
                gg.slow_print(f'\nCongrats on getting accepted to {college2} as a(n) {chosen_major} major!',0.03)
            
            
        #shows initial stats,type of dorm room they get, number of classes they will take
        gg.slow_print(f'\nHere are somethings to note before you start your semester!',0.04)
        player.display_college_info()
        living_spot = player.living_spot()
        number_classes = rand.randint(4,6)
        gg.slow_print(f'\nYou will be living in a {living_spot} dorm room for the semester!',0.04)
        gg.slow_print('\nDuring the summer you managed to make your ideal schedule.',0.04)
        gg.slow_print(f'You will be taking {number_classes} classes this semester!',0.04)
        gg.slow_print('They are on Monday, Wednesday, and Friday. You got so lucky to have Tuesday and Wednesday off!',0.04)
        #show how much money they have to start
        gg.slow_print(f"\nYou currently have ${player.money} to your name.",0.04)       
        gg.slow_print("You're thinking about whether or not you should get a job.",0.04)
        #part time job
        work = gg.slow_input('\nWill you be getting a job this semester? ',0.04)
        work = gg.check_yes_no(work)
        wage = cp.will_work(work) #returns $ wage so that you can do math with it in the other functions 
        #begin the game here
        gg.slow_print('\nNow that we got the small details out the way, lets get you ready for your semester!',0.04)
        gg.slow_print("You're semester will be 7 weeks long!",0.04)
        gg.slow_print("Try to get through the semester without dying or failing the semester!",0.04)
            
        #go through 8ish weeks of college
        cg.syllabus_week(player) #player = cp(name=name), will keep updating the players stats
        cg.week2(player,wage) 
        cg.week3(player,wage)
        cg.week4(player,wage)
        cg.week5(player,wage) 
        cg.week6(player,wage)
        cg.finals_week(player,wage)

        player.update_stats()
        player.check_wol_conditions()
        
    def syllabus_week(player): #player = player stats, and classes = number of classes the student has
        #5 choices a week (classes will take up roughly two days)
        #if i make it so that they skip class might have to add more code and make the week a bit longer you'll get there soon

        gg.slow_print('\nSunday, August 28th, 8:00 am',0.05)
        gg.slow_print('Lets get you moved into your dorm room!',0.04)
        gg.slow_print('You get to you room and you are excited to start your campus life.',0.04)
        gg.slow_print('Since classes have not started yet, you have a lot of free time.',0.04)
        gg.slow_print('What are you going to do with it?',0.04)

        action1_choices = ['unpack', 'socialize','find classes']
        gg.print_list(action1_choices)
        action1 = gg.slow_input('Whats the first thing you would like to do, now that you are on campus? ',0.03)
        action1 = gg.check_number_answer(action1,action1_choices)

        if action1 == '0':
            gg.endgame()
        elif action1 == '1':
            player.unpack() #Updates stats from unpack action (says cp(name=name).unpack())
            gg.slow_print('\nYou look at the clock and you have plenty of time to do something else!',0.04)
            next_choice = ['socialize','take a nap']
            gg.print_list(next_choice)
            next = gg.slow_input('What would you like to do next? ',0.04)
            next = gg.check_number_answer(next,next_choice)
            if next == '0':
                gg.endgame()
            elif next == '1':
                player.socialize()
            else:
                player.take_nap()
        elif action1 == '2': #socialize 
            player.socialize() 
            gg.slow_print('\nYou look at the clock and its already 5 pm!',0.04)
            gg.slow_print('You go back to your room and unpack your things.',0.04)
            player.unpack()   
        else: #find classes 
            player.find_classes()
            next_choice = ['unpack','socialize']
            gg.print_list(next_choice)
            next = gg.slow_input('What would you like to do next? ',0.04)
            next = gg.check_number_answer(next,next_choice)
            if next == '0':
                gg.endgame()
            elif next == '1':
                player.unpack()
                gg.slow_print('\nThere is still some time to go meet people.',0.04)
                player.socialize()
            else:
                player.socialize()
                gg.slow_print('\nYou go back to your room and unpack.',0.04)
                player.unpack()

        #player.check_tired()
        gg.slow_print('\nDang! It is already MIDNIGHT!',0.04)
        gg.slow_print("Lets make sure you don't f$%k up your sleep schedule!",0.03)
        gg.slow_print('GET TO BED KID, FIRST DAY IS TOMORROW!',0.04)
        player.next_day()

        gg.slow_print('\nMonday, August 29th, 9:00 am',0.05)
        gg.slow_print("\nFirst day of classes! Aren't you excited?!?!?!?",0.04)
        gg.slow_print("Lets start the semester off right!",0.04)

        gg.slow_print('\nYou go to all of your classes for the week and get adjust to your new life.',0.03) 
        
        gg.slow_print('\nCongrats on making it through syllabus week!',0.04)
        gg.slow_print("This week might have been way too easy, but don't worry.",0.04)
        gg.slow_print("These next few weeks are going to be IMPOSSIBLE.",0.04)
        gg.slow_print('Just kidding!',0.05)
        gg.slow_print('But seriously, get ready because you should always expect the unexpected!',0.04)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_health()

    def week2(player,wage):
        gg.slow_print('\nSunday, 9/4, 9:00 am',0.05)
        gg.slow_print("Since it was just syllabus week, there isn't much homework to be done yet.",0.04)
        
        options = ['work','sleep','relax']
        gg.print_list(options)
        decision = gg.slow_input('What do you want to do today? ',0.04)
        decision = gg.check_number_answer(decision, options)
        if decision == "0":
            gg.endgame()
        elif decision == '1': #work
            hours = gg.slow_input("\nHow many hours would you like to work? ",0.04)
            player.work(wage, hours)
        elif decision == '2': #sleep
            player.sleep()
            gg.slow_print("\nYOU SLEPT ALL DAY!")
            gg.slow_print("AND NOW YOU CAN'T SLEEP!")
            player.health += rand.randint(-20,0)

            options = ['read a book','play video games']
            gg.print_list(options)
            what = gg.slow_input('What are you going to do? ')
            what = gg.check_number_answer(what, options)
            
            if what == '0':
                gg.endgame()
            elif what == '1':
                player.read_book()
            else: 
                player.video_games()
        else: #relax
            player.relax()

        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nMonday, 9/5, 9:00 am',0.05)
        gg.slow_print("IT'S LABOR DAY!!!",0.04)
        digit = rand.randint(1,2)
        if digit == 1:
            gg.slow_print('\nYour school does not allow students to have labor day off.',0.04)
            gg.slow_print("THIS IS OUTRAGEOUS!!!!",0.04)
            player.no_labor_day()

            gg.slow_print('\nTheres two options you can go with here.',0.04)
            go = ['skip class','go to class']
            gg.print_list(go)
            choice = gg.slow_input('Whats the ultimate decisions boss? ',0.04)
            choice = gg.check_number_answer(choice,go) 

            if choice == '0':
                gg.endgame()
            elif choice == '1': #skip class
                player.skip_class()
                gg.slow_print("\nI hope this doesn't become a habit.",0.04)
                gg.slow_print('Since you skipped, you have so much free time now!',0.04)
                cg.labor_day(player)
            else: #go class for school on labor day 
                player.go_class()
                player.extra_time()
        else: #no class on labor day 
            gg.slow_print('No classes today!',0.04)
            cg.labor_day(player)
        
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()
        
        gg.slow_print('\nTuesday, 9/6, 8:00 am',0.05)
        gg.slow_print('Your day off!',0.04)
        cg.sunday_tuesday(player,wage)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nWednesday, 9/7, 8:15 am',0.05)
        gg.slow_print('You got classes today!',0.04)
        cg.monday_wednesday(player)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nThursday, 9/8, 9:45 am',0.05)
        cg.saturday_thursday(player,wage)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nFriday, 9/9, 9:15 am',0.05)
        gg.slow_print('You got classes today!',0.04)
        cg.club_day(player)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nSaturday, 9/10, 1:30 pm',0.05)
        cg.saturday_thursday(player,wage)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()
  
    def week3(player,wage):
        gg.slow_print('\nSunday, 9/11, 2:00 pm',0.05)
        cg.sunday_tuesday(player,wage)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nMonday, 9/12,  6:00 am',0.05)
        cg.monday_wednesday(player)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nTuesday, 9/13, 9:00 am',0.05)
        cg.sunday_tuesday(player,wage)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nWednesday, 9/14, 8:45 am',0.05)
        cg.mwf_exam(player)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nThursday, 9/15, 7:30 am',0.05)
        cg.saturday_thursday(player, wage)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nFriday, 9/16, 9:25 am',0.05)
        cg.friday(player)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nSaturday, 9/17, 12:00 pm',0.05)
        cg.saturday_thursday(player, wage)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

    def week4(player,wage):
        gg.slow_print('\nSunday, 9/18, 9:50 pm',0.05)
        cg.sunday_tuesday(player,wage)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nMonday, 9/19, 8:50 am',0.05)
        cg.mwf_exam(player)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nTuesday, 9/20, 11:21 am',0.05)
        cg.sunday_tuesday(player,wage)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nWednesday, 9/21, 7:50 pm',0.05)
        cg.yes_no_concert(player)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nThursday, 9/22, 10:10 am',0.05)
        cg.saturday_thursday(player, wage)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nFriday, 9/23, 8:10 pm',0.05)
        cg.mwf_exam(player)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nSaturday, 9/24, 1:00 pm',0.05)
        cg.saturday_thursday(player, wage)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

    def week5(player,wage):
        gg.slow_print('\nSunday, 9/25, 12:00 pm',0.05)
        cg.sunday_tuesday(player,wage)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nMonday, 9/26, 8:06 am',0.05)
        cg.mwf_exam(player)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nTuesday, 9/27, 9:08 am',0.05)
        cg.sunday_tuesday(player,wage)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nWednesday, 9/28, 5:16 am',0.05)
        cg.monday_wednesday(player)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nThursday, 9/29, 11:01 am',0.05)
        cg.saturday_thursday(player, wage)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nFriday, 9/30, 9:42 pm',0.05)
        cg.friday(player)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()


        gg.slow_print('\nSaturday, 10/1, 11:11 pm',0.05)
        cg.saturday_thursday(player, wage)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

    def week6(player,wage):
        gg.slow_print('\nSunday, 10/2, 7:59 am',0.05)
        cg.sunday_tuesday(player,wage)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nMonday, 10/3, 8:00 am',0.05)
        cg.yes_no_concert(player)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nTuesday, 10/4, 8:59 am',0.05)
        cg.sunday_tuesday(player,wage)
        player.sleep()
        1()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nWednesday, 10/5, 9:59 am',0.05)
        cg.mwf_exam(player)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nThursday, 10/6, 10:00 am',0.05)
        cg.saturday_thursday(player, wage)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nFriday, 10/7, 10:59 am',0.05)
        cg.friday(player)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nSaturday, 10/8, 11:00 pm',0.05)
        cg.saturday_thursday(player, wage)
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

    def finals_week(player,wage):
        gg.slow_print('WOW! You made it to FINALS WEEK!')
        gg.slow_print('Congrats')
        gg.slow_print('Your exams are on Monday and Friday!.')

        gg.slow_print('\nSunday, 10/9, 10:00 am',0.05)
        options = ['study', 'work', 'hangout with friends','play video games']
        gg.print_list(options)
        choice = gg.slow_input("How will you start finals week? ",0.04)
        choice = gg.check_number_answer(choice,options)

        if choice == '0':
            gg.endgame()
        elif choice == '1':
            player.study()
        elif choice == '2':
            hours = gg.slow_print('\nHow many hours will you work? ',0.04)
            player.work(wage,hours)
        elif choice == '3':
            player.hangout_day()
        else:
            player.video_games()
            player.extra_time()
        
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nMonday, 10/10, 8:15 am',0.05)
        gg.slow_print("FINALS DAY!!",0.05)
        cg.final_exam(player)
        
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nTuesday, 10/11, 12:16 pm',0.05)
        options = ['study', 'work', 'hangout with friends','play video games']
        gg.print_list(options)
        choice = gg.slow_input("What will you do on your day off? ",0.04)
        choice = gg.check_number_answer(choice,options)

        if choice == '0':
            gg.endgame()
        elif choice == '1':
            player.study()
        elif choice == '2':
            hours = gg.slow_input('\nHow many hours will you work? ',0.04)
            player.work(wage,hours)
        elif choice == '3':
            player.hangout_day()
        else:
            player.video_games()
            player.extra_time()
        
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nWednesday, 10/12, 9:34 am',0.05)
        yes = gg.slow_input('Would you go to a concert today? ',0.04)
        gg.check_yes_no(yes)
        if yes == 'y':
            gg.slow_print("That is crazy cause...",0.04)
            player.concert()
        else:
            options = ['study', 'work', 'hangout with friends','play video games']
            gg.print_list(options)
            choice = gg.slow_input("What will you do on your day off? ",0.05)
            choice = gg.check_number_answer(choice,options)

        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nThursday, 10/13, 9:54 am',0.05)
        options = ['study', 'work', 'hangout with friends','play video games ']
        gg.print_list(options)
        choice = gg.slow_input("How will you start finals week? ",0.04)
        choice = gg.check_number_answer(choice,options)

        if choice == '0':
            gg.endgame()
        elif choice == '1':
            player.study()
        elif choice == '2':
            hours = gg.slow_input('\nHow many hours will you work? ',0.04)
            player.work(wage,hours)
        elif choice == '3':
            player.hangout_day()
        else:
            player.video_games()
            player.extra_time()
        
        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nFriday, 10/14, 12:00 pm',0.05)
        gg.slow_print('LAST FINAL!',0.06)
        cg.final_exam(player)

        player.sleep()
        player.update_stats()
        player.display_college_info()
        player.check_tired()
        player.check_health()

        gg.slow_print('\nSaturday, 10/15, 1:00 pm',0.05)
        gg.slow_print("It's move out day!",0.05)
        gg.slow_print("What a great semester you've had!",0.05)
        player.happiness += rand.randint(0,25)

    def friday(player):
        gg.slow_print('Whats the plan for today?',0.04)
        options = ['skip class','go to class']
        gg.print_list(options)
        enter = gg.slow_input("What's the plan for today? ",0.04)
        if enter == "0":
            gg.endgame()
        elif enter == '1':
            player.skip_class()
            player.skip()

            gg.slow_print('\nYour friends are going out tonight and invite you to come!',0.03)
            out = gg.slow_input("Do you wanna go out tonight? ",0.04)
            gg.check_yes_no(out)
            if out == 'y':
                player.bar()
            else:
                gg.slow_print('\nYou decide that after a long day of NO classes, your bed is calling your name!',0.03)
                
        else: 
            player.go_class()
            player.extra_time()

    def labor_day(player):
                options = ['hangout with friends',
                           'take a nap',
                            'read your syllabi and do homework',
                            'play video games']
                gg.print_list(options)
                what = gg.slow_input('What are you going to do? ',0.04)
                what = gg.check_number_answer(what,options)

                if what == '0':
                    gg.endgame()
                elif what == '1':
                    player.hangout_day()
                elif what == '2':
                    player.take_nap()
                elif what == '3':
                    gg.slow_print("You found out that you're going to have at least one exam every week!",0.04)
                    gg.slow_print('None this week though, you got super lucky!',0.04)
     
                    player.happiness += rand.randint(-15,15)
                    player.do_hw()
                else:
                    gg.slow_print('Good thing your school gives you access to some games for free!',0.04)
                    player.video_games()

    def monday_wednesday(player):
        #code school day, but also have the option to skip
        option1 = ['skip classes', 'go to classes']
        gg.print_list(option1)
        enter = gg.slow_input("Which one is making the most sense today? ",0.04)
        if enter == "0":
            gg.endgame()
        elif enter == '1':
            player.skip_class()
            player.skip()
            player.extra_time()
        else: 
            player.go_class()
            player.extra_time()
        
    def mwf_exam(player):
        gg.slow_print('\nEXAM DAY!!!',0.04)
        digit = rand.randint(1,3)
        if digit == 1:
            gg.slow_print("I hope your prepared for your one exam today!",0.04)
            player.happiness += rand.randint(-10,0)
        else:
            gg.slow_print("I hope you're well prepared for your exams today!",0.04)
            player.happiness += rand.randint(-30,0)
        
        digit = rand.randint(1,4)
        if digit == 1:
            gg.slow_print('**SPECIAL EVENT**',0.06)
            options = ['skip exam(s)','take exam(s)']
            gg.print_list(options)
            enter = gg.slow_input("Whats the plan? ",0.05)
            enter = gg.check_number_answer(enter,options)
            if enter == "0":
                gg.endgame()
            elif enter == '1':
                player.skip_class()
                player.concert()
            else:
                player.go_class()
                player.take_exam()
                player.extra_time()
        else:
            options = ['skip exam(s)','take exam(s)']
            gg.print_list(options)
            enter = gg.slow_input("Whats the plan? ",0.05)
            enter = gg.check_number_answer(enter,options)
            if enter == "0":
                gg.endgame()
            elif enter == '1':
                player.skip_class()
                player.skip()
                player.extra_time()
            else:
                player.go_class()
                player.take_exam()
                player.extra_time()
    
    def sunday_tuesday(player,wage):
        options = ['work','do homework','relax', 'hang out with friends']
        gg.print_list(options)
        choice = gg.slow_input('Which one is calling your name? ',0.04)
        choice = gg.check_number_answer(choice,options)

        if choice == '0':
            gg.endgame()
        elif choice == '1':
            hours = gg.slow_input('How many hours would you like to work? ',0.04)
            player.work(wage,hours)
        elif choice == '2':
            player.do_hw()
            gg.slow_print('\nYou have some extra time!',0.04)
            options = ['hangout with friends','take a nap', 'play video games']
            gg.print_list(options)
            what = gg.slow_input('What would you like to do? ',0.04)
            if what == '0':
                gg.endgame
            elif what == '1':
                player.hangout_day()
            elif what == '2':
                player.take_nap()
            else:
                player.video_games()
        elif choice == '3':
            player.relax()
            gg.slow_print('Today was peaceful and very much needed.',0.04)
        else:
            player.hangout_day()
    
    def saturday_thursday(player,wage):
        options = ['work','do homework','relax','go to the bars']
        gg.print_list(options)
        choice = gg.slow_input("What's your plan for today? ",0.04)
        choice = gg.check_number_answer(choice,options)

        if choice == '0':
            gg.endgame()
        elif choice == '1':
            hours = gg.slow_input('How many hours will you work? ',0.04)
            player.work(wage,hours)
            
            gg.slow_print('\nWould you look at the time its 10:30 pm!',0.04)
            will = gg.slow_input("Will you go out to the bars tonight? ",0.04)
            gg.check_yes_no(will)

            if will == 'y':
                player.bar()
            else: # no bar option #can add to it more later if want ot 
                gg.slow_print('\nGood choice!',0.05)
                gg.slow_print('The bars are so overrated!',0.04)
                options = ['play video games', 'read a book']
                what = gg.slow_input('What do you wanna do instead? ',0.04)
                what = gg.check_number_answer(what,options)
                if what == '0':
                    gg.endgame()
                if what == '1':
                    player.video_games()
                else:
                    player.read_book()                           
        elif choice == '2':
            player.do_hw()
            options = ['hangout with friends','take a nap', 'play video games', 'go out to the bars']
            gg.print_list(options)
            what = gg.slow_input('What would you like to do? ',0.04)
            if what == '0':
                gg.endgame
            if what == '1':
                player.hangout_day()
            if what == '2':
                player.take_nap()
            if what == '3':
                player.video_games()
            else:
                player.bar() #this needs to be coded 
        elif choice == '3':
            player.relax()
            gg.slow_print('Today was peaceful and very much needed.',0.04)
        else:
            player.bar()

    def club_day(player):
        gg.slow_print('\nToday every club will be at the First Look Fair!',0.04)
        choice = gg.slow_input("Would you like to go? You will have to skip classes for it. ",0.04)
        gg.check_yes_no(choice)
        
        if choice == 'y':
            player.skip_class()
            gg.slow_print('\nYou head towards the First Look Fair!',0.04)
            gg.slow_print('There are so many clubs!',0.04)
            luck = rand.randint(1,2)
            if luck == 1:
                gg.slow_print('\nYou get overwhelmed by the amount of people!',0.04)
                gg.slow_print('You leave without looking at any of the clubs.',0.04)
                player.health += rand.randint(-15,0)
                player.happiness += rand.randint(-30,0)
                player.gpa = cp.calc_gpa(player,rand.uniform(-0.25,0))
            else:
                gg.slow_print('\nYou look at a few clubs that you might join.',0.04)
                gg.slow_print("\nYou decide not to join any since all the times don't fit your schedule.",0.04)
                player.happiness += rand.randint(-10,10)
                player.gpa = cp.calc_gpa(player,rand.uniform(-0.15,0))
                player.health += rand.randint(-15,0)
            player.extra_time()
        else:
            player.go_class()
            player.extra_time()

    def concert_day(player,artist):
        gg.slow_print(f'You head towards the venue to see {artist}.',0.04)
        
        transport = ['metro','uber','friends car']
        gg.print_list(transport)
        which = gg.slow_input('What mode of transport will you take? ',0.04)
        which = gg.check_number_answer(which,transport)

        if which == '0':
            gg.endgame()
        elif which == '1':
            gg.slow_print('You take the metro!',0.04)
            lucky = rand.randint(1,3)
            if lucky == 1:
                gg.slow_print('You make it to the concert with no problems!',0.04)
                gg.slow_print('You and your friends enjoyed the concert!',0.04)
                player.happiness += rand.randint(0,20)
            else:
                gg.slow_print("You lost your metro card!",0.04)
                player.happiness += rand.randint(-25,0)

                option = ['buy a new one ($15)','hop the entrance']
                gg.print_list(option)
                choice = gg.slow_input('What are you going to do? ',0.04)
                choice = gg.check_number_answer(choice,option)

                if choice == '0':
                    gg.endgame()
                elif choice == '1':
                    gg.slow_print('You bought a new metro card!',0.04)
                    gg.slow_print('You and your friends make it to the concert!',0.04)
                    gg.slow_print('You and your friends enjoyed the concert!',0.04)
                    player.money -= 15
                else:
                    luck = rand.randint(1,2)
                    if luck == 1:
                        gg.slow_print('Security did not catch you hopping over the gates!',0.04)
                        player.happiness += rand.randint(0,15)
                    else:
                        gg.slow_print('Security caught you hopping over the gate!',0.04)
                        gg.slow_print('You paid a $40 fine!',0.04)
                        player.money -= 40
                        player.happiness += rand.randint(-50,0)
                    gg.slow_print('You and your friends make it to the concert!',0.04)
                    gg.slow_print('You and your friends enjoyed the concert!',0.04)
        elif which == '2':
            gg.slow_print(f'You take an uber to see {artist}!',0.04)
            luck = rand.randint(1,2)
            price = rand.randint(15,45)
            if luck == 1:
                gg.slow_print('You got to the venue before the concert started!',0.04)
                gg.slow_print(f'The uber was ${price}.',0.04)
                gg.slow_print('You and your friends enjoyed the concert!',0.04)
                player.money -= price
            else:
                gg.slow_print('The uber driver crashed into someone!',0.04)
                gg.slow_print("You were concussed.",0.04)
                gg.slow_print("You can't go to the concert now!",0.04)
                gg.slow_print("You call a friend to pick you up and take you home.",0.04)
                player.health += rand.randint(-30,0)
                player.happiness += rand.randint(-50,0)
                player.money -= price 
        else:
            gg.slow_print(f'You and your friends drive to see {artist}',0.04)
            gg.slow_print('Everyone enjoyed the concert!',0.04)
            player.happiness += rand.randint(0,30)
            player.health += rand.randint(-10,0)

    def final_exam(player):
        gg.slow_print('Will you let your grade tank or try and save it?',0.04)
        options = ["don't take exams",'go take exams']
        gg.print_list(options)
        choice = gg.slow_input('What will you do? ',0.04)

        if choice == '0':
            gg.endgame()
        elif choice == '1':
            player.skip()
            player.extra_time()
        else:
            player.take_final()
            gg.slow_print('You feel exhuasted after today!',0.04)
          
    def yes_no_concert(player):
        yes = gg.slow_input('Would you go to a concert today? ',0.04)
        gg.check_yes_no(yes)
        if yes == 'y':
            gg.slow_print("That is crazy cause...",0.04)
            player.concert()
        else:
            gg.slow_print('You decide not to go and go to class instead',0.04)
            player.go_class()
            player.take_exam()
            player.extra_time()

class general_game: #general functions for the game
    def check_college_choice(answer, c1,c2):
        college1 = c1
        college2 = c2
        if answer == 'y':
            gg.slow_print(f"{college1} and {college2} are great choices!",0.02)
        else:
            while answer == 'n':
                gg.slow_print('Bruh....',0.06) 
                gg.slow_print('What are are your top two schools?',0.04)
                college1 = gg.slow_print('First choice: ',0.04)
                college2 = gg.slow_print('Second choice: ',0.04)
                gg.slow_print(f"Your favorite colleges are {college1} and {college2}.",0.03)
                a = gg.slow_input('Is this correct? ',0.03)
                answer = gg.check_yes_no(a)            
        return college1, college2 
        
    def check_yes_no(answer): #makes sure input is yes or no
        while answer.lower() not in ('y','n'): #has to be y or n
            gg.slow_print("\nInvalid response.",0.04)
            answer = gg.slow_input("Please enter y or n. ",0.03)
        return answer
     
    def check_number(answer): #checks that input is a number
        if answer.isdigit():
            return answer
        else:
            while not answer.isdigit():
                answer = gg.slow_input('Please enter a number: ',0.03)
            return answer

    def check_number_answer(number, list): #makes sure input is a number in the list provided
        if number.isdigit() and 0 <= int(number) <= len(list):
            number = number
        else:
            while not number.isdigit() or not 0 <= int(number) <= len(list):
                gg.slow_print(f'\nInvalid choice. Please enter a valid number (0,{len(list)}).',0.03)
                number = gg.slow_input('Enter new number: ',0.04)
            number = number
        return number

    def doublecheck_answer(answer,list): #double checks users input
        a = gg.slow_input('Are you sure? ',0.04)
        a = gg.check_yes_no(a)
        if a == 'y':
            gg.slow_print('Perfect!',0.04)
        else:
            while a == 'n':
                answer = gg.slow_input('Ok, pick another choice: ',0.03)
                answer = gg.check_number_answer(answer,list)
                a = gg.slow_input(f'You chose {list[int(answer)-1]}, correct? ',0.04)
                a = gg.check_yes_no(a)
        return answer
          
    def endgame(): #end the game
        gg.slow_print('\nThanks for playing!',0.06)
        gg.slow_print('Goodbye!',0.06)
        sys.exit()

    def exitgame(answer): #exit game at the start
        if answer == 'n':
            gg.slow_print("\nYou didn't even play the game! :`(",0.06)
            gg.slow_print('Goodbye!',0.06)
            sys.exit()
    
    def game_rules(): #general rules of the game
        gg.slow_print("\nHere are the general rules to the game: \n",0.02)
        gg.slow_print("1. If you wish to quit the game enter 0 (when the option is available).",0.02)
        gg.slow_print("2. For yes and no questions answer with y or n.",0.02)
        gg.slow_print("3. For decision questions enter the corresponding number.",0.02)
        gg.slow_print("4. For any other questions feel free to enter any reponse.",0.02)
        gg.slow_print('5. Some decisions will allow you to change your choice, but not all of them will.',0.02)

    def get_name(): #get the players name
        name = gg.slow_input("\nWhat is your name? ",0.02).strip().capitalize()
        a = gg.slow_input(f'Your name is {name}? ',0.02)
        a = gg.check_yes_no(a)
        if a == 'y':
            gg.slow_print(f'Nice to meet you, {name}!',0.02)

        else:
            while a == 'n': #make sure that the palyers name is correct
                gg.slow_print('\nLet try that again',0.02)
                name = gg.slow_input("What is your name? ",0.02).strip()
                a = gg.slow_input(f'Your name is {name}? ',0.02)
                a = gg.check_yes_no(a)
            gg.slow_print(f"Nice to meet you {name}!",0.02)
        return name

    def print_list(list): #prints a list for the player to see the options
        for i, var in enumerate(list,1):
                gg.slow_print(f'{i}. {var}',0.02)
        gg.slow_print("0. endgame",0.02)
         
    def slow_print(text, delay): #haven't used yet but (will slowly print out the text)
        for word in text:
            print(word, end='',flush=True)
            time.sleep(delay)
        print()
    
    def slow_input(text,delay): #haven't used yet but (will slowly print out the text and take an input)
        for word in text:
            print(word, end='',flush=True)
            time.sleep(delay)
        player_input = input()
        return player_input
         
    def story_description(): #descrition of the game
        gg.slow_print('\nIn Semester Quest: Autumn Excursion, you will be going through a 8ish week semester of college.',0.04)
        hint = gg.slow_input('Would you like a hint? ',0.04)
        hint = gg.check_yes_no(hint)
        if hint == 'y': 
            gg.slow_print('To win you have to get good grades and keep yourself healthy.',0.04)
        else: 
            gg.slow_print("Gamer at heart, huh? Good Luck!",0.04)

if __name__ == "__main__": #game code
    gg = general_game
    cp = college_player
    cg = college_game

    gg.slow_print("\nSemester Quest: Autumn Excursion",0.06)
    play = gg.slow_input("\nWould you like to play (y/n)? ",0.06)
    play = gg.check_yes_no(play) #makes sure this is 'y' or 'n'
    if play == 'n':
        gg.exitgame(play) #exit game
    else:
        gg.game_rules() #general game rules 
        gg.story_description() #description of the story
        ready = gg.slow_input("\nAre you ready? ",0.06)
        ready = gg.check_yes_no(ready) #makes sure this is 'y' or 'n'
        if ready == 'y': #ready to play = start game
            cg.college_life()        
        else: #not ready to play = exit game
            gg.exitgame(ready)
