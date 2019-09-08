import pytest
from ..models import db, User
from ..user_app import create_app


@pytest.fixture(scope="module")
def new_user():
    user = User("admin", "user")
    return user


@pytest.fixture(scope='module')
def test_client():
    config_name = 'testing'
    flask_app = create_app(config_name)
    """Flask provides a way to test your appicaltion by
        exposing the Werkzueg test Client
        and handling the context locals for you.
    """
    testing_client = flask_app.test_client()
    """
        Establish an application context before running
    """
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client  #This is where the testing occurs

    db.session.close()
    db.drop_all()
    ctx.pop()


# @pytest.fixture(scope='function')
# def init_database():
#     db.create_all()
#     # #Insert user data
#     # db.session.add(user1)
#     # db.session.add(user2)
#     # # Commit the changes for the users
#     # db.session.commit()
#     yield db  # This is where the testing happens
#     db.drop_all()
