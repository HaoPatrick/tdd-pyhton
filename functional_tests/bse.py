from selenium import webdriver
from unittest import skip
import unittest
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
import time
class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
    def check_if_item_in_table(self,send_message):
        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')
        self.assertIn(send_message,[rows.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)
        self.assertIn('To-Do lists',self.browser.title)

        header_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

    @skip
    def test_cannot_add_empty_list_items(self):
        self.fail('wirte me')


if __name__=='__main__':
    unittest.main(warnings='ignore')
