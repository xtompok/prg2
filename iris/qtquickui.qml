import QtQuick 2.0
import QtPositioning 5.8
import QtLocation 5.9
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.3

// Root item
Item {
    width: 1000
    height: 500

    // Plugin for providing tiles for the map
    Plugin {
        id: mapPlugin
        name: "osm" // "mapboxgl", "esri", ...
        // specify plugin parameters if necessary
        // PluginParameter {
        //     name:
        //     value:
        // }
    }
    // Content of the window will be in column
    ColumnLayout {
        id: col
        anchors.fill: parent	// fill parent component with this component

        Button {
            text: "Update"	// text on the button
            Layout.fillWidth: true // button should be from side to side
            height: 50
            // When clicked, call slot update on itemModel (which represents python object)
            onClicked: {
                itemModel.update()
            }
        }

        RowLayout {
            id: row
            Layout.fillWidth: true // RowLayout should fill entire width of the column
            spacing: 10

            CheckBox {
                checked: true	// should be checked on start
                objectName: "tramCheckBox"	// this name is used when referencing this component from Python
                text: "Tramvaje"	// text aside of checkbox
            }

            CheckBox {
                checked: false
                objectName: "trolCheckBox"
                text: "Trolejbusy"
            }
        }

        // Map component
        Map {
            id: map
            Layout.fillWidth: true
            Layout.fillHeight: true
            plugin: mapPlugin	// show tiles form previously created plugin
            /*   gesture.preventStealing: true
        gesture.onRotationUpdated: {
            if (map.bearing < 30 || map.bearing > 330) map.bearing = 0;
        }
        gesture.onRotationFinished: {
            if (map.bearing < 30 || map.bearing > 330) map.bearing = 0;
        }*/

            zoomLevel: (maximumZoomLevel - minimumZoomLevel) / 2 // set initial zoomlevel
            center {	// set initial center
                latitude: 50
                longitude: 14.5
            }

            // All vehicles are drawn through this view
            MapItemView {
                model: itemModel
                delegate: mapitem
            }

            // This component is used as a single vehicle icon
            Component {
                id: mapitem

                // Component holding icon data
                MapQuickItem {
                    id: marker
                    // What point of the component should be placed right on the coordinates
                    anchorPoint.x: sourceItem.width / 2
                    anchorPoint.y: markerCircle.height / 2
                    // To get coordinates from the model use posRole role
                    coordinate: posRole

                    // Icon shown on the map
                    sourceItem: Column {
                        // Circle (rectangle with round corners)
                        Rectangle {
                            id: markerCircle
                            anchors.horizontalCenter: parent.horizontalCenter // center circle horizontally
                            width: 14
                            height: 14
                            color: "red"
                            radius: 7
                        }
                        Text {
                            id: markerText	// text shown under the circle
                            anchors.horizontalCenter: parent.horizontalCenter
                            text: displayRole //To get the text from the model use displayRole role
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
