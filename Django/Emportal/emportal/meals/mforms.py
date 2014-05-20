from django import forms

TOPIC_CHOICES = (
	('general', 'General enquiry'),
	('bug', 'Bug report'),
	('suggestion', 'Suggestion'),
	)

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	email = forms.EmailField(required=False, label='Your E-mail')
	message = forms.CharField(widget=forms.Textarea)

	def clean_message(self):
		message = self.cleaned_data['message']
		num_words = len(message.split())
		if num_words < 4:
			raise forms.ValidationError('Not enough words!')
		return message
