$(document).ready(function () {
    $('#loadDataBtn').click(function () {
        $.ajax({
            url: '/api/data',
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                populateTable(data);
                createGraph(data);
            },
            error: function (error) {
                console.log(error);
            }
        });
    });

    function populateTable(data) {
        var tableHtml = '<table class="table-primary" id="dataTable">';
        tableHtml += '<thead><tr><th>ID</th><th>Name</th><th>Age</th></tr></thead>';
        tableHtml += '<tbody>';
        data.forEach(function (item) {
            tableHtml += '<tr><td>' + item.id + '</td><td>' + item.name + '</td><td>' + item.age + '</td></tr>';
        });
        tableHtml += '</tbody>';
        tableHtml += '</table>';

        $('#tableContainer').html(tableHtml);

        $('#dataTable').DataTable();
    }

    function createGraph(data) {
        var names = data.map(function (item) {
            return item.name;
        });

        var ages = data.map(function (item) {
            return item.age;
        });

        var graphData = [{
            x: names,
            y: ages,
            type: 'bar'
        }];

        var layout = {
            title: 'Dummy Data Graph',
            xaxis: { title: 'Name' },
            yaxis: { title: 'Age' }
        };

        Plotly.newPlot('graphContainer', graphData, layout);
    }
});
