from django import forms
from .models import Products

class ProductData(forms.Form):
	class meta:
		model = Products
		fields = '__all__'