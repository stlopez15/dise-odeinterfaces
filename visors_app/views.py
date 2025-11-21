from django.shortcuts import render, redirect, get_object_or_404
from .models import InterfaceAR
from .forms import InterfaceForm


def subir_interface(request):
    if request.method == "POST":
        form = InterfaceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_interfaces')
    else:
        form = InterfaceForm()

    return render(request, 'visor/subir_interface.html', {'form': form})


def lista_interfaces(request):
    interfaces = InterfaceAR.objects.all()
    return render(request, 'visor/lista_interfaces.html', {'interfaces': interfaces})

def demo_ra(request):
    return render(request, "demo_ra.html")

def ver_ra(request, id):
    interfaz = get_object_or_404(InterfaceAR, id=id)
    interfaces = InterfaceAR.objects.all()
    return render(request, 'visor/ver_ra.html', {
        'interfaz': interfaz,
        'interfaces': interfaces
    })

from django.shortcuts import redirect

def subir(request):
    return render(request,'subir_interface.html')


