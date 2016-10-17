from django.test import TestCase
from django.core.urlresolvers import resolve	
from lists.views import home_page	


# Create your tests here.
class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')						# resolve是Django内部函数，用于解析url并将其映射到相应视图函数。
		self.assertEqual(found.func, home_page)		# 检查解析网站根路径“”是否有名为home_page的函数
		