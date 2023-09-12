from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
# 1. Khai báo browser
browser = webdriver.Chrome()#"./chromedriver_mac_arm64/chromedriver")

# 2. Mở URL của post
browser.get("https://www.youtube.com/watch?v=3HCUG4Ux0tA")
sleep(1)

for i in range(0,50):
    print(i)
    browser.execute_script("window.scrollTo(0, {});".format((i+1)*500))
    sleep(2)

comment_box = browser.find_element(By.ID, value="contents")
# print(comment_box)

comments = comment_box.find_elements(By.TAG_NAME, value="ytd-comment-thread-renderer")
comments_list = []
for comment in comments:
    # print(comment)
    author_text = comment.find_element(By.ID, value="author-text")
    print(author_text.text)
    content_text = comment.find_element(By.ID, value="content-text")
    print(content_text.text)
    content_text = content_text.text.replace("\r","")
    content_text = content_text.replace("\n", "")
    comments_list.append({"name":author_text.text,"comment":content_text})

df = pd.DataFrame(comments_list)
df.to_csv("a.csv",encoding="utf-8")