from django import forms
from .models import PG, Review

class PGForm(forms.ModelForm):

    class Meta:
        model = PG

        fields = ['name', 'city', 'rent', 'description', 'image']


class ReviewForm(forms.ModelForm):

    class Meta:

        model=Review
        fields=['rating', 'comment']