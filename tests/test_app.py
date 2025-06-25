from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    """
    Esse teste tem 3 etapas (AAA)
    - A: Arrange - Arranjo
    - A: Act     - Executa a coisa (SUT)
    - A: Assert  - Garanta que A é A
    """
    # arrange
    client = TestClient(app)

    # act
    response = client.get('/')

    # assert
    assert response.json() == {'message': 'Olá mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_exercicio_deve_retornar_html():
    client = TestClient(app)
    response = client.get('/exercicio-html')
    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo </h1>' in response.text
