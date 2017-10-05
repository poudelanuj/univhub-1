  console.log("pickup_js loaded");

$('#scheduleDateButton').click(function(){

alert("check");
//    server_query(
//        'pickup',
//        'schedule',
//        $("#scheduleDateForm").serializeObject(),
//        {success:function(response){
//            alert(JSON.stringify(response));
//        }}
//    )
    $.ajax({
        type: 'POST',
        url: "ajaxscheduledate/",
        data: $("#scheduleDateForm").serialize(),
        success : function(data) {
                $('#schedule-date').modal('toggle');
         }
        });
});
