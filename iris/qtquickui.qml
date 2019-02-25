import QtQuick 2.0
import QtPositioning 5.8
import QtLocation 5.9
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.3

Item {
    Plugin {
        id: mapPlugin
        name: "osm" // "mapboxgl", "esri", ...
        // specify plugin parameters if necessary
        // PluginParameter {
        //     name:
        //     value:
        // }
    }
    ColumnLayout {
        id: col
        anchors.fill: parent

        Button {
            text: "Update"
            Layout.fillWidth: true
            height: 50
            onClicked: {
                itemModel.update()
            }
        }

        RowLayout {
            id: row
            Layout.fillWidth: true
            spacing: 10

            CheckBox {
                checked: true
                objectName: "tramCheckBox"
                text: "Tramvaje"
            }

            CheckBox {
                checked: false
                id: trolCheckBox
                text: "Trolejbusy"
            }


        }

        Map {
            id: map
            Layout.fillWidth: true
            Layout.fillHeight: true
            plugin: mapPlugin
            /*   gesture.preventStealing: true
        gesture.onRotationUpdated: {
            if (map.bearing < 30 || map.bearing > 330) map.bearing = 0;
        }
        gesture.onRotationFinished: {
            if (map.bearing < 30 || map.bearing > 330) map.bearing = 0;
        }*/

            zoomLevel: (maximumZoomLevel - minimumZoomLevel) / 2
            center {
                latitude: 50
                longitude: 14.5
            }

            MapItemView {
                model: itemModel
                delegate: mapitem
            }

            Component {
                id: mapitem

                MapQuickItem {
                    id: marker
                    anchorPoint.x: sourceItem.width / 2
                    anchorPoint.y: markerCircle.height / 2
                    coordinate: posRole

                    sourceItem: Column {
                        Rectangle {
                            id: markerCircle
                            anchors.horizontalCenter: parent.horizontalCenter
                            width: 14
                            height: 14
                            color: "red"
                            radius: 7
                        }
                        Text {
                            id: markerText
                            anchors.horizontalCenter: parent.horizontalCenter
                            text: displayRole
                        }
                    }
                }
            }
        }
    }


}

/*##^## Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
 ##^##*/
