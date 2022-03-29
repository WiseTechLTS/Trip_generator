
import random 
import datetime 

def display_title():
    print("W e l c o m e   t o   W i s e c a r v e r   D a y   T r i p   G e n e r a t o r!")
    choice = input('Shall we begin? Simply type yes or no: ')
    if choice == 'yes':
        print("We will start with choosing your Destination!")
    else:
        print("Don't worry, it will be over in no time")

display_title()
pass

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

destinations = ['Colton, California', 'Frankfurt, Germany', 'Glendale, Arizona', 'Houston, Texas', 'Lake Tahoe, Nevada', 'Ontario, Canada', 'Reno, Nevada', 'San Diego, California', 'Seattle, Washington', 'Seoul, South Korea']
restaurants = ['Dirt M Good', 'Free Food Only', 'In N Out', 'Octagon', 'Pizza Shack', 'Roadkill Grill', 'Sams Deli', 'Share a Bite', 'Steak 48', 'Whataburger']
transportation = ['Bicycle', 'Green Scooter', 'Hitch hike', 'Lyft', 'Run', 'Skate Board', 'Taxi', 'Tram', 'Uber', 'Walking']
entertainment =  ['Club Octagon', 'Dancing', 'Hack a Thon', 'Indoor Rave', 'Iphone Zoom Meeting', 'Movie Theatre', 'Open Mic', 'Park', 'Stadium Rave', 'Vino & Wine']

def display_title():
    print("W e l c o m e   t o   W i s e c a r v e r   D a y   T r i p   G e n e r a t o r!")
    choice = input('Shall we begin? Simply type yes or no: ')
    if choice == 'yes':
        print("We will start with choosing your Destination!")
    else:
        print("Don't worry, it will be over in no time")

def list_loop(list, topic):
    random_pick = random.choice(list)
    user_reply = input(f'How does {random_pick} sound for your {topic}? Enter yes or no to make a selection: ')
    if user_reply == 'yes':
        print("Great decision!")
    elif user_reply == 'no':
        print('We have many more to choose from, no worries.')       
        random_pick = random.choice(list)
        user_reply = input(f'What about {random_pick}? Enter yes or no to make a selection: ')
    if  user_reply == 'yes':
        print("Like I said, something for everyone.")
        return random.choice(list)

def complete(dest, rest, trans, entertain):
    satisfied = input('Are you satisfied with all your choices? Enter yes or no to make a selection: ')
    while satisfied == 'yes':
        print("Great Choice!")
        print(f"You will enjoy a day trip in {dest} where you will eat at {rest}. You will use {trans} to travel and attend {entertain}!")
    else:
        input('The End')

final_destination = list_loop(destinations, "destinations")
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
    if  complete_user == 'yes':
        print('T H A N K  Y O U  F O R  U S I N G  W I S E C A R V E R  D A Y  T R I P  G E N E R A T O R')
    elif complete_user == 'no':
        print('Have a great trip!')
                
destinations = ['Colton, California', 'Frankfurt, Germany', 'Glendale, Arizona', 'Houston, Texas', 'Lake Tahoe, Nevada', 'Ontario, Canada', 'Reno, Nevada', 'San Diego, California', 'Seattle, Washington', 'Seoul, South Korea']
restaurants = ['Dirt M Good', 'Free Food Only', 'In N Out', 'Octagon', 'Pizza Shack', 'Roadkill Grill', 'Sams Deli', 'Share a Bite', 'Steak 48', 'Whataburger']
transportation = ['Bicycle', 'Green Scooter', 'Hitch hike', 'Lyft', 'Run', 'Skate Board', 'Taxi', 'Tram', 'Uber', 'Walking']
entertainment = ['Club Octagon', 'Dancing', 'Hack a Thon', 'Indoor Rave', 'Iphone Zoom Meeting', 'Movie Theatre', 'Open Mic', 'Park', 'Stadium Rave', 'Vino & Wine']
    

display_title()
pass

list_loop(destinations, "destinations")
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
    while  complete_user == 'yes':
        print('T H A N K  Y O U  F O R  U S I N G  W I S E C A R V E R  D A Y  T R I P  G E N E R A T O R')
    break