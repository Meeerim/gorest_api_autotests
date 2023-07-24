import json
import logging
import os.path
import random

import allure
import curlify
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from requests import Session, Response


def load_json_schema(name: str):
    schema_abs_path = r'C:\Users\skmee\PycharmProjects\gorest_autotests_api\gorest_autotests_api\schemas'
    schema_path = os.path.join(schema_abs_path, name)
    with open(schema_path) as schema:
        return json.loads(schema.read())


class CustomSession(Session):
    def __init__(self, base_url):
        self.base_url = base_url
        super().__init__()

    def request(self, method, url, *args, **kwargs) -> Response:
        response = super(CustomSession, self).request(method=method, url=self.base_url + url, *args, **kwargs)
        curl = curlify.to_curl(response.request)
        logging.info(curl)
        with step(f'{method} {url}'):
            allure.attach(body=curl, name="Request curl", attachment_type=AttachmentType.TEXT, extension='txt')
            try:
                response_body = response.json()
            except json.JSONDecodeError:
                response_body = response.text

            allure.attach(
                body=json.dumps(response_body, indent=2),
                name="Response Body",
                attachment_type=AttachmentType.JSON,
            )

            return response


base_session = CustomSession('https://gorest.co.in')


def get_existing_user_ids():
    response = base_session.get(url='/public/v2/users/')
    if response.status_code == 200:
        user_data = response.json()
        print(user_data)
        user_ids = {user['id'] for user in user_data}
        return user_ids
    else:
        # Handle the scenario where the GET request failed
        print(f"Failed to retrieve user IDs. Status code: {response.status_code}")
        return []


def choose_random_user_id_for_deletion(existing_user_ids):
    user_ids_list = list(existing_user_ids)
    return random.choice(user_ids_list)
