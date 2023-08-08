import os

import allure

from jsonschema.validators import validate
from gorest_autotests_api.helpers.base_session import load_json_schema, base_session, get_existing_user_ids, \
    choose_random_user_id_for_deletion
from gorest_autotests_api.helpers.data import user


@allure.tag("api")
@allure.label('owner', 'meerim')
@allure.feature('Get users details')
@allure.story('Get all users and details ')
def test_get_users():
    with allure.step("Get all users and details"):
        schema = load_json_schema('get_users.json')
        response = base_session.get(
            url='/public/v2/users',
            headers={
                "Authorization": f"Bearer {os.getenv('token')}",
                "Content-Type": "application/json"
            }
        )
    with allure.step("Verify expected status code and validate the received schema"):
        validate(instance=response.json(), schema=schema)
        assert response.status_code == 200


@allure.tag("api")
@allure.label('owner', 'meerim')
@allure.feature('Create new user')
@allure.story('Create new user with POST request')
def test_create_new_user(setup_new_user):
    with allure.step("Create new user with POST request"):
        schema = load_json_schema('post_create_user.json')
        response = base_session.post(
            url='/public/v2/users',
            json={
                "name": user.full_name,
                "email": user.email,
                "gender": user.gender,
                "status": user.status
            },
            headers={
                "Authorization": f"Bearer {os.getenv('token')}",
                "Content-Type": "application/json"
            }
        )
    with allure.step("Verify of successful user creation by checking id and status code"):
        validate(instance=response.json(), schema=schema)
        assert response.status_code == 201
        data = response.json()
        assert "id" in data


@allure.tag("api")
@allure.label('owner', 'meerim')
@allure.feature('Update user details')
@allure.story('Update only user email with PUT request')
def test_update_user_email(setup_new_user):
    with allure.step("Retrieve existing user IDs"):
        existing_user_ids = get_existing_user_ids()

    if not existing_user_ids:
        print("No user IDs found for deletion.")
        return

    with allure.step("Choose a random user ID for deletion"):
        user_id = choose_random_user_id_for_deletion(existing_user_ids)
    with allure.step("Update user email"):
        response = base_session.put(
            url=f'/public/v2/users/{user_id}',
            json={
                "email": user.email
            },
            headers={
                "Authorization": f"Bearer {os.getenv('token')}",
                "Content-Type": "application/json"
            }
        )
    with allure.step("Validate email changed as expected"):
        assert response.status_code == 200


@allure.tag("api")
@allure.label('owner', 'meerim')
@allure.feature('Update user details')
@allure.story('Update user details with Patch request')
def test_update_user_info(setup_new_user):
    with allure.step("Retrieve existing user IDs"):
        existing_user_ids = get_existing_user_ids()

    if not existing_user_ids:
        print("No user IDs found for deletion.")
        return

    with allure.step("Choose a random user ID for deletion"):
        user_id = choose_random_user_id_for_deletion(existing_user_ids)
    with allure.step("Update user name and email"):
        schema = load_json_schema('patch_user.json')
        response = base_session.patch(
            url=f'/public/v2/users/{user_id}',
            json={
                "name": user.full_name,
                "email": user.email2,
                "gender": user.gender,
                "status": user.status
            },
            headers={
                "Authorization": f"Bearer {os.getenv('token')}",
                "Content-Type": "application/json"
            }
        )
    with allure.step("Verify user details changed and received expected status code"):
        validate(instance=response.json(), schema=schema)
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == user.full_name



@allure.tag("api")
@allure.label('owner', 'meerim')
@allure.feature('Delete user')
@allure.story('Delete user')
def test_delete_user():
    with allure.step("Retrieve existing user IDs"):
        existing_user_ids = get_existing_user_ids()

    if not existing_user_ids:
        print("No user IDs found for deletion.")
        return

    with allure.step("Choose a random user ID for deletion"):
        user_id_for_deletion = choose_random_user_id_for_deletion(existing_user_ids)

    with allure.step(f"Delete user with id {user_id_for_deletion}"):
        response = base_session.delete(
            url=f'/public/v2/users/{user_id_for_deletion}',
            headers={
                "Authorization": f"Bearer {os.getenv('token')}",
                "Content-Type": "application/json"
            }
        )

    with allure.step("Validate response status code as expected"):
        assert response.status_code == 204

@allure.tag("api")
@allure.label('owner', 'meerim')
@allure.feature('Retrieves user posts')
@allure.story('Verify that the API returns the posts for the specified user (ID 2241)')
def test_user_posts():
    with allure.step("Get user posts"):
        schema = load_json_schema('get_user_posts.json')
        response = base_session.get(
            url='/public/v2/users/2241/posts',
            headers={
                "Authorization": f"Bearer {os.getenv('token')}",
                "Content-Type": "application/json"
            }
        )
    with allure.step("Verify the  response"):
        validate(instance=response.json(), schema=schema)
        assert response.status_code == 200
        data = response.json()
        for post in data:
            assert post["user_id"] == 2241
