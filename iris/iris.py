import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtProperty, QObject, QUrl
from PyQt5.QtQml import qmlRegisterType, QQmlComponent, QQmlApplicationEngine
from PyQt5.QtQuick import QQuickView

from itemmodel import ItemModel

# Create the application instance.
app = QApplication(sys.argv)

# Create data model
model = ItemModel()

# Create a QML engine.
view = QQuickView()
# View should fill entire window
view.setResizeMode(QQuickView.SizeRootObjectToView)
# Get context, it is used to pass data to QML GUI
ctx = view.rootContext()
# In GUI, variable 'model' will be accessible as property 'itemModel'
ctx.setContextProperty("itemModel",model)

# Create a component factory and load the QML script.
view.setSource(QUrl('qtquickui.qml'))
# Show GUI
view.show()
# Add attribute 'tramCheckBox' to instance 'model'. tramCheckBox represents GUI
# checkbox and it can be determined the state of the checkbox from Python code
model.tramCheckBox = view.findChild(QObject,"tramCheckBox")

# Run main program loop. This will block until GUI is closed (or error occurs)
sys.exit(app.exec())

