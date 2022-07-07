from django.views import generic
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance

from geopy.geocoders import Nominatim
import folium

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
        address = request.POST['address']
        geo_locator = Nominatim(user_agent='shop')
        location = geo_locator.geocode(address)
        if location is not None:
            latitude = location.latitude
            longitude = location.longitude
            user_location = Point(longitude, latitude, srid=4326)
            queryset = Shop.objects.annotate(distance=Distance('location', user_location)).order_by('distance')[
                       0:10]

            # folium map
            m = folium.Map(width=800, height=500, location=[latitude, longitude], zoom_start=12)
            # location marker
            folium.Marker([latitude, longitude], tooltip='Click here for more', popup=address,
                          icon=folium.Icon(color='blue')).add_to(m)

            # mapping the queryset
            for i in queryset:
                lat = i.location.coords[1]
                lon = i.location.coords[0]
                folium.Marker(location=[lat, lon], tooltip='Click here for more',
                              popup=i.name, icon=folium.Icon(color='red')).add_to(m)

            return render(request, self.template_name, context={"shops": queryset, "map": m._repr_html_(), "address": address})
        else:
            return render(request, 'not_found.html', context={})


