Salient.Utils.textToParagraph = function(text) {
    result = "<p>" + text + "</p>";
    result = result.replace(/\r\n\r\n/g, "</p><p>").replace(/\n\n/g, "</p><p>");
    result = result.replace(/\r\n/g, "<br />").replace(/\n/g, "<br />");
    return result;
}

Salient.Utils.handleError = function(xhr, msg, status) {
    console.log(status);
};
