# input library
from django import forms

# membuat objek form dengan nama class HomeInput yang hanya berisi satu field yaitu text area
class HomeInput(forms.Form):
    text = forms.CharField(
        label='', 
        required=True,
        widget=forms.Textarea(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Input your essay here',
                'id' : 'text_input',
                'rows':10, 'cols':100,
            }
        ))