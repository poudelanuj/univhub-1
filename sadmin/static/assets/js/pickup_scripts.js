

$('#scheduleDateButton').click(function(){

alert("called here");
//    $.ajax({
//        type: 'POST',
//        url: "/sadmin/requesthandler/pickup/scheduledate/",
//        data: $("#scheduleDateForm").serialize(),
//        success :
//        });
//});
server_query('pickup','scheduledate',
    $("#scheduleDateForm").serializeObject(),
    {success:
        function(data) {
                $('#schedule-date').modal('toggle');
         }
     }
)