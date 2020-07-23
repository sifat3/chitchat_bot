import pyttsx3
friend = pyttsx3.init()
print("I can speak now.  My name is chitchat buddy.  I am not developed completely.   BUT soon I will.  I am your Computer   Companion   so   that   you   don't   get    bored   \nwhile   working on your computer.    now   i   can   not   understand   your     voice    but    soon    i will    can     ")
friend.say("I can speak now.  My name is chitchat buddy.  I am not developed completely.   BUT soon I will.  I am your Computer   Companion   so   that   you   don't   get    bored   while   working on your computer.    now   i   can   not   understand   your     voice    but    soon    i will   can     ")
friend.runAndWait()


#list of head password

main_password = 'mr.sifat0421'

#list of passwords

passwords = []

#list of users on this computer

users = []

#register user/users

print("Do you want to register as an admin in this pc?")
friend.say("Do you want to register as an admin in this pc?")
friend.runAndWait()

l = input("Yes/No? ")
if l.lower() == 'no':


    print("Okay then!")
    friend.say("Okay then!")
    friend.runAndWait()

elif l.lower() == 'yes':

    friend.say("please enter the main Password")
    friend.runAndWait()
    pas = input("please enter the Main Password: ")


    if pas == main_password:
        friend.say("May I know your name?,Please type it")
        friend.runAndWait()
        user_name = input("May I know your name?,Please type it: ")


        print("registering you as an admin!!")
        friend.say("registering you as an admin!!")
        friend.runAndWait()


        if user_name in users:
            print("You were previosly registered")
            friend.say("You were previosly registered")
            friend.runAndWait()
        else:
            user1 = user_name.lower()
            users.append(user1)
            print("now you have to choose a super rememberable password for you ")
            friend.say("now you have to choose a super rememberable password for you ")
            friend.runAndWait()

            friend.say("Please enter a password: ")
            friend.runAndWait()
            password = input("Please enter a password: ")


            if password in passwords:
                print("Sorry,choose another one,this one is already in use ")
                friend.say("Sorry,choose another one,this one is already in use ")
                friend.runAndWait()

            else:
                passwords.append(password)
                print("User register successfull!!")
                friend.say("User register successfull!!")
                friend.runAndWait()
    else:
        print("Sorry you can't register")
        friend.say("Sorry you can't register")
        friend.runAndWait()

else:
    print("sorry! can't get you")
    friend.say("sorry! can't get you")
    friend.runAndWait()

#list of people singed in or tried to in this pc

other_people = []


#output to show at first

print("Hello!! how are you? Um your chitchat buddy,you want to talk?")
friend.say("Hello!! how are you? Um your chitchat buddy,you   want      to   talk?")
friend.runAndWait()

#ask user if he/she wanna talk or not

talk = input('Yes/No? ')
if talk.lower() == 'no':
    print("okay nice to meet you,Bye")
    friend.say("okay nice to meet you,Bye")
    friend.runAndWait()

    k = input("may i know your name?")
    friend.say("may i know your name?")
    friend.runAndWait()

    name = k.lower()
    if name not in users:
        other_people.append(name)
    else:
        print("Welcome Admin " + name.title())
        friend.say("Welcome Admin " + name.title())
        friend.runAndWait()

elif talk.lower() == 'yes':

    friend.say("may i know your name?")
    friend.runAndWait()
    k = input("may i know your name?: ")


    name = k.lower()
    if name not in users:
        other_people.append(name)
    else:
        print("Welcome Admin " + name.title())
        friend.say("Welcome Admin " + name.title())
        friend.runAndWait()
    print("I have joke for you")
    friend.say("I have a joke for you")
    friend.runAndWait()

    print("Two guys stole a calendar. They got six months each.HAHAHAHA")
    friend.say("Two guys stole a calendar. They got six months each    HAHAHAHA")
    friend.runAndWait()

    friend.say("How was it?")
    friend.runAndWait()

    k = input("How was it?: ")



    if k.lower() == 'lame':
        print("If I am lame,you're lame too,    because you are making me")
        friend.say("If I am lame,you're lame too,    because you are making me")
        friend.runAndWait()



    else:
        print("thank you for your compliment")
    friend.say("thank you for your compliment")
    friend.runAndWait()



    friend.say(" can I say something?")
    friend.runAndWait()
    say = input(" can I say something?: ")
    if say == 'yes':
        print("I don't think you can complete me   fast     because   you are too slow   and    lame also ")
        friend.say("I don't think you can complete me   fast     because   you are too slow   and    lame also ")
        friend.runAndWait()
    else:
        print("HUH")

    print("")

else:
    print("Sorry!can't get you")
    friend.say("Sorry!can't get you")
    friend.runAndWait()


friend.say("Do      you     have  any      work        to do?")
friend.runAndWait()
print("Do you have any work to do?")