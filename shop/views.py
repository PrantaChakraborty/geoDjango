from django.views import generic
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance


from .models import Shop

latitude = 23.7931353
longitude = 90.4056248

user_location = Point(longitude, latitude, srid=4326)


class NearestShopView(generic.ListView):
    """
    return nearest 10 shops based on user
    """
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.annotate(distance=Distance('location', user_location)).order_by('distance')[0:10]
    template_name = 'index.html'

