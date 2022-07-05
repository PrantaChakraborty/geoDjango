from django.db import migrations
import json
from django.contrib.gis.geos import fromstr
from pathlib import Path


DATA_FILENAME = 'data/gulshan_shops.json'


def load_data(apps, schema_editor):
    Shop = apps.get_model('shop', 'Shop')
    jsonfile = Path(__file__).resolve().parent / DATA_FILENAME

    with open(str(jsonfile)) as datafile:
        objects = json.load(datafile)
        for obj in objects['elements']:
            try:
                objType = obj['type']
                if objType == 'node':
                    tags = obj['tags']
                    name = tags.get('name', 'no-name')
                    longitude = obj.get('lon', 0)
                    latitude = obj.get('lat', 0)
                    address = obj.get('addr', '')
                    location = fromstr(f'POINT({longitude} {latitude})', srid=4326)
                    Shop(name=name, location=location, address=address).save()
            except KeyError:
                pass
