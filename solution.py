import geocoder

locations = [
    "Space Needle",
    "Crater Lake",
    "Golden Gate Bridge",
    "Yosemite National Park",
    "Las Vegas, Nevada",
    "Grand Canyon National Park",
    "Aspen, Colorado",
    "Mount Rushmore",
    "Yellowstone National Park",
    "Sandpoint, Idaho",
    "Banff National Park",
    "Capilano Suspension Bridge"
]

for point in locations:
    g = geocoder.arcgis(point)
    print("{place} is located at ({lat:.4f}, {long:.4f})".format(place=point, lat=g.latlng[0], long=g.latlng[1]))
