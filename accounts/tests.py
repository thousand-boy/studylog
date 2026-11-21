from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class SignUpTests(TestCase):
    def test_signup_page_is_open_to_anonymous_users(self):
        response = self.client.get(reverse("accounts:signup"))
        self.assertEqual(response.status_code, 200)

    def test_signup_creates_user_and_redirects_to_login(self):
        response = self.client.post(
            reverse("accounts:signup"),
            {
                "username": "newuser",
                "password1": "Study-log-2026!",
                "password2": "Study-log-2026!",
            },
        )
        self.assertRedirects(response, reverse("accounts:login"))
        self.assertTrue(User.objects.filter(username="newuser").exists())


class LoginLogoutTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user("alice", password="pass-for-test-1")

    def test_login_redirects_to_record_list(self):
        response = self.client.post(
            reverse("accounts:login"),
            {"username": "alice", "password": "pass-for-test-1"},
        )
        self.assertRedirects(response, reverse("records:record_list"))

    def test_logout_accepts_only_post(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("accounts:logout"))
        self.assertEqual(response.status_code, 405)

        response = self.client.post(reverse("accounts:logout"))
        self.assertRedirects(response, reverse("accounts:login"))
        # ログアウト後は一覧を開くとログイン画面に戻される
        response = self.client.get(reverse("records:record_list"))
        self.assertEqual(response.status_code, 302)
