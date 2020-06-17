from django.shortcuts import render

def mdb_home_page_view(request):
    return render(request,'home-page.html')
