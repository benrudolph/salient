window.Salient = {
    ViewModels: {},
    // View Model instances
    VM: {},
    Models: {},
    // Sammy app
    App: null,
    Utils: {},
    // Functions to get data
    Data: {},
    // Highcharts Objects
    HC: {}
};

/* Use of publish and subscribe */
(function($) {

  var o = $({});

  $.subscribe = function() {
    o.on.apply(o, arguments);
  };

  $.unsubscribe = function() {
    o.off.apply(o, arguments);
  };

  $.publish = function() {
    o.trigger.apply(o, arguments);
  };

}(jQuery));
