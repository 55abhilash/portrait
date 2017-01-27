
$('#machines_entry').append(
        "<ul id='nav1'>" +
            "<li> <a class='sidebar_element' id='sidebar_am' href='http://localhost/all_minions/'>All minions</a>" +
            "</li>" + 
            "<li> <a class='sidebar_element' id='sidebar_pr' href='http://localhost/pending_reg/'>View Pending Registrations</a>" + 
            "</li>" +
        "</ul>" + 
        "</div>");
$('#machines').append(
        "<div class='row' id='disp_area'>" + 
            "&nbsp; &nbsp; &nbsp; &nbsp;" +
        "</div>" +
        "<div class='actionbar'>" + 
            "<ul id='nav2'>" + 
            "</ul>" +
            "</div>");
$('.actionbar').css({'left':'85%', 'width':'20%', 'height':'100%', 'padding-top':'48px', 'padding-left':'75px'});

$('#machines').toggle(false);
$('#nav1').toggle(false);

$('a#machines_entry').click(function(event) {
    $('#nav1').toggle();
    $('.sidebar_element').css({'font-size':'16px'});
});


$('a.sidebar_element').click(function(event) {
     event.preventDefault();
     if ($(this).attr('href') == "http://localhost/pending_reg/") {
         $('#disp_area').html("<b>Pending Registrations</b>");
         $('#disp_area').append("<br>" + "&nbsp;&nbsp;" +
             "<table id='minion-table'>" +
             "<tr>" +
             "<th class='tab-head'>Request from </th>" +
             "<th class='tab-head'></th>" +
             "</tr>" +
             "</table>");
     } else if ($(this).attr('href') == "http://localhost/all_minions/") {
         $('#disp_area').html("<b>All Minions</b>");
         $('#disp_area').append("<br>" + "&nbsp;&nbsp;" +
             "<table id='minion-table'>" +
             "<tr>" +
             "<th></th>" +
             "<th class='tab-head'>Minion name</th>" +
             "<th style='text-align:center;'>OS</th>" +
             "<th></th>" +
             "<th>Latest IP Address</th>" +
             "<th></th>" +
             "<th class='tab-head' style='text-align:center;'>Status</th>" +
             "<th>Refresh </th>" +
             "</tr>" +
             "</table>");
     } else if ($(this).attr('href') == "http://localhost/task_page/") {}
     $('#disp_area').css({
         'left': '25%',
         'width': '75%',
         'font-size': '100%',
         'text-align': 'center',
         'padding':'8px'
     });
     $.ajax({
         url: $(this).attr('href'),
         success: function(response) {
             if (response.status == '-1') {
                 window.location.replace(response.url);
             } else {
                 var element;
                 var selected_ids = Array();
                 var checkbox_cnt_pr = 0;
                 var checkbox_cnt_am = 0;
                 if (this.url == "http://localhost/all_minions/") {
                     for (element in response) {
                         // The table in all_minions section
                         // Note that the third column is an empty one 
                         // with just three blank spaces present
                         // This is deliberately done to increase gap between 
                         // the columns adjoining to it
                         $('#minion-table').append("<tr>" +
                             "<td style='padding: 5px;'>" + "<input type='checkbox' id=chkboxam" + checkbox_cnt_am + ">" + "</td>" +
                             "<td id='minnameam" + checkbox_cnt_am + "'>" + element + "</td>" +
                             "<td>" + response[element][0] + "</td>" +
                             "<td>" + "&nbsp;&nbsp;&nbsp;" + "</td>" +
                             "<td>" + response[element][1] + "</td>" +
                             "<td>" + "&nbsp;" + "</td>" +
                             "<td id=" + element + " class=" + response[element][2] + ">" + response[element][2] + "</td>" +
                             "<td> " + "<a class='ref' href='http://localhost/refresh?ids=" + element + "'>" + "<img src='/static/img/refresh.png' class='refresh'>" + "</a>" + "</td>" +
                             "</tr>");
                         checkbox_cnt_am += 1;
                     }
                     $('#nav2').html("<li id='actbar1'>" +
                         "<a id='am' class='ar' href='http://localhost/delete_minions/'>Delete</a>" +
                         "</li>");
                     $('#nav2').append("<li id='actbar2'>" +
                         "<a class='task_page_class' href='http://localhost/task_page/'>Connect To Selected </a>" +
                         "</li>");
                     //class = ar implies that page is to be refreshed after the corresponding ajax success
                     //class = sidebar_element implies completely new content to be put in the sidebars and disp-area
                 }
                 //Append checkboxes in front of minion names
                 else if (this.url == "http://localhost/pending_reg/") {
                     for (element in response) {
                         $('#minion-table').append("<tr>" +
                             "<td id='minnamepr" + checkbox_cnt_pr + "'>" + response[element] + "</td>" +
                             "<td style='padding: 5px;'>" + "<input type='checkbox' id=chkboxpr" + checkbox_cnt_pr + ">" + "</td>" +
                             "</tr>");
                         checkbox_cnt_pr += 1;
                     }
                     $('#nav2').html("<li id='actbar1'>" +
                         "<a id='pr' class='ar' href='http://localhost/accept/'>Accept</a>" +
                         "</li>");
                     $('#nav2').append("<li id='actbar2'>" +
                         "<a id='pr' class='ar' href='http://localhost/reject/'>Reject</a>" +
                         "</li>");
                 } else if (this.url == "http://localhost/task_page/") {
                     //$('#nav1').html("<li>" + 
                     //        "<a id='task_input' href='http://localhost/task?tid=" + response["0"]  + "'>" + response["1"] + "</a>" +
                     //        "</li>");    
                     alert(this.url);
                 }

                 function get_selected_ids(id) {
                     var i = 0;
                     var checkbox_cnt;
                     if (id == "am") {
                         checkbox_cnt = checkbox_cnt_am;
                     } else {
                         checkbox_cnt = checkbox_cnt_pr;
                     }
                     for (i = 0; i < checkbox_cnt; i++) {
                         console.log('chkbox' + id + i);
                         if (document.getElementById('chkbox' + id + i).checked) {
                             selected_ids.push($('#minname' + id + i).text());
                         }
                     }
                     return selected_ids;
                 }
                 $('a.ar').click(function(event) {
                     event.preventDefault();
                     console.log("this.attr(url) = " + $(this).attr('href'));
                     $.ajax({
                         url: $(this).attr('href'),
                         type: "GET",
                         data: {
                             'ids': JSON.stringify(get_selected_ids($(this).attr('id'))),
                         },
                         contentType: "application/json; charset=utf-8",
                         success: function(response) {
                             window.location.replace("http://localhost/#tabs-2");
                             console.log("this.url = " + this.url);
                             if (this.url.startsWith("http://localhost/delete_minions/")) {
                                 $('#sidebar_am').click();
                                 checkbox_cnt_am -= selected_ids.length;
                             } else {
                                 $('#sidebar_pr').click();
                                 checkbox_cnt_pr -= selected_ids.length;
                             }
                         }
                     });
                 });
                 $('a.task_page_class').click(function(event) {
                     event.preventDefault();
                     $('#disp_area').html("<b>Select task to apply from right pane</b>");
                     $('#nav2').html('');
                     $.ajax({
                         url: $(this).attr('href'),
                         type: "GET",
                         success: function(response) {
                             for (element in response) {
                                 $('#nav2').append("<li>" +
                                     "<a id='task_input' href='http://localhost/task?tid=" + element + "'>" + response[element] + "</a>" +
                                     "</li>");
                             }
                         }
                     });
                 });
                 $('a.ref').click(function(event) {
                     event.preventDefault();
                     $.ajax({
                         url: $(this).attr('href'),
                         type: "GET",
                         success: function(resp) {
                             for (element in resp) {
                                 if ((oc = $('#' + element).attr('class')) != resp[element][2]) {
                                     $('#' + element).toggleClass(oc + ' ' + resp[element][2]);
                                 }

                                 $('#' + element).html(resp[element][2]);
                             }

                         }
                     });
                 });
             }
             var ti = $('#minion-table');
             var pos = ti.offset();
             bottom = pos.top + ti.height()
             $('#tabs-2').css({
                 'min-height': bottom
             });
            $('#machines').toggle(true);
         }
     });
     return false; //for good measure
 });

$('#leftbar').css({'width' : '250px'});
$('#rightarea').css({'marginLeft' : '250px'});

$('#togglesidebar').click(function(event) {
    if($('#leftbar').css('width') == '250px') {
        $('#leftbar').css({'width' : '0px'});
        $('#rightarea').css({'marginLeft' : '0px'});
    }
    else {
        $('#leftbar').css({'width' : '250px'});
        $('#rightarea').css({'marginLeft' : '250px'});
    }
});  
