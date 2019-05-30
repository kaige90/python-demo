from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def main():
    # 模拟登陆163邮箱
    driver = webdriver.Chrome()
    driver.get("http://mail.163.com/")
    # 用户名 密码
    loginDiv = driver.find_element_by_id("loginDiv")
    frame = loginDiv.find_element_by_tag_name("iframe")
    # 切入
    driver.switch_to.frame(frame)
    elem_user = driver.find_element_by_name("email")
    elem_user.send_keys("kaige90")
    elem_pwd = driver.find_element_by_name("password")
    elem_pwd.send_keys("********")
    elem_pwd.send_keys(Keys.RETURN)

    time.sleep(5)
    driver.close()
    driver.quit()


main()
