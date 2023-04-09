from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()
driver.get("https://pixabay.com/vi/music/")
# Tạm dừng 5 giây để trang tải và hiển thị kết quả
time.sleep(5)
# Lấy mã HTML của trang hiện tại
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
audios = soup.find_all("audio")
for audio in audios:
    audio_src = audio['src']
    print(audio_src)
# Đóng trình duyệt
driver.quit()
