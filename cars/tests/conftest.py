import pytest
from pytest_factoryboy import register
from automakers import OwnerFactory, CarFactory, UserFactory
from rest_framework.authtoken.models import Token

register(CarFactory, 'car')
register(OwnerFactory, 'owner')
register(UserFactory, 'user')


@pytest.fixture
def token_user(user):
    return Token.objects.create(user=user)


@pytest.fixture
def data_response_0_cars():
    return {
        'count': 0,
        'next': None,
        'previous': None,
        'results': []
    }


@pytest.fixture
def data_response_not_credential():
    return {
        'detail': 'As credenciais de autenticação não foram fornecidas.'
    }


@pytest.fixture
def data_response_retrieve():
    return {
        'id': 2,
        'owner': {
            'id': 2,
            'sales_opportunity': False,
        },
        'color': 'Y',
        'car_model': 'SE'
    }

@pytest.fixture
def data_response_post_validation_error():
    return ['Attention, this owner already owns 3 cars!']


@pytest.fixture
def data_create_car(owner):
    return {
        "color": "Y",
        "car_model": "SE",
        "owner": owner.id
    }


@pytest.fixture
def data_response_create_car():
    return {
        'car_model': 'SE',
        'color': 'Y',
        'id': 1,
        'owner': 1
    }


@pytest.fixture
def data_response_create_car_without_body():
    return {
        'color': ['Este campo é obrigatório.'],
        'car_model': ['Este campo é obrigatório.'],
        'owner': ['Este campo é obrigatório.']
    }