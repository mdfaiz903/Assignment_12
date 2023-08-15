from django import forms
from django.core.validators import RegexValidator

class UserInformationForm(forms.Form):
    first_name = forms.CharField(max_length=255, required=True, label="First Name")
    last_name = forms.CharField(max_length=255, required=True, label="Last Name")
    email = forms.EmailField(required=True, label="Email")
    birth_date = forms.DateField(
        label = "Birth Date",
        widget=forms.DateInput(attrs={'type':'date'}),
        
    )
    # age = forms.IntegerField(required=True, label="Age", min_value=5,max_value=25)
    roll_no = forms.IntegerField(required=True, label="Roll No", min_value=1, help_text="Enter 4 digit roll number")
    phone_regex = RegexValidator(
        regex=r'^\+?88?\d{9,11}$',
        message="Phone number must be entered in the format: '+88'. Up to 11 digits allowed."
    )

    phone = forms.CharField(
        validators=[phone_regex],
        required=True,
        label="Phone"
    )    
    is_current_student = forms.BooleanField(required=False, label="Current Student", widget=forms.CheckboxInput())
    # created_date = forms.DateTimeField(required=False, label="Created Date", widget=forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM:SS'}))
    
    created_date = forms.DateField(
        required=False,
        label="Created Date",
        widget=forms.DateInput(attrs={'type': 'date'}),
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows':5,'cols':30}),
        label='Comment'
    )
    file = forms.FileField(required=False, label="File")
