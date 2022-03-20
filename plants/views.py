from dajngo.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Plant


def index(request):
    latest_plant_list = Plant.objects.order_by('-meta_created')[:5]
    # output = ', '.join([p.common_name for p in latest_plant_list])
    # template = loader.get_template('plants/index.html')
    context = {
        'latest_plant_list': latest_plant_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'plants/index.html', context)


def detail(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    return render(request, 'plants/detail.html', {'plant': plant})


def propogations(request, plant_id):
    response = "You're looking at the propogations of plant %s."
    return HttpResponse(response % plant_id)


def propogate(request, plant_id):
    return HttpResponse("You're propogating %s." % plant_id)
