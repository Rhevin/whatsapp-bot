from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('/home/rhevin/Downloads/chromedriver')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

with open("contact.txt") as f:
	for line in f:
		inp_xpath_search = "//input[@title='Search or start new chat']"
		input_box_search = wait.until(EC.presence_of_element_located((
			By.XPATH, inp_xpath_search)))
		try:
			name = (line.rstrip('\n'))
			var = name.split("/")
			text = """Hello {},
                        Selamat sore, kami informasikan hosting Anda {} saat ini dalam status "suspended" karena belum melakukan perpanjangan. Hal ini menyebabkan website Anda tidak bisa diakses sehingga berpotensi menurunnya pengunjung ataupun calon pembeli Anda. Berikut detail layanan Anda yang sudah saatnya diperpanjang
                        No invoice : NH{}
                        Akun hosting : NH{}
                        Jumlah tagihan : {}
                        Silakan balas pesan ini untuk informasi lebih lanjut.""".format(var[1], var[3], var[2], var[3], var[4])
			input_box_search.send_keys(var[0])
			time.sleep(10)
			
			emoji = driver.find_element_by_class_name('chat')
			
			if emoji:
				input_box_search.send_keys(Keys.ENTER)
				x_arg_contact = '//div[@class="chat-title"]'
				input_box_contact = wait.until(EC.presence_of_element_located((
					By.XPATH, x_arg_contact)))

				time.sleep(2)
				inp_xpath = "//div[@contenteditable='true']"
				input_box = wait.until(EC.presence_of_element_located((
					By.XPATH, inp_xpath)))
				input_box.send_keys(text + Keys.ENTER)

			time.sleep(5)
			print("send")
		except:
			input_box_search.send_keys(Keys.BACKSPACE * 20)
			time.sleep(5)
			print("error")
