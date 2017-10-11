function create_notification_upload() {
    //TODO: The creating message while notification is being uploaded.
    server_query(
        'notification',
        'create',
        $("#notification_create_form").serializeObject(),
        {
            success: function (response) {
                $('#send-notice-modal .btn-submit').attr('data-dismiss', 'modal');
            },
            error: function () {
                alert("Error Hit send again")
                //    TODO : The error handling on failing to create notification on server
            }
        }
    );
};

function get_notification_by_type(type, duration, page) {
    //TODO: The loading display while it get's loaded
    server_query(
        'notification',
        'filter',
        {
            filter_by: ['type', 'duration'],
            type: type,
            duration: duration,
            page: page
        },
        {
            success: function (response) {
                $("#notification_list_view").html(response);
            },
            error: function (response) {
                alert("Notification fetch has failed")
                //TODO : The error handling while failing to get notification
            }
        }
    )
};


// handle change of type selection
var current_type = $('#notifications_type_select').val();
$('#notifications_type_select').change(function () {
    current_type = $(this).val();
    get_notification_by_type(current_type, current_duration, 0);

});

//handle change of time selection
var current_duration = 1;
$('#notification_time_select').on('click', '> *', function () {
    var duration = $(this).val();
    if (current_duration == duration) {
        return;
    }
    current_duration = duration;
    get_notification_by_type(current_type, current_duration, 0)
});


var duration = 'today';
