from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt, QVariant, pyqtSlot
from PyQt5.QtPositioning import QGeoCoordinate
from urllib.request import urlopen
import json

URL="https://mapa.idsjmk.cz/api/vehicles.json"


class ItemModel(QAbstractListModel):
	"""Class for maintaining vehicle data. Inherits from QAbstractListModel,
	which is needed for use with QML GUI as a model."""

	# The delegate in QML could ask for one object for different roles.
	# PosRole is custom role to serve coordinates of the vehicle
	PosRole = Qt.UserRole + 1

	# Dictionary to store available roles. QML must know available roles to
	# use them
	_roles = {PosRole: b"posRole", Qt.DisplayRole: b"displayRole"}

	def __init__(self,parent=None,*args):
		""" Initialize model object. 
		Creates one dummy vehicle to show on map """
		# Create parent initializator
		super(ItemModel,self).__init__()
		# Create vehicle list with dummy vehicle
		self.vehicles = [{"name":1234,"pos":QGeoCoordinate(49,14)}]
		# Create checkbox attribute, will be filled in iris.py
		self.tramCheckBox = None
	
	
	def rowCount(self,parent=QModelIndex()):
		""" Overriden method of QAbstractListModel, returns number of
		vehicles """
		return len(self.vehicles)
	
	def data(self,index,role=Qt.DisplayRole):
		""" Overriden method of QAbstractListModel, it is called when
		QML wants some data from model. 

		Arguments:
			self - self object reference
			index - index of the requested item
			role - which role of the item is requested

		Returns data of the requested item according to requested role.
		"""

		# DisplayRole - we return vehicle name
		if role == Qt.DisplayRole:
			return self.vehicles[index.row()]["name"]
		# PosRole - we return vehicle coordinates
		elif role == self.PosRole:
			return self.vehicles[index.row()]["pos"]
		# Other role - we return empty QVariant, QVariant() instead of
		# None is needed due to C++ internals of the Qt framework
		else:
			return QVariant()
	
	def flags(self,index):
		""" Overriden method of QAbstractListModel, returns that every
		item is enabled """ 
		return Qt.ItemIsEnabled
	
	def roleNames(self):
		""" Overriden method of QAbstractListModel, returns available
		roles for this model """
		return self._roles
	

	# Folowing method is a slot == it is callable from other Qt components
	# including QML GUI
	@pyqtSlot()
	def update(self):
		print("Updating data")
		# Download vehicle data	
		vehicles_json = urlopen(URL)
		# Parse vehicle json and get the vehicles list
		vehicles = json.load(vehicles_json)["Vehicles"]
		print(len(vehicles))

		# Get the status of Tram checkbox
		showTrams = self.tramCheckBox.property("checked")
		new_vehicles = []
		# If Tram checkbox is checked, add trams to the visible vehicles
		for v in vehicles:
			if v['VType'] == 0 and showTrams:
				new_vehicles.append(v)
			else:
				pass

		vehicles = new_vehicles

		# Notify GUI that we will remove all old vehicles
		self.beginRemoveRows(QModelIndex(),0,len(self.vehicles))
		# Really remove all old vehicles
		self.vehicles = []
		# Notify GUI that we removed all vehicles
		self.endRemoveRows()

		# Notify GUI that we will add new vehicles
		self.beginInsertRows(QModelIndex(),0,len(vehicles))
		# Really add new vehicles
		for v in vehicles:
			# QGeoCoordinate is a class used to store coordinates in Qt
			self.vehicles.append({"name":v["ID"],"pos":QGeoCoordinate(v["Lat"],v["Lng"])})
		# Notify GUI that we added new vehicles
		self.endInsertRows()
