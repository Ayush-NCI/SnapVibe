# """
# Module containing test cases for models for the users app.
# """
# from django.test import TestCase
# from django.contrib.auth.models import User
# from .models import Profile

# class ProfileModelTestCase(TestCase):
#     """
#     Model representing user profile test case information.
#     """
#     @classmethod
#     def setUpTestData(cls):
#         # Create a test user
#         cls.user = User.objects.create_user(username='testuser', password='12345')

#         # Create a test profile
#         cls.profile = Profile.objects.create(
#             user=cls.user,
#             photo='test_photo.jpg'
#         )

#     def test_profile_creation(self):
#         """
#         representation of the profile creation.
#         """
#         self.assertEqual(self.profile.user, self.user)
#         self.assertEqual(self.profile.photo, 'test_photo.jpg')
#         self.assertEqual(str(self.profile), 'testuser')
