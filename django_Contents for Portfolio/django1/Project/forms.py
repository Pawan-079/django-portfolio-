from django import forms


class userForm(forms.Form):
    num1=forms.CharField(label="value1",required=True,widget=forms.Textarea(attrs={'class':'form-control'}))
    
    num1=forms.CharField(label="value2") 