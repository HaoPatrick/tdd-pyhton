from selenium import webdriver
from unittest import skip
import unittest
from .bse import FunctionalTest
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
import time
class NewVisitorTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        self.fail('wirte me')


if __name__=='__main__':
    unittest.main(warnings='ignore')
