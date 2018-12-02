from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from maff.models import maff

@login_required()
def funkcje(request, funk, int1, int2):
    try:
        int1 = float(int1)
        int2 = float(int2)
        funk not in ('dod', 'ode', 'pom', 'pod')
    except:
        return HttpResponse(content="Podałeś zrąbane liczby lub fukcję, ziom")
    if funk == 'dod':
        wynik = float(int1) + float(int2)
        return HttpResponse(content=f"{int1} + {int2} to: {wynik} ")
    elif funk == 'ode':
        wynik = float(int1) - float(int2)
        return HttpResponse(content=f"{int1} - {int2} to: {wynik} ")
    elif funk == 'pom':
        wynik = float(int1) * float(int2)
        return HttpResponse(content=f"{int1} * {int2} to: {wynik} ")
    elif funk == 'pod':
        wynik = float(int1) / float(int2)
        return HttpResponse(content=f"{int1} / {int2} to: {wynik} ")


def calculate(funk, int1, int2):
    try:
        int1 = float(int1)
        int2 = float(int2)
        funk not in ('dod', 'ode', 'pom', 'pod')
    except:
        return HttpResponse(content="Podałeś zrąbane liczby lub fukcję, ziom")
    result = None
    if funk == "dod":
        result = int1 + int2
    elif funk == "odj":
        result = int1 - int2
    return result


def maff_list(request):
    objects = maff.objects.all()
    out = ""
    # for o in objects:
    #     out += f"{o.funk}: {o.int1}: {o.int2}<br>"
    return render(
        request=request,
        template_name="maff_list.html",
        context={"maffs": objects}
    )

def maff_details(request, id):
    objects = maff.objects.get(pk=id)
#    out = f"""
# Operacja: {m.funk}<br>
# Argument1: {m.int1}<br>
# Argument2: {m.int2}<br>
# ===============<br>
# Wynik: {calculate(m.funk,m.int1,m.int2)}<br>
# """
#     return HttpResponse(out)
    return render(
        request=request,
        template_name="maff_det.html",
        context={f"maffs": objects}
    )

