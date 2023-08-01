from django import forms

class CalculatorForm(forms.Form):
    number1 = forms.FloatField(label='Number 1', required=True)
    number2 = forms.FloatField(label='Number 2', required=True)
    function = forms.ChoiceField(label='Function', choices=[
        ('+', '+'),
        ('-', '-'),
        ('*', '*'),
        ('/', '/'),
    ])
    