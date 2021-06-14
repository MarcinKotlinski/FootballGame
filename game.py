import turtle
import sys
import random

questions = {
    'Where does Cristiano ronaldo play?': "Real Madrid",
    'Where does Lionel Messi play?': "Barcelona",
    'Where does Neymar play?': 'PSG',
    'Where does Kylian Mbappé  play?': 'PSG',
    'Where does Zlatan Ibrahimović play? ': 'PSG',
    'Where does Paul Pogba play?': 'Manchester United',
    'Where does Gareth Bale play?': 'Real Madrid',
    'Where does Robert Lewandowski play?': ' Bayern Munich',
    'Where does Eden Hazard play?': 'Real Madrid',
    'Where does Sergio Agüero play? ': 'Man City',
    'Where does Sadio Mané play?': 'Liverpool',
    'Where does Jamie Vardy play?': 'Leicester City',
    'Where does Kevin De Bruyne play?': 'Man city',
    'Who is Chelseas GoalKeeper?': 'Kepa',
    'Whos the best Chelsea Midfielder?': 'KANTE!',
    'What animal has a long neck?': 'Giraffee',
    'Where does Mohamed Salah play?': 'Liverpool',
    'Where does Lingard play?': 'ManchesterCity',
    'What position does Virgil van Dijk play?': 'Defender',
    'What position does Karim Benzema play?': 'Striker',
    'What position does Manuel Neuer play?': 'GoalKeeper',
    'Where does Tony Kroos play?': 'RealMadrid',
    'What position does Peter Schmeichel play?': 'GoalKeeper',
    'What position does Son play?': 'Midfielder',
    'What position does Petr Cech play?': 'GoalKeeper'
}
turtle.color('black')
style = ('Arial', 30, 'italic')
turtle.bgpic("pitch.gif")
screen = turtle.Screen()
screen.setup(628, 402)
turtle.hideturtle()

def Win():
    if Kevin.position() == (540.00, 0.00):
        turtle.write('Win!', font=style, align='center')


def Loose():
    if Kevin.position() == (-540.00, 0.00):
        turtle.write('Loose!', font=style, align='center')


Kevin = turtle.Pen()
Kevin.up()

# print("What is 2 + 2?")
# question1 = int(sys.stdin.readline())
# if question1 == 4:
#     Kevin.forward(90)
# else:
#     Kevin.backward(90)
# Win()
# Loose()
#
# print("What is 10 - 5?")
# question2 = int(sys.stdin.readline())
# if question2 == 5:
#     Kevin.forward(90)
# else:
#     Kevin.backward(90)
# Win()
# Loose()
#
# print("What is 2 * 12?")
# question3 = int(sys.stdin.readline())
# if question3 == 24:
#     Kevin.forward(90)
# else:
#     Kevin.backward(90)
# Win()
# Loose()
#
# # print("What is 6 / 2?")
# question4 = int(sys.stdin.readline())
# if question4 == 3:
#     Kevin.forward(90)
# else:
#     Kevin.backward(90)
# Win()
# Loose()
#
# # print("What is 9 - 3?")
# question5 = int(sys.stdin.readline())
# if question5 == 6:
#     Kevin.forward(90)
# else:
#     Kevin.backward(90)
# Win()
# Loose()
#
# # print("What is 44 - 11?")
# question6 = int(sys.stdin.readline())
# if question6 == 33:
#     Kevin.forward(90)
# else:
#     Kevin.backward(90)
# # Win()
# # Loose()

while(Kevin.position() != (540.00,0.00) or Kevin.position() != (-540.00,0.00)):
    key = random.choice(list(questions))
    print(key)
    answer = str(sys.stdin.readline())
    if answer == "%s\n" % questions[key]:
        Kevin.forward(90)
    else:
        Kevin.backward(90)
    print(answer)
    print(questions[key])
    Win()
    Loose()

# print(Kevin.position())
turtle.mainloop()
