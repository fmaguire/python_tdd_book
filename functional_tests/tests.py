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
        # User goes to website homepage
        self.browser.get(self.live_server_url)

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

        self.check_for_row_in_list_table('1: buy X')

        # Text box persists and user adds 'sell Y' to it
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('sell Y')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: buy X')
        self.check_for_row_in_list_table('2: sell Y')


        self.fail('Finish the test!')
        # User presses enter and page updates and now shows both items

        # User sees explanatory text that custom url has been generated for her list

        # User checks custom url and confirms list is still there

        # User leaves

