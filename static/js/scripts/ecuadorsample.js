var latlong = {};
latlong["EC-A"] = {
    "latitude": -3.0473,
    "longitude": -79.1815
};
latlong["EC-B"] = {
    "latitude": -1.5988,
    "longitude": -79.0835
};
latlong["EC-C"] = {
    "latitude": 0.7216,
    "longitude": -78.0225
};
latlong["EC-D"] = {
    "latitude": -0.8537,
    "longitude": -76.2332
};
latlong["EC-E"] = {
    "latitude": 0.753,
    "longitude": -79.1926
};
latlong["EC-F"] = {
    "latitude": -2.5721,
    "longitude": -78.9319
};
latlong["EC-G"] = {
    "latitude": -2.0578,
    "longitude": -79.8395
};
latlong["EC-H"] = {
    "latitude": -1.9266,
    "longitude": -78.7618
};
latlong["EC-I"] = {
    "latitude": 0.3985,
    "longitude": -78.2632
};
latlong["EC-L"] = {
    "latitude": -4.1314,
    "longitude": -79.5694
};
latlong["EC-M"] = {
    "latitude": -0.6249,
    "longitude": -80.0508
};
latlong["EC-N"] = {
    "latitude": -0.614,
    "longitude": -77.934
};
latlong["EC-O"] = {
    "latitude": -0.8537,
    "longitude": -76.2332
};
latlong["EC-P"] = {
    "latitude": -0.1231,
    "longitude": -78.5577
};
latlong["EC-R"] = {
    "latitude": -1.4866,
    "longitude": -79.556
};
latlong["EC-S"] = {
    "latitude": -2.4914,
    "longitude": -77.9824
};
latlong["EC-SD"] = {
    "latitude": -0.2883,
    "longitude": -79.1682
};
latlong["EC-SE"] = {
    "latitude": -2.0927,
    "longitude": -80.5444
};
latlong["EC-T"] = {
    "latitude": -1.2891,
    "longitude": -78.4772
};
latlong["EC-U"] = {
    "latitude": -0.0719,
    "longitude": -76.3217
};
latlong["EC-W"] = {
    "latitude": -0.2944,
    "longitude": -89.8408
};
latlong["EC-X"] = {
    "latitude": -0.9301,
    "longitude": -78.8338
};
latlong["EC-Y"] = {
    "latitude": -1.7212,
    "longitude": -76.9362
};
latlong["EC-Z"] = {
    "latitude": -4.0867,
    "longitude": -78.8784
};



var mapData = [{
    "code": "EC-A",
    "name": "Azuay",
    "value": 32358260,
    "color": "#eea638"
}, {
    "code": "EC-B",
    "name": "Bolívar",
    "value": 3215988,
    "color": "#d8854f"
}, {
    "code": "EC-C",
    "name": "Carchi",
    "value": 35980193,
    "color": "#de4c4f"
}, {
    "code": "EC-D",
    "name": "Orellana",
    "value": 19618432,
    "color": "#de4c4f"
}, {
    "code": "EC-E",
    "name": "Esmeraldas",
    "value": 40764561,
    "color": "#86a965"
}, {
    "code": "EC-F",
    "name": "Cañar",
    "value": 3100236,
    "color": "#d8854f"
}, {
    "code": "EC-G",
    "name": "Guayas",
    "value": 22605732,
    "color": "#8aabb0"
}, {
    "code": "EC-H",
    "name": "Chimborazo",
    "value": 8413429,
    "color": "#d8854f"
}, {
    "code": "EC-I",
    "name": "Imbabura",
    "value": 9306023,
    "color": "#d8854f"
}, {
    "code": "EC-L",
    "name": "Loja",
    "value": 1323535,
    "color": "#eea638"
}, {
    "code": "EC-M",
    "name": "Manabí",
    "value": 150493658,
    "color": "#eea638"
}, {
    "code": "EC-N",
    "name": "Napo",
    "value": 9559441,
    "color": "#d8854f"
}, {
    "code": "EC-O",
    "name": "El Oro",
    "value": 10754056,
    "color": "#d8854f"
}, {
    "code": "EC-P",
    "name": "Pichincha",
    "value": 9099922,
    "color": "#de4c4f"
}, {
    "code": "EC-R",
    "name": "Los Ríos",
    "value": 738267,
    "color": "#eea638"
}, {
    "code": "EC-S",
    "name": "Morona Santiago",
    "value": 10088108,
    "color": "#86a965"
}, {
    "code": "EC-SD",
    "name": "Santo Domingo de los Tsáchilas",
    "value": 3752228,
    "color": "#d8854f"
}, {
    "code": "EC-SE",
    "name": "Santa Elena",
    "value": 2030738,
    "color": "#de4c4f"
}, {
    "code": "EC-T",
    "name": "Tungurahua",
    "value": 196655014,
    "color": "#86a965"
}, {
    "code": "EC-U",
    "name": "Sucumbíos",
    "value": 405938,
    "color": "#eea638"
}, {
    "code": "EC-W",
    "name": "Galápagos",
    "value": 7446135,
    "color": "#d8854f"
}, {
    "code": "EC-X",
    "name": "Cotopaxi",
    "value": 16967845,
    "color": "#de4c4f"
}, {
    "code": "EC-Y",
    "name": "Pastaza",
    "value": 8575172,
    "color": "#de4c4f"
}, {
    "code": "EC-Z",
    "name": "Zamora Chinchipe",
    "value": 14305183,
    "color": "#eea638"
}];

var map;
var minBulletSize = 3;
var maxBulletSize = 70;
var min = Infinity;
var max = -Infinity;

AmCharts.theme = AmCharts.themes.black;

// get min and max values
for (var i = 0; i < mapData.length; i++) {
    var value = mapData[i].value;
    if (value < min) {
        min = value;
    }
    if (value > max) {
        max = value;
    }
}

// build map
AmCharts.ready(function() {
    map = new AmCharts.AmMap();
    map.projection = "mercator";

    map.addTitle("Datos del Estudio Costa Ecuatoriana", 14);
    map.addTitle("Hombres con Diabetes", 11);
    map.areasSettings = {
        unlistedAreasColor: "#FFFFFF",
        unlistedAreasAlpha: 0.1
    };
    map.imagesSettings = {
        balloonText: "<span style='font-size:14px;'><b>[[title]]</b>: [[value]]</span>",
        alpha: 0.6
    }

    var dataProvider = {
        mapVar: AmCharts.maps.ecuadorLow,
        images: []
    }

    // create circle for each country

    // it's better to use circle square to show difference between values, not a radius
    var maxSquare = maxBulletSize * maxBulletSize * 2 * Math.PI;
    var minSquare = minBulletSize * minBulletSize * 2 * Math.PI;

    // create circle for each country
    for (var i = 0; i < mapData.length; i++) {
        var dataItem = mapData[i];
        var value = dataItem.value;
        // calculate size of a bubble
        var square = (value - min) / (max - min) * (maxSquare - minSquare) + minSquare;
        if (square < minSquare) {
            square = minSquare;
        }
        var size = Math.sqrt(square / (Math.PI * 2));
        var id = dataItem.code;

        dataProvider.images.push({
            type: "circle",
            width: size,
            height: size,
            color: dataItem.color,
            longitude: latlong[id].longitude,
            latitude: latlong[id].latitude,
            title: dataItem.name,
            value: value
        });
    }



    // the following code uses circle radius to show the difference
    /*
    for (var i = 0; i < mapData.length; i++) {
        var dataItem = mapData[i];
        var value = dataItem.value;
        // calculate size of a bubble
        var size = (value - min) / (max - min) * (maxBulletSize - minBulletSize) + minBulletSize;
        if (size < minBulletSize) {
            size = minBulletSize;
        }
        var id = dataItem.code;

        dataProvider.images.push({
            type: "circle",
            width: size,
            height: size,
            color: dataItem.color,
            longitude: latlong[id].longitude,
            latitude: latlong[id].latitude,
            title: dataItem.name,
            value: value
        });
    }*/



    map.dataProvider = dataProvider;

    map.write("mapdiv");
});


