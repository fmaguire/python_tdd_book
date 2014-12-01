from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # User goes to home page and accidentally submits an empty
        # list item
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # home page refreshes with an error message saying list items can't be
        # blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # user tries again with some text and item now adds correctly
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # user then again accidentally enters a blank item
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # receives a similar warning to previous on list page
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # they can correct error by filling in text
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
        self.browser.check_for_row_in_list_table('1: Buy milk')
        self.browser.check_for_row_in_list_table('2: Make tea')
