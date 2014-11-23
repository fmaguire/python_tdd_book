from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_user_can_start_a_list_and_retrieve_it_later(self):
        # User1 goes to website homepage
        self.browser.get(self.live_server_url)

        # User1 sees page has title and header about todo lists
        self.assertIn('todo', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('todo', header_text)

        # User1 is invited to enter item to todo list
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a todo item')

        # User1 adds 'buy X' into a text box
        inputbox.send_keys('buy X')

        # User1 hits enter and page updates and lists '1: buy X' as an item in todo list
        inputbox.send_keys(Keys.ENTER)
        user1_list_url = self.browser.current_url
        self.assertRegex(user1_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: buy X')

        # Text box persists and user1 adds 'sell Y' to it
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('sell Y')

        # User1 presses enter and page updates and now shows both items
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: buy X')
        self.check_for_row_in_list_table('2: sell Y')


        # New User2 visits site

        ## Use a browser session to make sure no information from
        ## User1 is coming through (e.g. cookies)
        self.browser.quit()
        self.browser.webdriver.Firefox()

        # User2 visits home page and can't see User1's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('buy X', page_text)
        self.assertNotIn('sell Y', page_text)

        # User2 starts a new list by entering an item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Refactor Z')
        inputbox.send_keys(Keys.ENTER)

        # User2 gets their own unqiue URL
        user2_list_url = self.browser.current_url
        self.assertRegex(user2_list_url, '/lists/.+')
        self.assertNotEqual(user2_list_url, user1_list_url)

        # again there is no trace of User1's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('buy X', page_text)
        self.assertIn('Refactor Z', page_text)

