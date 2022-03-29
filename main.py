# Options for destinations, restaurants, transportationm, entertainment

destinations = ['Colton, California', 'Frankfurt, Germany', 'Glendale, Arizona', 'Houston, Texas', 'Lake Tahoe, Nevada', 'Ontario, Canada', 'Reno, Nevada', 'San Diego, California', 'Seattle, Washington', 'Seoul, South Korea']
#destinations.sort() --Sorts list to be in alphabetical order
restaurants = ['Dirt M Good', 'Free Food Only', 'In N Out', 'Octagon', 'Pizza Shack', 'Roadkill Grill', 'Sams Deli', 'Share a Bite', 'Steak 48', 'Whataburger']

transportation = ['Bicycle', 'Green Scooter', 'Hitch hike', 'Lyft', 'Run', 'Skate Board', 'Taxi', 'Tram', 'Uber', 'Walking']

entertainment=  ['Club Octagon', 'Dancing', 'Hack a Thon', 'Indoor Rave', 'Iphone Zoom Meeting', 'Movie Theatre', 'Open Mic', 'Park', 'Stadium Rave', 'Vino & Wine']

import random 
#import random so we can make random choices in lists

import datetime 
#brings current date and time values into the console

x = datetime.datetime.now()
print(x)


def display_title():  
    print("Welcome to Wisecarver Day Trip Generator!")
#Program Welcome

#Loop for random choosing/ set parametes as 1.list 2.topic

def list_loop(list, topic): 
    random_pick = random.choice(list)
    user_reply = input(f'How does {random_pick} sound for your {topic}? Enter Y/N to make a selection: ')
    if user_reply == 'y':
        return random_pick
    while user_reply == 'n':
        random_pick = random.choice(list)
        user_reply  = input(f'What about {random_pick}? Enter Y/N to make a selection: ')
    if user_reply == 'y':
        return random_pick 

def complete(dest, rest, trans, entertain):
    satisfied = input('Are you satisfied with all your choices? Enter Y/N to make a selection: ')
    if  satisfied == 'y':
        print("Great Choice!")
        satisfied = input("Are you satisfied with your choices? y/n: ")
        print(f"You will enjoy a day trip in {dest} where you will eat at {rest}. You will use {trans} to travel and attend {entertain}!")


display_title():
print("Come back anytime you would like for a quick way to plan a day out!")

final_destination = list_loop(destinations, "destinations")
final_restaurant = list_loop(restaurants, "restaurants")
final_transportations = list_loop(transportation, "transportation")
final_entertainment = list_loop(entertainment, "entertainment")

for number in range(2):
    print(f'Enjoy {final_destination} as well as the food at {final_restaurant}. Today your mode of transportation will be {final_transportations} please feel free to use it to attend {final_entertainment}! ')
    





## Obselete version

# # Options for destinations, restaurants, transportationm, entertainment
# destinations = ['Glendale, Arizona','Seoul, South Korea','Houston, Texas','Reno, Nevada','San Diego, California','Frankfurt, Germany','Ontario, Canada','Seattle, Washington','Colton, California','Lake Tahoe, Nevada']
# restaurants =  ['In N Out','Steak 48','Octagon','Sams Deli','Pizza Shack','Dirt M Good','Roadkill Grill','Free Food Only','Share a Bite','Whataburger']
# transportation =  ['Walking','Lyft','Uber','Taxi','Tram','Green Scooter','Run','Hitch hike','Skate Board','Bicycle']
# entertainment=  ['Movie Theatre','Indoor Rave','Hack a Thon','Open Mic','Vino & Wine','Dancing','Club Octagon','Stadium Rave','Iphone Zoom Meeting','Park']

# import random #import random so we can make random choices in lists

# def display_title(): #Program Welcome
#     print("Welcome to Wise Works Day Trip Generator!")

# def list_loop(list, topic):#Loop for random choosing/ set parametes as 1. list 2. topic
#     random_pick = random.choice(list)
#     user_reply = input(f'How does {random_pick} sound for your {topic}? Y/N: ')
#     if user_reply == 'y' or user_reply == 'yes':
#         return random_pick
#     while user_reply == 'n' or user_reply == 'no':
#         random_pick = random.choice(list)
#         user_reply  = input(f'What about {random_pick}? y/n: ')
#         if user_reply == 'y' or user_reply == 'yes':
#             return random_pick 

# def complete(dest, rest, trans, entertain):
#     satisfied = input('Are you satisfied with all your choices? y/n: ')
#     if satisfied == 'y' or satisfied == 'yes':
#         print(f'You will your day in {dest} where your meal will be from {rest}. You will use {trans} to reach your destinations including {entertain}!')
#     while satisfied == 'n':
#         change = input("Type 1 to change Destination, 2 for Restaurant, 3 for Transportation or 4 for Entertainment. Press 0 to finalize changes: ")
#         if change == "1":
#             final_destination = list_loop(destinations, 'destinations')
#         elif change == "2":
#             final_restaurant = list_loop(restaurants, 'restautants')
#         elif change == "3":
#             final_transportation = list_loop(transportation, "transportation")
#         elif change == "4":
#             final_entertainment = list_loop(entertainment, "entertainment")
#         else:
#             satisfied = input("Are you satisfied with your choices? y/n: ")
#             print(f"You will enjoy a day trip in {dest} where you will eat at {rest}. You will use {trans} to travel and attend {entertain}!")
#             return

# display_title()
# final_destination = list_loop(destinations, "destinations")
# final_restaurant = list_loop(restaurants, "restaurants")
# final_transportations = list_loop(transportation, "transportation")
# final_entertainment = list_loop(entertainment, "entertainment")

# for number in range(3):
#     print(f'Enjoy {final_destination} as well as the food at {final_restaurant}. Today your mode of transportation will be {final_transportations} please feel free to use it to attend {final_entertainment}! ')

