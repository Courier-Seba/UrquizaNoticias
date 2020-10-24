from django.contrib.auth.forms import UserCreationForm
from .models import UrquizaUser

class UrquizaUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = UrquizaUser
        fields = ('email', 'username', 'password1', 'password2')
