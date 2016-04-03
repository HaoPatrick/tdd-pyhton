from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page,view_list
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item,List
# Create your tests here.

class ListAndItemModelsTest(TestCase):

    def test_saving_and_retriving_items(self):
        list_=List()
        list_.save()

        first_item=Item.objects.create(text='The first (ever) list item',list=list_)
        second_item=Item.objects.create(text='The second list item',list=list_)

        saved_list=List.objects.first()
        self.assertEqual(saved_list,list_)

        saved_items=Item.objects.all()
        self.assertEqual(saved_items.count(),2)

        first_saved_item=saved_items[0]
        second_saved_item=saved_items[1]
        self.assertEqual(first_saved_item.text,'The first (ever) list item')
        self.assertEqual(first_saved_item.list,list_)
        self.assertEqual(second_saved_item.list,list_)
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

    '''def test_home_page_can_redirect(self):
        request=HttpRequest()
        request.method='POST'
        request.POST['item_text']='A new list item'

        response=home_page(request)

        self.assertEqual(response.status_code,302)
        self.assertEqual(response['location'],'/')
    '''
