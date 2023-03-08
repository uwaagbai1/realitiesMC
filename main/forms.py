from django import forms

class ContactForm(forms.Form):

	full_name = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'required data-error':'Please enter your name',}), max_length = 50)
	subject = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject', 'required data-error':'Please enter a Subject',}), max_length = 50)
	email_address = forms.EmailField(widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Email', 'required data-error':'Please enter your Email Address',}),  max_length = 150)
	message = forms.CharField(widget = forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Leave a message here', 'style':'height:200px', 'required data-error':'Please enter a message',}), max_length = 2000)
