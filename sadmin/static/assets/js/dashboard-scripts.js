
	$(document).ready( function() {
		$(document).bind('DOMNodeInserted', function(e) {
		$('.activities-tab').pmdTab();
	});
	});

	$(document).ready( function() {

		// additional scripts for ajax call to update admins information.
		$('body').on('click','.ajaxCallForDeleteRole', function () {
			var userId = $(this).val();
			$.ajax({
				url: "ajax/CallForDeleteRole/",
				data: {'userId':userId},
				success:
					function (data)
					{
						$('#admininformations').html(data);
					}
				});
		});


		$('body').on('click','.ajaxCallForActivationRole', function () {
			var userId = $(this).val();
			$.ajax({
				url: "ajax/CallForActivationRole/",
				data: {'userId':userId},
				success:
					function (data)
					{
						$('#admininformations').html(data);
					}
				});
		});






        $(".pmd-sidebar .pmd-sidebar-nav li a").on("click", function(e) {
            // e.preventDefault();
            $(".pmd-sidebar .pmd-sidebar-nav li a").removeClass("active");
            $(this).addClass('active');
        });
		$(".select-simple").select2({
		theme: "bootstrap"
		});

		$('.aside_notifications').click(function(){
			$("#content").load('notifications.html')
		});



		$('.aside_pickup').click(function(){
			$("#content").load('pickup.html',function(){
				var datetimepickerStyles = "/static/assets/css/bootstrap-datetimepicker.css/";
				var pmddatetimepickerStyles = "/static/assets/css/pmd-datetimepicker.css/";
				$.get(datetimepickerStyles, function(css){
				$('<style type="text/css"></style>')
					.html(css)
					.appendTo("head");
				});
				$.get(pmddatetimepickerStyles, function(css){
				$('<style type="text/css"></style>')
					.html(css)
					.appendTo("head");
				});

				$.getScript("/static/assets/js/propeller.js/");
				$.getScript("/static/assets/js/moment-with-locales.js/");
				$.getScript("/static/assets/js/bootstrap-datetimepicker.js/",function(){
					$('#datepicker').datetimepicker({
					format: 'DD/MM/YYYY'
				});
				$('#timepicker').datetimepicker({
				format: 'LT'
				});
				$(".pickup .pick-up-tab-content .included_docs span del").click(function(){
					$(this).parent().remove();
				})
				});
			});

			//schedule date
			    $('#shedulePickupForm').submit(function(event) {
			    alert('check');
			     /* stop form from submitting normally */
			         event.preventDefault();
			     /* get the action attribute from the <form action=""> element */
			         var $form = $( this ),
                        url = $form.attr( 'action' );
                   /* Send the data using post with element id of all*/
                     var posting = $.post( url, { delivery_man: $('#delivery_man').val(),
                        datepicker: $('#datepicker').val(), timepicker: $('#timepicker').val() } );

                      alert('done here');
                     posting.done(function( data ) {
                      alert('success');
                      });

                });

                    // remove documents from pickup
                $('#content').on('click', '.ajaxRemovePickupDocument', function() {
                  var documentID = $(this).val();
                 $.ajax({
                        url: "ajax/ajaxRemovePickupDocument/",
                        data: {'documentID':documentID}

                         });
                 $(this).parent().remove();
                });
		});


		$('.aside_students').click(function(){
			$("#content").load('students-list.html',function(){
				$.getScript("/static/assets/js/propeller.js/" );
				$.getScript("/static/assets/js/circle-progress.min.js/",function(){
					$('.student-progress').circleProgress({
						startAngle: 4.75,
						size: 80,
						thickness: "5",
						animation:false,
						fill: "#10a084"
					  });
				});
			});
		});

		$('.aside_offers').click(function(){
			$("#content").load('offers.html',function(){
				$.ajaxSetup({ cache: true });
				var datetimepickerStyles = "/static/assets/css/bootstrap-datetimepicker.css";
				var pmddatetimepickerStyles = "/static/assets/css/pmd-datetimepicker.css";
				$.get(datetimepickerStyles, function(css){
				$('<style type="text/css"></style>')
					.html(css)
					.appendTo("head");
				});
				$.get(pmddatetimepickerStyles, function(css){
				$('<style type="text/css"></style>')
					.html(css)
					.appendTo("head");
				});
				$.getScript("/static/assets/js/moment-with-locales.js",function(){
					$.ajaxSetup({ cache: false });
				});
				$.getScript('/static/assets/js/bootstrap-datetimepicker.js',function(){
					$('#offer-datepicker').datetimepicker({
						format: 'DD/MM/YYYY',
					});
					$.ajaxSetup({ cache: false });
				});
				$('#offer_university, #scholarship_percentage').parent().hide();
				$('#offer_type').each(function() {
					$('#offer_type').on('change', function() {
						if( $('#offer_type option : selected').text() == "Test Classes Discount" ){
							$('#offer_university, #scholarship_percentage').parent().hide();
							$('#offer_class,  #discount_percentage').parent().show();
						}
						else if( $('#offer_type option:selected').text() == "Scholarship" ){
							$('#offer_class, #discount_percentage').parent().hide();
							$('#offer_university, #scholarship_percentage').parent().show();
						}
						else if( $('#offer_type option:selected').text() == "Discount" ){
							$('#offer_class, #offer_university, #scholarship_percentage').parent().hide();
							$('#discount_percentage').parent().show();
						}
					});
				});
			});
		});

		$('.aside_classes').click(function(){
			$("#content").load('classes.html',function(){
				$.ajaxSetup({ cache: true });
				var datetimepickerStyles = "/static/assets/css/bootstrap-datetimepicker.css";
				var pmddatetimepickerStyles = "/static/assets/css/pmd-datetimepicker.css";
				$.get(datetimepickerStyles, function(css){
				$('<style type="text/css"></style>')
					.html(css)
					.appendTo("head");
				});
				$.get(pmddatetimepickerStyles, function(css){
				$('<style type="text/css"></style>')
					.html(css)
					.appendTo("head");
				});
				$.getScript('/static/assets/js/moment-with-locales.js',function(){
					$.ajaxSetup({ cache: false });
				});
				$.getScript('/static/assets/js/bootstrap-datetimepicker.js',function(){
					$('#class_start_date-datepicker').datetimepicker({
						format: 'DD/MM/YYYY',
					});
					$.ajaxSetup({ cache: false });
				});
				$.getScript('/static/assets/js/bootstrap-datetimepicker.js',function(){
					$('#class_end_date-datepicker').datetimepicker({
						format: 'DD/MM/YYYY',
						useCurrent: false
					});
					$.ajaxSetup({ cache: false });
				});
				// start date picke on chagne event [select minimun date for end date datepicker]
				$("#class_start_date-datepicker").on("dp.change", function (e) {
					$('#class_end_date-datepicker').data("DateTimePicker").minDate(e.date);
				});
				// Start date picke on chagne event [select maxmimum date for start date datepicker]
				$("#class_end_date-datepicker").on("dp.change", function (e) {
					$('#class_start_date-datepicker').data("DateTimePicker").maxDate(e.date);
				});
			});
		});
    });
	// SAMPLE JSON DATA FOR MAP
	var regions=[
	{
        "district_name": "Baglung",
        "total_students": 188,
        "visa_granted": 48,
        "today_registered": 126,
        "app_on_process": 10
    },
    {
        "district_name": "Mustang",
        "total_students": 1258,
        "visa_granted": 458,
        "today_registered": 126,
        "app_on_process": 12
    },
	{
        "district_name": "Manang",
        "total_students": 1258,
        "visa_granted": 0,
        "today_registered": 126,
        "app_on_process": 26
    }
	,
	{
        "district_name": "Kathmandu",
        "total_students": 12058,
        "visa_granted": 4500,
        "today_registered": 126,
        "app_on_process": 16
    }
	];

	function hover(){
		$('#geo_select option[value="Default"]').attr("selected", true);
		$('.map g path').css("fill","rgb(204, 204, 204)");
	$('.info_panel').remove();
	for (i = 0; i < regions.length; i++) {
    $('#'+ regions[i].district_name).data('region', regions[i]);

	}
	var region_data=$(this).data('region');
	$('<div class="info_panel">'+
		region_data.district_name +'<br> Total Students: '+
		region_data.total_students +'<br> Visa Granted: '+
		region_data.app_on_process +'<br> Application on Process: '+
		region_data.visa_granted +'<br> Today Registered: '+
		region_data.today_registered +
		'</div>'
		).appendTo('body');
}
function mousemove(e){
	var mouseX = e.pageX, //X coordinates of mouse
            mouseY = e.pageY; //Y coordinates of mouse
        $('.info_panel').css({
            top: mouseY-110,
            left: mouseX - ($('.info_panel').width()/2)
        });
}
function mouseleave(){
	$('.info_panel').remove();
	$('#geo_select option[value="Default"]').attr("selected", true);
}

$('.map g').mouseover(hover).mousemove(mousemove).mouseleave(mouseleave);


$('#geo_select').each(function() {
$('#geo_select').on('change', function(e) {
$('.info_panel').remove();
$('#geo_select option[value="Default"]').attr("selected", false);
$('.map g path').css("fill","rgb(204, 204, 204)");
var geo_name = $(this).find( 'option:selected' ).val();
var ids = $('#map-svg > g').map(function(){
  return $(this).attr('id');
  }).get();
var check = $.inArray(geo_name,ids);
	if (check){
		$('#'+geo_name+' path').css("fill","#6dbfaf");
		// Run function to show data in districts
	for (i = 0; i < regions.length; i++) {
    $('#'+ regions[i].district_name).data('region', regions[i]);

	}
	var region_data = $( ".map " +"#"+geo_name ).data('region');
		$('<div class="info_panel">'+
		region_data.district_name +'<br> Total Students: '+
		region_data.total_students +'<br> Visa Granted: '+
		region_data.app_on_process +'<br> Application on Process: '+
		region_data.visa_granted +'<br> Today Registered: '+
		region_data.today_registered +
		'</div>'
		).appendTo("body");
		var offsets = $(".map " +"#"+geo_name).offset();
		var top  = offsets.top-110,
			left = offsets.left-60
		$('.info_panel').css({
            top: top,
            left: left
        });

	// --------==================================---------------------------//
	}
});
});



//the function to serialie the json object
(function($){
    $.fn.serializeObject = function(){

        var self = this,
            json = {},
            push_counters = {},
            patterns = {
                "validate": /^[a-zA-Z][a-zA-Z0-9_]*(?:\[(?:\d*|[a-zA-Z0-9_]+)\])*$/,
                "key":      /[a-zA-Z0-9_]+|(?=\[\])/g,
                "push":     /^$/,
                "fixed":    /^\d+$/,
                "named":    /^[a-zA-Z0-9_]+$/
            };


        this.build = function(base, key, value){
            base[key] = value;
            return base;
        };

        this.push_counter = function(key){
            if(push_counters[key] === undefined){
                push_counters[key] = 0;
            }
            return push_counters[key]++;
        };

        $.each($(this).serializeArray(), function(){

            // skip invalid keys
            if(!patterns.validate.test(this.name)){
                return;
            }

            var k,
                keys = this.name.match(patterns.key),
                merge = this.value,
                reverse_key = this.name;

            while((k = keys.pop()) !== undefined){

                // adjust reverse_key
                reverse_key = reverse_key.replace(new RegExp("\\[" + k + "\\]$"), '');

                // push
                if(k.match(patterns.push)){
                    merge = self.build([], self.push_counter(reverse_key), merge);
                }

                // fixed
                else if(k.match(patterns.fixed)){
                    merge = self.build([], k, merge);
                }

                // named
                else if(k.match(patterns.named)){
                    merge = self.build({}, k, merge);
                }
            }
            json = $.extend(true, json, merge);
        });

        return json;
    };

})(jQuery);

function create_notification_upload(){
    data=$("#notification_create_form").serializeObject();

    data['action']={data:'notification',operation:'create'}

     $.ajax({ // create an AJAX call...
        "data":JSON.stringify(data)  , // get the form data
        type: "post", // GET or POST
        contentType: "application/json",
        url: 'jsonhandler.django', // the file to call
        success: function(response) { // on success..
                alert(JSON.stringify(response))
        }
     });

     alert("Serialized:"+JSON.stringify(data));
}


