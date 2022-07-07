# geoDjango A practice project with geo location.
* Followed by Official documentation(https://docs.djangoproject.com/en/4.0/ref/contrib/gis/tutorial/#:~:text=GeoDjango%20is%20an%20included%20contrib,OGC%20geometries%20and%20raster%20data.)
* All dependencies installation process are given on the officiatial documentation.

## Project Description
* It contains two apps. One is `world` and the other is `shop`.
* `world` app contains all codes from the official documentation.
* `shop` app shows the nearest shops of your location. For now location is hardcoded. Will get it from IP in the future.
* In `shop` app there is a directory called `data`. The `data` directory stores all the shops' data that are downloaded from here(https://overpass-turbo.eu/).
* To insert the data from the data file first need to create an empty migration by using this command ` python manage.py makemigrations shops --empty`
  * Then in the empty migration file write the following code
  ```python
  from django.db import migrations
  from ..load import load_data
  
  
  class Migration(migrations.Migration):
      dependencies = [
          ('shop', '0003_auto_20220705_1543'),
      ]
  
      operations = [
          migrations.RunPython(load_data)
      ]
  
  ```
  * Then run the following command to migrate `python manage.py migrate`. It will create Shop objects based on the data files named `shop/data/gulshan_shops.json`

* Then run the command `python manage.py runserver`

## Input and Output
* User need to input his/her address. If nearest location found then a table contain list will be shows will be shown with a map also.

![image](/media/pranta/D/geoDjango/geoDjango/input&table.png)


![image](/media/pranta/D/geoDjango/geoDjango/map.png)

* If not found then an error page will be shown.

![image](/media/pranta/D/geoDjango/geoDjango/Screenshot from 2022-07-07 17-56-02.png)
