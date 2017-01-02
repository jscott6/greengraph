

import requests
from mock import patch
from greengraph.map import map

def test_Map_init():

    base = "http://maps.googleapis.com/maps/api/staticmap?"
    params = params = dict(
                sensor = 'false',
                zoom = 10,
                size = '400x400',
                center = '51.5074,-0.1278',
                style = 'feature:all|element:labels|visibility:off',
                maptype = 'satellite'
                 )

    with patch.object(requests, 'get') as mock_get:
        try:
            london_map = Map(51.5074,-0.1278)
            mock_get.assert_called_with(base, params = params)
        except:
            mock_get.assert_called_with(base, params = params)

def test_Map_green():

    # get map as an array of pixels
    # manually override the pixels to test values
    # ensure returns are as expected

    london_map = Map(51.5074,-0.1278)

    london_map.pixels[:,:,0] =
    london_map.pixels[:,:,1] =
    london_map.pixels[:,:,2] =

    assert london_map.green(1.1) ==
    assert london
