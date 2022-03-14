from django import forms

from .models import StockMarket, StockQuery


class StockMarketForm(forms.ModelForm):
    class Meta:
        model = StockMarket
        fields = ['id', 'name', 'email', 'title', 'current_price', 'about']


class StockQueryForm(forms.ModelForm):
    class Meta:
        model = StockQuery
        fields = ['query','username','stock_id']
