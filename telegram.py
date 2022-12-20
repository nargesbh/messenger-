from datetime import datetime
from typing import Counter
import server
import sys


def sign_up():
    dateTimeObj = datetime.now()
    dateObj = str(dateTimeObj.date())
    
    new_user = []

    print("please enter your first name:", end=' ' )
    first_name = input()

    print("enter your last name:", end=' ')
    last_name = input()

    print("enter the year you were born :", end=' ')
    birth_year = input()

    print("please enter the your desired username :", end=' ')
    user_name = input()

    all_users = server.main("i need user names")

    while( user_name in all_users):
        print("this user name already exists, please enter enother user name :", end=' ')
        user_name = input()
    
    print("enter a password :", end=' ')
    password = input()
    while (password == "NONE"):
        print("your password can not be NONE please pick another password :", end=' ')
        password = input()

    new_user.append(user_name)
    new_user.append(password)
    new_user.append(first_name)
    new_user.append(last_name)
    new_user.append(birth_year)
    new_user.append(dateObj)

    new_user = str(tuple(new_user))
    
    query = """INSERT INTO USERS VALUES""" + new_user + """;"""
    
    server.main(query)

    print("you are successfully registered.")
    sys.exit()


def sign_in():

    print("user_name:", end=' ')
    user_name = input()
    query = "password " + user_name

    password = server.main(query)
    while (password == "NONE"):
        print("There is not any acount with that user name.")
        sign_in()

    print("password :", end=" ")
    inp_pas = input()

    while(inp_pas != password):
        print("WRONG PASSWORD!")
        print("password :", end=" ")
        inp_pas = input()

    print("you are successfully signed in")
    after_enter(user_name)

def after_enter(user):
    global you_blocked_bool 
    global he_blocked_bool 

    you_blocked_bool = 0
    he_blocked_bool = 0

    query = "i need user names"
    all_users = server.main(query)
    print("These are all users:")
    user_counter = 1
    all_users.remove(user)
    for i in all_users:        
        help = str(user_counter) + " - " + i
        print(help)
        user_counter += 1
    
    print("enter the number assigned to the user you want to interact with(enter -1 if you waant to quit):", end=" ")
    chosed_user = int(input())
    if (chosed_user == -1 ):
        sys.exit()
    show_all_messages(user, all_users[chosed_user-1])


    block_check(user, all_users[chosed_user-1])

    if (you_blocked_bool == 0 and he_blocked_bool == 0):
        print("Do you want to message this user(Y/N) ?", end=" ")
        if_check = input()

        if (if_check == "Y" or if_check == "y"):
            return send_message(user, all_users[chosed_user-1])
        return after_enter(user)

    elif (he_blocked_bool):
        print("this user has blocked you so you can not send message.")
        after_enter(user)

    elif (you_blocked_bool):
        print("you have blocked this user so you can not message.")
        after_enter(user)


def send_message(sender, reciever):

    new_message = []
    new_message.append(sender)
    new_message.append(reciever)
    
    print("Enter your message:", end=" ")
    message = input()
    new_message.append(message)

    dateTimeObj = datetime.now()
    dateObj = str(dateTimeObj.date())
    timeObj = str(dateTimeObj.time())[:5]
    new_message.append(timeObj)
    new_message.append(dateObj)

    new_message = str(tuple(new_message))
    query = """INSERT INTO MESSAGES VALUES""" + new_message + """;"""
    server.main(query)

    # print("message successfully sent.")
    show_all_messages(sender, reciever)


    print("do you want to send another message(Y/N):", end=" ")
    if_check = input()
    if (if_check == "Y" or if_check == "y"):
        return send_message(sender, reciever)

    return after_enter(sender)

def show_all_messages(sender, reciever):

    query = """SELECT * FROM MESSAGES WHERE ( SENDER_ID = '""" + sender + """' AND RECEIVER_ID = '"""+ reciever + """' ) OR 
    ( SENDER_ID = '""" + reciever + """' AND RECEIVER_ID = '"""+ sender + """' )"""
    all_messages = server.main(query)
    Counter = len(all_messages)-1

    if Counter < 0 :
        return
        
    print(sender)
    date = all_messages[Counter][4]
    print("          ***"+ date + "***")

    for i in range(Counter+1):

        if all_messages[i][4] != date :
            date = all_messages[i][4]
            print("          ***"+ date + "***")

        if(all_messages[i][0] == sender):
            print("you : " + all_messages[i][2], end=" ")
            print("( "+ all_messages[i][3]+ " )")

        elif(all_messages[i][0] != sender):
            print(all_messages[i][0] +" : " + all_messages[i][2], end=" ")
            print("( "+ all_messages[i][3]+ " )")

def block_func(blocker, blocked_id):

    query = "INSERT INTO BLOCKS VALUES( '" + blocker + "', '" + blocked_id + "' )" 
    server.main(query)
    after_enter(blocker)

def block_check(sender, reciever):

    global you_blocked_bool
    global he_blocked_bool

    you_blocked = """SELECT * FROM BLOCKS WHERE ( BLOCKER = '""" + sender + """' AND BLOCKED_ID = '"""+ reciever + """' ) """
    he_blocked = """SELECT * FROM BLOCKS WHERE ( BLOCKER = '""" + reciever + """' AND BLOCKED_ID = '"""+ sender + """' ) """
    you_blocked_bool = server.main(you_blocked)
    he_blocked_bool = server.main(he_blocked)


    if you_blocked_bool == 1 :
        print("do you want to unblock this user (Y/N) ?", end=" ")
        help = input()
        if (help == "Y" or help == "y") :
            query = "DELETE FROM BLOCKS WHERE BLOCKER = '"+ sender + "';"
            server.main(query)
            you_blocked_bool = 0

    if you_blocked_bool == 0 :
        print("do you want to block this user (Y/N) ?", end=" ")
        help = input()
        if (help == "Y" or help == "y") :
            block_func(sender, reciever)
    

print("If you want to sign up enter 1 and if you want to sign in enter 2 :", end=' ')
a = int(input())

if a==1 :
    sign_up()

elif a==2:
    sign_in()
