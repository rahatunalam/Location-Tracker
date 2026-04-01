import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

key = "6d6f969fd9024ac8afde957f0c86a5ba"

def start_tracing(target):
    check_number = phonenumbers.parse(target,None)
    num_location = geocoder.description_for_number(check_number,"en")
    print(f"[+] Location: {num_location}")

    print(f"Service Provider: {carrier.name_for_number(check_number,"en")}")
    geocode = OpenCageGeocode(key)

    query = str(num_location)
    results = geocode.geocode(query)

    lat = results[0]["geometry"]["lat"]
    lon = results[0]["geometry"]["lng"]
    print(f"Latitude: {lat}")
    print(f"Longitude: {lon}")

    map_loc = folium.Map(location=[lat, lon], zoom_start=9)
    folium.Marker(location=[lat, lon], popup=query).add_to(map_loc)
    map_loc.save("location.html")

phn_num = input("Enter phone number: ")
start_tracing(phn_num)
#start_tracing("+1 744-208-1965")