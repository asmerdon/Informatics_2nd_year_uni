import sys
import requests
import pandas
import pandas as pd
from collections import OrderedDict
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, QInputDialog, QLineEdit

def App (QWidget):

    def action(inputff,inputGenre):
        url = 'https://query.wikidata.org/sparql'
        query = '''
            SELECT DISTINCT ?game ?gameLabel
            WHERE {?game wdt:P31 wd:Q7889.
            ?game wdt:P136  ?genre.
            ?genre rdfs:label ?genreLabel .
            FILTER CONTAINS(?genreLabel, "%s") .
            SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
            }
            LIMIT %s
        ''' % (inputGenre,inputff)
        r = requests.get(url, params = {'format': 'json', 'query': query})
        data = r.json()
        
        urls = []
        games = []
        for item in data["results"]["bindings"]:
            #games.append(OrderedDict({
            #    "game":item["gameLabel"]["value"]
            #    }))
            games.append(item["gameLabel"]["value"])
            urls.append(item["game"]["value"])

        for i in range(inputff):
            j = games[i]
            s = urls[i]
            tableWidget.setItem(i,0, QTableWidgetItem(j))
            tableWidget.setItem(i,1, QTableWidgetItem(s))
        df = pd.DataFrame(games)
        print(df)

    genres = ("Action", "Racing", "platformer")
    app = QApplication([])
    app.setStyle('Fusion')
    window = QWidget()
    layout = QVBoxLayout()
    inputff = QInputDialog.getInt(window, "Number", "Choose how many results you want")[0]
    #inputText = QLineEdit.text()
    
    def getText(self):
        text, okPressed = QInputDialog.getText(self, "Get text","Your name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            print(text)
            
    inputGenre = str(QInputDialog.getItem(window, "s", "Choose which genre you would like to see", genres, 0, False)[0])
    tableWidget = QTableWidget()
    tableWidget.setRowCount(inputff)
    tableWidget.setColumnCount(2)
    layout.addWidget(tableWidget)
    window.setLayout(layout)
    window.show()
    action(inputff,inputGenre)
    #app.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App(QWidget)
    sys.exit(app.exec_())
