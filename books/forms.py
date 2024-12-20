from django import forms
from .models import Book, Review

class BookForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=Book._meta.get_field('category').related_model.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Categories"
    )
    
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['author', 'borrowed_by']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 2,})
        }
        labels = { 'body': ''}