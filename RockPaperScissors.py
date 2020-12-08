from random import randint

t=['Rock','Paper','Scissors']

computer=t[randint(0, 2)]

player=False

while player==False:
    player=input('Rock Paper Scissors')
    print('Player got :',player)
    print('Compuer got :', computer)
    if player==computer:
        print('Match tied')
    elif player=="Rock":
        if computer== 'Paper':
            print('You lose !', computer, ' covers the ', player)
        else:
            print('You won', player,' smashes the ', computer)
    elif player=="Paper":
        if computer== 'Rock':
            print('You win !', player,' covers the ', computer)
        else:
            print('You lose !', computer, ' cut ', computer, ' into pieces')
    elif player=="Scissors":
        if computer== 'Paper':
            print('You won ! ',player,' cuts the ',player,' into pieces')
        else:
            print('You lose !', computer, ' smashes the ', player)
    else:
        print('Make sure you check spelling correctly')
    a=input('Do you continue to play?Y | N')
    if a.lower()=='y':
        player=False
        computer=t[randint(0, 2)]
    else:
        player=True
        print('Thanks for playing')
        break