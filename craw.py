from selenium import webdriver
import time
import openpyxl
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd


music_data = []
# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()

# Đi tới trang
driver.get("https://pixabay.com/vi/music/")
time.sleep(5)
# Lấy mã HTML của trang hiện tại
html = driver.page_source

# Phân tích cú pháp HTML
soup = BeautifulSoup(html, "html.parser")
audios = soup.find_all("div",class_="main--4+PDC")
while True:
    
    for audio in audios:
        name = audio.find("a",class_="name--q8l1g").text.strip()
        artist = audio.find("a", class_="artist--VkDWG").text.strip()
        time = audio.find("span").text.strip()
        #time = pd.to_datetime(time_str, format='%M:%S').time()
        #link=audio['href']

        # thêm thông tin vào list
        music_data.append({
            "Title": name,
            "Artist": artist,
            "Time":time,
            #"Link":link
        })
        print(name,artist,time)
    load_more_button = driver.find_element(By.CSS_SELECTOR,"a.discoverMoreButton--PZSrF")
    if load_more_button:
        load_more_button.click()
        time.sleep(5)
    if not load_more_button:
        break
# Tạo dataframe từ dữ liệu
df = pd.DataFrame(music_data)

# Lưu dataframe vào file Excel
df.to_excel('music_data.xlsx', index=False)

# Đóng trình duyệt
driver.quit()
