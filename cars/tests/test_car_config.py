import pytest
from cars.apps import CarsConfig

@pytest.mark.django_db
def test_config_payment_file_app():
    assert CarsConfig.name == "cars"