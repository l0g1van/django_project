import math

from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from django.shortcuts import redirect

from catalog.forms import TriangleForm


# class TriangleView(generic.View):
#     template_name = 'catalog/triangle.html'

    # def

def triangle(request):
    if request.method == "POST":

        form = TriangleForm(request.POST)

        if request.POST.get('leg_1') and request.POST.get('leg_2') and form.is_valid():

            form.clean()

            leg_1 = form.cleaned_data.get('leg_1')
            leg_2 = form.cleaned_data.get('leg_2')
            gip = round(math.sqrt(leg_1**2 + leg_2**2), 2)

            return render(request, 'hypotenuse.html', {'gip': gip})

    else:
        form = TriangleForm()

    return render(request, 'triangle.html', {'form': form})
