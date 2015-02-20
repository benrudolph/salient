$(document).ready(function() {
    Salient.VM = new Salient.ViewModels.DocVisualize()
    ko.applyBindings(Salient.VM);
    Salient.App.run();
});

Salient.ViewModels.DocVisualize = function() {
    var self = this;



    self.volumes = ko.observableArray([]);
    self.doc = ko.observable({});

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
        $.get('/api/docs/' + id).success(function(doc) {
            self.doc(doc)
            if (cb)
                cb(doc);
        }).error(Salient.Utils.handleError);
    };
    /* End doc logic */


};

Salient.App = Sammy('#content', function() {
    var initialized = false;

    this.before(function() {
        if (!initialized) {
            Salient.VM.fetchVolumes(function(volumes) {
                initialized = true;
            });
        }
    })


    this.get('#volume/:vid/doc/:did', function() {
        var did = this.params['did'];
        var vid = this.params['vid'];

        Salient.VM.fetchDoc(did);

        Salient.Data.wordFreq(did)
            .success(function(data) {
                var options = _.clone(Salient.HC.WordFreq);
                options.chart.renderTo = 'word-freq';

                var chart = new Highcharts.Chart(options);

                chart.xAxis.categories = _.map(data, function(d) { return d['word_stemmed']; });

                chart.series[0].setData(_.map(data, function(d) { return d.freq; }, true));
            }).error(Salient.Utils.handleError);


    });

    // Default route
    this.get('', function() {
        console.log('default')
    });
})

