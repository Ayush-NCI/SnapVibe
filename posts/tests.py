# """
# Module containing test cases for models for the posts app.
# """
# from django.test import TestCase
# from django.contrib.auth.models import User
# from .models import Post, Comment

# class PostModelTestCase(TestCase):
#     """
#     Model representing Post test case information.
#     """
#     @classmethod
#     def setUpTestData(cls):
#         """
#         representation of the test data.
#         """
#         # Create a test user
#         cls.user = User.objects.create_user(username='testuser', password='12345')

#         # Create a test post
#         cls.post = Post.objects.create(
#             user=cls.user,
#             image='test_image.jpg',
#             caption='Test Caption',
#             title='Test Title'
#         )
#     def test_post_creation(self):
#         """
#         test cases for posts.
#         """
#         self.assertEqual(self.post.title, 'Test Title')
#         self.assertEqual(self.post.caption, 'Test Caption')
#         self.assertEqual(self.post.user, self.user)
#         self.assertTrue(self.post.slug)  # Ensure slug is generated

# class CommentModelTestCase(TestCase):
#     """
#     Model representing comment test case information.
#     """
#     @classmethod
#     def setUpTestData(cls):
#         """
#         representation of the test data for comment.
#         """
#         cls.user = User.objects.create_user(username='testuser', password='12345')

#         # Create a test post
#         cls.post = Post.objects.create(
#             user=cls.user,
#             image='test_image.jpg',
#             caption='Test Caption',
#             title='Test Title'
#         )

#         # Create a test comment
#         cls.comment = Comment.objects.create(
#             post=cls.post,
#             body='Test Comment Body',
#             posted_by='Test User'
#         )

#     def test_comment_creation(self):
#         """
#         test cases for comment.
#         """
#         self.assertEqual(self.comment.body, 'Test Comment Body')
#         self.assertEqual(self.comment.post, self.post)
#         self.assertEqual(self.comment.posted_by, 'Test User')
