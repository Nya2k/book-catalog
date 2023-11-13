import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='login/')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    context = {
        'name' : request.user.username,
        'class' : 'PBP-D',
        'application_name': 'BOOK CATALOG',
        'items' : items,
        'last_login': request.COOKIES['last_login']
    }

    return render(request, "main.html", context)

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_product = Item(name=name, amount=amount, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def add_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "add_item.html", context)

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_product = Item(name=name, amount=amount, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def add_amount(request, id, amount):
    item = Item.objects.get(pk=id)
    item.amount = amount + 1
    item.save()
    return HttpResponseRedirect(reverse('main:show_html'))

@csrf_exempt
def add_amount_ajax(request):
  if request.method == 'POST':
    id = request.POST.get("id")
    updated = Item.objects.get(pk=id)
    updated.amount += 1
    updated.save()
    return HttpResponse(b"UPDATED", status=201)
  return HttpResponseNotFound()


def subtract_amount(request, id, amount):
    if (amount != 0):
        item = Item.objects.get(pk=id)
        item.amount = amount - 1
        item.save()
    return HttpResponseRedirect(reverse('main:show_html'))

@csrf_exempt
def subtract_amount_ajax(request):
  if request.method == 'POST':
    id = request.POST.get("id")
    updated = Item.objects.get(pk=id)
    if (updated.amount > 0):
        updated.amount -= 1
    updated.save()
    return HttpResponse(b"UPDATED", status=201)
  return HttpResponseNotFound()

def delete_item(request, id):
    item = Item.objects.get(pk=id)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_html'))

@csrf_exempt
def delete_item_ajax(request):
  if request.method == 'POST':
    id = request.POST.get("id")
    item = (Item.objects.get(pk=id))
    item.delete()
    return HttpResponse(b"DELETED", STATUS=201)
  return HttpResponseNotFound()

def show_html(request):
    items = Item.objects.filter(user=request.user)
    return render(request, 'show_html.html', {"items": items})

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_product_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_user(request):
    items = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', items), content_type="application/json")