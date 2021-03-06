from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string
from lists.models import Item,List


# Create your tests here.
class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')						# resolve是Django内部函数，用于解析url并将其映射到相应视图函数。
		self.assertEqual(found.func, home_page)		# 检查解析网站根路径“”是否有名为home_page的函数

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		# self.assertTrue(response.content.startswith(b'<html>'))
		# self.assertIn(b'<title>To-Do lists</title>', response.content)
		# self.assertTrue(response.content.endswith(b'</html>'))
		expected_html = render_to_string('home.html', request=request)	# 书中Django为1.7，无需加request参数即可，当前环境使用的是1.9需添加该参数
		self.assertEqual(response.content.decode(), expected_html)

		# print('response.content.decode()\n', response.content.decode())
		# print('expected_html\n', expected_html)

class ItemModelTest(TestCase):

	def test_saving_and_retrieving_items(self):
		list_ = List()
		list_.save()

		first_item = Item()
		first_item.text = 'The first(ever) list item'
		first_item.list = list_
		first_item.save()

		second_item = Item()
		second_item.text = 'Item the sencond'
		second_item.list = list_
		second_item.save()

		save_list = List.objects.first()
		self.assertEqual(save_list, list_)

		save_items = Item.objects.all()
		self.assertEqual(save_items.count(), 2)

		first_save_item = save_items[0]
		second_save_item = save_items[1]
		self.assertEqual(first_save_item.text, 'The first(ever) list item')
		self.assertEqual(first_save_item.list, list_)
		self.assertEqual(second_save_item.text, 'Item the sencond')
		self.assertEqual(second_item.list, list_)

class ListViewTest(TestCase):

	def test_uses_list_template(self):
		response = self.client.get('/lists/the-only-list-in-the-world/')
		self.assertTemplateUsed(response, 'list.html')

	def test_displays_all_items(self):
		list_ = List.objects.create()
		Item.objects.create(text='itemey 1', list=list_)
		Item.objects.create(text='itemey 2', list=list_)

class NewListTest(TestCase):

	def test_saving_a_POST_request(self):
		self.client.post(
			'/lists/new',
			data = {'item_text' : 'A new list item'}
		)
		self.assertEqual(Item.objects.count(),1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text,'A new list item')

	def test_redirects_after_POST(self):
		response = self.client.post(
			'/lists/new',
			data = {'item_text': 'A new list item'}
		)
		# self.assertEqual(response.status_code, 302)
		# self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')
		self.assertRedirects(response, '/lists/the-only-list-in-the-world/')
