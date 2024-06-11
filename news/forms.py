from django import forms

from .models import News
from products.widgets import CustomClearableFileInput


class NewsForm(forms.ModelForm):
    """
    A class for the news form
    """
    class Meta:
        model = News
        fields = ('title', 'news_item_text', 'image', 'status')

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput)
