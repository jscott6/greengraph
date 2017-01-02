
from pytest import approx
from ggraph import Greengraph
import numpy as np

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
    with patch.object(requests, 'get'):
