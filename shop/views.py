from django.views import generic
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance

from geopy.geocoders import Nominatim

from django.shortcuts import render, HttpResponse


from .models import Shop


class NearestShopView(generic.View):
    """
    return nearest 10 shops based on user
    """
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name, context={})

    def post(self, request):
        # try:
        address = request.POST['address']
        geo_locator = Nominatim(user_agent='shop')
        location = geo_locator.geocode(address)
        if location is not None:
            latitude = location.latitude
            longitude = location.longitude
            user_location = Point(longitude, latitude, srid=4326)
            queryset = Shop.objects.annotate(distance=Distance('location', user_location)).order_by('distance')[
                       0:10]
            return render(request, self.template_name, context={"shops": queryset})
        else:
            return render(request, 'not_found.html', context={})



