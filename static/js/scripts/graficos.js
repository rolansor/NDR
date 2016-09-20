var h = document.getElementById("h").value;
var m = document.getElementById("m").value;
var hd = document.getElementById("hd").value;
var md = document.getElementById("md").value;
var diaLocE = document.getElementById("diaLocE").value;
var diaLocM = document.getElementById("diaLocM").value;
var diaLocG = document.getElementById("diaLocG").value;
var diaLocO = document.getElementById("diaLocO").value;
var diaLocR = document.getElementById("diaLocR").value;
var diaLocS = document.getElementById("diaLocS").value;
var insE = document.getElementById("insE").value;
var insM = document.getElementById("insM").value;
var insG = document.getElementById("insG").value;
var insO = document.getElementById("insO").value;
var insR = document.getElementById("insR").value;
var insS = document.getElementById("insS").value;



$(function () {
   var doughnutData = [
        {
            value: parseInt(hd),
            color: "#a3e1d4",
            highlight: "#1ab394",
            label: "Hombres con Diabetes"
        },
        {
            value: parseInt(md),
            color: "#dedede",
            highlight: "#1ab394",
            label: "Mujeres con Diabetes"
        },
    ];

   var doughnutOptions = {
        segmentShowStroke: true,
        segmentStrokeColor: "#fff",
        segmentStrokeWidth: 2,
        percentageInnerCutout: 0, // This is 0 for Pie charts
        animationSteps: 100,
        animationEasing: "easeOutBounce",
        animateRotate: true,
        animateScale: false,
        responsive: true,
   };


   var ctx = document.getElementById("hvsmdiabetes").getContext("2d");
   var myNewChart = new Chart(ctx).Doughnut(doughnutData, doughnutOptions);

   var barData = {
        labels: ["Esmeraldas", "Manabí", "Guayas", "El Oro", "Los Rios", "Santa Elena"],
        datasets: [
            {
                label: "Diabetes por Provincia",
                fillColor: "rgba(26,179,148,0.5)",
                strokeColor: "rgba(26,179,148,0.8)",
                highlightFill: "rgba(26,179,148,0.75)",
                highlightStroke: "rgba(26,179,148,1)",
                data: [parseInt(diaLocE), parseInt(diaLocM), parseInt(diaLocG), parseInt(diaLocO), parseInt(diaLocR), parseInt(diaLocS)]
            }
        ]
    };

    var barOptions = {
        scaleBeginAtZero: true,
        scaleShowGridLines: true,
        scaleGridLineColor: "rgba(0,0,0,.05)",
        scaleGridLineWidth: 1,
        barShowStroke: true,
        barStrokeWidth: 2,
        barValueSpacing: 5,
        barDatasetSpacing: 1,
        responsive: true
    }


    var ctx = document.getElementById("diaxLocalidad").getContext("2d");
    var myNewChart = new Chart(ctx).Bar(barData, barOptions);

    var doughnutData1 = [
            {
                value: parseInt(h),
                color: "#a3e1d4",
                highlight: "#1ab394",
                label: "Hombres"
            },
            {
                value: parseInt(m),
                color: "#dedede",
                highlight: "#1ab394",
                label: "Mujeres"
            },
        ];

       var doughnutOptions1 = {
            segmentShowStroke: true,
            segmentStrokeColor: "#fff",
            segmentStrokeWidth: 2,
            percentageInnerCutout: 45, // This is 0 for Pie charts
            animationSteps: 100,
            animationEasing: "easeOutBounce",
            animateRotate: true,
            animateScale: false,
            responsive: true,
       };


       var ctx = document.getElementById("hvsm").getContext("2d");
       var myNewChart = new Chart(ctx).Doughnut(doughnutData1, doughnutOptions1);

       var barData1 = {
            labels: ["Esmeraldas", "Manabí", "Guayas", "El Oro", "Los Rios", "Santa Elena"],
            datasets: [
                {
                    label: "Diabetes por Provincia",
                    fillColor: "rgba(26,179,148,0.5)",
                    strokeColor: "rgba(26,179,148,0.8)",
                    highlightFill: "rgba(26,179,148,0.75)",
                    highlightStroke: "rgba(26,179,148,1)",
                    data: [parseInt(insE), parseInt(insM), parseInt(insG), parseInt(insO), parseInt(insR), parseInt(insS)]
                }
            ]
        };

        var barOptions1 = {
            scaleBeginAtZero: true,
            scaleShowGridLines: true,
            scaleGridLineColor: "rgba(0,0,0,.05)",
            scaleGridLineWidth: 1,
            barShowStroke: true,
            barStrokeWidth: 2,
            barValueSpacing: 5,
            barDatasetSpacing: 1,
            responsive: true
        }


        var ctx = document.getElementById("insulinachart").getContext("2d");
        var myNewChart = new Chart(ctx).Bar(barData1, barOptions1);


});