import random

user_wins=0
computer_wins=0

while True:
    user_input=input('Type Rock/Paper/Scissors or q to quit').lower()
    if user_input == 'q' :
        break
    options =['rock','paper','scissors']
    if user_input not in options:
        continue

    random_number=random.randint(0,2)
    #rock=0 , paper=1 ,scissors=2
    computer_pick=options[random_number]
    print(f'Computer picked {computer_pick}. ')
    if computer_pick=='rock' and user_input=='paper':
        print ('You win')
        user_wins +=1
    elif computer_pick=='paper' and user_input=='scissors':
        print ('You win')
        user_wins +=1   
    elif computer_pick=='scissors' and user_input=='rock':
        print ('You win')
        user_wins +=1  
    elif computer_pick=='paper' and user_input=='rock':
        print ('You lose')
        computer_wins+=1    
    elif computer_pick=='rock' and user_input=='scissors':
        print ('You lose')
        computer_wins+=1   
    elif computer_pick=='scissors' and user_input=='paper':
        print ('You lose')
        computer_wins+=1       
    else:
        print('It\'s a draw.')
print(f'You won {user_wins}times.')
print(f'You lost {computer_wins} times.')            
print('Goodbye')
