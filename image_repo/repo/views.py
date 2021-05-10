from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from .models import Item

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
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    if request.method == 'POST':
        search = request.POST['item_search']
        results = Item.objects.filter(name__contains=search)[:15]
        print(results)
        context = {'results': results}
        return render(request, 'repo/index.html', context)
    return render(request, 'repo/index.html')

def main(request, name):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    context = {
        'name': name.capitalize()
    }
    return render(request, 'repo/index.html', context)

def add(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    if request.method == 'POST':
        # populate new form with user sumbmission
        form = AddItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            image_url = form.cleaned_data['image_url']
            num_reviews = form.cleaned_data['num_reviews']
            price = form.cleaned_data['price']
            tags = form.cleaned_data['tags']
            new_item = Item.objects.create(name=name, image_url=image_url, num_reviews=num_reviews, price=price, user=request.user)
            new_item.save()
            return HttpResponseRedirect(reverse('repo:add'))
        else:
            # if form is invalid from server-side return form back to user for them to edit
            context = {'form': form}
            return render(request, 'repo/add.html', context)
    context = {
        'form': AddItemForm()
    }
    return render(request, 'repo/add.html', context)