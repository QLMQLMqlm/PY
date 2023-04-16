import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

#   driver = webdriver.Edge(executable_path="E:\\study\\webdriver\\msedgedriver.exe")
s = Service(executable_path="E:\\study\\webdriver\\msedgedriver.exe")
driver = webdriver.Edge(service=s)  # 找到msedgedriver
driver.maximize_window()
driver.get("https://test-www.skyviewfund.com/login2")
normal_login_username = driver.find_element(By.ID, "normal_login_username")
normal_login_password = driver.find_element(By.ID, "normal_login_password")
normal_login_username.clear()
normal_login_username.send_keys("投资经理")
normal_login_password.clear()
normal_login_password.send_keys("test2022jizhi")
login_btn = driver.find_element(By.XPATH,
                                "//*[@id='root']/div/section/section/main/div/div/div[2]/form/div[""3]/"
                                "div/div/span/button/span")
driver.execute_script("arguments[0].click();", login_btn)
time.sleep(3)
switchover = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div/section/footer/div/span/div")
switchover.click()
deal_subscript = driver.find_element(By.XPATH, "/html/body/div/div/section/div/section/main/div/div/div/ul/li[3]/div")
deal_subscript.click()
time.sleep(2)
deal_my = driver.find_element(By.XPATH, "/html/body/div/div/section/div/section/main/div/div/div/ul/li[3]/ul/li[2]")
deal_my.click()
time.sleep(3)
create_deal = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div/div[1]/"
                                            "div[1]/div[2]/button")
create_deal.click()
time.sleep(2)
deal_name = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div[2]/div"
                                          "/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/div[2]/div/div/input") \
    .send_keys("复杂批注-005")
time.sleep(1)
referrer = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div[2]/div/div[1]"
                                         "/div[1]/div[2]/div[1]/div[3]/div/div[3]/div/div[2]/div/div/input") \
    .send_keys("牛马一号")
time.sleep(1)
project_tag = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                            "/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[4]/div/div/div[2]"
                                            "/div/div/div/div/ul/li/div/input") \
    .send_keys("牛马")
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                              "/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[4]/div/div/div[2]"
                              "/div/div/div/div/ul/li/div/input").send_keys(Keys.ENTER)
time.sleep(1)
business_model_tag = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                   "/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[6]/div/div/div["
                                                   "2]/div/div/div/div/ul/li/div/input") \
    .send_keys("牛马")
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div/div[1]/div["
                              "1]/div[2]/div[1]/div[6]/div/div/div[2]/div/div/div/div/ul/li/div/input") \
    .send_keys(Keys.ENTER)
time.sleep(1)
founder = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div[2]"
                                        "/div/div[1]/div[3]/div[2]/div[1]/div[1]/div/div[1]/div/div[2]/div/div/input") \
    .send_keys("复杂批注-005")
driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div[2]"
                              "/div/div[1]/div[3]/div[2]/div[1]/div[1]/div/div[1]/div/div[2]/div/div/input") \
    .send_keys(Keys.ENTER)
time.sleep(1)
manager_list = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                             "2]/div/div[1]/div[6]/div[2]/div[1]/div[1]/div/div[2]/div/div["
                                             "2]/div/div/div")
manager_list.click()
#   Select(manager_list).select_by_visible_text("投资经理2")    #  selenium.common.exceptions.UnexpectedTagName
#   Exception: Message: Select only works on <select> elements, not on <div>
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                              "2]/div/div[1]/div[6]/div[2]/div[1]/div[1]/div/div[2]/div/div["
                              "2]/div/div/div") \
    .send_keys(Keys.ENTER)  # 默认主导人为管理员！！！！
submit_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                              "2]/div/div[2]/div/div/div/button")
submit_button.click()
time.sleep(2)
ok_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button")
ok_button.click()
my_deal = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                        "3]/div/button[2]")
my_deal.click()
