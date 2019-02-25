from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt, QVariant, pyqtSlot
from PyQt5.QtPositioning import QGeoCoordinate
from urllib.request import urlopen
import json

URL="https://mapa.idsjmk.cz/api/vehicles.json"

class ItemModel(QAbstractListModel):

	PosRole = Qt.UserRole + 1
	#Role = Qt.UserRole + 2

	_roles = {PosRole: b"posRole", Qt.DisplayRole: b"displayRole"}

	
	def __init__(self,parent=None,*args):
		super(ItemModel,self).__init__()
		self.vehicles = [{"name":1234,"pos":QGeoCoordinate(49,14)}]
		self.tramCheckBox = None
	
	def rowCount(self,parent=QModelIndex()):
		return len(self.vehicles)
	
	def columnCount(self,parend=QModelIndex()):
		return 1
	
	def data(self,index,role=Qt.DisplayRole):
		if role == Qt.DisplayRole:
			return self.vehicles[index.row()]["name"]
		elif role == self.PosRole:
			return self.vehicles[index.row()]["pos"]
		else:
			return QVariant()
	
	def flags(self,index):
		return Qt.ItemIsEnabled
	
	def roleNames(self):
		return self._roles
	


	@pyqtSlot()
	def update(self):
		print("Updating data")
		vehicles_json = urlopen(URL)
		vehicles = json.load(vehicles_json)["Vehicles"]
		print(len(vehicles))
		print(self.tramCheckBox.property("checked"))
		self.beginRemoveRows(QModelIndex(),0,len(self.vehicles))
		self.vehicles = []
		self.endRemoveRows()
		self.beginInsertRows(QModelIndex(),0,len(vehicles))
		for v in vehicles:
			self.vehicles.append({"name":v["ID"],"pos":QGeoCoordinate(v["Lat"],v["Lng"])})
		self.endInsertRows()
