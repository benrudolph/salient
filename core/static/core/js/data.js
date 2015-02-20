Salient.Data.wordFreq = function(did, options) {
    return $.get('/analyzer/docs/' + did + '/word_frequency')
};
