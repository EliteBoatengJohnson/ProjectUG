from django import forms
from .models import Claim, Report

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe why you are claiming this item...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].label = "Claim Description"

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['additional_info']
        widgets = {
            'additional_info': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Provide any additional information about the item...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['additional_info'].label = "Additional Information"