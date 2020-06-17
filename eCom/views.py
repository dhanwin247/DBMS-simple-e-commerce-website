from django.shortcuts import render

def mdb_home_page_view(request):
    return render(request,'product-page.html')
