from selenium.webdriver.common.by import By


class PostStatus:

    def __init__(self,driver):
        self.driver = driver

    create = (By.XPATH,"//div[@aria-label='Create']")
    post_link = (By.XPATH,"(//div[@data-visualcompletion = 'ignore-dynamic'])[1]")
    text = (By.XPATH,"(//div[@class = '_1mf _1mj'])[2]")
    post = (By.XPATH,"//div[@aria-label = 'Post']")

    def create_button(self):
        return self.driver.find_element(*PostStatus.create)

    def post_link_tab(self):
        return self.driver.find_element(*PostStatus.post_link)

    def enter_text(self):
        return self.driver.find_element(*PostStatus.text)

    def post_button(self):
        return self.driver.find_element(*PostStatus.post)