from django.test import TestCase
from django.urls import resolve, reverse
from django.contrib.auth.models import User
from .. import views


class PageTest(TestCase):
    """ All pages should:
        1. Resolve to the proper View
        2. Return a 200 (login_required urls return 302 if not logged in)
        3. Use the appropriate template
        4. Contain the proper context data
    """
    fixtures = ['initial_data.json', ]

    def test_mainpage(self):
        """
        Test the mainpage url and view
        """
        url = reverse('management:mainpage')
        v = resolve(url)
        self.assertEqual(v.func.__name__, views.MainView.__name__)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'management/mainpage.html')

