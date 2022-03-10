import unittest
import datetime

# run: python -m unittest 19_test-note-class.py
class Note:
    def __init__(self, content):
        self.content = content
        self.creation_time = datetime.datetime.now().strftime(
            '%m-%d-%Y %H:%M:%S')

    def find(self, word):
        return word.lower() in self.content.lower()


class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, content):
        self.notes.append(Note(content))

    def search(self, value):
        return [note.content for note in self.notes if note.find(value)]


class TestNote(unittest.TestCase):

    def setUp(self):
        self.note = Note('Simple note.')
        
    def test_note_has_content_instance_attr(self):
        self.assertTrue(hasattr(self.note,'content'), 'A Note instance does not have a content attribute.')

    def test_note_has_category_class_attr(self):
        self.assertTrue(hasattr(Note,'category'), 'The Note class does not have a category attribute.')

class TestNotebook(unittest.TestCase):

    def setUp(self):
        self.notebook = Notebook()
        self.notebook.new_note('Big Data')
        self.notebook.new_note('Data Science')
        self.notebook.new_note('Machine Learning')

    def test_notebook_search_method(self):
        self.assertEqual(self.notebook.search('data'),['Big Data', 'Data Science'])