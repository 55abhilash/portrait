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

/*Running tasks tab
Table consists of these coloumns:
      Task name
      JID
      Status

 Right hand side area in the running tasks div is 
 for outputs
 We call it the output area
*/
$('#runningtasks').html(
        "<div class='row' id='disp_area_tasks'>" +
        "&nbsp; &nbsp; &nbsp; &nbsp;" +
        "</div>" + 
        "<div class='output_area' id='output_area'>" +
        "</div>"
);
$('#output_area').css({'left': '80%', 'padding-top': '48px', 'padding-left': '500px'});
 $('#disp_area_tasks').css({
    'left': '25%',
    'width': '75%',
    'font-size': '100%',
    'text-indent': '200px',
    'padding':'8px'
 });

$('#disp_area_tasks').html('<b>Tasks</b>');
// First of all the coloumn headers in the table
// // are displayed.
$('#disp_area_tasks').append("<br>" + "&nbsp;&nbsp;" +
        "<table id='task_table' class='minion-table'>" +
        "<tr>" +
        "<th class='tab-head'>Task</th>" + 
        "<th> Job ID</th>" +
        "<th> &nbsp;&nbsp;</th>" +
        "<th> Status</th>" +
        "</tr>" +
        "</table>"
);
$('#runningtasks').toggle(false);
$('#runningtasks_entry').click(function(event) {
    $('#machines').hide();
    $('#dashboard').hide();
    $('#runningtasks').toggle();
    $('#output_area').html('');
    //TODO : Store task name along with jids
    // How to deal with the statuses of the jobs?
    // -> Write fn to get individual / status of list of jobs..
    // .. and keep on polling the request after an interval
    //
    // Keep the jid as a href link, which when clicked will
    // display status, and if completed, will let us know on which 
    // machines it is completed and which is yet to complete and
    // on which it has completed succesfully and on which it has failed
    //

    $.ajax({
        url: '/task/get_all_jobs',
        type: 'GET',
        success: function(response) {
            // Expect response in the form:
            //         jid : {taskname, status}
            for(element in response) {
                all_jids_list.push(response[element][0] + ',' + element);
            }
            //alert(JSON.stringify(response))
            for(item in all_jids_list) {
                var parsed_item = all_jids_list[item].split(",");
                var taskname = parsed_item[0];
                var jobid = parsed_item[1];
                if($('#task_table').html().indexOf(jobid) == -1) { 
                
                    $('#task_table').append(
                        "<tr id='row_" + jobid + "'>" +
                        "<td>" + taskname + "</td>" +
                        "<td>" + "<a class='job_entry' href='/task/job_info?jobid=" + jobid + "'>" + jobid + "</a></td>" +
                        "<td>" + "" + "</td>" + 
                        "</tr>"
                    );
                }
                //alert("Response[jobid][1] = " + JSON.stringify(response[jobid][1]));
                if(JSON.stringify(response[jobid][1]) === "true") {   
                    //We check if the logo is already there for both types of logos
                    if($('#logo_job_done_' + jobid).length == 0) {
                        $('#row_' + jobid).append("<td id='logo_job_done_" + jobid + "'>" + "&nbsp;&nbsp;<image id='" + jobid + "_img' src=/static/img/job_done.png ></image>" + "</td>");  
                    }
                }
                else {
                    if($('#logo_running_' + jobid).length == 0) {
                        $('#row_' + jobid).append("<td id='logo_running_" + jobid + "'>" + "&nbsp;&nbsp;<image id='" + jobid + "_img' src=/static/img/running.gif ></image>" + "</td>");   
                    }
                }
                $('#' + jobid + '_img').attr("width", "16");
                $('#' + jobid + '_img').attr("height", "16");

            }
            $('.job_entry').click(function(event) {
                event.preventDefault();
                // First empty the output area
                // so as not to append same job info
                // again and again
                $('#output_area').html('');
                $.ajax({
                    url: $(this).attr('href'),
                    success: function(response) {
                    // Expect response in the form:
                    //         minion_name: result_on_that_minion
                        for(element in response) {
                            $('#output_area').append(
                                    "<a class='rslt' id='" + element + "_result_href' " + "href='#" + element + "_result'>" + "&#10 &#13" +  element + "</a>" +
                                    //"<div id='" + element + "_result'>" + JSON.stringify(response[element], null) +  "</div>"
                                    "<div id='" + element + "_result'>" + JSON.stringify(response[element]).replace(/{/g, "").replace(/}/g, "").replace(/"/g, "").replace(/:/g, "&#13<br>").replace(/\\n/g, "<br>") +  "</div>"
                                    );
                            $('#' + element + '_result').toggle();
                            $('#' + element + '_result_href').click(function(event) {
                                event.preventDefault();
                                //The required division id is elementname_result
                                //So we have to obtain only the elementname :
                                $('#' + element + '_result').toggle();
                            });
                        }
                    }
                });     
            });
            setTimeout(job_statuses, 30000);
            function job_statuses() {
                //$(document).ajaxStart(function() {
                  //  $("body").removeClass('loading');
                //});
                $.ajax({
                    url: '/job_statuses/',
                    global: false,
                    success: function(response) {
                        for(jid in response) {
                            //if job finished on all, change icon to tick mark
                            if(response[jid][0] == response[jid][1]) {
                                $('#' + jid + '_img').attr("src", "/static/img/job_done.png");
                                $('#' + jid + '_img').attr("title", "Job completed on " + response[jid][0] + " out of " + response[jid][1] + " machines.");
                            }
                            else {
                                $('#' + jid + '_img').attr("title", "Job completed on " + response[jid][0] + " out of " + response[jid][1] + " machines.");
                            }
                        }
                        setTimeout(job_statuses, 60000);
                    }
                });
            }
        }
    });
});



