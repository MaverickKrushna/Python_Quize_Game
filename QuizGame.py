# ---function of the Quiz python
from threading import Timer
import random
def QuizGame(name):
    correct_attempt = 0
    question_num = 1
    flag = 0
    money = 10
    total_money = 0
    for Question in questionOfQuiz:
        print("__________________________+  %s  +______________________________\n"%(name).upper())
        print("-------PYTHON  QUIZ Q.%d---------\n" % (question_num))
        print("____WINING PRICE AMOUNT IS %d $ YOU HAVE ONLY 15 SECONDS____"%(money))
        print("\n", question_num, ".", Question, "\n")
        for i in optionsOfQuiz[question_num - 1]:
            print(i)
        timeStamp = Timer(15, timeOut)
        timeStamp.start()
        answer = input("Enter (a, b, c, d) :")
        try:
            if timeStamp.is_alive():
                ansOfQuestion = answer.lower()
                flag = correct_attempt
                correct_attempt += check_answer(questionOfQuiz.get(Question), ansOfQuestion)
                if flag == correct_attempt:
                    print(" %s YOU ARE OUT FROM THE QUIZ \n"%(name).upper())
                    timeStamp.cancel()
                    break
            else:
                print("%s.... YOU ARE OUT FROM THE QUIZ ....\n"%(name).upper())
                timeStamp.cancel()
                break
        except :
            print("Something get wrong !!")

        timeStamp.cancel()
        total_money += money
        Random_money  = random.randint(0, 30)
        money += Random_money
        question_num += 1
    print("____________________ +-+ GAME OVER +-+ ___________________________")
    score =input("ENTER 1 FOR DISPLAY HOW MUCH YOU WIN  : ")
    if score == '1':
        print()
        display_score(correct_attempt, name , total_money)
    else:
        print("\n...Your score is hidden !")
    print("\nTHANK YOU !! %s FOR PLAYING PYTHON QUIZ !! " % (name))
    print("\n PYTHON QUIZ TEST IS TERMINATED...............\n")

# --- time out function
def timeOut():
    print("\n:::::  Time Out :::::")
    # print("PRESS ENTER FOR NEXT QUESTION !!")
    print("GAME OVER ")
    print("Press anyKey for continue ---")


# -- check the answer
def check_answer(ans, attempt):
    if ans == attempt:
        print(":: congratulations  ! ::\n")
        return 1
    else:
        print(":: Oops ! you lose  !::\n")
        return 0


# ---- Display the score

def display_score( correct_attempt , name , total_money):
    print("______________ PYTHON QUIZ RESULT _______________\n")
    if int(total_money) > 100 :
        print(" congratulations  !! %s"%(name).upper())
    elif int(total_money) > 200 :
        print(" Yh .. congratulations  !! %s" % (name).upper())

    print("\nYOU WON THE AMOUNT OF %d $ IN OUR PYTHON QUIZ ::"%(total_money))


    # score = float((correct_attempt / len(questionOfQuiz)) * 100)
    # print(":: ____%s YOUR SCORE IS : " % (name).upper() + str(score) + "%\n")


questionOfQuiz = {
    "Who is an Indian Tech reviewer among these ?": "a",
    "Who is the director of RRR movie ?": "a",
    "Which is the famous dialogue of Pushpa ?": "d",
    "which avenger turned into a monster from Gamma rays (Marvel Studio)?": "d",
    "The Super  follows  feature has been introduced by which social media giant ? ": "b",
    "Burbn social media now days called as ?": "c",
    "Which online store is widely used for clothes shopping ?": "b",
    "what led to the sinking of the Titanic ?": "a",
    "Who amongst these was awarded the Param Vir Chakra ? ": "d",
    "Python developed in which year ?": "b",
    "which is the oldest monument in India ?": "c",
    "Which is the traditional food of west Bengal ? ": "a",
    "Where was Chhatrapati SHivaji Maharaj Born ?" : "b",
    "What's the deadlist military Weapon ?" : "d",
    "WHich two countries were the first to declare war on Germany ? " : "a"

}


optionsOfQuiz = [
    ['a) Gaurav Chaudhary ', 'b) MKBHD ', 'c) Arun Rupesh Maini', 'd) Austin Evans'],
    ['a) S.S Rajamouli ', 'b) Rajkumar Hirani', 'c) Prasant Neel ', 'd) Rohit shetty'],
    ["a) Violence, Violence, Violence, I don’t like, i Avoid.… but Violence likes me, I can’t Avoid. ",
     "b) Ilaaka apun ka, kanun bhi apun ka, Kaat Dalega!", "c) If you think you're bad.. i'm your dad",
     "d) main jhukega nhi , sala."],
    ["a) Thor", "b) Thanos ", "c) Ironman", "d) Hulk"],
    ["a) facebook ", "b) twitter", "c) Instagram  ", "d) whatsapp "],
    ["a) bingo", "b) youtube ", "c) instagram", "d) snapchat "],
    ["a) Amazon", "b) Myntra", "c) flipKart", "d) Meesso "],
    ["a) iceberg", "b) Bermunda", "c) storm", "d) Tsunami "],
    ["a) Capt. Kenguruse", "b) Naik Digendra Kumar", "c) Lt balwan sing", "d) Capt. Vikram Batra"],
    ["a) 1999", "b) 1991 ", "c) 2004", "d) 1989 "],
    [ "a) Qutub minar " , "b) Khajuraho ", "c) Ajanta Caves " , "d) Taj Mahal"],
    [ "a) Rice and Fish ", "b) Moomos " , "c) Bisi Bele Bath " , "d) Thukpa "],
    ["a) Raigad" , "b) Shivneri" , "c) pune " , "d) BijayaPur "],
    ["a) AK 47 "   , "b) Maxim Machine gun "  , "c) rifle " , "d) Tsar Bomba "] , 
    [ "a) Britain & France " , "b) America & Englond " , "c) italy & France " , "d) Norway & Denmark "]
]




if __name__ == '__main__':
    print("\n \n______________||+||| PYTHON QUIZ USER DETAILS |||+||________________\n")
    name = input("Enter your name : ")
    print(" \n%s !! YOUR ARE WELCOME TO PYTHON QUIZ .." % (name).upper())
    print("\n|||||||||||||||||..... PYTHON QUIZ ......||||||||||||||||\n")



    playAgain = True
    while playAgain:
        press = input("%s ! PRESS 1 FOR START THE QUIZ : "%(name).upper())

        if press == '1':
            QuizGame(name)
            tryAgain = input("PRESS 1 FOR TRY AGAIN THE QUIZ : ")
            if tryAgain == '1':
                print("\n WELCOME AGAIN TO PYTHON QUIZ %s\n" % (name).upper())
                playAgain = True
            else:
                print("THANK YOU %s !:: QUIZ GAME OVER  "%(name).upper())
                playAgain = False

        else:
            print("%s.....YOU DON'T WANT TO PLAY !! , BYE!"%(name).upper())
            playAgain = False




