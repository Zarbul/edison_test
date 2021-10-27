from django import forms


class InputNumberForm(forms.Form):
    number = forms.IntegerField(label='You`r number:', min_value=10, max_value=99)

