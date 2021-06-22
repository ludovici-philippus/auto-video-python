import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class ImageDownloader:
    def __init__(self, name):
        self.name = name
        self.op = webdriver.ChromeOptions()
        #self.op.add_argument("headless")
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=self.op)
        self.main()

    def go_to_site(self):
        self.driver.get(f"https://www.pexels.com/pt-br/procurar/{self.name}/?orientation=landscape")

    def select_the_first_image(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until((EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/article/a[1]/img'))))
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/article/a[1]/img")
        elem.click()

    def download_the_image(self):
        sleep(1)
        elem = self.driver.find_element_by_xpath('//*[@id="photo-modal"]/div[2]/div/div/section[2]/div/a/div/img')
        elem.screenshot(f'{self.name}.png')

    def main(self):
        self.go_to_site()
        self.select_the_first_image()
        self.download_the_image()
        self.driver.close()

if __name__ == "__main__.py":
    image = ImageDownloader('pleasure')
