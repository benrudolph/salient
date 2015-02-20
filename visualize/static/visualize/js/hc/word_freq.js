Salient.HC.WordFreq =
    {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Word Frequency'
        },
        xAxis: {
            categories: []
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Word Count'
            }
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        series: [{
            name: 'Word Frequency',
            data: []

        }]
    }
