var map = new Datamap({
  element: document.getElementById('container'),
  scope: 'usa',

  setProjection: function(element) {
    var projection = d3.geo.equirectangular()
      .center([-70, 42])
      .rotate([4.4, 0])
      .scale(2000)
      .translate([element.offsetWidth / 2, element.offsetHeight / 2]);
    var path = d3.geo.path()
      .projection(projection);

    return {path: path, projection: projection};
  },

  geographyConfig: {
    highlightOnHover: true,
    popupOnHover: true
  }
});

newLabels = {'AK':'Alaska'};
map.labels({'customLabelText': newLabels});
