

import requests
from io import BytesIO

def map_at(lat, long, satellite = False, zoom = 12,
            size = (400,400), sensor = False):

    base = "http://maps.googleapis.com/maps/api/staticmap?"

    params = dict(
        sensor = str(sensor).lower,
        zoom = zoom,
        size = "x".join(map(str, size)),
        center = ",".join(map(str,(lat,long))),
        style = "feature:all|element:labels|visibility:off"
    )

    if satellite:
        params["maptype"] = "satellite"

    return BytesIO(requests.get(base, params = params))


type BytesIO

bytes(1)
