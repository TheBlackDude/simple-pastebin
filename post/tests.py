from django.test import TestCase
from django.core.exceptions import ValidationError

from .models import Post
from .forms import PostForm


class PostModelTest(TestCase):

    def test_cannot_save_empty_post(self):
        post = Post()
        with self.assertRaises(ValidationError):
            post.save()
            post.full_clean()

    def test_can_generate_slug(self):
        post = Post.objects.create(name='the good post', content='good post')
        self.assertEqual(post.slug, 'the-good-post')

    def test_can_generate_random_string(self):
        post = Post.objects.create(name='awesome post', content='really awesome')
        self.assertTrue(post.post_url)

    def test_cannot_save_duplicate_posts(self):
        Post.objects.create(name='test1', content='test1 content')
        with self.assertRaises(ValidationError):
            duplicate = Post(name='test1', content='test1 content')
            duplicate.full_clean()


class PostFormTest(TestCase):

    def test_post_form_inputs_have_placeholder_and_css_classes(self):
        form = PostForm()
        self.assertIn('placeholder="Post Title"', form.as_p())
        self.assertIn('class="form-control"', form.as_p())

    def test_form_validation_for_empty_post(self):
        form = PostForm(data={'name': '', 'content': ''})

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ["The post title can't be empty"])
        self.assertEqual(form.errors['content'], ["The post content can't be empty"])

    def test_form_validation_for_unique_post(self):
        Post.objects.create(name='good post', content='awesome post')
        form = PostForm(data={'name': 'good post', 'content': 'best post'})

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ["You can't have two posts with the same name"])
