from django.contrib.auth.models import User
from django.forms import ModelForm


class Profile(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


