from django import forms
g=[['male','MALE'],['female','FEMALE']]
class ContactForm(forms.Form):
    name=forms.CharField(max_length=100,label='First',label_suffix='Name',help_text='please enter first name',required=True)
    age=forms.IntegerField(max_value=50)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)

