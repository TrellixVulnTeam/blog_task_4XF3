from django import forms
from django.forms import ModelForm
from .models import *

Grade_Choices = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
)
GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others')
]

Subject_Choice = [
    ('Physics', 'Physics'),
    ('Bilogy', 'Biology'),
    ('Chemistry', 'Chemistry'),
    ('Maths', 'Maths'),
    ('Nepali', 'Nepali'),
    ('Social', 'Social'),
]


class StudentForm(forms.ModelForm):
    name=forms.CharField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    subjects = forms.MultipleChoiceField(choices=Subject_Choice,
                                         widget=forms.CheckboxSelectMultiple)
    grade = forms.CharField(label='Class', widget=forms.RadioSelect(choices=Grade_Choices))

    class Meta:
        model = Student
        fields = '__all__'
        # labels = {'name': 'Full Name', 'grade': 'Class'}
        labels = {'name': 'Full Name', 'roll': 'Roll Number',
                  'email': 'Email ID'}
        help_texts = {'roll': 'Enter your class roll no'}
        error_messages = {'name': {'required': 'Name is required'}}
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Nirajan Lamichhane'})}
