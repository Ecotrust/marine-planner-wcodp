from django.views.generic.base import TemplateView
from django.urls import re_path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django_registration.backends.activation import views as registration_views
activate = registration_views.ActivationView.activate
register = registration_views.RegistrationView.register
from mp_profile.views import *

try:
    use_openid = settings.OPENID_ENABLED
except:
    use_openid = False

urlpatterns = [
    re_path(r'^password/reset/$',
        auth_views.PasswordResetView, {'email_template_name': 'registration/mp_password_reset_email.html',
                                    'from_email': settings.DEFAULT_FROM_EMAIL,
                                    'post_reset_redirect': '/mp_profile/password/reset/done/' }),
    re_path(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView, { 'template_name': 'registration/mp_password_reset_confirm.html',
                                             'post_reset_redirect': '/mp_profile/password/reset/complete/' },
        name='mp_password_reset_confirm'),
    re_path(r'^password/reset/complete/$',
        auth_views.PasswordResetCompleteView, { 'template_name': 'registration/mp_password_reset_complete.html' }),
    re_path(r'^password/reset/done/$',
        auth_views.PasswordResetDoneView, {'template_name': 'registration/mp_password_reset_done.html'}),
    re_path(r'^password_change/(?P<username>\w+)/$', password_change),

    re_path(r'^signup/$',
        register,
        {'backend': 'registration.backends.default.DefaultBackend',
         #'disallowed_url': '',
         'success_url': 'registration/complete/',
         'template_name': 'registration/mp_registration_username_retry.html'},
         #'extra_context': {'username': 'Sam'}},
        name='mp_registration_register'
    ),
    re_path(r'^signup/registration/complete/$',
        TemplateView.as_view(template_name='registration/mp_registration_complete.html'),
        name='mp_registration_complete'),

    re_path(r'^forgot_username/$', send_username),
    re_path(r'^update_profile/(?P<username>\w+)/$', update_profile, {'use_openid': use_openid}),

    re_path(r'^duplicate_username$', duplicate_username),
    re_path(r'^verify_password$', verify_password),
]
