from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):	# 测试组织成类的形式，继承自unittest.TestCase

	def setUp(self):	# 初始化，每次执行用例前先执行setUp打开浏览器,结束后执行tearDown关闭浏览器。遇到错误也会正常执行这两个方法
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)		# 隐式等待，打开浏览器等待3秒

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):	# 测试方法，主要代码都写在里面

		# browser = webdriver.Firefox()
		# 伊迪丝听说有个很酷的在线待办事项应用
		# 他去看了这个应用的首页
		self.browser.get('http://localhost:8000')

		# browser.get('http://localhost:8000')

		# 他注意到网页的标题和头部都包含了“To-Do”这词

		# assert 'To-Do' in browser.title, "Browser title was " + browser.title 	# 不使用unittest框架的断言
		# unittest提供的断言函数
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test')	# 生成错误信息,用这个方法提醒测试结束了

		# 应用邀请他输入一个待办事项

		# 他在一个文本框中输入了“Buy peacock feathers”
		# 伊迪丝的爱好是用假蝇做饵钓鱼

		# 他按回车后，页面更新了
		# 待办事项表格中显示了“Buy peacock feathers”

		# 页面中又显示了一个文本框，可以输入其他待办事项
		# 他又输入了“use peacock feathers to make a fly”
		# 伊迪丝做事很有条理

		# 页面再次更新，他的清单中显示了两个待办事项

		# 伊迪丝想知道这个网站是否会记住他的清单
		# 他看到网站为他生成了一个唯一的url
		# 而且页面中有些文字解说这个功能

		# 他访问的url，发现他的待办事项列表还在

		# 他很满意，去睡觉了


if __name__ == '__main__':
	unittest.main(warnings='ignore')