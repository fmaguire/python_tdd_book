from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('todo', header_text)

        # User is invited to enter item to todo list
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a todo item')

        # User adds 'buy X' into a text box
        inputbox.send_keys('buy X')

        # User hits enter and page updates and lists '1: buy X' as an item in todo list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: buy X' for row in rows),
                "New todo item did not appear in table -- its text was:\n "
                "{0}".format(table.text,))


        self.fail('Finish the test!')

        # Text box persists and user adds 'sell Y' to it

        # User presses enter and page updates and now shows both items

        # User sees explanatory text that custom url has been generated for her list

        # User checks custom url and confirms list is still there

        # User leaves

if __name__ == '__main__':
    unittest.main(warnings='ignore')


