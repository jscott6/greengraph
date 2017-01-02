
from pytest import approx
from ggraph import Greengraph
import numpy as np
from mock import Mock
from nose.tools import assert_raises

graph = Greengraph("London", "Paris")


def test_init():
    assert graph.start == "London"
    assert graph.end == "Paris"

def test_geolocate():
    # test method returns correct latitude & longitude
    assert graph.geolocate('London') == approx((51.5074, -0.1278), abs = 1e-3)

def test_location_sequence():
    # test method returns the correct sequence of coordinates
    # between 2 locations given an arbitrary step size

    steps = 10
    lond_coords = np.asarray(graph.geolocate("London"))
    paris_coords = np.asarray(graph.geolocate("Paris"))
    diff = (paris_coords - lond_coords)/(steps-1)
    coord_seq = graph.location_sequence(lond_coords, paris_coords, steps)

    for i in range(0, steps):
        assert coords_seq[i] == lond_coords + i*diff

def test_green_between():

    # we test the funnctionality of count_green in test_map
    # here we look at the size of the returned array and
    # that we accept positive integers only

    steps = 10
    green_between = graph.green_between(steps)

    assert np.shape(green_between) == (10,)

    with assert_raises(ValueError):
        assert graph.green_between(-1)
