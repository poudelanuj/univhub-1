from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from sadmin.forms import SignupForm
from sadmin.tokens import account_activation_token


def signup_student(request):
    try:
        form = SignupForm(request)
        if form.is_valid():
            user = form.save()
            subject = 'Activate your UnivHub Account.'
            message = render_to_string('acc_active_email.html', {
                'user': user, 'domain': '127.0.0.1:8000',
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            # user.email_user(subject, message)
            toemail = form.cleaned_data.get('email')
            email = EmailMessage(subject, message, to=[toemail])
            email.send()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'Reason': "Form data is not valid", "errors": form.errors})
    except Exception as e:
        print("Exception", *e.args)
        return JsonResponse({'success': False})
