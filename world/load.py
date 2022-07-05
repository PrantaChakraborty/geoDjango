from pathlib import Path
from django.contrib.gis.utils import LayerMapping

from .models import WorldBorder

world_mapping = {
    # key contains the model fields and value contains the .shp fields name
    'fips': 'FIPS',
    'iso2': 'ISO2',
    'iso3': 'ISO3',
    'un': 'UN',
    'name': 'NAME',
    'area': 'AREA',
    'pop2005': 'POP2005',
    'region': 'REGION',
    'subregion': 'SUBREGION',
    'lon': 'LON',
    'lat': 'LAT',
    'mpoly': 'MULTIPOLYGON',
}

# need to extract the zip file inside world/data directory

world_shp = Path(__file__).resolve().parent / 'data' / 'TM_WORLD_BORDERS-0.3.shp'


def run(verbose=True):
    lm = LayerMapping(WorldBorder, world_shp, world_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
