from django.views import generic

from .models import Plant


class IndexView(generic.ListView):
    template_name = 'plants/index.html'
    context_object_name = 'latest_plant_list'

    def get_queryset(self):
        """Return the last five published plants."""
        return Plant.objects.order_by('-meta_created')[:5]


class DetailView(generic.DetailView):
    model = Plant
    template_name = 'plants/detail.html'

# def propogations(request, plant_id):
#     response = "You're looking at the propogations of plant %s."
#     return HttpResponse(response % plant_id)

# class PropogationsView(generic.DetailView):

# def propogate(request, plant_id):
#     return HttpResponse("You're propogating %s." % plant_id)
