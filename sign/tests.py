from django.test import TestCase
from sign.models import Event,Guest
from django.contrib.auth.models import User

# '''测试模型'''
# class ModelTest(TestCase):
#     def setUp(self):
#         Event.objects.create(id=1,name="华为发布会",status=True,limit=2000,address='xian',start_time='2018-12-31 10:00:00')
#         Guest.objects.create(id=1,event_id=1,realname='张三',phone='13892561289',email='zhangsan@163.com',sign=False)
#
#     def test_event_models(self):
#         result = Event.objects.get(name="华为发布会")
#         self.assertEqual(result.address,"xian")
#         self.assertTrue(result.status)
#
#     def test_guest_models(self):
#         result = Guest.objects.get(phone='13892561289')
#         self.assertEqual(result.realname,'张三')
#         self.assertFalse(result.sign)
#
# '''测试index登录首页'''
# class IndexPageTest(TestCase):
#     def test_index_page_renders_index_template(self):
#         response = self.client.get('/index/')
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed(response,'index.html')

'''测试登录动作'''
class LoginActionTest(TestCase):
    def setUp(self):
        User.objects.create_user('test','test@qq.com','test123456')

    '''测试添加用户'''
    def test_add_admin(self):
        user = User.objects.get(username="test")
        self.assertEqual(user.username,"test")
        self.assertEqual(user.email,'test@qq.com')

    '''用户名密码为空'''
    def test_login_action_username_password_null(self):
        test_data = {'username':'','password':''}
        response = self.client.post('/login_action/',data=test_data)
        self.assertEqual(response.status_code,200)
        self.assertIn(b"username or password error!",response.content)

    '''用户名或密码错误'''
    def test_login_action_username_password_error(self):
        test_data = {'username':'abc','password':'123'}
        response = self.client.post('/login_action/',data=test_data)
        self.assertEqual(response.status_code,200)
        self.assertIn(b"username or password error!",response.content)

    def test_login_action_success(self):
        test_data = {'username':'test','password':'test123456'}
        response = self.client.post('/login_action/',data=test_data)
        self.assertEqual(response.status_code,302)