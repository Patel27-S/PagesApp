from django.test import SimpleTestCase

# Create your tests here.


class SimpleTest(SimpleTestCase):

    def test_home_page_status(self):
        response = self.client.get('/').status_code
        self.assertEqual(response, 200)

    def test_about_page_status(self):
        response = self.client.get('/about/').status_code
        self.assertEqual(response, 200)
