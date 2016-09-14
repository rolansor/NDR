var data_esmeraldas = 12;
var data_manabi = 14;
var data_guayas = 20;
var data_losrios = 7;
var data_eloro = 15;
var data_sln = 18;
var titulo= "Personas con Nefropatía Diabetica";

var map;
var minBulletSize = 20;
var maxBulletSize = 60;
var min = Infinity;
var max = -Infinity;

var latlong = {};
latlong["EC-E"] = {
    "latitude": 0.753,
    "longitude": -79.1926
};
latlong["EC-G"] = {
    "latitude": -2.0578,
    "longitude": -79.8395
};
latlong["EC-M"] = {
    "latitude": -0.6249,
    "longitude": -80.0508
};
latlong["EC-O"] = {
    "latitude": -3.5231,
    "longitude": -79.7839
};
latlong["EC-R"] = {
    "latitude": -1.4866,
    "longitude": -79.556
};
latlong["EC-SE"] = {
    "latitude": -2.0927,
    "longitude": -80.5444
};

$("#generar").click(function () {
        $.ajax({
            type: "POST",
            url: "/geo_reportes",
            dataType: "json",
            data: {
                'sexo': $("#sexo").val(),
                'provincia': $("#provincia").val(),
                'criterio': $("#criterio").val()
            },
            success: function(resp){
                data_esmeraldas = resp.ESM;
                data_manabi = resp.MAN;
                data_guayas = resp.GUA;
                data_losrios = resp.RIO;
                data_eloro = resp.ORO;
                data_sln = resp.SLN;
                titulo= resp.busqueda;
                dibujarMapa();
                map.validateData();
            }

        });
    });



var mapData = [{
    "code": "EC-E",
    "name": "Esmeraldas",
    "value": data_esmeraldas,
    "color": "#003300"
}, {
    "code": "EC-G",
    "name": "Guayas",
    "value": data_guayas,
    "color": "#0033cc"
}, {
    "code": "EC-M",
    "name": "Manabí",
    "value": data_manabi,
    "color": "#ffff00"
}, {
    "code": "EC-O",
    "name": "El Oro",
    "value": data_eloro,
    "color": "#663300"
}, {
    "code": "EC-R",
    "name": "Los Ríos",
    "value": data_losrios,
    "color": "#9900cc"
}, {
    "code": "EC-SE",
    "name": "Santa Elena",
    "value": data_sln,
    "color": "#ff0000"
}];

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
    dibujarMapa();
});


function dibujarMapa() {
    map = new AmCharts.AmMap();
    map.projection = "mercator";

    AmCharts.theme = AmCharts.themes.dark;
    map.addTitle("Datos del Estudio Costa Ecuatoriana", 14);
    map.addTitle(titulo, 11);
    map.areasSettings = {
        autoZoom: true,
        rollOverBrightness:10,
        selectedBrightness:20
    };

    map.imagesSettings = {
        balloonText: "<span style='font-size:14px;'><b>[[title]]</b>: [[value]]</span>",
        alpha: 1
    }

    var dataProvider = {
        mapVar: AmCharts.maps.ecuadorLow,
        getAreasFromMap:true,
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
    map.dataProvider = dataProvider;

    map.write("mapdiv");
}


