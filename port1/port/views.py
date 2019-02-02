from django.shortcuts import render,redirect
from .models import Port
from .forms import PortForm
# Create your views here.
def makeport(request):
    form = PortForm(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = PortForm()


            return redirect('showport' )

    else:
        form = PortForm()

    return render(request,'port/makeport.html',{'b':form})

def showport(request):
    port = Port.objects.all()
    context = {
    'bb':port,
    }
    return render(request,'port/showport.html',context)

def showfullport(request,pk):
    port = Port.objects.get(id = pk)
    context = {
    'bbb' : port
    }
    return render(request,'port/showfullport.html',context)
