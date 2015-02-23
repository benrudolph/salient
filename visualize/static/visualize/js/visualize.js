$(document).ready(function() {
    Salient.VM = new Salient.ViewModels.DocVisualize()
    ko.applyBindings(Salient.VM);
    Sammy.RegularFormSubmitFix(Salient.App);
    Salient.App.run();
});

Salient.ViewModels.DocVisualize = function() {
    var self = this;



    self.volumes = ko.observableArray([]);
    self.doc = ko.observable({});
    self.volume = ko.observable({});
    self.wordFreqData = {};
    self.wordFreq = null;
    self.wordType = 'word_stemmed';
    self.xrayBuckets = 100;
    self.display = ko.observable(Salient.Constants.DOC_CONTENT);

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

    self.fetchXRay = function(formEl) {
        var q = $(formEl).serializeArray()[0].value;

        var success = function(raw) {
            var mapping,
                reduceFn,
                options = _.clone(Salient.HC.XRay),
                data = [];


            reduceFn = function(memo, d) {
                // [X, Y, VAL]
                var bucket
                    X = 0,
                    Y = 1,
                    VAL = 2;

                bucket = Math.floor(mapping(d.position));

                existing = _.find(memo, function(p) { return p[X] === bucket });

                if (existing) {
                    existing[VAL] ++;
                } else {
                    memo.push([bucket, 0, 1]);
                }
                return memo;
            }

            mapping = d3.scale.linear()
                .domain([raw.min_position, raw.max_position])
                .range([0, self.xrayBuckets]);

            data = _.reduce(raw.positions, reduceFn, [])

            //options.xAxis.categories =
            //    _.map(data, function(d) { return d['word_stemmed']; });
            options.chart.renderTo = 'xray';
            console.log(data);

            self.xray = new Highcharts.Chart(options);
            self.xray.addSeries({ name: 'Words in document', data: data })
        }

        Salient.Data.xray(self.doc().id, q)
            .success(success)
            .fail(Salient.Utils.handleError);
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
        }).error(Salient.Utils.handleError);

    };

    self.fetchVolume = function(id, cb) {
        $.get('/api/volumes/' + id).success(function(volume) {
            self.volume(volume);
            if (cb)
                cb(volume);
        }).error(Salient.Utils.handleError);
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
        var self = this;
        if (!initialized) {
            Salient.VM.fetchVolumes(function(volumes) {
                initialized = true;

                if ((self.path === '/' || !self.path) && volumes.length) {
                    self.redirect('#volume/' + volumes[0].id);
                }
            });
        }
    })


    this.get('#volumes/:vid/docs/:did', function() {
        var did = this.params['did'];
        var vid = this.params['vid'];

        Salient.VM.display(Salient.Constants.DOC_CONTENT);

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

    this.get('#volumes/:vid', function() {
        var vid = this.params['vid'];

        Salient.VM.display(Salient.Constants.VOL_CONTENT);

        Salient.VM.fetchVolume(vid);
    });

    // Default route
    this.get('', function() {
    });
})

