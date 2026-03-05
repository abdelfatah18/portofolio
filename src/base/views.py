from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import MessageForm
# Create your views here.
def index(request):
    return render(request, "base/index.html")



def portfolio(request):
    return render(request, "base/portfolio.html")

def about(request):
    return render(request, "base/about.html")

def services(request):
    return render(request, "base/services.html")            


from django.shortcuts import render, redirect


from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import MessageForm

def contact(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            # إضافة رسالة نجاح
            messages.success(request, "تم حفظ البيانات بنجاح!")
            return redirect('contact')  # بعد الريفرش، تظهر الرسالة
    else:
        form = MessageForm()

    return render(request, "base/contact.html", {'form': form})





def portfolio_details(request):
    return render(request, "base/portfolio-details.html")

def services_details(request):
    return render(request, "base/services-details.html")

def resume(request):
    return render(request, "base/resume.html")  

def starter(request):
    return render(request, "base/starter.html")
