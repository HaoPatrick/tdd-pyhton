from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
class NewVisitorTest(unittest.TestCase):
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
        self.browser.get("http://localhost:8000")
        self.assertIn('To-Do lists',self.browser.title)

        header_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)

        inputbox.send_keys('Use peacock feathers to make me fly')
        inputbox.send_keys(Keys.ENTER)

        check_if_item_in_table('1. Buy peacock feathers')
        check_if_item_in_table('2. Use peacock feathers to make me fly')
        #self.assertTrue(
        #        any(row.text=='1: Buy peacock feathers' for row in rows)
        #       ,"New to-do item did not appear in table")
        #self.assertIn('1: Buy peacock feathers',[row.text for row in rows])
        #self.assertIn('2: Use peacock feathers to make me fly', [row.text for row in rows])
        self.fail('Finish the test')

if __name__=='__main__':
    unittest.main(warnings='ignore')
