from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page,view_list
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item,List
# Create your tests here.

class NewListTest(TestCase):

    def test_can_save_a_POST_to_an_existing_list(self):
        other_list=List.objects.create()
        correct_list=List.objects.create()

        self.client.post(
                '/list/%d/add_item'%(correct_list.id,),
                data={'item_text':'A new item for an existing list'}
                )
        self.assertEqual(Item.objects.count(),1)
        new_item=Item.objects.first()
        self.assertEqual(new_item.text,'A new item for an existing list')
        self.assertEqual(new_item.list,correct_list)

    def test_redirect_to_list_view(self):
        other_list=List.objects.create()
        correct_list=List.objects.create()

        response=self.client.post(
                '/list/%d/add_item'%(correct_list.id,),
                data={'item_text':'A new item for an existing list'}
                )
        self.assertRedirects(response,'/list/%d/'%(correct_list.id,))

    def test_save_a_POST_request(self):
        self.client.post(
                '/list/new',
                data={'item_text':'A new list item'})
        self.assertEqual(Item.objects.count(),1)
        new_item=Item.objects.first()
        self.assertEqual(new_item.text,'A new list item')

    def test_redirect_after_POST(self):
        response=self.client.post(
                '/list/new',
                data={'item_text':'A new list item'}
                )
        new_list=List.objects.first()
        self.assertRedirects(response,'/list/%d/'%(new_list.id,))

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
    '''def test_home_page_can_list_all_items(self):
        list_=List.objects.create()
        Item.objects.create(text='first list',list=list_)
        Item.objects.create(text='Second list',list=list_)

        request=HttpRequest()
        response=view_list(request)

        self.assertIn('first list',response.content.decode())
        self.assertIn('Second list',response.content.decode())
    '''
class list_view_test(TestCase):
    def test_uses_list_templates(self):
        list_=List.objects.create()
        response=self.client.get('/list/%d/'%(list_.id,))
        self.assertTemplateUsed(response,'list.html')

    def test_display_only_items_for_that_list(self):
        correct_list=List.objects.create()
        Item.objects.create(text='item 1',list=correct_list)
        Item.objects.create(text='item 2',list=correct_list)

        other_list=List.objects.create()
        Item.objects.create(text='other list item 1',list=other_list)
        Item.objects.create(text='other list item 2',list=other_list)


        response=self.client.get('/list/%d/'%(correct_list.id,))

        self.assertContains(response,'item 1')
        self.assertContains(response,'item 2')
        self.assertNotContains(response,'other list item 1')
        self.assertNotContains(response,'other list item 2')
    def test_passes_correct_list_to_templates(self):
        other_list=List.objects.create()
        correct_list=List.objects.create()
        response=self.client.get('/list/%d/'%(correct_list.id,))
        self.assertEqual(response.context['list'],correct_list)


