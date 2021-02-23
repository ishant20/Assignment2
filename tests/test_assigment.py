import time

import pytest

from PageObject.LoginPage import LoginPage
from PageObject.PostStatus import PostStatus

@pytest.mark.usefixtures("setup")
class Testassignment:
    def test_post(self,getData):
        # Login Page
        login_page = LoginPage(self.driver)
        login_page.user_name().send_keys(getData[0])
        login_page.user_password().send_keys(getData[1])
        login_page.login_button().click()

        # Post Status
        post_status = PostStatus(self.driver)
        post_status.create_button().click()
        time.sleep(2)
        post_status.post_link_tab().click()
        time.sleep(3)
        post_status.enter_text().send_keys("Hello World")
        time.sleep(2)
        post_status.post_button().click()


    @pytest.fixture(params = [("userName","password")])
    def getData(self,request):
        return request.param