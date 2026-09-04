from django.test import TestCase
from django.urls import reverse


class HelloApiTest(TestCase):

    def test_hello_api(self):
        response = self.client.get("/api/hello/")

        self.assertEqual(response.status_code, 500)

        self.assertEqual(
            response.json()["status"],
            "success"
        )