var WordFreq = function(config) {

    this.data = config.data;
    this.el = '';

}

WordFreq.prototype.render = function() {
    return this;
}

WordFreq.prototype.data = function(_data) {
    if (!arguments.length)
        return this.data;
    this.data = _data;
    return this;
}
