from django import forms

class serverForm(forms.Form):
	name = forms.CharField(required=True, max_length=50)
	cpu = forms.CharField(max_length=10)
	memory = forms.CharField(max_length=10)
	model = forms.CharField(max_length=50)
	ip = forms.CharField(max_length=50)
	status = forms.CharField(max_length=20)
	user = forms.CharField(max_length=50)
	location = forms.CharField(max_length=50)
	comment = forms.CharField(max_length=100)

class searchServerForm(forms.Form):

	USER_CHOICES = (
	('', ''),
	('Kevin', 'Kevin'),
	('Zoe', 'Zoe'),
	('Guoying', 'Guoying'),
	)

	USED_CHOICES = (
	('', ''),
	('Y', 'Y'),
	('N', 'N'),
	)

	name = forms.CharField(max_length=50)
	status = forms.CharField(max_length=20)
	user = forms.ChoiceField(widget=forms.Select(), choices=USER_CHOICES)
	used = forms.ChoiceField(widget=forms.Select(), choices=USED_CHOICES)