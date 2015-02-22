Salient.Data.wordFreq = function(did, options) {
    return $.get('/analyzer/docs/' + did + '/word_frequency')
};

Salient.Data.xray = function(did, q, options) {
    return $.get('/analyzer/docs/' + did + '/xray', { q: q })
};


