from django import forms
from django.forms import ModelForm, modelformset_factory
from .models import User, Candidate, Recruiter

#SignIn, general, should we have a register form?
class SignInForm(forms.Form):
	username = forms.CharField(label = 'Username', min_length = 8, max_length = 50, required = True)
	password = forms.CharField(label = 'Password', min_length = 8, widget = forms.PasswordInput(), required = True)

#Candidate information, specific
class CandidateForm(forms.Form):
	firstName = forms.CharField(label = 'First Name', min_length = 1, max_length = 100, required = True)
	lastName = forms.CharField(label = 'Last Name', min_length = 1, max_length = 100, required = True)
	
	# Education levels
	EDU_LEVELS = (
		('N', 'None'),
		('H', 'High School Diploma'),
		('T', 'Technical Diploma'),
		('A', 'Associate\'s Degree'),
		('B', 'Bachelor\'s Degree'),
		('M', 'Master\'s Degree'),
		('D', 'Doctorate Degree')
	)

	highestEducation = forms.ChoiceField(choices = EDU_LEVELS, label = 'Highest Education Level', required = True)
	
	# Education status levels
	EDU_STATUS = (
		('G', 'Graduated'),
		('I', 'In Progress'),
		('N', 'Not Complete')
	)

	educationStatus = forms.ChoiceField(choics = EDU_STATUS, label = 'Education Status', required = True)
	programField = forms.CharField(label = 'Major/Field', min_length = 1, max_length = 50, required = True)
	yearsExperience = forms.IntegerField(label = 'Years Experience', min_value = 1, max_value = 20, required = True)
	relevantEmployer = forms.CharField(label = 'Relevant Employer', min_length = 1, max_length = 50, required = True)

#Recruiter information
class RecruiterForm(forms.Form):
	firstName = forms.CharField(label = 'First Name', min_length = 1, max_length = 100, required = True)
	lastName = forms.CharField(label = 'Last Name', min_length = 1, max_length = 100, required = True)
	employer = forms.CharField(label = 'Employer', min_length = 1, max_length = 50, required = True)
	title = forms.CharField(label = 'Title', min_length = 1, max_length = 50, required = True)

#PreSurvey
class PreSurveyForm(forms.Form):

	# Predefine possible response in pre-survey
	RESPONSES = (
		(1, 'Strongly disagree'),
		(2, 'Disagree'),
		(3, 'Neutral'),
		(4, 'Agree'),
		(5, 'Strongly Agree')
	)

	questionOneResponse = forms.ChoiceField(choices = RESPONSES, label = 'Question One Response', required = True)
	questionTwoResponse = forms.ChoiceField(choices = RESPONSES, label = 'Question Two Response', required = True)
	questionThreeResponse = forms.ChoiceField(choices = RESPONSES, label = 'Question Three Response', required = True)
	questionFourResponse = forms.ChoiceField(choices = RESPONSES, label = 'Question Four Response', required = True)
	questionFiveResponse = forms.ChoiceField(choices = RESPONSES, label = 'Question Five Response', required = True)

#PostSurvey
class PostSurveyForm(forms.Form):

	# Predefine possible response in pre-survey
	RESPONSES = (
		(1, 'Strongly disagree'),
		(2, 'Disagree'),
		(3, 'Neutral'),
		(4, 'Agree'),
		(5, 'Strongly Agree')
	)

	questionOneResponse = forms.ChoiceField(choices = RESPONSES, label = 'Question One Response', required = True)
	questionTwoResponse = forms.ChoiceField(choices = RESPONSES, label = 'Question Two Response', required = True)
	questionThreeResponse = forms.ChoiceField(choices = RESPONSES, label = 'Question Three Response',required = True)
	questionFourResponse = forms.ChoiceField(choices = RESPONSES, label = 'Question Four Response', required = True)
	questionFiveResponse = forms.ChoiceField(choices = RESPONSES, label = 'Question Five Response', required = True)

#Transcript
class TranscriptForm(forms.Form):
	speakerChoice = forms.CharField(label = 'Speaker', max_length = 1, required = True)
	lineNumber = forms.IntegerField(label = 'Line Number', min_value = 1, max_value = 2000)
	lineContents = forms.CharField(label = 'Line Content', min_length = 1, max_length = 2000)