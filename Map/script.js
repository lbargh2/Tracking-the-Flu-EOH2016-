  //basic map config with custom fills, mercator projection
 var map = new Datamap({

   element: document.getElementById('container2'),

   //projection: '',
   geographyConfig: {
     dataUrl: 'community-districts-polygon.json'//'census_tracts_2010.json'
   },

   scope: 'community-districts-polygon',//'nyct2010',

   setProjection: function(element) {
     var projection = d3.geo.equirectangular()
       .center([-73.9, 40.75])
       .scale(68000)
     var path = d3.geo.path()
       .projection(projection);

     return {path: path, /*projection: projection*/};
   },

   fills: {
     defaultFill: 'rgb(225,236,86)',

     low : 'rgb(225,225,0)',

     medium : 'rgb(225,128,0)',

     high : 'rgb(225,0,0)',

     lt50: 'rgba(0,244,244,0.9)',
     gt50: 'red',
     something : '#B58929',


   },

   data: {


     '1': {fillKey: 'low' },
     10 : {fillKey: 'medium' },

     15 : {fillKey: 'high' },

     //'001': {fillKey: 'gt50' }
   }

 });


//<div class="datamaps-hoverover" style="z-index: 10001; position: absolute; display: none; top: 156.188px; left: 598px;"><div class="hoverinfo"><strong>undefined</strong></div></div>

  //.classed('new', true)
