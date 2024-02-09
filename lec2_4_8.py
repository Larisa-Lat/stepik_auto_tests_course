from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12 * math.sin(x))))

try:
	# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
	browser = webdriver.Chrome()
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser.get(link)
	
	# неявное ожидание
	browser.implicitly_wait(5)

	# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
	WebDriverWait(browser, 12).until(
        	EC.text_to_be_present_in_element((By.ID, "price"), "100")
	)

	# Нажать на кнопку "Book"
	browser.find_element(By.ID, "book").click()

	# Считать значение для переменной x.
	get_x = browser.find_element(By.ID, "input_value")
	browser.execute_script("return arguments[0].scrollIntoView(true);", get_x)
	x = int(get_x.text)
	# Посчитать математическую функцию от x.
	y = calc(x)

	# Проскроллить страницу вниз.
	input = browser.find_element(By.TAG_NAME, "input")
	browser.execute_script("return arguments[0].scrollIntoView(true);", input)
	input.send_keys(y)

	# Нажать на кнопку "Submit".
	button = browser.find_element(By.ID, "solve")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	button.click()

except Exception as error:
	print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
	time.sleep(120)
	browser.quit()
