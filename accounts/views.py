from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from validate_email import validate_email
from dynamictariff.url import get_url
from .tokens import generate_token
import requests

def register_view(request):
    if request.method == 'POST':
        context = {
            'data': request.POST,
            'has_error': False
        }
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = email
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if name == '':
            messages.add_message(request, messages.ERROR, 'Name is Required')
            context['has_error'] = True
        if len(password1) < 3:
            messages.add_message(request, messages.ERROR, 'passwords should be atleast 3 characters long')
            context['has_error'] = True
        if password1 != password2:
            messages.add_message(request, messages.ERROR, 'passwords do not match')
            context['has_error'] = True
        if not validate_email(email):
            messages.add_message(request, messages.ERROR, 'Please provide a valid email')
            context['has_error'] = True
        
        url = get_url("appF.php")
        pload = {'name':name, 'email':email, 'password':password1, 'function':'SignUpWeb'}
        response = requests.post(url, data = pload).text
        if response[-1] == '0':
            pass
        elif response[-1] == '2':
            messages.add_message(request, messages.ERROR, 'Email is Already Registered!')
            context['has_error'] = True
        else:
            messages.add_message(request, messages.ERROR, 'Sign Up Failed! Try Again Later!')
            context['has_error'] = True

        if context['has_error']:
            return render(request, 'accounts/register.html', context, status=400)

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password1)
        user.first_name = name
        # user.last_name = 
        user.is_active = False
        user.save()

        current_site = get_current_site(request)
        email_subject = 'Activate your account'
        message = render_to_string('accounts/activate.html', 
                {
                    'user': user,
                    'domain': current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':generate_token.make_token(user),
                }
                )

        email_message = EmailMessage(
            email_subject,
            message,
            settings.EMAIL_HOST_USER,
            [email]
        )

        email_message.send()
        messages.add_message(request, messages.SUCCESS, 'Account created succesfully. Confirm your email to sign in')

        return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':

        context = {
            'data': request.POST,
            'has_error': False
        }
        email = request.POST.get('email')
        password = request.POST.get('password1')
        
        if email == '':
            messages.add_message(request, messages.ERROR, 'Email is required')
            context['has_error'] = True
        if password == '':
            messages.add_message(request, messages.ERROR, 'Password is required')
            context['has_error'] = True

        url = get_url("appF.php")
        pload = {'email':email, 'password':password, 'function':'LoginWeb'}
        response = requests.post(url, data = pload).text
        if response[-1] == '0':
            try:
                user = User.objects.get(email=email)
            except(User.DoesNotExist):
                name = response[10:-3]
                user = User.objects.create_user(username=email, email=email)
                user.set_password(password)
                user.first_name = name
                # user.last_name = 
                user.is_active = bool(response[-2])
                user.save()
                user = User.objects.get(email=email)
        elif response[-1] == '1':
            messages.add_message(request, messages.ERROR, 'Wrong Password')
            context['has_error'] = True
        elif response[-1] == '2':
            messages.add_message(request, messages.ERROR, 'Record does not exist')
            return render(request, 'accounts/login.html')
        else:
            messages.add_message(request, messages.ERROR, 'Something went wrong! Contact admin')
            return render(request, 'accounts/login.html')

        if context['has_error']:
            return render(request, 'accounts/login.html', status=401, context=context)
        
        login(request, user)

        if 'next' in request.POST:
            return redirect(request.POST.get('next'))
        else:
            return redirect('userApp:home')

    else:
        return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Signed out successfully')
    return redirect('accounts:login')

def ActivateView(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and generate_token.check_token(user, token):
        email = user.email
        url = get_url("appF.php")
        pload = {'email':email, 'function':'VerifyWeb'}
        response = requests.post(url, data = pload).text
        if response[-1] == '0':
            user.is_active = True
            user.save()
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Thank you for your email confirmation.')
        else:
            messages.add_message(request, messages.ERROR, 'Email confirmation failed.')
        return redirect('userApp:home')
    else:
        messages.add_message(request, messages.ERROR, 'Activation link is invalid! Please re-request the activation link')
        return redirect('accounts:register')
