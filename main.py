print('Welcome to Registration!')
print('1. Student 2. Admin 3. Logout')
main = input('Enter: ')

bus174 = int(67)
bus175 = int(65)
bus174waitlist = int(0)
bus175waitlist = int(0)

while main != '3':
    if main == '1':
        print()
        print('Which course would you like to register for? ')
        print()
        print('1. BUS 174 2. BUS 175 3. Main Menu')
        course = input('Enter: ')
        if course == '1':
            print()
            print('There are ', 75 - bus174, 'of 75 seats available for BUS 174')
            print('Would you like to 1. add or 2. drop BUS 174? ')
            adddrop = input()
            if adddrop == '1':
                if 0 < bus174 < 75:
                    bus174 = bus174 + 1
                    print()
                    print('You have been added to BUS 174')
                    print(75 - bus174, 'of 75 seats remaining for BUS 174')
                    print()
                elif bus174 > 74:
                    if bus174waitlist >= 10:
                        print()
                        print('Waitlist for BUS 174 is full. ')
                        print()
                    elif bus174waitlist < 10: 
                        bus174waitlist = bus174waitlist + 1
                        print()
                        print('You have been added to the waitlist for BUS 174')
                        print(10 - bus174waitlist, 'of 10 seats remain on the waitlist')
                    
            
            if adddrop == '2':
                if 0 < bus174 < 75:
                    bus174 = bus174 - 1
                    print()
                    print('You have been dropped from BUS 174')
                    print(75 - bus174, 'seats remaining for BUS 174')
                    print()
                elif bus174 > 74:
                    if bus174waitlist < 1:
                        bus174 = bus174 - 1
                        print()
                        print('You have been dropped from BUS 174')
                        print(75 - bus174, 'seats remaining for BUS 174')
                        print()
                    elif bus174waitlist >= 1:
                        bus174waitlist = bus174waitlist - 1
                        print()
                        print('You have been dropped from the waitlist for BUS 174')
                        print(10 - bus174waitlist, 'seats remain on the waitlist')
                        if bus174waitlist < 0:
                            print('Waitlist for BUS 174 is empty. ')
            
        elif course == "2":
            print()
            print('There are ', 75 - bus175, 'of 75  seats available for BUS 175')
            print('Would you like to 1. add or 2. drop BUS 175? ')
            adddrop = input('Enter: ')
            if adddrop == '1':
                if 0 < bus175 < 75:
                    bus175 = bus175 + 1
                    print()
                    print('You have been added to BUS 175')
                    print(75 - bus175, 'of 75 seats remaining for BUS 175')
                    print()
                elif bus175 > 74:
                    if bus175waitlist >= 10:
                        print()
                        print('Waitlist for BUS 175 is full. ')
                        print()
                    elif bus175waitlist < 10: 
                        bus175waitlist = bus175waitlist + 1
                        print()
                        print('You have been added to the waitlist for BUS 175')
                        print(10 - bus175waitlist, 'of 10 seats remain on the waitlist')

                
            if adddrop == '2':
                if 0 < bus175 < 75:
                    bus175 = bus175 - 1
                    print()
                    print('You have been dropped from BUS 175')
                    print(75 - bus175, 'seats remaining for BUS 174')
                    print()
                elif bus175 > 74:
                    if bus175waitlist < 1:
                        bus175 = bus175 - 1
                        print()
                        print('You have been dropped from BUS 175')
                        print(75 - bus175, 'seats remaining for BUS 175')
                        print()
                    elif bus175waitlist >= 1:
                        bus175waitlist = bus175waitlist - 1
                        print()
                        print('You have been dropped from the waitlist for BUS 175')
                        print(10 - bus175waitlist, 'seats remain on the waitlist')
                        if bus175waitlist < 0:
                            print('Waitlist for BUS 175 is empty. ')

        elif course == '3':
            print()
            print('Welcome to Registration!')
            print('1. Student 2. Admin 3. Exit')
            main = input('Enter: ')
    
    elif main == '2':
        print()
        print('1. View Students 2. View Waitlist 3. Main Menu' )
        admin = input('Enter: ')
        if admin == '1':
            print()
            print('There are ', bus174, 'students enrolled. With ', 75 - bus174, 'seats remaining for BUS 174. ')
            print('There are ', bus175, 'students enrolled. With ', 75 - bus175, 'seats remaining for BUS 175. ')
            print()
        elif admin == '2':  
            print()
            print('See waitlist: 1. BUS174 2. BUS175 3. Main Menu')
            viewwl = input('Enter: ')
            if viewwl == '1':
                print()
                print('There are ', bus174waitlist, 'students on the waitlist for BUS 174. ')
                print()
            elif viewwl == '2':
                print()
                print('There are ', bus175waitlist, 'students on the waitlist for BUS 175. ')
                print()
        elif admin == '3':
            print()
            print('Welcome to Registration!')
            print('1. Student 2. Admin 3. Exit')
            main = input('Enter: ')

print()
print('Thank you for using our registration system! ')
