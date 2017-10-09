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
$('.student_profile_uploaded_documents').click(function(){

$('#detailportion').load('/student/uploadeddocuments/'+$(this).attr('data-student_id'));
});

$('.student_profile_applied_universities').click(function(){

$('#detailportion').load('/student/applieduniversities/'+$(this).attr('data-student_id'));
});

$('.student_profile_classes').click(function(){

$('#detailportion').load('/student/classes/'+$(this).attr('data-student_id'));
});