from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Eudora Vanya Lindsay',
        'class' : 'PBP-D',
        'application_name': 'BOOK CATALOG',
        'book_name': 'Hujan',
        'bbok_amount': '7',
        'book_description': 'Novel Hujan merupakan novel yang mengisahkan kisah cinta serta perjuangan hidup Lail.'
    }

    return render(request, "main.html", context)