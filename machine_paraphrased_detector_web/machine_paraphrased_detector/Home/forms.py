from django import forms

class HomeInput(forms.Form):
    text = forms.CharField(
        label='', 
        widget=forms.Textarea(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Input your essay here'
            }
        ))