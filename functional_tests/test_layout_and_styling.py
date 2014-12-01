from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        # user1 goes to home page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # they notice the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] /2,
                               512,
                               delta=5)

        # they start a new list and see that the input is nicely centered
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] /2,
                               512,
                               delta=5)


