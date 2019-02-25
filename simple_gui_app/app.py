from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from mainwindow import Ui_MainWindow
import time
from urllib.request import urlopen
import json

URL="https://mapa.idsjmk.cz/api/vehicles.json"

@pyqtSlot()
def clickSlot():
    vehicles_json = urlopen(URL)
    vehicles = json.load(vehicles_json)
    print(vehicles["Vehicles"])
    ui.label.setNum(len(vehicles["Vehicles"]))


app = QtWidgets.QApplication([])

w = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(w)
ui.pushButton.clicked.connect(clickSlot)

w.show()
app.exec()
