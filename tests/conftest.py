from faker import Faker
import pytest
from dotenv import load_dotenv

from gorest_autotests_api.helpers.data import user


@pytest.fixture(scope='session', autouse=True)
def auto_env():
    load_dotenv()



fake = Faker()


@pytest.fixture(scope='function')
def setup_new_user():
    # Create a new user with a dynamically generated email
    user.email = fake.email()
    user.email2 = fake.email()