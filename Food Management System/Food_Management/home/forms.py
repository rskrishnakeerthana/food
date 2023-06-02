from django import forms
from .models import OrderForm
 
class detailsform(forms.ModelForm):
    class Meta:
        model=OrderForm
        fields = "__all__"