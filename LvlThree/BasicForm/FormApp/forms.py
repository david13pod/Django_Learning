from django import forms
from django.core import validators

# Another custom validator
def check_for_z (value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Need name starting with z')

class Formname(forms.Form):
    name=forms.CharField(validators=[check_for_z])
    email=forms.EmailField()
    verifyemail=forms.EmailField(label='Enter email again')
    text=forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False, widget=forms.HiddenInput,
                            validators=[validators.MaxLengthValidator(0)])



    def clean(self):
        all_cleandata= super().clean()
        email=all_cleandata['email']
        vmail=all_cleandata['verifyemail']

        if email != vmail:
            raise forms.ValidationError('check email again')




    #for custom validation
    # def clean_botcatcher(self):
    #     botcatcher=self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError('caught you')
    #     return botcatcher