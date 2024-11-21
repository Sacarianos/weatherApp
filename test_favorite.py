import unittest
import os
from favorites import load_favorites, save_favorites, add_favorite, remove_favorite, FAVORITES_FILE

class TestFavorites(unittest.TestCase):
    def setUp(self):
        """Setup a clean test environment before each test."""
        if FAVORITES_FILE.exists():
            FAVORITES_FILE.unlink()
        save_favorites([])  # Start with an empty favorites list.

    def tearDown(self):
        """Clean up after tests."""
        if FAVORITES_FILE.exists():
            FAVORITES_FILE.unlink()

    def test_add_favorite(self):
        add_favorite("New York", "10001")
        favorites = load_favorites()
        self.assertIn(("New York", "10001"), favorites)

    def test_remove_favorite(self):
        add_favorite("New York", "10001")
        remove_favorite("New York", "10001")
        favorites = load_favorites()
        self.assertNotIn(("New York", "10001"), favorites)

    def test_view_empty_favorites(self):
        favorites = load_favorites()
        self.assertEqual(favorites, [])

    def test_add_duplicate_favorite(self):
        add_favorite("New York", "10001")
        add_favorite("New York", "10001")
        favorites = load_favorites()
        self.assertEqual(favorites.count(("New York", "10001")), 1)

    def test_invalid_add(self):
        add_favorite("", "")
        favorites = load_favorites()
        self.assertEqual(favorites, [])

if __name__ == "__main__":
    unittest.main()