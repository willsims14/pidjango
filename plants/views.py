from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    latest_question_list = Question.objects.order_by('-meta_created')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, plant_id):
    return HttpResponse("You're looking at plant %s." % plant_id)

def propogations(request, plant_id):
    response = "You're looking at the propogations of plant %s."
    return HttpResponse(response % plant_id)

def propogate(request, plant_id):
    return HttpResponse("You're propogating %s." % plant_id)