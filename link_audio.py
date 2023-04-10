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
#tìm nút play để kích vào
plays=soup.find_all("button", fdprocessedid="yji6")
#chạy từng nút play
for play in plays:
    play.click() #kích vào nút play
    Audio=soup.find("audio") #sau khi ấn nút play sẽ hiện ra thanh audio
    file_mp3=Audio['src'] #lấy đường dẫn của file audio
    print(file_mp3)
# Đóng trình duyệt
driver.quit()
