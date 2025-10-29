from http import HTTPStatus


def test_get_token(client, user):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert token['token_type'] == 'Bearer'
    assert 'access_token' in token


# def test_get_user_not_found_ex01_aula_07(client):
#     data = {'mail': 'test'}
#     token = create_access_token(data)

#     response = client.delete(
#         '/users/1',
#         headers={'Authorization': f'Bearer {token}'},
#     )

#     assert response.status_code == HTTPStatus.UNAUTHORIZED
#     assert response.json() == {'detail': 'Could not validate credentials'}


# def test_get_current_user_does_not_exists_ex02_aula_07(client):
#     data = {'sub': 'test@test'}
#     token = create_access_token(data)

#     response = client.delete(
#         '/users/1',
#         headers={'Authorization': f'Bearer {token}'},
#     )

#     assert response.status_code == HTTPStatus.UNAUTHORIZED
#     assert response.json() == {'detail': 'Could not validate credentials'}
