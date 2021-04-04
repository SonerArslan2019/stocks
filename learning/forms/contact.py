from django import forms
from learning.models import Product


class Contact(forms.Form):
    name = forms.CharField(
        label='isim',
        max_length=50,
        min_length=5,
        required=True,
        initial='isminizi giriniz.....',
        help_text='burasi isim yardim metnidir',
        error_messages={
            'required': 'lutfen isim giriniz',
            'max_length': 'En fazla 50 karekter girebilirsiniz',
            'min_length': 'En az 5 karekter girmelisiniz'
        },
        disabled=False,
        widget=forms.TextInput(
            attrs={
                'class': 'special',
                'size': '40',
                'title': 'isminiz',
                'required': True
            }
        )

    )

    email = forms.EmailField(label='Email Adresi')
    content = forms.CharField(widget=forms.Textarea)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'




