from django.test import TestCase

from .models import Faculty, Cafedra, Group
from .views import FOR_TEST

class FacultyMethodTest(TestCase):
    def test_Method_FOR_TEST(self):
        result = FOR_TEST()
        none_type = type(None)
        self.assertEqual( type(result), type('2'))



class CafedraMethodTest(TestCase):

    pass

class GroupMethodTest(TestCase):

    pass
