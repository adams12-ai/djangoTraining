from django.forms import ModelForm

from accounts.models import Customer


class RegisterForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
