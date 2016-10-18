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
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		
		# 应用邀请他输入一个待办事项
		inputbox = slef.browser.find_element_by_id('id_new_item')
		self.assertEqual(
				inputbox.get_attribute('placeholder'),
				'Enter a to-do item'
			)

		# 他在一个文本框中输入了“Buy peacock feathers”
		# 伊迪丝的爱好是用假蝇做饵钓鱼
		inputbox.send_keys('Buy peacock feathers')

		# 他按回车后，页面更新了
		# 待办事项表格中显示了“Buy peacock feathers”
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_element_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1:Buy peacock feathers' for row in rows)
			)

		# 页面中又显示了一个文本框，可以输入其他待办事项
		# 他又输入了“use peacock feathers to make a fly”
		# 伊迪丝做事很有条理
		self.fail('Finish the test')	# 生成错误信息,用这个方法提醒测试结束了

		# 页面再次更新，他的清单中显示了两个待办事项

		# 伊迪丝想知道这个网站是否会记住他的清单
		# 他看到网站为他生成了一个唯一的url
		# 而且页面中有些文字解说这个功能

		# 他访问的url，发现他的待办事项列表还在

		# 他很满意，去睡觉了


if __name__ == '__main__':
	unittest.main(warnings='ignore')