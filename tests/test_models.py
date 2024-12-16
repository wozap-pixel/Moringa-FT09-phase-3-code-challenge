import unittest
from models.magazine import Magazine
from models.author import Author
from models.article import Article

class TestModels(unittest.TestCase):
    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")
        
    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        article = Article(1, "AI Revolution", "Content about AI", 1, 1)
        self.assertEqual(article.title, "AI Revolution")
        self.assertEqual(article.content, "Content about AI")

if __name__ == '__main__':
    unittest.main()
