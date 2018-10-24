from django.test import TestCase
from django.core.exceptions import ValidationError

from .models import Post


class PostModelTest(TestCase):

    def test_cannot_save_empty_post(self):
        post = Post()
        with self.assertRaises(ValidationError):
            post.save()
            post.full_clean()

    def test_can_generate_slug(self):
        post = Post.objects.create(name='the good post', content='good post')
        self.assertEqual(post.slug, 'the-good-post')

    def test_cannot_save_duplicate_posts(self):
        Post.objects.create(name='test1', content='test1 content')
        with self.assertRaises(ValidationError):
            duplicate = Post(name='test1', content='test1 content')
            duplicate.full_clean()
