        var tid;
        //tid = get_current_tid(); <---------------
        // TODO : Write function to get what is the current task id
        tid = 23;
        alert("In script!");
        $("#disp_area").append('<a id="submit_install_software" href="http://localhost/run_task/"</a>');
        $('#submit_install_software').html("Run task");
        $("#submit_install_software").on("click", function(event) {
            event.preventDefault();
            args[1] = Array();
            args[1][0] = $("#ibox").html();
            $.ajax({
                url: $(this).attr('href'),
                type: "GET",
                data: {
                    'tid' : 23,
                    'args': JSON.stringify(args),
                },
                success: function(response) {
                  // Print the message : " modulename installed successfully"
                    $('#mod_install_software_div').html(response);
                }
            });
        });
