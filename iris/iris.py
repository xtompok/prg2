import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtProperty, QObject, QUrl
from PyQt5.QtQml import qmlRegisterType, QQmlComponent, QQmlApplicationEngine
from PyQt5.QtQuick import QQuickView

from itemmodel import ItemModel

# Create the application instance.
app = QApplication(sys.argv)

model = ItemModel()

# Create a QML engine.
view = QQuickView()
view.setResizeMode(QQuickView.SizeRootObjectToView)
ctx = view.rootContext()
ctx.setContextProperty("itemModel",model)

# Create a component factory and load the QML script.
view.setSource(QUrl('qtquickui.qml'))
view.show()
model.tramCheckBox = view.findChild(QObject,"tramCheckBox")

sys.exit(app.exec())

