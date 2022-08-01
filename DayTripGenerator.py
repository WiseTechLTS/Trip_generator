import random
# Destinations list
destination: list[str] = ['Alabama - Montgomery', 'Alaska - Juneau', 'Arizona - Phoenix', 'Arkansas - Little Rock', 'California - Sacramento', 'Colorado - Denver', 'Connecticut - Hartford', 'Delaware - Dover', 'Florida - Tallahassee', 'Georgia - Atlanta', 'Hawaii - Honolulu', 'Idaho - Boise', 'Illinois - Springfield', 'Indiana - Indianapolis', 'Iowa - Des Moines', 'Kansas - Topeka', 'Kentucky - Frankfort', 'Louisiana - Baton Rouge', 'Maine - Augusta', 'Maryland - Annapolis', 'Massachusetts - Boston', 'Michigan - Lansing', 'Minnesota - St. Paul', 'Mississippi - Jackson', 'Missouri - Jefferson City', 'Montana - Helena', 'Nebraska - Lincoln', 'Nevada - Carson City', 'New Hampshire - Concord', 'New Jersey - Trenton', 'New Mexico - Santa Fe', 'New York - Albany', 'North Carolina - Raleigh', 'North Dakota - Bismarck', 'Ohio - Columbus', 'Oklahoma - Oklahoma City', 'Oregon - Salem', 'Pennsylvania - Harrisburg', 'Rhode Island - Providence', 'South Carolina - Columbia', 'South Dakota - Pierre', 'Tennessee - Nashville', 'Texas - Austin', 'Utah - Salt Lake City', 'Vermont - Montpelier', 'Virginia - Richmond', 'Washington - Olympia', 'West Virginia - Charleston', 'Wisconsin - Madison', 'Wyoming - Cheyenne']
# Restaurants List
restaurants: list[str] = ['1 McDonalds', '2	Starbucks', '3	Chick-fil-A', '4 Taco Bell', '5	Wendys', '6	Dunkin', '7	Burger King', '8 Subway', '9 Dominos', '10	Chipotle Mexican Grill', '11 Sonic Drive-In', '12 Panera Bread', '13 Pizza Hut', '14 KFC', '15	Popeyes', '16	Panda Express', '17	Dairy Queen', '18	Arbys', '19	Little Caesars', '20	Olive Garden', '21	Applebees', '22	Jack in the Box', '23	Buffalo Wild Wings', '24	Texas Roadhouse', '25	Papa Johns', 'Rank	Chain', '26	Chilis Grill & Bar', '27	Whataburger', '28	IHOP', '29	Outback Steakhouse', '30	Culvers', '31	Dennys', '32	Cracker Barrel', '33	Raising Canes Chicken Fingers', '34	Red Lobster', '35	Jimmy Johns', '36	The Cheesecake Factory', '37	Zaxbys', '38	LongHorn Steakhouse', '39	Jersey Mikes Subs', '40	Wingstop', '41	Five Guys', '42	Hardees', '43	In-N-Out Burger', '44	Carls Jr.', '45	Bojangles', '46	Red Robin', '47	Waffle House', '48	Golden Corral', '49	BJs Restaurant & Brewhouse', '50	Firehouse Subs']
transportation: list[str] = ['Cab', 'Walking', 'Private Jet']
entertainment: list[str] = ['Movie', 'Theatre', 'Street Art', 'Tour', 'Museum']
## Our Generator will begin
def display_title() -> None:
    print('Welcome to Wisecarver Day Trip Generator!')
    choice: str = input('Shall we begin? Simply type yes or no: ')
    if choice == 'yes':
        print('Destination is up first!')
    else:
        print('Error, try again.')


def list_loop(list, topic):
    random_pick = random.choice(list)
    user_reply = input(
        f'How does {random_pick} sound for your {topic}? Enter yes or no to make a selection: ')
    if user_reply == 'yes':
        print("Great decision!")
    elif user_reply == 'no':
        print('We have many more to choose from, no worries.')
        random_pick = random.choice(list)
        user_reply = input(
            f'What about {random_pick}? Enter yes or no to make a selection: ')
    if user_reply == 'yes':
        print("Like I said, something for everyone.")
        return random.choice(list)


def complete(dest, rest, trans, entertain):
    satisfied = input(
        'Are you satisfied with all your choices? Enter yes or no to make a selection: ')
    while satisfied == 'yes':
        print("Great Choice!")
        print(
            f"You will enjoy a day trip in {dest} where you will eat at {rest}. You will use {trans} to travel and attend {entertain}!")
    else:
        input('The End')


final_destination = list_loop(destination, "destinations")
final_restaurant = list_loop(restaurants, "restaurants")
final_transportation = list_loop(transportation, "transportation")
final_entertainment = list_loop(entertainment, "entertainment")


for number in range(1):
    print(f'Enjoy {final_destination}')

    print(f"The food at {final_restaurant} should be pleasurable.")

    print(f"Today your mode of transportation will be {final_transportation}")

    print(f"Please feel free to use it to attend {final_entertainment}!")

    input('Great Job! You decided that in no time!  Are you sure this is the trip you want?: type yes or no ')
    complete_user = input('')
    if complete_user == 'yes':
        print('T H A N K  Y O U  F O R  U S I N G  W I S E C A R V E R  D A Y  T R I P  G E N E R A T O R')
    elif complete_user == 'no':
        print('Have a great trip!')
# Destinations list
destination: list[str] = ['Alabama - Montgomery', 'Alaska - Juneau', 'Arizona - Phoenix', 'Arkansas - Little Rock', 'California - Sacramento', 'Colorado - Denver', 'Connecticut - Hartford', 'Delaware - Dover', 'Florida - Tallahassee', 'Georgia - Atlanta', 'Hawaii - Honolulu', 'Idaho - Boise', 'Illinois - Springfield', 'Indiana - Indianapolis', 'Iowa - Des Moines', 'Kansas - Topeka', 'Kentucky - Frankfort', 'Louisiana - Baton Rouge', 'Maine - Augusta', 'Maryland - Annapolis', 'Massachusetts - Boston', 'Michigan - Lansing', 'Minnesota - St. Paul', 'Mississippi - Jackson', 'Missouri - Jefferson City',
                          'Montana - Helena', 'Nebraska - Lincoln', 'Nevada - Carson City', 'New Hampshire - Concord', 'New Jersey - Trenton', 'New Mexico - Santa Fe', 'New York - Albany', 'North Carolina - Raleigh', 'North Dakota - Bismarck', 'Ohio - Columbus', 'Oklahoma - Oklahoma City', 'Oregon - Salem', 'Pennsylvania - Harrisburg', 'Rhode Island - Providence', 'South Carolina - Columbia', 'South Dakota - Pierre', 'Tennessee - Nashville', 'Texas - Austin', 'Utah - Salt Lake City', 'Vermont - Montpelier', 'Virginia - Richmond', 'Washington - Olympia', 'West Virginia - Charleston', 'Wisconsin - Madison', 'Wyoming - Cheyenne']
# Restaurants List
restaurants: list[str] = ['1 McDonalds', '2	Starbucks', '3	Chick-fil-A', '4 Taco Bell', '5	Wendys', '6	Dunkin', '7	Burger King', '8 Subway', '9 Dominos', '10	Chipotle Mexican Grill', '11 Sonic Drive-In', '12 Panera Bread', '13 Pizza Hut', '14 KFC', '15	Popeyes', '16	Panda Express', '17	Dairy Queen', '18	Arbys', '19	Little Caesars', '20	Olive Garden', '21	Applebees', '22	Jack in the Box', '23	Buffalo Wild Wings', '24	Texas Roadhouse', '25	Papa Johns', 'Rank	Chain', '26	Chilis Grill & Bar',
                          '27	Whataburger', '28	IHOP', '29	Outback Steakhouse', '30	Culvers', '31	Dennys', '32	Cracker Barrel', '33	Raising Canes Chicken Fingers', '34	Red Lobster', '35	Jimmy Johns', '36	The Cheesecake Factory', '37	Zaxbys', '38	LongHorn Steakhouse', '39	Jersey Mikes Subs', '40	Wingstop', '41	Five Guys', '42	Hardees', '43	In-N-Out Burger', '44	Carls Jr.', '45	Bojangles', '46	Red Robin', '47	Waffle House', '48	Golden Corral', '49	BJs Restaurant & Brewhouse', '50	Firehouse Subs']
transportation: list[str] = ['Cab', 'Walking', 'Private Jet']
entertainment: list[str] = ['Movie', 'Theatre', 'Street Art', 'Tour', 'Museum']
list_loop(destination, "destinations")
list_loop(restaurants, "restaurants")
list_loop(transportation, "transportation")
list_loop(entertainment, "entertainment")

for number in range(1):
    print(f'Enjoy {final_destination}')

    print(f"The food at {final_restaurant} should be pleasurable.")

    print(f"Today your mode of transportation will be {final_transportation}")

    print(f"Please feel free to use it to attend {final_entertainment}!")

    input('Great Job! You decided that in no time!  Are you sure this is the trip you want?: type yes or no ')
    complete_user = input('')
    while complete_user == 'yes':
        print('T H A N K  Y O U  F O R  U S I N G  W I S E C A R V E R  D A Y  T R I P  G E N E R A T O R')
    break
