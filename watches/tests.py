from django.test import TestCase
from .models import Watch


class WatchModelTest(TestCase):
    """Test cases for Watch model"""
    
    def setUp(self):
        self.watch = Watch.objects.create(
            name='Test Watch',
            description='A test watch',
            price=99.99
        )
    
    def test_watch_creation(self):
        """Test that a watch can be created"""
        self.assertEqual(self.watch.name, 'Test Watch')
        self.assertEqual(str(self.watch), 'Test Watch')
