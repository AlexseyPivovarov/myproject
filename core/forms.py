from django.contrib.auth.models import User
from django.forms import ModelForm, Form
from .models import Product


class Profile(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ('product_name', 'product_category', 'product_info',
                  'product_image', 'product_price', 'product_vip_moderation')
