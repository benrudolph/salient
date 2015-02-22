$(document).ready(function() {
    Salient.VM = new Salient.ViewModels.DocVisualize()
    ko.applyBindings(Salient.VM);
    Salient.App.run();
});

Salient.ViewModels.DocVisualize = function() {
    var self = this;



    self.volumes = ko.observableArray([]);
    self.doc = ko.observable({});
    self.wordFreqData = {};
    self.wordFreq = null;
    self.wordType = 'word_stemmed';


    self.filterCategories = function(model, e) {
        var xAxis = self.wordFreq.xAxis[0],
            q = $(e.currentTarget).val(),
            filterFn;

        filterFn = function(d) {
            return d[self.wordType].toLowerCase().startsWith(q.toLowerCase());
        }



        Salient.VM.wordFreq.series[0].setData(
                _.chain(self.wordFreqData)
                .filter(filterFn)
                .map(function(d) { return d.freq; }, true)
                .value());

        xAxis.update({
            categories: _.chain(self.wordFreqData)
                .filter(filterFn)
                .map(function(d) { return d[self.wordType]; })
                .value()
        })

    };

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

                options.xAxis.categories =
                    _.map(data, function(d) { return d['word_stemmed']; });
                options.chart.renderTo = 'word-freq';

                Salient.VM.wordFreqData = data
                Salient.VM.wordFreq = new Highcharts.Chart(options);
                Salient.VM.wordFreq.series[0].setData(
                    _.map(data, function(d) { return d.freq; }, true));

            }).error(Salient.Utils.handleError);


    });

    // Default route
    this.get('', function() {
        console.log('default')
    });
})

