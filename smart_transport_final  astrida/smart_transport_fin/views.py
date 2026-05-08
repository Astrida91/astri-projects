from django.shortcuts import render

def landing_page_view(request):
    return render(request, 'landing_page.html')
def about(request):
    return render(request, 'about_us.html')
def contact(request):
    return render(request, 'contact.html')
