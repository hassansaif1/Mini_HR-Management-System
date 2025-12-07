from django import forms    
from .models import LeaveRequest


class ApplyLeaveForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = [ 'start_date', 'end_date', 'reason', ] 
        widgets ={
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Reason', 'rows':3}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            
            }
