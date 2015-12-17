from django.forms import ModelForm
from nocaptcha_recaptcha.fields import NoReCaptchaField

from simpleapp.models import Feedback


class FeedbackForm(ModelForm):
    captcha = NoReCaptchaField()

    class Meta:
        model = Feedback
        fields = ['name', 'category', 'subject', 'text']
