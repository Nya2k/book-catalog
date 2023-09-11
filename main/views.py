from django.shortcuts import render

def show_main(request):
    context = {
        'application': 'BOOK CATALOG',
        'name': 'Hujan',
        'amount': '7',
        'description': 'Novel Hujan merupakan novel yang mengisahkan kisah cinta serta perjuangan hidup Lail.'
    }

    return render(request, "main.html", context)