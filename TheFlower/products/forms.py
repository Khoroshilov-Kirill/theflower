from django import forms

from .models import Review


class SendReview(forms.ModelForm):
    review = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'placeholder':'Оставьте свой отзыв здесь ... '}),
        label='',
    )

    class Meta:
        model = Review
        fields = ['review']


