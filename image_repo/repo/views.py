from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse

class AddItemForm(forms.Form):
    name = forms.CharField(max_length=50, label='')
    image_url = forms.URLField(max_length=400, label='')
    num_reviews = forms.IntegerField(min_value=0, label='')
    price = forms.FloatField(min_value=0, label='')
    tags = forms.CharField(max_length=50, required=False, label='')

    def __init__(self, *args, **kwargs):
        super(AddItemForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Item Name'
        self.fields['image_url'].widget.attrs['placeholder'] = 'Item Image Url'
        self.fields['num_reviews'].widget.attrs['placeholder'] = 'Number of Reviews'
        self.fields['price'].widget.attrs['placeholder'] = 'Price'
        self.fields['tags'].widget.attrs['placeholder'] = 'Tags'

# Create your views here.
def index(request):
    return render(request, 'repo/layout.html')

def main(request, name):
    context = {
        'name': name.capitalize()
    }
    return render(request, 'repo/index.html', context)

def add(request):
    if request.method == 'POST':
        # populate new form with user sumbmission
        form = AddItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            image_url = form.cleaned_data['image_url']
            num_reviews = form.cleaned_data['num_reviews']
            price = form.cleaned_data['price']
            tags = form.cleaned_data['tags']
            # add data to database here
        else:
            # if form is invalid from server-side return form back to user for them to edit
            context = {'form': form}
            return render(request, 'repo/add.html', context)
    context = {
        'form': AddItemForm()
    }
    return render(request, 'repo/add.html', context)