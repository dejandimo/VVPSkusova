from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Настройка на драйвъра0
driver = webdriver.Chrome()  # Увери се, че chromedriver е в PATH

# Отваря страницата
driver.get(r"C:/Users/Dell/PycharmProjects/pythonProject2/Polet.html")  # Увери се, че използваш правилния път

# Функция за мануално въвеждане на град и дата, с автоматично изпълнение на останалите действия
def manual_input_and_test():
    # Ръчно въвеждане на град и дата
    city = input("Въведете град (например 'София'): ")  # Попитай потребителя за град
    date = input("Въведете дата (например '2025-05-20'): ")  # Попитай потребителя за дата

    # Попълни полетата за град и дата с въведените стойности
    city_input = driver.find_element(By.ID, "city")
    city_input.clear()  # Изчистваме предишния текст
    city_input.send_keys(city)  # Въвеждаме град

    date_input = driver.find_element(By.ID, "date")
    date_input.clear()  # Изчистваме предишната дата
    date_input.send_keys(date)  # Въвеждаме дата

    # Изчакваме малко време за обработка на въведената информация
    time.sleep(1)

    # Натискаме бутона за търсене
    search_button = driver.find_element(By.ID, "search-button")
    search_button.click()

    # Изчакваме да се заредят резултатите
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "results"))
    )

    # Вземаме резултатите от търсенето
    results = driver.find_element(By.ID, "results").text
    print(f"Резултати: {results}")

    # Проверка дали въведената дата и град се съдържат в резултатите
    if city in results and date in results:
        print(f"Тестът с дата {date} и град {city} премина успешно!")
    else:
        print(f"Тестът не премина. Резултати: {results}")

# Извикваме функцията за мануално тестване
manual_input_and_test()

# Затвори браузъра
driver.quit()
