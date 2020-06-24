from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm 

class UserForm(UserCreationForm):
    

    class Meta():
        model = get_user_model()
        fields = ('first_name','last_name','username','email','password1','password2')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #Customizing Labels
        self.fields['username'].label = 'User Id'
        self.fields['email'].label = 'Email Address'