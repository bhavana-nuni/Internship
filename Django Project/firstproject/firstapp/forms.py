from django import forms
from django.db.models.base import Model
from django.forms import ModelForm, fields, widgets
from firstapp.models import Rolereq, User, Userorder
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from firstproject import settings
class usgform(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2",
        "placeholder":"Enter Password",
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2",
        "placeholder":"ConfirmPassword",
    }))
    class Meta:
        model = User
        fields = ["username"]
        widgets = {
            "username":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Username",
            }),

        }


class Rltype(forms.ModelForm):
    class Meta:
        model = Rolereq
        fields= ["Uname","rltype"]
        widgets= {
            "rltype":forms.Select(attrs={
                "class":"form-control my-2"
            })
        }

class Rlupd(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","role"]
        widgets = {
            "username":forms.TextInput(attrs={
                "class":"form-control my-2",
                "readonly":True,
            }),
            "role":forms.Select(attrs={
                "class":"form-control my-2",
            }),
        }

class Pfupd(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email","age","mobilenumber","uimg"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True,
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Last Name",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Email",
			}),
		"age":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Age",
			}),
		"mobilenumber":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Mobile Number",
			}),
		}

class Chgepwd(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter Old Password"
		}))
	new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter New Password",
		}))
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter New Confirm Password",
		}))
	class Meta:
		model = User
		fields = ["old_password","new_password1","new_password2"]

class OrderForm(forms.ModelForm):
    class Meta:
        model = Userorder
        fields = ["person","t1","t1q","t2","t2q","t3","t3q","t4","t4q","number","address"]
        widgets = {
            "person":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Ordering person name",
            }),
            "t1":forms.Select(attrs={
                "class":"form-control my-2",
                "placeholder":"Select item",
            }),
            "t1q":forms.NumberInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Select quantity"
            }),
            "t2":forms.Select(attrs={
                "class":"form-control my-2",
                "placeholder":"Select item"
            }),
            "t2q":forms.NumberInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Select quantity"
            }),
            "t3":forms.Select(attrs={
                "class":"form-control my-2",
                "placeholder":"Select item"
            }),
            "t3q":forms.NumberInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Select quantity"
            }),
            "t4":forms.Select(attrs={
                "class":"form-control my-2",
                "placeholder":"Select item"
            }),
            "t4q":forms.NumberInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Select quantity"
            }),
            "number":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter number"
            }),
            "address":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter address"
            }),
        }

