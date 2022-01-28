from django.forms import ModelForm
from .models import Fooditem, UserFooditem
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class fooditemForm(ModelForm):
    class Meta:
        models = Fooditem
        fields = '__all__'


class addUserFooditem(ModelForm):
    class Meta:
        model = UserFooditem
        fields = '__all__'

class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']