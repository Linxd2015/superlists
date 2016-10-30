from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase 

class NewVisitorTest(LiveServerTestCase):	# 测试组织成类的形式，继承自unittest.TestCase

	def setUp(self):	# 初始化，每次执行用例前先执行setUp打开浏览器,结束后执行tearDown关闭浏览器。遇到错误也会正常执行这两个方法
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)		# 隐式等待，打开浏览器等待3秒

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):	# 测试方法，主要代码都写在里面

		# browser = webdriver.Firefox()
		# 伊迪丝听说有个很酷的在线待办事项应用
		# 他去看了这个应用的首页
		# self.browser.get('http://localhost:8000')
        
		self.browser.get(self.live_server_url)

		# 他注意到网页的标题和头部都包含了“To-Do”这词

		# assert 'To-Do' in browser.title, "Browser title was " + browser.title 	# 不使用unittest框架的断言
		# unittest提供的断言函数
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		
		# 应用邀请他输入一个待办事项
		inputbox = self.browser.find_element_by_id('id_new_item')
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
		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/lists/.+')
		self.check_for_row_in_list_table('1: Buy peacock feathers')

		table = self.browser.find_element_by_id('id_list_table') 
		rows = table.find_elements_by_tag_name('tr')
		# self.assertTrue(
		# 	any(row.text == '1:Buy peacock feathers' for row in rows),
		# 	"New to-do item did not appear in table"
		# )
		self.assertIn('1: Buy peacock feathers', [row.text for row in rows],'')

		# 页面中又显示了一个文本框，可以输入其他待办事项
		# 他又输入了“use peacock feathers to make a fly”
		# 伊迪丝做事很有条理
		self.fail('Finish the test')	# 生成错误信息,用这个方法提醒测试结束了
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)

		# 页面再次更新，他的清单中显示了两个待办事项
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
		self.check_for_row_in_list_table('1: Buy peacock feathers')

		# 现在一个叫弗朗西斯的新用户访问了网站
		
		## 我们使用一个新的浏览器会话
		## 确保伊迪丝的信息不会从cookie中泄露出来
		self.browser.quit()
		self.browser = webdriver.Firefox()

		# 弗朗西斯访问首页
		# 页面中看不到伊迪丝的清单
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers`', page_text)
		self.assertNotIn('make a fly', page_text)

		# 弗朗西斯输入一个新待办事项，新建一个清单
		# 他不像伊迪丝那样兴趣盎然
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(keys.ENTER)

		# 弗朗西斯获得了他的唯一url
		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/lists/.+')
		slef.assertNotEqual(francis_list_url, edith_list_url)

		# 这个页面还是没有伊迪丝的清单
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotin('Buy peacock feathers', page_text)
		self.assertIn('Buy milk', page_text)

		# 两人都很满意，去睡觉了
		