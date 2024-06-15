import phonenumbers
from phonenumbers import geocoder
import folium

number=" +977 9811081479 "
key="6d6f969fd9024ac8afde957f0c86a5ba"

checkNumber=phonenumbers.parse(number)
numberLocation=geocoder.description_for_number(checkNumber,'en')
print(numberLocation)

from phonenumbers import carrier
serviceProvider=phonenumbers.parse(number)
print(carrier.name_for_number(serviceProvider,'en'))

from opencage.geocoder import OpenCageGeocode
geocoder=OpenCageGeocode(key)
query=str(numberLocation)
result=geocoder.geocode(query)

lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']
print(lat,lng)

# mapLocation=folium.Map(location=[lat,lng],zoomStart=9)
# folium.Marker([lat,lng],popup=numberLocation.add_to(mapLocation))
# mapLocation.save("mylocation.html")