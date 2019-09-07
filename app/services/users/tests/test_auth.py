import pytest
from users.models import db, User


def test_user_model(new_user):
    """
        GIVEN a User model
        WHEN a new User is Created
        THEN check  weather the username field is defined correctly 
    """
    user = User("user", "user")
    assert user.username == "user"


def test_get_all_users(test_client):
    """Given a flask application
    when the '/users' page is requested(GET)
    Then check the response is valid
    """
    response = test_client.get('api/v1/users')
    assert response.status_code == 200


def test_create_user(test_client):
    """
        when an 'api/v1/users' route is requested
        a user should be created and a 
        response message returned
    """
    response = test_client.post('api/v1/auth/signup',
                                data=dict(username='user', password='user'))

    # assert response.status_code == 201
    assert b"Your account has been created succesfully" in response.data


def test_create_duplicate_user(test_client):
    response = test_client.post('api/v1/auth/signup',
                                data=dict(username='nom', password='nom'))
    dupicate_user = test_client.post('api/v1/auth/signup',
                                     data=dict(username='nom', password='nom'))

    # raise Exception(dupicate_user.data)


# @pytest.mark.django_db
# def test_my_user():
#     me = User.objects.get(username='naome')
#     assert me.is_superuser

# import unittest
# from users import create_app
# from users.models import db
# import json

# class BaseCase(unittest.TestCase):
#     """class holds all the unittests for the auth endpoints"""
#     def setUp(self):
#         """
#             This method is run at the begining of each test
#             also initialises the client where tests will be run
#         """
#         config_name = 'testing'
#         self.app = create_app(config_name)
#         self.app_context = self.app.app_context()
#         self.app_context.push()
#         self.client = self.app.test_client()

#     def test(self):
#         response = self.client.get('/api/v1/auth/signup')
#         raise Exception(response)
#         # pass

# def test_user_resgistration(self):
#     """ Registers a user to be used for tests"""
#     user = {'user_id': 1, 'username': 'naome', 'password': 'naome'}

#     response = self.client.post('/api/v1/auth/signup',
#                                 data=json.dumps(user),
#                                 content_type='application/json')
#     self.assertEqual(response.status_code, 201)
#     self.assertIn('Your account has been created succesfully',
#                   str(response.data))

# def test_duplicate_user(self):
#     """Test for registering a duplicate user"""
#     user = {'user_id': 1, 'username': 'naome', 'password': 'naome'}

#     response = self.client.post('/api/v1/auth/signup',
#                                 data=json.dumps(user),
#                                 content_type='application/json')
#     response1 = self.client.post('/api/v1/auth/signup',
#                                  data=json.dumps(user),
#                                  content_type='application/json')
#     self.assertEqual(response.status_code, 403)
#     self.assertIn('User already exists', str(response.data))

# def tearDown(self):
#     db.drop_all()
#     # return super().tearDown()

# if __name__ == '__main__':
#     unittest.main()
