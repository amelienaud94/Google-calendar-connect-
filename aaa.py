import requests
import urllib
adresseDepart="48 Boulevard des Batignolles, 75017 Paris "
print(urllib.quote(adresseDepart))
rcoordDepart=requests.get("http://maps.googleapis.com/maps/api/geocode/json?address="+urllib.quote(adresseDepart)+"&sensor=false")
print(rcoordDepart.json()['results'][0]['geometry']['location']);

r=requests.get("https://developer.citymapper.com/api/1/traveltime/?startcoord=51.525246%2C0.084672&endcoord=51.559098%2C0.074503&time=2014-11-06T19%3A00%3A02-0500&time_type=arrival&key=a5e47d7d91fa9dc49610d5ffca14fdea")
print(r.text);

coord=requests.get("http://maps.googleapis.com/maps/api/geocode/json?address=546%20rue%20Baruch%20de%20Spinoza,%20Avignon&sensor=false")
print(coord.json()['results'][0]['geometry']['location']);
