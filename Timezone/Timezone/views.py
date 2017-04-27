from django.http import HttpResponse

import arrow
from arrow.parser import ParserError

from . import time_zone_logic


def _parse_lng_lat(lng_lat_str):
    """Parses a 'lat,lng' location string to a lat, lng float pair.
    >>> _parse_lng_lat('12.34,56.78')
    (12.34, 56.78)
    >>> _parse_lng_lat('12.34')
    Traceback (most recent call last):
        ...
    ValueError: not 'lng,lat' str: '12.34'
    """
    lng_lat = tuple(float(coord_str) for coord_str in lng_lat_str.split(','))
    if len(lng_lat) != 2:
        raise ValueError("not 'lng,lat' str: {!r}".format(lng_lat_str))
    return lng_lat

def get_time_at_server(_):
    tzf = time_zone_logic.TimezoneFuncs();
    try:
        myservertime = tzf.get_time_at_server();
    except ValueError:
        return HttpResponse('no timezone', status=400)
    return HttpResponse(myservertime)

def get_time_at_lat_lng(_, lat_lng_str):
    try:
        lat_lng = _parse_lng_lat(lat_lng_str)
    except ValueError:
        return HttpResponse('bad location', status=400)
    tzf = time_zone_logic.TimezoneFuncs();
    myservertime = tzf.get_time_at_lat_lng(lat_lng[0], lat_lng[1]);
    return HttpResponse(myservertime.isoformat())

def get_tz_lat_lng(_, lat_lng_str):
    try:
        lat_lng = _parse_lng_lat(lat_lng_str)
    except ValueError:
        return HttpResponse('bad location', status=400)
    tzf = time_zone_logic.TimezoneFuncs();
    myservertz = tzf.get_tz_lat_lng(lat_lng[0], lat_lng[1]);
    return HttpResponse(myservertz)

def get_time_at_time_lat_lng(_, time_str, lat_lng_str):
    """View that renders a given time in the local timezone at a location in ISO format."""
    try:
        time = arrow.get(time_str)
    except ParserError:
        return HttpResponse('bad timestamp', status='400')
    try:
        lat_lng = _parse_lng_lat(lat_lng_str)
    except ValueError:
        return HttpResponse('bad location', status=400)
    tzf = time_zone_logic.TimezoneFuncs();
    lat_lng_time = tzf.get_time_at_time_lat_lng(time, lat_lng[0], lat_lng[1])
    return HttpResponse(lat_lng_time)

def helloworld(_):
    return HttpResponse("helloworld")
