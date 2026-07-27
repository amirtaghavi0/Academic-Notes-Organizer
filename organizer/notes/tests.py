
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Course, Note


User = get_user_model()


class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

    def test_create_user_with_bio(self):
        user = User.objects.create_user(
            username="ali",
            password="pass12345",
            bio="student of data science"
        )
        self.assertEqual(user.username, "ali")
        self.assertEqual(user.bio, "student of data science")

    def test_course_creation(self):
        course = Course.objects.create(
            user=self.user,
            title="Mathematics",
            description="Linear algebra and calculus"
        )
        self.assertEqual(course.user, self.user)
        self.assertEqual(course.title, "Mathematics")
        self.assertEqual(course.description, "Linear algebra and calculus")

    def test_note_creation(self):
        course = Course.objects.create(
            user=self.user,
            title="Python",
            description="Programming course"
        )
        note = Note.objects.create(
            course=course,
            title="Decorators",
            description="Important topic",
            content="A decorator is a function...",
            tag="python"
        )
        self.assertEqual(note.course, course)
        self.assertEqual(note.title, "Decorators")
        self.assertEqual(note.description, "Important topic")
        self.assertEqual(note.content, "A decorator is a function...")
        self.assertEqual(note.tag, "python")

    def test_course_has_notes_relation(self):
        course = Course.objects.create(
            user=self.user,
            title="Django",
            description="Web framework"
        )
        note1 = Note.objects.create(
            course=course,
            title="Models",
            tag="backend"
        )
        note2 = Note.objects.create(
            course=course,
            title="Views",
            tag="backend"
        )

        self.assertIn(note1, course.notes.all())
        self.assertIn(note2, course.notes.all())
        self.assertEqual(course.notes.count(), 2)

    def test_updated_field_changes_on_save(self):
        course = Course.objects.create(
            user=self.user,
            title="Machine Learning",
            description="Initial description"
        )
        old_updated = course.updated

        course.description = "Updated description"
        course.save()

        self.assertGreater(course.updated, old_updated)


class CourseViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.other_user = User.objects.create_user(
            username="otheruser",
            password="otherpass123"
        )

    def test_login_required_for_course_list(self):
        response = self.client.get(reverse("course_list"))
        self.assertEqual(response.status_code, 302)

    def test_course_list_shows_only_logged_in_users_courses(self):
        course1 = Course.objects.create(
            user=self.user,
            title="Algebra",
            description="Math course"
        )
        Course.objects.create(
            user=self.other_user,
            title="History",
            description="Humanities course"
        )

        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("course_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Algebra")
        self.assertNotContains(response, "History")

