import phonenumbers
from phonenumbers import geocoder
countryName=phonenumbers.parse("+918160582215","CH")
print(geocoder.description_for_number(countryName,"en"))

from phonenumbers import carrier
servcieProvider=phonenumbers.parse("+918160582215","RO")
print(carrier.name_for_number(servcieProvider,"en"))