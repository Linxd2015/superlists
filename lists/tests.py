from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest	
from lists.views import home_page
from django.template.loader import render_to_string


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

	def test_home_page_can_save_a_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new list item'

		response = home_page(request)
		self.assertIn('A new list item', response.content.decode())
		expected_html = render_to_string(
				'home.html',
				{'new_item_text': 'A new list item'},
				request=request
			)
		self.assertEqual(response.content.decode(), expected_html)