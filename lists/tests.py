from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item
# Create your tests here.

class ItemModelTest(TestCase):

    def test_saving_and_retriving_items(self):
        first_item=Item.objects.create(text='The first (ever) list item')
        second_item=Item.objects.create(text='The second list item')

        saved_items=Item.objects.all()
        self.assertEqual(saved_items.count(),2)

        first_saved_item=saved_items[0]
        second_saved_item=saved_items[1]
        self.assertEqual(first_saved_item.text,'The first (ever) list item')
        self.assertEqual(second_saved_item.text,'The second list item')
    def test_home_page_can_save_a_Post_request(self):
        request=HttpRequest()
        request.method='POST'
        request.POST['item_text']='A new list item'

        response=home_page(request)

        self.assertEqual(Item.objects.count(),1)
        new_item=Item.objects.first()
        self.assertEqual(new_item.text,'A new list item')

        #self.assertIn('A new list item',response.content.decode())
        excepted_html=render_to_string(
                'home.html',
                {'new_item_text': 'A new list item'})

    def test_home_page_can_redirect(self):
        request=HttpRequest()
        request.method='POST'
        request.POST['item_text']='A new list item'

        response=home_page(request)

        self.assertEqual(response.status_code,302)
        self.assertEqual(response['location'],'/')

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found=resolve('/')
        self.assertEqual(found.func,home_page)
    '''def test_home_page_returns_correct_html(self):
        request=HttpRequest()
        response=home_page(request)
        excepted_html=render_to_string('home.html')
        self.assertEqual(response.content.decode(),excepted_html)
    '''
    def test_home_page_save_a_post(self):
        request=HttpRequest()
        request.method='POST'
        request.POST['item_text']='A new list item'

        response=home_page(request)
        #self.assertIn('A new list item',response.content.decode())
        excepted_html=render_to_string(
                'home.html',
                {'new_item_text':'A new list item'}
                )
    def test_home_page_can_list_all_items(self):
        Item.objects.create(text='first list')
        Item.objects.create(text='Second list')

        request=HttpRequest()
        response=home_page(request)

        self.assertIn('first list',response.content.decode())
        self.assertIn('Second list',response.content.decode())

