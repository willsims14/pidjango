from django.http import HttpResponse

from .models import Plant


def index(request):
    latest_plant_list = Plant.objects.order_by('-meta_created')[:5]
    output = ', '.join([p.common_name for p in latest_plant_list])
    return HttpResponse(output)


def detail(request, plant_id):
    return HttpResponse("You're looking at plant %s." % plant_id)


def propogations(request, plant_id):
    response = "You're looking at the propogations of plant %s."
    return HttpResponse(response % plant_id)


def propogate(request, plant_id):
    return HttpResponse("You're propogating %s." % plant_id)
