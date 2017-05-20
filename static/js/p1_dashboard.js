/*
Copyright (C) <2017>  Abhilash Mhaisne <55abhilash@openmailbox.org>
                      Ajinkya Panaskar <ajinkya.panaskar@outlook.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
*/

// 2 graphs are present in the following 2 divs
// One is the task frequency graph, another is
// TBD

$('#dashboard').html(
        "<div class='row'>" + 
            "<div class='col-md-6 graph_title'> <b>Task Frequency</b>" + 
            "</div>" +
            "<div class='col-md-6 graph_title'> <b>Minion Targetting Frequency</b>" + 
            "</div>" +
        "</div>" + 
        "<div class='row'>" +
            "<div class='graph col-md-5' id='graph1'>" +
            "</div>" + 
            "<div class='graph col-md-7' id='graph2'>" +
            "</div>" + 
        "</div>"
        );
$('.graph_title').css({
    'text-align': 'center',
    'padding':'10px'
});

//$('#graph2').css({'left': '80%', 'padding-top': '48px', 'padding-left': '550px'});

    $.ajax({
        url: '/get_graph_data_tasks',
        type: 'GET',
        success: function(response) {
        //response is of the form :
        //      task : times it ran
        
            var x_elems = Array();
            var y_elems = Array();
            for(item in response) {
                y_elems.push(item);
                x_elems.push(Number(response[item]));
            }
            var data = [
                {
                    values: x_elems,
                    labels: y_elems,
                    type: 'pie'
                }
            ];
            var layout = {
                height: 400,
                width: 500
            };
            Plotly.newPlot('graph1', data, layout);
        }
    });
    $.ajax({
        url: '/get_graph_data_minions',
        type: 'GET',
        success: function(response) {
        //response is of the form :
        //      task : times it ran
        
            var x_elems = Array();
            var y_elems = Array();
            for(item in response) {
                x_elems.push(item);
                y_elems.push(Number(response[item]));
            }
            var data = [
                {
                    x: x_elems,
                    y: y_elems,
                    type: 'bar'
                }
            ];

            Plotly.newPlot('graph2', data);
        }
    });
$('#dashboard').toggle(true);
$('#dashboard_entry').click(function(event) {
    $('#machines').hide();
    $('#runningtasks').hide();
    $('#dashboard').toggle();
});
