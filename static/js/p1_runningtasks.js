//Running tasks tab
//Table consists of these coloumns:
//      Task name
//      JID
//      Status

$('#runningtasks').html(
        "<div class='row' id='disp_area_tasks'>" +
        "&nbsp; &nbsp; &nbsp; &nbsp;" +
        "</div>"
);
 $('#disp_area_tasks').css({
    'left': '25%',
    'width': '75%',
    'font-size': '100%',
    'text-align': 'center',
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
        "<th> Status</th>" +
        "<th> Refresh</th>" +
        "</tr>" +
        "</table>"
);
$('#runningtasks').toggle(false);
$('#runningtasks_entry').click(function(event) {
    $('#machines').hide();
    $('#runningtasks').toggle();
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
for(item in all_jids_list) {
    var parsed_item = all_jids_list[item].split(",");
    var taskname = parsed_item[0];
    var jobid = parsed_item[1];
    $('#task_table').append(
            "<tr>" +
            "<td>" + taskname + "</td>" +
            "<td>" + "<a href='http://localhost/task/job_info?jobid=" + jobid + "'>" + jobid + "</a></td>" +
            "<td>" + "<image src=/path/to/gif ></image>" + "</td>" + 
            "<td>" + "<a class='ref' href='http://localhost/task/get_status?jobid=" + jobid + "'>" + "<img src='/static/img/refresh.png' class='refresh'>" + "</a>" + "</td>" + 
            "</tr>"
            );
    
}
});

