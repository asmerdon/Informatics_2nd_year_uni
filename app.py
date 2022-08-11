def action():
    import requests
    import pandas
    url = 'https://query.wikidata.org/sparql'
    query = """
        SELECT ?game ?gameLabel
        WHERE {?game wdt:P31 wd:Q7889.
        ?game wdt:P136  ?genre.
        ?genre rdfs:label ?genreLabel .
        FILTER CONTAINS(?genreLabel, "action") .
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
        }
        LIMIT 10
    """
    r = requests.get(url, params = {'format': 'json', 'query': query})
    data = r.json()

    import pandas as pd
    from collections import OrderedDict

    games = []
    for item in data["results"]["bindings"]:
        games.append(OrderedDict({
            "game":item["gameLabel"]["value"]
            }))

    df = pd.DataFrame(games)

    print(df)


def racing():
    import requests
    import pandas
    url = 'https://query.wikidata.org/sparql'
    query = """
        SELECT DISTINCT ?game ?gameLabel
        WHERE {
        ?game wdt:P31 wd:Q7889.
        ?game wdt:P136  ?genre.
        ?genre rdfs:label ?genreLabel .
        FILTER CONTAINS(?genreLabel, "racing") .
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
        }
        LIMIT 10
    """
    r = requests.get(url, params = {'format': 'json', 'query': query})
    data = r.json()

    import pandas as pd
    from collections import OrderedDict

    games = []
    for item in data["results"]["bindings"]:
        games.append(OrderedDict({
            "game":item["gameLabel"]["value"]
            }))

    df = pd.DataFrame(games)
    df.set_index("game", inplace=True)
    df.head()
    print(df)

def platformer():
    import requests
    import pandas
    url = 'https://query.wikidata.org/sparql'
    query = """
        SELECT DISTINCT ?game ?gameLabel
        WHERE {
        ?game wdt:P31 wd:Q7889.
        ?game wdt:P136  ?genre.
        ?genre rdfs:label ?genreLabel .
        FILTER CONTAINS(?genreLabel, "platformer") .
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
        }
        LIMIT 10
    """
    r = requests.get(url, params = {'format': 'json', 'query': query})
    data = r.json()

    import pandas as pd
    from collections import OrderedDict

    games = []
    for item in data["results"]["bindings"]:
        games.append(OrderedDict({
            "game":item["gameLabel"]["value"]
            }))

    df = pd.DataFrame(games)
    df.set_index("game", inplace=True)
    df.head()
    print(df)


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
button1 = QPushButton("Action")
button2 = QPushButton("Racing")
button3 = QPushButton("Platformer")
def on_button_clicked_action():
    action()
def on_button_clicked_racing():
    racing()
def on_button_clicked_platformer():
    platformer()
button1.clicked.connect(on_button_clicked_action)
button2.clicked.connect(on_button_clicked_racing)
button3.clicked.connect(on_button_clicked_platformer)
layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)
window.setLayout(layout)
window.show()
app.exec_()
