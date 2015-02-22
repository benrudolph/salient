Salient.HC.XRay =
    {
        chart: {
            type: 'heatmap'
        },
        xAxis: {
            type: 'category',
            // Percentage of doc -- 0 = 0 - 10% ... 9 = 90% - 100%
            categories: _.map(Array(15), function(d, i) { return i; })
        },
        colorAxis: {
            min: 0,
            minColor: '#FFFFFF',
            maxColor: Highcharts.getOptions().colors[0]
        },
        yAxis: {
            title: {
                text: 'Documents'
            },
            categories: [] // Document name(s)
        },
    }

