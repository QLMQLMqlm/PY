import time
# import datetime
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
normal_login_username.send_keys("钱立民扫码")
normal_login_password.clear()
normal_login_password.send_keys("test2022jizhi")
login_btn = driver.find_element(By.XPATH,
                                "//*[@id='root']/div/section/section/main/div/div/div[2]/form/div[""3]/"
                                "div/div/span/button/span")
driver.execute_script("arguments[0].click();", login_btn)
time.sleep(3)
switchover = driver.find_element(By.XPATH, "/html/body/div/div/section/div/section/header/div")
switchover.click()  # 登录与切换菜单！！！！！
deal_subscript = driver.find_element(By.XPATH, "/html/body/div/div/section/div/section/main/div[1]/ul/li["
                                               "2]/div/span/span[1]")
deal_subscript.click()
time.sleep(2)
deal_my = driver.find_element(By.XPATH, "/html/body/div/div/section/div/section/main/div[1]/ul/li[2]/ul/li[2]/span[1]")
deal_my.click()
time.sleep(3)
create_deal = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div/div[1]/"
                                            "div[1]/div[2]/button")
create_deal.click()
time.sleep(2)
deal_name = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div[2]/div"
                                          "/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/div[2]/div/div/input") \
    .send_keys("主管权限-002")
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
    .send_keys("主管权限-002")
manager_list = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                             "2]/div/div[1]/div[6]/div[2]/div[1]/div[1]/div/div[2]/div/div["
                                             "2]/div/div/div")
manager_list.click()
#   Select(manager_list).select_by_visible_text("投资经理2")    #  selenium.common.exceptions.UnexpectedTagName
#   Exception: Message: Select only works on <select> elements, not on <div>
time.sleep(1)
manager_list.send_keys(Keys.DOWN)
manager_list.send_keys(Keys.DOWN)
manager_list.send_keys(Keys.DOWN)
manager_list.send_keys(Keys.DOWN)
manager_list.send_keys(Keys.DOWN)
manager_list.send_keys(Keys.DOWN)
manager_list.send_keys(Keys.DOWN)
manager_list.send_keys(Keys.DOWN)
time.sleep(1)
manager_list.send_keys(Keys.ENTER)
time.sleep(1)
submit_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                              "2]/div/div[2]/div/div/div/button")
submit_button.click()
time.sleep(3)
ok_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button")
ok_button.click()  # 创建deal完毕
time.sleep(2)
Deal_Info = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div["
                                          "2]/span/span/a")
driver.execute_script("arguments[0].click();", Deal_Info)  # 创建deal之后直接进入deal基本信息
time.sleep(6)
windows = driver.window_handles  # 打开所有窗口。   注意需要在新的窗口操作是需要切换窗口滴！！！
driver.switch_to.window(windows[-1])  # 切换到最新打开的窗口
time.sleep(2)
Create_Conference1 = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div["
                                                   "2]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]")
Create_Conference1.click()  # 点击新建会议
time.sleep(1)
Create_Conference2 = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div[2]"
                                                   "/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div"
                                                   "/div/div/div/div[1]/div")
Create_Conference2.click()  # 点击新建会议下一步  ”项目全图/会议纪要“
time.sleep(1)
Conference_Type = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div["
                                                "3]/div/div")
Conference_Type.click()
time.sleep(1)
Conference_Type.send_keys(Keys.ENTER)  # 会议类型是项目全图
time.sleep(1)
Conference_Time = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[3]/div/div[1]/div["
                                                "3]/span/div/input")
Conference_Time.click()
time.sleep(1)
Conference_Time1 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div[2]/div[3]/span/a")
Conference_Time1.click()  # 会议时间默认都为“今天”
time.sleep(1)
Conference_Modality = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                    "/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div["
                                                    "3]/div/div[2]/div[3]/div/div")
Conference_Modality.click()
Conference_Modality.send_keys(Keys.DOWN)
Conference_Modality.send_keys(Keys.DOWN)
Conference_Modality.send_keys(Keys.ENTER)  # 会议形式为“电话会”
time.sleep(1)
Click_Create_Conference = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                        "/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[3]/button[2]")
Click_Create_Conference.click()
time.sleep(3)
Ok_Button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button")
Ok_Button.click()  # 创建会议完毕点击OK弹框
time.sleep(6)
Memo_Garde = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]"
                                           "/div[3]/div[1]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div[2]"
                                           "/div[2]/div")
Memo_Garde.click()
time.sleep(1)
Memo_Garde.send_keys(Keys.DOWN)
Memo_Garde.send_keys(Keys.ENTER)  # 默认主导人一人参会，并且评级为A+
time.sleep(1)
Ok_Button2 = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[2]")
Ok_Button2.click()
time.sleep(8)  # 默认主导人一人参会，并且评级为A+, 二次确认弹框
Edit_Memo = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div["
                                          "3]/div[1]/div[2]/div/div[3]/div/div/div[2]/div/div/div/div[1]/button")
time.sleep(2)
Edit_Memo.click()
time.sleep(5)  # 点击项目全图编辑按钮
Core_Business = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]"
                                              "/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[3]/div[3]/div/div[1]"
                                              "/div/div[2]/div[3]/div/div/div/div[2]/div[1]")
# driver.execute_script("arguments[0].scrollIntoView(true)", Core_Business)  # 定位到元素与页面顶部对齐
time.sleep(1)
Core_Business.click()
time.sleep(1)
Core_Business.send_keys("核心业务：智能工业控制领域的安卓系统（程炎备注：项目方的比喻可能不太精准，我会在下文的解释中给出原因）这里采用类比的"
                        "方法解释崧智具体在做什么：设想自己家是一个工厂，家中有很多的智能硬件，比如摄像头、温度计、扫地机器人等等。这些硬件可"
                        "以通过用户的手机进行控制。比如家中的小米摄像头检测到地面脏了，于是将指令发送到手机上的小米APP上。小米APP通过手机系"
                        "统调用了科沃斯的APP，科沃斯的APP就下达指令给科沃斯扫地机器人，指挥机器人扫地。这样就完成了一个自动化的任务。以这个"
                        "场景类比工厂的场景，用户的手机类比一台工业计算机。小米摄像头、科沃斯机器人类比是工业视觉、工业机器人。手机上小米app"
                        "、科沃斯app类比为不同工业设备的控制app（叫做控制系统）。手机上的安卓系统类比为工业计算机的底层系统（这个底层系统一"
                        "般是windows或者linux）")
time.sleep(1)  # 选中核心业务并输入

Save_Button = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]"
                                            "/div[3]/div[1]/div[2]/div/div[3]/div/div/div[2]/div/div/div/div[1]"
                                            "/div[2]/button[2]")
time.sleep(2)
Save_Button.click()
# driver.close()
# driver.quit()
