from django import forms
from .models import Account
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder" : "請輸入密碼",
        'class' : "form-control",
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder" : "確認密碼",
        'class' : "form-control",
    }))
    phone_number = forms.CharField(
        label="手機號碼",
        validators=[RegexValidator(r'^09\d{8}$', "手機號碼格式錯誤")],
    )
    class Meta:
        model = Account
        fields = ['username', 'phone_number', 'email', 'password']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == "password":
                continue
            elif name == "password1":
                continue
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}
