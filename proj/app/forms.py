from django import forms


class AddProduct(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "title"}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': "title"}), )
    url = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': "title"}))

    price = forms.IntegerField(widget=forms.TextInput(attrs={'class': "title"}))