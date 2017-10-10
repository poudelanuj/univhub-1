$(document).ready( function() {
    $(".profile-sidenav-nav li a").on("click", function(e) {
        e.preventDefault();
        $(".profile-sidenav-nav li a").removeClass("active");
        $(this).addClass('active');
    });
});
    $(document).ready( function() {
    $('.overview-details-tab').pmdTab();
});

$(function () {
        $('[data-toggle="tooltip"]').tooltip()
    })

$('input:radio[name="currentaddres_same_per"]').change(
    function(){
        if (this.checked && this.value == 'no') {
            $('.currentaddres_same_per').css("display","block")
        }
        else{
            $('.currentaddres_same_per').css("display","none")
        }
    });

    $(document).ready( function() {
        $(".profile-sidenav-nav li a").on("click", function(e) {
            e.preventDefault();
            $(".profile-sidenav-nav li a").removeClass("active");
            $(this).addClass('active');
        });
        $(".select-simple, .select-simple2").select2({
        theme: "bootstrap",
        minimumResultsForSearch: Infinity,
    });
    });

 	$(document).ready( function() {
		$('.overview-details-tab').pmdTab();
    });
    $(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

$('input:radio[name="currentaddres_same_per"]').change(
    function(){
        if (this.checked && this.value == 'no') {
            $('.currentaddres_same_per').css("display","block");
        }
        else{
            $('.currentaddres_same_per').css("display","none");
        }
    });

	$('.datepicker-dob-bs.date, .datepicker-dob-ad.date').datepicker({
    clearBtn: true,
    autoclose: true,
    startView: 2,
    clearBtn: true,
    todayHighlight: true
});

$('.sponsors #relationship').each(function() {
$('.sponsors #relationship').on('change', function() {
var relationship_name = $(this).find( 'option:selected' ).val();
if( relationship_name == 'other'){
    $(this).parent().parent().find(".mention_relationship").css("display","block");
}
else{
    $(this).parent().parent().find(".mention_relationship").css("display","none");
}
});
});


// -------------------------------//


var regex = /^(.+?)(\d+)$/i;
var addIndex = $(".sponsors").length + 1;

if ($(".sponsors").length == 1) {
        $('.btn-remove').hide();
    } else {
        $('.btn-remove').show();
    }

function add(){
    $(this).siblings('#sponsors').children(".sponsors:last").clone(true,true).appendTo("#sponsors").attr("id", "sponsor" +  addIndex).find("*").each(function() {
        $(".sponsors:last-child input").val("");
            var id = this.id || "";
            var match = id.match(regex) || [];
            if (match.length == 3) {
                this.id = match[1] + (addIndex);
            }
        })
        .on('click', '.btn-add', add)
        .on('click', '.btn-remove', remove);
        addIndex++;
        if ($(".sponsors").length > 1) {
            $(".btn-add").hide();
        }
        else{
            $(".btn-add").show();
        }
        if ($(".sponsors").length == 1) {
        $('.btn-remove').hide();
    } else {
        $('.btn-remove').show();
    }


}


function remove(){
    $(this).parent(".sponsors").remove();
    if ($(".sponsors").length == 1) {
        $('.btn-remove').hide();
    } else {
        $('.btn-remove').show();
    }
    if ($(".sponsors").length > 5) {
            $(".btn-add").hide();
        }
        else{
            $(".btn-add").show();
        }
}

    $(".btn-add").on("click", add);
    $(".btn-remove").on("click", remove);

$('.student_profile_uploaded_documents').click(function(){

$('#detailportion').load('/student/uploadeddocuments/'+$(this).attr('data-student_id'));
});

$('.student_profile_applied_universities').click(function(){

$('#detailportion').load('/student/applieduniversities/'+$(this).attr('data-student_id'));
});

$('.student_profile_classes').click(function(){

$('#detailportion').load('/student/classes/'+$(this).attr('data-student_id'));
});

$('.student_profile_notice').click(function(){

$('#detailportion').load('/student/notice/'+$(this).attr('data-student_id'));
});

$('.student_edit_profile').click(function(){

$('#detailportion').load('/student/editprofile/'+$(this).attr('data-student_id'));
});