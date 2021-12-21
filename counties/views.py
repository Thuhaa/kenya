from django.shortcuts import render
from django.http import HttpResponse
from .models import  Stations
from djngo.core.serializers import serialize

def map_view(request):
	data = serialize('geojson',Stations.objects.all(), geometry_field='geom',
          fields=('name','station'))
	data_json = json.dumps(data)
	return render(request, "counties/index.html", {"data_json":data_json})

def request_coords(request, coodinates):
	return HttpResponse("Return Coords")
