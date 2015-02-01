Salient.ViewModels.Doc = function() {
    var self = this;

    self.docType = ko.observable('')

    self.showUrl = ko.computed(function() { return self.docType() === 'UR'; });
    self.showInput = ko.computed(function() { return self.docType() === 'IN'; });
    self.showTextFile = ko.computed(function() { return self.docType() === 'TX'; });

    self.onDocTypeChange = function(a) {
        console.log(self.docType());
    };
};

ko.applyBindings(new Salient.ViewModels.Doc());
