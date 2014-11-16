from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_user_can_start_a_list_and_retrieve_it_later(self):
        # User goes to website homepage
        self.browser.get('http://localhost:8000')

        # User sees page has title and header about todo lists
        self.assertIn('todo', self.browser.title)
        self.fail('Finish the test!')

        # User is invited to enter item to todo list

        # User adds 'buy X' into a text box

        # User hits enter and page updates and lists '1: buy X' as an item in todo list

        # Text box persists and user adds 'sell Y' to it

        # User presses enter and page updates and now shows both items

        # User sees explanatory text that custom url has been generated for her list

        # User checks custom url and confirms list is still there

        # User leaves

if __name__ == '__main__':
    unittest.main(warnings='ignore')


