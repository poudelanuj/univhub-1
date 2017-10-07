
(function ($) {
    $.fn.serializeObject = function () {

        var self = this,
            json = {},
            push_counters = {},
            patterns = {
                "validate": /^[a-zA-Z][a-zA-Z0-9_]*(?:\[(?:\d*|[a-zA-Z0-9_]+)\])*$/,
                "key": /[a-zA-Z0-9_]+|(?=\[\])/g,
                "push": /^$/,
                "fixed": /^\d+$/,
                "named": /^[a-zA-Z0-9_]+$/
            };


        this.build = function (base, key, value) {
            base[key] = value;
            return base;
        };

        this.push_counter = function (key) {
            if (push_counters[key] === undefined) {
                push_counters[key] = 0;
            }
            return push_counters[key]++;
        };

        $.each($(this).serializeArray(), function () {

            // skip invalid keys
            if (!patterns.validate.test(this.name)) {
                return;
            }

            var k,
                keys = this.name.match(patterns.key),
                merge = this.value,
                reverse_key = this.name;

            while ((k = keys.pop()) !== undefined) {

                // adjust reverse_key
                reverse_key = reverse_key.replace(new RegExp("\\[" + k + "\\]$"), '');

                // push
                if (k.match(patterns.push)) {
                    merge = self.build([], self.push_counter(reverse_key), merge);
                }

                // fixed
                else if (k.match(patterns.fixed)) {
                    merge = self.build([], k, merge);
                }

                // named
                else if (k.match(patterns.named)) {
                    merge = self.build({}, k, merge);
                }
            }
            json = $.extend(true, json, merge);
        });

        return json;
    };

})(jQuery);


$(document).ready(function () {
    // the function to get cookie name
    function getCookie(c_name) {
        if (document.cookie.length > 0) {
            var c_start = document.cookie.indexOf(c_name + "=");
            if (c_start != -1) {
                c_start = c_start + c_name.length + 1;
                var c_end = document.cookie.indexOf(";", c_start);
                if (c_end == -1) c_end = document.cookie.length;
                return unescape(document.cookie.substring(c_start, c_end));
            }
        }
        return "";
    }
    // the function to append the csrf token into the header
    $(function () {
        $.ajaxSetup({
            headers: {
                "X-CSRFToken": getCookie("csrftoken")

            }
        });
    });

    // $('.log-btn').click(function () {
    //     $('.alert').fadeIn(500);
    //     setTimeout("$('.alert').fadeOut(1500);", 3000);
    // });

    $('.form-control').keypress(function () {
        $('.log-status').removeClass('wrong-entry');
    });

    $('.log-btn').click(function () {
        $.ajax({
           url:$('#login_form').action,
            type:"post",
            contentType:'application/json',
            data:JSON.stringify($('#login_form').serializeObject()),
            success:function(response){
               if (response['success']){
                   window.location=response['home'];
               }
            },
            error:function(response){
                $('.log-status').addClass('wrong-entry');
                setTimeout( "$('.log-status').removeClass('wrong-entry');",3500 );
                $('.alert').html('Invalid login details');
                $('.alert').removeClass('alert_log');
                $('.alert').addClass('alert_error');
                $('.alert').fadeIn();
                setTimeout( "$('.alert').fadeOut(500);$('.alert').addClass('alert_log');",3000 );
            }
        });
        $('.alert').html('Trying to Log in');
        $('.alert').fadeIn();
        //return false;  // do this if you don't want to submit the form
    });

});