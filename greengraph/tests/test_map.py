

import requests
from mock import patch
from greengraph.map import map
import numpy as np

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

    # testing functionality for 1 pixel
    # get map as an array of pixels
    # manually override the pixels to test values
    # ensure returns are as expected

    london_map = Map(51.5074,-0.1278)

    london_map.pixels[0,0,0] = 1.0
    london_map.pixels[0,0,1] = 1.1
    london_map.pixels[0,0,2] = 1.0

    assert london_map.green(1.1)[0,0] == False
    assert london_map.green(1.2)[0,0] == False
    assert london_map.green(1.0)[0,0] == True


def test_Map_count_green():

    london_map = Map(51.5074,-0.1278)

    size = np.shape(london_map)[1]
    limit = size/2

    # set limit/size of the pixels so that behaviour uniformly determined by
    # chosen thresholds
    london_map.pixels[:,:limit,0] = 1.0
    london_map.pixels[:,:limit,1] = 1.1
    london_map.pixels[:,:limit,2] = 1.0

    # set (1-limit)/size of the pixels to 'True' automatically
    london_map.pixels[:,limit:,0] = 1.0
    london_map.pixels[:,limit:,1] = 5.0
    london_map.pixels[:,limit:,2] = 1.0

    assert london_map.count_green() == size**2/2
    assert london_map.count_green(1.2) == size**2/2
    assert london_map.count_green(1.0) == size**2
