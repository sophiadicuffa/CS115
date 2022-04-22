"""
Group Project Part 2
Sophia, Mike, Elizabeth
We pledge our honor that we have abided by the Stevens Honor System
4/18/22
"""

MUSIC_FILE = "musicrecplus_ex1.txt"

#AUTHOR: Sophia
def loadUsers(fileName):
    ''' Reads in a file of stored users' preferences
        stored in the file 'fileName'.
        Returns a dictionary containing a mapping
        of user names to a list preferred artists
    '''
    file = open(fileName, 'r')
    userDict = {}
    for line in file:
        [userName, bands] = line.strip().split(":")
        bandList = bands.split(",")
        bandList.sort()
        userDict[userName] = bandList
    file.close()
    return userDict

#AUTHORS: Sophia and Liz
def menu():
    """Displays the menu and sends user to proper locations when inputs entered"""
    while(True):
        print("Enter a letter to choose an option:")
        print("\te - Enter preferences")
        print("\tr - Get recommendations")
        print("\tp - Show most popular artists")
        print("\th - How popular is the most popular")
        print("\tm - Which user has the most likes")
        print("\tq - Save and quit")
        selection = input("Enter selection: ")
        if "e" == selection:
            getPreferences(userName, userMap)
            saveUserPreferences(userName, userMap[userName], userMap, MUSIC_FILE)
        elif "r" == selection:
            print(getRecommendations(userName, userMap[userName], userMap))
        elif "p" == selection:
            printPopularArtists(userMap)
        elif "h" == selection:
            howPopular(userName, userMap[userName], userMap)
        elif "m" == selection:
            mostLikes(userMap)
        elif "q" == selection:
            saveUserPreferences(userName, userMap[userName], userMap, MUSIC_FILE)
            break
        else:
            print("Invalid input, please try again")

#AUTHORS: Liz
def getPreferences(userName, userMap):
    """Returns a list of the user's preferred artists.
    If the system already knows the user, it gets the
    current preferences from the userMap dictionary and
    then asks the user if they have a new preference.
    If user is new, it simply asks for preferences.
    """
    newPref = ""
    if userName in userMap:
        prefs = userMap[userName]
        print("I see that you have used this system before.")
        print("Your current music taste includes:")
        for artist in prefs:
            print(artist)
        newPref = input("Enter an artist that you like ( Enter to finish ):")
    else:
        prefs = []
        print("I see you're a new user, welcome!")
        newPref = input("Enter an artist that you like ( Enter to finish ):")

    while newPref != "":
        prefs.append(newPref.strip().title())
        newPref = input("Enter an artist that you like ( Enter to finish ):")

    prefs.sort()
    prefs = set(prefs) #sorts out any repeats
    userMap[userName] = prefs
    return prefs

def saveUserPreferences(userName, prefs, userMap, fileName):
    ''' Writes all of the user preferences to the file.
        Returns nothing. '''
    userMap[userName] = prefs
    file = open(fileName, "w")
    for user in userMap:
        toSave = str(user) + ":" + ",".join(userMap[user]) + \
                    "\n"
        file.write(toSave)
    file.close()

def getRecommendations(currUser, prefs, userMap):
    """ Gets recommendations for a user (currUser) based on the users
    in userMap (a dictionary) and the user's preferences in pref (a list).
    Returns a list of recommended artists."""
    bestUser = findBestUser(currUser, prefs, userMap)
    if bestUser == None:
        return("No recommendations available at this time .")
    recommendations = drop(prefs, userMap[bestUser])
    recommendations.sort()
    return recommendations

def findBestUser(currUser, prefs, userMap):
    """Find the user with the most common prefs as the current user"""
    users = list(userMap.keys())
    bestScore = -1
    bestMatch = None
    for user in users:
        if user[-1] == "$": #looks to see what the last character of user is
            continue #skips this user
        if user == currUser:
            continue
        score = numMatches(prefs, userMap[user])
        if score > bestScore:
            bestScore = numMatches(prefs, userMap[user])
            bestMatch = user
    return bestMatch

def drop(list1, list2):
    '''Return a new list that contains only the elements in
        list2 that were NOT in list1. '''
    list3 = []
    for i in list2:
        if i not in list1:
            list3 += [i]
    return list3

def numMatches( list1, list2 ):
    ''' return the number of elements that match between
        two sorted lists '''
    same = 0
    for i in list1:
        if i in list2:
            same += 1
    return same

# AUTHOR: Sophia
def printPopularArtists(userMap):
    '''determines most popular artist'''
    artists = {}
    for user in userMap:
        for artist in userMap[user]:
            if artist in artists:
                artists[artist] += 1
            else:
                artists[artist] = 1
    popularArtists = []
    count = 0
    for artist in artists:
        if artists[artist] > count:
            popularArtists = []
            popularArtists += [artist]
            count = artists[artist]
        elif artists[artist] == count:
            popularArtists += [artist]
    if len(popularArtists) == 0:
        print("Sorry, there are no preferences entered yet!")
    elif len(popularArtists) > 1:
        print("The most popular artists are...")
    else:
        print("The most popular artist is...")
    for artist in popularArtists:
        print(artist)
        
def mostLikes(userMap):
    '''determines person with the most likes and prints their name and
        preferences'''
    length = 0
    mostLikes = ""
    for user in userMap:
        if len(userMap[user]) > length:
            mostLikes = user
            length = len(userMap[user])
    if length != 0:
        nameOfUser = mostLikes
        print("The user with the most likes is...")
        print(mostLikes)
        print(userMap[nameOfUser])
    else:
        print("Sorry, no users could be found with preferences")
        
# AUTHOR: Mike
def howPopular(currUser, prefs, userMap):
    """Find the user with the most common prefs as the current user"""
    users = list(userMap.keys())
    bestScore = -1
    bestMatch = None
    for user in users:
        if user[-1] == "$": #looks to see what the last character of user is
            continue #skips this user
        if user == currUser:
            continue
        score = numMatches(prefs, userMap[user])
        if score > bestScore:
            bestScore = numMatches(prefs, userMap[user])
    print("The most popular artist is mentioned ", bestScore, " times.")


        
#######start of program#########    
print("Welcome to the music recommender system!")

userName = input("Please enter your name: ") #establishes userName
print("Hello,", userName)

userMap = loadUsers(MUSIC_FILE) #reads through file and puts items in dict

if userName not in userMap: #checks to see if user is new
    getPreferences(userName, userMap)
    saveUserPreferences(userName, userMap[userName], userMap, MUSIC_FILE)

menu()
