$(document).ready(function() {

    Salient.ViewModels.DocVisualize = function() {
        this.volumes = ko.observableArray([]);

    };

    Salient.App = Sammy('#content', function() {

        // Default route
        this.get('', function() {
            console.log('default')
        });
    })

    ko.applyBindings(new Salient.ViewModels.DocVisualize());

    window.Salient.App.run();
});
