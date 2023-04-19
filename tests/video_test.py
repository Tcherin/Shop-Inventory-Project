import unittest

from models.video import Video

class TestVideo(unittest.TestCase):

    def setUp(self):
        self.video = Video("Jaws", "Horror", "Hero shark gets cancelled for being too 'real'.", 10, 2, 5)

    def test_video_has_name(self):
        self.assertEqual("Jaws", self.video.name)

    def test_video_has_genre(self):
        self.assertEqual("Horror", self.video.genre)

    def test_video_has_description(self):
        self.assertEqual("Hero shark gets cancelled for being too 'real'.", self.video.description)

    def test_video_has_stock_quantity(self):
        self.assertEqual(10, self.video.stock_quantity)

    def test_video_has_buying_cost(self):
        self.assertEqual(2, self.video.buying_cost)

    def test_video_has_selling_price(self):
        self.assertEqual(5, self.video.selling_price)