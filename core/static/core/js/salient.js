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
    HC: {},

    Constants: {
        DOC_CONTENT: 'document-content',
        VOL_CONTENT: 'volume-content',
    }

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

$(function($) {

  Sammy = Sammy || {};

  /**
   * This plugin is meant to prevent regular forms (that do not have a
#/ prefix on their action) to submit to the
   * Sammy Application. If sammy intercepts, it seems certain
parameters are discarded if the route is not found.
   *
   * This plugin will therefore verify during form submission if the
action starts with a hash (#) and if not, it will
   * not route the request through the sammy application, but rather
submit the form normally to the server.
   *
   * @credits to Fabien Baligand for the fix. I just wrapped it in a
plugin for easier re-usability.
   * @param app
   */
  Sammy.RegularFormSubmitFix = function(app) {

    // Monkey patch
    // Reference: http://groups.google.com/group/sammyjs/browse_thread/thread/1185bed98824df3f/28e901549b853796

    app.defaultCheckFormSubmission = this._checkFormSubmission;
    app._checkFormSubmission = function (form) {
      var $form, path, verb;
      $form = $(form);
      path = $form.attr("action") || '';
      verb = this._getFormVerb($form);
      if (verb === "get" && !path.startsWith("#")){
        return false;
      }
      else {
        return this.defaultCheckFormSubmission(form);
      }
    };

  }

});
