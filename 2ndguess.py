numbs=[2,5,6,9,12,15,21,27]

while True:
    ch=input('Please guess a number or type q to quit')
    if ch == 'q':
        break
    try:
        ch=int(ch)
    except ValueError:
        print('Please type a number')
    if ch in numbs:
        print('you have guessed right')
   
    else:
        print('You guessed wrong')
    


