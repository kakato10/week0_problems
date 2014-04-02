import unittest
import solution


class ReduceFilePathTest(unittest.TestCase):
    def test_reduce_file_path(self):
        self.assertEqual("/", solution.reduce_file_path("/"))
        self.assertEqual("/srv/www/htdocs/wtf", solution.reduce_file_path("/srv/www/htdocs/wtf/"))
        self.assertEqual("/", solution.reduce_file_path("/srv/../"))
        self.assertEqual("/srv/www/htdocs/wtf", solution.reduce_file_path("/srv/www/htdocs/wtf"))
        self.assertEqual("/srv", solution.reduce_file_path("/srv/./././././"))
        self.assertEqual("/etc/wtf", solution.reduce_file_path("/etc//wtf/"))
        self.assertEqual("/", solution.reduce_file_path("/etc/../etc/../etc/../"))
        self.assertEqual("/", solution.reduce_file_path("//////////////"))
        self.assertEqual("/", solution.reduce_file_path("/../"))

if __name__ == '__main__':
    unittest.main()
