from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'project_type', 'subject', 'message']
        widgets = {
            'project_type': forms.Select(attrs={
                'class': 'form-control', 
                'required': True,
                'style': 'background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); color: #f8fafc; padding: 12px 15px; border-radius: 10px;'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Your Name',
                'style': 'background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); color: #f8fafc; padding: 12px 15px; border-radius: 10px;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Your Email',
                'style': 'background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); color: #f8fafc; padding: 12px 15px; border-radius: 10px;'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Subject',
                'style': 'background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); color: #f8fafc; padding: 12px 15px; border-radius: 10px;'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Your Message', 
                'rows': 6,
                'style': 'background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); color: #f8fafc; padding: 12px 15px; border-radius: 10px; min-height: 150px;'
            }),
        }