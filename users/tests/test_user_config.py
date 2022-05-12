import pytest
from users.apps import UsersConfig

@pytest.mark.django_db
def test_config_payment_file_app():
    assert UsersConfig.name == "users"