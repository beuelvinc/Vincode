from django import forms 
class SearchForm(forms.Form):
	search=forms.TextInput(attrs={'size': 20,'required': True,'name':'search-btn','class':'form-control form-control-block search-input'})
