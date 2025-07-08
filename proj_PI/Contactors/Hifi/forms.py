from django import forms

class ContactorForm(forms.Form):
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    emailid = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    mobileNumber = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    DOB = forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    CC = [
        ('IND', 'INDIA'),
        ('US', 'UNITED STATES'),
        ('UK', 'UNITED KINGDOM'),
        ('MEX', 'MEXICO'),
        ('CHN', 'CHINA'),
        ('PAK', 'PAKISTAN'),
        ('AFG', 'AFGANISTAN'),
        ('ALG', 'ALGERIA'),
        ('INA', 'INDONESIA'),
        ('IRN', 'IRAN'),
        ('QTR', 'QATAR'),
        ('RUS', 'RUSSIA'),
        ('SPN', 'SPAIN'),
        ('TURK', 'TURKEY'),
        ('AUS', 'AUSTRALIA'),
        ('BRZ', 'BRAZIL'),
        ('FRANCE', 'FRANCE'),
        ('GER', 'GERMANY'),
        ('JPN', 'JAPAN'),
        ('PL', 'PALESTINE'),
        ('YEMEN', 'YEMEN')
    ]
    country = forms.ChoiceField(choices=(CC), widget=forms.Select(attrs={'class':'form-control'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)