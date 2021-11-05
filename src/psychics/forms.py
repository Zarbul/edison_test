from django import forms


class InputNumberForm(forms.Form):
    number = forms.IntegerField(label='Ваше число:', min_value=10, max_value=99)

