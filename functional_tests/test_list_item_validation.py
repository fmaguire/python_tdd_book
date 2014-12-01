from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # User goes to home page and accidentally submits an empty
        # list item

        # home page refreshes with an error message saying list items can't be
        # blank

        # user tries again with some text and item now adds correctly

        # user then again accidentally enters a blank item

        # receives a similar warning to previous on list page

        # they can correct error by filling in text
        self.fail('write text')
