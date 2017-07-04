from __future__ import unicode_literals
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field
from authtools import forms as authtoolsforms
from django.contrib.auth import forms as authforms
from django.core.urlresolvers import reverse


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, initial=False, label='Запомнить меня')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["username"].widget.input_type = "email"  # ugly hack

        self.helper.layout = Layout(
            Field('username', placeholder="Введите Email", autofocus=""),
            Field('password', placeholder="Введите пароль"),
            HTML('<a href="{}">Забыли пароль?</a>'.format(
                reverse("accounts:password-reset"))),
            Field('remember_me'),
            Submit('sign_in', 'Войти',
                   css_class="btn btn-lg btn-primary btn-block"),
        )


class SignupForm(authtoolsforms.UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['password2'].help_text = "Введите пароль еще раз, для подтверждения."
        self.helper = FormHelper()
        self.fields["email"].widget.input_type = "email"  # ugly hack

        self.helper.layout = Layout(
            Field('email', placeholder="Введите Email", autofocus=""),
            Field('name', placeholder="Введите ФИО"),
            Field('password1', placeholder="Введите Пароль"),
            Field('password2', placeholder="Повторите Пароль"),
            Submit('sign_up', 'Регистрация', css_class="btn-warning"),
        )


class PasswordChangeForm(authforms.PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field('old_password', placeholder="Введите старый пароль",
                  autofocus=""),
            Field('new_password1', placeholder="Введите new пароль"),
            Field('new_password2', placeholder="Введите new пароль (еще раз)"),
            Submit('pass_change', 'Изменить пароль', css_class="btn-warning"),
        )


class PasswordResetForm(authtoolsforms.FriendlyPasswordResetForm):

    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field('email', placeholder="Введите email",
                  autofocus=""),
            Submit('pass_reset', 'Сброс пароля', css_class="btn-warning"),
        )


class SetPasswordForm(authforms.SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(SetPasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field('new_password1', placeholder="Введите новый пароль",
                  autofocus=""),
            Field('new_password2', placeholder="Введите новый пароль (еще раз)"),
            Submit('pass_change', 'Изменить пароль', css_class="btn-warning"),
        )
