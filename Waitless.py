

#user input
def greeting():
    app_greeting=input("Are you waiting to be seated or are you looking for a restaurant?")
    if greeting == "waiting":
        waiting()
    else:
        looking()

def waiting():
    location: input("Please enter the restaurant you're at.")
    restaurant_list=open("waitless.txt", "r")
    places=restaurant_list.readlines()
    for i in range(len(places)):
        places[i] = places[i].rstrip('\n') 

def looking():
    print("Here are the current wait times for each restaurant:")
    restaurant_list=open("waitless.txt", "r")
    places=restaurant_list.read()
    print(places)

     #location: input("Please select the restaurant you're at.")
    #restaurant_list=open("waitless.txt", "r")
    #reading

greeting()
