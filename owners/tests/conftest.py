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
def data_response_not_credential():
    return {
        'detail': 'As credenciais de autenticação não foram fornecidas.'
    }


@pytest.fixture
def data_create_owner_without_body():
    return {
        'name': ['Este campo é obrigatório.'],
        'doc_number': ['Este campo é obrigatório.']
    }


@pytest.fixture
def data_response_0():
    return {
        'count': 0,
        'next': None,
        'previous': None,
        'results': []
    }


@pytest.fixture
def data_create_owner():
    return {
        'name': 'TESTE',
        'doc_number': '00000000000'
    }


@pytest.fixture
def data_response_create_owner():
    return {
        'id': 4,
        'sales_opportunity': False,
        'name': 'TESTE',
        'doc_number': '00000000000'
    }
