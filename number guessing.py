import random
r=input('select the top of range')
print(r)
if r.isdigit():
    r=int(r)
    if r < 0:
        print('please write a number greater than zero next time')
        quit()
random_number= random.randrange(0,r)
guess = 0
while guess < 5:
    guess += 1
    user_guess = input('make a guess : ')
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print('Please type a number next time.')
        continue
    if user_guess == random_number:
        print('You guessed it correctly.')
        print(f'You got it in {guess} guesses') 
        break
    elif user_guess> random_number:
        print('Too high')
    elif user_guess<random_number:
        print('Too low')    
    else:
        print('You got wrong.') 
               