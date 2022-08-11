import requests
import pandas
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, QInputDialog, QLineEdit

#~ currently breaks on certain entries  for extra info specifically publicationdate and publisher, i think it may be to do with those entries not having the infomation
#~ also each entry is treated as a seperate game for each platform it is released on

def action(inputff,inputGenre):
    url = 'https://query.wikidata.org/sparql' #the data we are querying
    query = ''' 
        SELECT DISTINCT ?game ?gameLabel ?publisher ?publisherLabel ?developer ?developerLabel ?publicationdate ?publicationdateLabel ?platform ?platformLabel
        WHERE {?game wdt:P31 wd:Q7889.
        ?game wdt:P136  ?genre.
        ?genre rdfs:label ?genreLabel .
        FILTER CONTAINS(?genreLabel, "%s") .
        OPTIONAL{?game wdt:P123 ?publisher .}
        OPTIONAL{?game wdt:P178 ?developer .}
        OPTIONAL{?game wdt:P577 ?publicationdate .}
        OPTIONAL{?game wdt:P400 ?platform .}
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
        }
        LIMIT %s
    ''' % (inputGenre,inputff)

    #The sparql query we are using 
    r = requests.get(url, params = {'format': 'json', 'query': query})
    data = r.json() #the data we receive once the query has completed converted into JSON format
    #~ print(data)
    
    gameLabels = []
    gameUrls = []
    
    publisherLabels = []
    publisherUrls = []
    
    developerLabels = []
    developerUrls = []
    
    publicationdateLabels = []
    
    platformLabels = []
    platformUrls = []
    
    for item in data["results"]["bindings"]: #iterating through the data and getting the information we need put into usable lists
        gameLabels.append(item["gameLabel"]["value"])
        gameUrls.append(item["game"]["value"])
        publisherLabels.append(item["publisherLabel"]["value"])
        publisherUrls.append(item["publisher"]["value"])
        
        developerLabels.append(item["developerLabel"]["value"])
        developerUrls.append(item["developer"]["value"])
        
        publicationdateLabels.append(str(item["publicationdateLabel"]["value"]))
        
        platformLabels.append(item["platformLabel"]["value"])

    for i in range(inputff): #updating the table in the GUI 
        a = gameLabels[i]
        b = gameUrls[i]
        
        c = publisherLabels[i]
        d = publisherUrls[i]
        
        e = developerLabels[i]
        f = developerUrls[i]
        
        g = publicationdateLabels[i]
        
        h = platformLabels[i]
        
        tableWidget.setItem(i,0, QTableWidgetItem(a))
        tableWidget.setItem(i,1, QTableWidgetItem(b))
        tableWidget.setItem(i,2, QTableWidgetItem(c))
        tableWidget.setItem(i,3, QTableWidgetItem(d))
        tableWidget.setItem(i,4, QTableWidgetItem(e))
        tableWidget.setItem(i,5, QTableWidgetItem(f))
        tableWidget.setItem(i,6, QTableWidgetItem(g))
        tableWidget.setItem(i,7, QTableWidgetItem(h))
        
    df = pd.DataFrame(gameLabels)
    #~ print(data)



genres = ("action", "racing","platformer","2D","strategy","shooter","puzzle") #the genres we are querying

app = QApplication([])
app.setStyle('Fusion') #style set for the windows
window = QWidget()
layout = QVBoxLayout() #the layout used for our GUI
inputff = QInputDialog.getInt(window, "Number", "Choose how many results you want")[0] #users input for amount of results
inputGenre = str(QInputDialog.getItem(window, "s", "Choose which genre you would like to see", genres, 0, False)[0]) #user input for genre
tableWidget = QTableWidget() #setting up of the table
tableWidget.setRowCount(inputff)
tableWidget.setColumnCount(8)
layout.addWidget(tableWidget) #adding widgets to the GUI
window.setLayout(layout)
window.show() #displaying the GUI
action(inputff,inputGenre) #executing the function that queries wikipedia
app.exec_()
