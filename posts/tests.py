from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

class PostModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        cls.user = User.objects.create_user(username='testuser', password='12345')

        # Create a test post
        cls.post = Post.objects.create(
            user=cls.user,
            image='test_image.jpg',
            caption='Test Caption',
            title='Test Title'
        )
    def test_post_creation(self):
        # Test that the post was created successfully
        self.assertEqual(self.post.title, 'Test Title')
        self.assertEqual(self.post.caption, 'Test Caption')
        self.assertEqual(self.post.user, self.user)
        self.assertTrue(self.post.slug)  # Ensure slug is generated

class CommentModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        cls.user = User.objects.create_user(username='testuser', password='12345')

        # Create a test post
        cls.post = Post.objects.create(
            user=cls.user,
            image='test_image.jpg',
            caption='Test Caption',
            title='Test Title'
        )

        # Create a test comment
        cls.comment = Comment.objects.create(
            post=cls.post,
            body='Test Comment Body',
            posted_by='Test User'
        )

    def test_comment_creation(self):
        # Test that the comment was created successfully
        self.assertEqual(self.comment.body, 'Test Comment Body')
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.posted_by, 'Test User')

