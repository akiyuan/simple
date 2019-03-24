from django import forms

class UserForm(forms.ModelForm):
    # описывает модель для которой делается форма
    class Meta: 
        model = User
        fields = ('username', 'email', 'password')
