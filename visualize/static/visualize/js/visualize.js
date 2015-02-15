$(document).ready(function() {
    Salient.VM = new Salient.ViewModels.DocVisualize()
    ko.applyBindings(Salient.VM);
    Salient.App.run();
});

Salient.ViewModels.DocVisualize = function() {
    var self = this;



    self.volumes = ko.observableArray([]);
    self.docs = ko.observable([]);

    /* Volume logic */
    self.addVolumes = function(volumes) {
        _.each(volumes, function(v) {
            self.volumes.push(v);
        });
    };

    self.fetchVolumes = function(cb) {
        $.get('/api/volumes').success(function(volumes) {
            self.addVolumes(volumes);

            if (cb)
                cb(volumes);
        }).error(function(xhr, msg, status) {
            console.log(status);
        });

    };
    /* End volume logic */

    /* Doc logic */
    self.fetchDoc = function(id, cb) {

    };
    /* End doc logic */


};

Salient.App = Sammy('#content', function() {
    var initialized = false;

    this.before(function() {
        if (!initialized) {
            Salient.VM.fetchVolumes(volumes, function() {
                initialized = true;
            });
        }
    })


    this.get('#/doc/:id', function() {
        console.log('doc route');

    });

    // Default route
    this.get('', function() {
        console.log('default')
    });
})

