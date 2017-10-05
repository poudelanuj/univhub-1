// $.getScript('/path/to/imported/script.js', function()
// {
//     // script is now loaded and executed.
//     // put your dependent JS here.
// })


console.log("Loaded notificaiton_scripts");

function create_notification_upload() {
    var success_function = function (response) {
        alert(JSON.stringify(response));
    }
    server_query(
        'notification',
        'create',
        $("#notification_create_form").serializeObject(),
        {success: success_function}
    );

};

function get_notification_by_type(type, duration, page) {
    server_query(
        'notification',
        'filter',
        {
            'filter_by':['type','duration'],
            type:type,
            duration:duration,
            page: page
        },
        {
            success: function (response) {
                $("#notification_list_view").html(response);
            }
        }
    )
};


// handle change of type selection
var current_type=$('#notifications_type_select').val();
$('#notifications_type_select').change(function () {
    current_type = $(this).val();
    get_notification_by_type(current_type, current_duration, 0);

});

//handle change of time selection
var current_duration=1;
$('#notification_time_select').on('click', '> *', function() {
    var duration=$(this).val();
    if(current_duration==duration){
        return;
    }
    current_duration=duration;
    get_notification_by_type(current_type,current_duration,0)
});


var duration='today';
