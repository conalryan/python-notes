from django import forms
'''

@author: Conal
'''
class StockQuoteForm(forms.Form):
    stock_name = forms.CharField(label='Stock Symbol', max_length=50)
