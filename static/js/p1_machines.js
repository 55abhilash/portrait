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


// Pretty bad code I know,
// please bear with me.
// I'll organise this give me time :) 

//Did it ;)
var all_minions_list = Array();
var all_jids_list = Array();
$('#machines_entry').append(
        "<ul id='nav1'>" +
            "<li> <a class='sidebar_element' id='sidebar_am' href='/all_minions/'>All minions</a>" +
            "</li>" +
            "<li> <a class='sidebar_element' id='sidebar_pr' href='/pending_reg/'>View Pending Registrations</a>" +
            "</li>" +
        "</ul>" +
        "</div>");
$('#machines').html(
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
     // What is clicked on in the left pane under machines;
     // All minions or pending registrations
     // display respective html
     $('#runningtasks').hide();
     $('#dashboard').hide();
     if ($(this).attr('href') == "/pending_reg/") {
         $('#disp_area').html("<b>Pending Registrations</b>");
         $('#disp_area').append("<br>" + "&nbsp;&nbsp;" +
             "<table id='minion-table' class='minion-table'>" +
             "<tr>" +
             "<th class='tab-head'>Request from </th>" +
             "<th class='tab-head'></th>" +
             "</tr>" +
             "</table>");
     } else if ($(this).attr('href') == "/all_minions/") {
         $('#disp_area').html("<b>All Minions</b>");
         $('#disp_area').append("<br>" + "&nbsp;&nbsp;" +
             "<table id='minion-table' class='minion-table'>" +
             "<tr>" +
             "<th> <input id='select_all' type='checkbox'> </a></th>" +
             "<th class='tab-head'>Minion name</th>" +
             "<th style='text-align:center;'>OS</th>" +
             "<th></th>" +
             "<th>Latest IP Address</th>" +
             "<th></th>" +
             "<th class='tab-head' style='text-align:center;'>Status</th>" +
             "<th> </th>" +
             "</tr>" +
             "</table>");
     } else if ($(this).attr('href') == "/task_page/") {}
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
                 if (this.url == "/all_minions/") {
                     for (element in response) {
                         // The table in all_minions section
                         // Note that the third column is an empty one
                         // with just three blank spaces present
                         // This is deliberately done to increase gap between
                         // the columns adjoining to it
                         
                         if($.inArray(element, all_minions_list) == -1) 
                            all_minions_list.push(element);
                         $('#minion-table').append("<tr>" +
                             "<td style='padding: 5px;'>" + "<input type='checkbox' id=chkboxam" + checkbox_cnt_am + ">" + "</td>" +
                             "<td id='minnameam" + checkbox_cnt_am + "'>" + element + "</td>" +
                             "<td>" + response[element][0] + "</td>" +
                             "<td>" + "&nbsp;&nbsp;&nbsp;" + "</td>" +
                             "<td>" + response[element][1] + "</td>" +
                             "<td>" + "&nbsp;" + "</td>" +
                             "<td id=" + element + " class=" + response[element][2] + ">" + response[element][2] + "</td>" +
                             "<td> " + "<a class='ref' href='/refresh?ids=" + element + "'>" + "<img src='/static/img/refresh.png' class='refresh'>" + "</a>" + "</td>" +
                             "</tr>");
                         checkbox_cnt_am += 1;
                     }
                     $('#nav2').html("<li id='actbar1'>" +
                         "<a id='am' class='ar' href='/delete_minions/'>Delete</a>" +
                         "</li>");
                     $('#nav2').append("<li id='actbar2'>" +
                         "<a class='task_page_class' href='/task_page/'>Task Menu</a>" +
                         "</li>");
                     $('#nav2').append("<li id='actbar3'>" +
                         "<a id='ra' class='ar' href='/refresh/'>Refresh</a>" +
                         "</li>");
                     //class = ar implies that page is to be refreshed after the corresponding ajax success
                     //class = sidebar_element implies completely new content to be put in the sidebars and disp-area
                 }
                 //Append checkboxes in front of minion names
                 else if (this.url == "/pending_reg/") {
                     for (element in response) {
                         $('#minion-table').append("<tr>" +
                             "<td id='minnamepr" + checkbox_cnt_pr + "'>" + response[element] + "</td>" +
                             "<td style='padding: 5px;'>" + "<input type='checkbox' id=chkboxpr" + checkbox_cnt_pr + ">" + "</td>" +
                             "</tr>");
                         checkbox_cnt_pr += 1;
                     }
                     $('#nav2').html("<li id='actbar1'>" +
                         "<a id='pr' class='ar' href='/accept/'>Accept</a>" +
                         "</li>");
                     $('#nav2').append("<li id='actbar2'>" +
                         "<a id='pr' class='ar' href='/reject/'>Reject</a>" +
                         "</li>");
                 } else if (this.url == "/task_page/") {
                     //$('#nav1').html("<li>" +
                     //        "<a id='task_input' href='http://localhost/task?tid=" + response["0"]  + "'>" + response["1"] + "</a>" +
                     //        "</li>");
                     alert(this.url);
                 }

                 function get_selected_ids(id) {
                     var i = 0;
                     var checkbox_cnt;
                     if ((id == "am") || (id == "ra")) {
                         checkbox_cnt = checkbox_cnt_am;
                     } else {
                         checkbox_cnt = checkbox_cnt_pr;
                     }
                     for (i = 0; i < checkbox_cnt; i++) {
                         if(id == "ra") {
                            id = "am";
                         }
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
                             window.location.replace("/#tabs-2");
                             console.log("this.url = " + this.url);
                             if (this.url.startsWith("/delete_minions/")) {
                                 $('#sidebar_am').click();
                                 checkbox_cnt_am -= selected_ids.length;
                             } else if (this.url.startsWith("/pending_reg/")){
                                 $('#sidebar_pr').click();
                                 checkbox_cnt_pr -= selected_ids.length;
                             } else {
                                 $('#sidebar_am').click();
                             }
                             
                         }
                     });
                 });

                 // Request the html for new module installation
                 // The link for it has id = install_mod_page

                 $('a.task_page_class').click(function(event) {
                     event.preventDefault();
                     var jids_list = Array();
                     $('#disp_area').html("<b>Select task to apply from right pane</b>");
                     $('#nav2').html('');
                     $.ajax({
                         url: $(this).attr('href'),
                         type: "GET",
                         success: function(response) {
                             for (element in response) {
                                 $('#nav2').append("<li>" +
                                     "<a class='task_input' id='task_input' href='/task/" + element + "'>" + response[element] + "</a>" +
                                     "</li>");
                             }
                                $('#nav2').append("<li>" +
                                    "<a class='install_mod_page' href='/install_mod_page/'>Install new module</a>" +
                                    "</li>");
                                // The click event handler of install_mod_page needs
                                // to exist in the block where we append the element
                                // with the class install_mod_page.
                                // Eg. Here we write the event handler inside the
                                // success function of the ajax request
                                $('a.install_mod_page').click(function(event) {
                                    event.preventDefault();
                                    $("#disp_area").html("<b> Install new module </b>");
                                    $.ajax({
                                        url: $(this).attr('href'),
                                        type: "GET",
                                        success: function(resp) {
                                            $("#disp_area").append(resp);
                                /*$('#modform').submit(function(event) {
                                    event.preventDefault();
                                    alert("Clicked");
                                    $.ajax({
                                        url: "http://localhost/install_mod/",
                                        type: "POST",
                                        data: {
                                            'name': $('#name').val(),
                                            'desc': $('#desc').val(),
                                            'modfile': $('#modfile').val(),
                                            'csrfmiddlewaretoken': '{{csrf_token}}'
                                        },
                                        success : function(response) {
                                            $('#disp-area').html(response);
                                        }
                                    });
                                });*/
                                        }
                                    });
                                });
                                $('a.task_input').click(function(event) {
                                    event.preventDefault();
                                    $.ajax({
                                        url: $(this).attr('href'),
                                        type: "GET",
                                        success: function(resp) {
                                            $('#disp_area').html(resp);
                                            $('#disp_area').append("<b>Run on </b> " + 
                                                                   "<div  id=minion_bar style='padding: 0px 0px 0px 350px;'  >" +
                                                                   "<table id=minion_bar_tab ></table>" +
                                                                   '</div>');
                                            for(item in all_minions_list) { 
                                                $('#minion_bar_tab').append(
                                                        "<tr>" +
                                                        "<td style='padding: 5px;'>" + 
                                                        "<input type='checkbox' id='" + all_minions_list[item] + "chk'>" + 
                                                        "</td>" +
                                                        "<td id='" + all_minions_list[item] + "'>" + all_minions_list[item] + "</td>" +
                                                        "</tr>");
                                            }
                                        }
                                    });
                                });
                                
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
     $('#select_all').click(function(event) {
            var v = 0;
            if(document.getElementById('select_all').checked) {
                for(v = 0; v < all_minions_list.length; v++) {
                    $('#chkboxam' + v)[0].checked = true;
                }   
            }
            else {
                for(v = 0; v < all_minions_list.length; v++) {
                    $('#chkboxam' + v)[0].checked = false;
                }
            }
        });
     return false; //for good measure
 });

// Return the list of selected minions 
// from the table of all minions
// below the html of every task
//
function get_selected_minions() {
    var mins = Array();
    // Iterate over list of minions
    for(item in all_minions_list) {
        // The minions list checkboxes are labelled as:
        // // minionnamechk
        if(document.getElementById(all_minions_list[item] + 'chk').checked) {
                mins.push(all_minions_list[item]);
        }
    }
    return mins;
}

// Add new task to the running tasks tab
// JID is a hyperlink to check the status
// of that particular task

function new_task(taskname, jid) {
    if($.inArray(taskname + ',' + jid, all_jids_list) == -1) 
        all_jids_list.push(taskname + ',' + jid);
}

// Remove the minion table if not required by plugin
// WIll be present by default

function no_minions_disp() {
    $('#minion_bar_tab').html('');
}
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
