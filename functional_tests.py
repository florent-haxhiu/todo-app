from selenium import webdriver
from unittest import TestCase, main


class NewVisitorTest(TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # User goes to check out new to-do app
        self.browser.get("http://localhost:8000")

        # User notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        self.fail('Finish the test!')

        # User is invited to enter a to-do item straight away


if __name__ == 'main':
    main()
