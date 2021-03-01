command = ''
started = False
while True:
    command = input('>').lower()
    if command == 'start':
        if started:
            print('Car started already!')
        else:
            started = True
            print('Start car!')
    elif command == 'stop':
        if not started:
            print('Car is stopped already!')
        else:
            started = False
            print('Stop car!')
    elif command == 'help':
        print('''
start = Car is ready to go!
stop = stop the car now!
quit = exit the game''')
    elif command == 'quit':
        print('exiting game...')
        break
    else:
        print("I'm not sure what you mean")

