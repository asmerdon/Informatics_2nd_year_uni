def socialising(gamesArr):
    finalArr = []
    for i in gamesArr:
        if (i["genreLabel"] == "open world") and (i["gamemodeLabel"] == "multiplayer video game"):
            finalArr.append(i)
    return finalArr

def reaction(gamesArr):
    finalArr = []
    genres = ["action-adventure game","third-person shooter", "first-person shooter", "fighting game", "survival horror", "racing video game", "Adventure game"]
    inputs = ["gamepad","mouse","computer keyboard"]
    for i in gamesArr:
        if (i["genreLabel"] in genres) and (i["inputLabel"] in inputs):
            finalArr.append(i)
    return finalArr

def problemSolving(gamesArr): #placeholder 
    finalArr = []
    genres = ["puzzle video game","survival horror","turn-based strategy video game","real-time strategy","real-time tactics" "4X", "strategy video game",""]
    inputs = ["computer keyboard"]
    gamemodes =[]
    for i in gamesArr:
        if (i["genreLabel"] in genres) and (i["inputLabel"] in inputs):
            finalArr.append(i)
    return finalArr

def creativity(gamesArr):
    finalArr = []
    genres = ["open world"]
    inputs = ["gamepad","Wii Remote"]
    for i in gamesArr:
        if (i["genreLabel"] in genres) and (i["gamemodeLabel"] in inputs):
            finalArr.append(i)
    return finalArr

def excercise(gamesArr):
    finalArr = []
    genres = ["adventure game","platformer","Platform"]
    inputs =["Wii Remote","Wii Balance Board","PlayStation Move","Kinect"]
    for i in gamesArr:
        if (i["genreLabel"] == "action-adventure game") and (i["inputLabel"] == "Wii Remote"):
            finalArr.append(i)
    return finalArr

def coordination(gamesArr):
    finalArr = []
    genres = ["adventure game","platformer","Platform"]
    inputs =["Wii Remote","Wii Balance Board","PlayStation Move","Kinect"]
    for i in gamesArr:
        if (i["genreLabel"] == "action-adventure game") and (i["inputLabel"] == "Wii Remote"):
            finalArr.append(i)
    return finalArr
