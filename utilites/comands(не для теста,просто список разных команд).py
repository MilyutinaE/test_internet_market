import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# открытие браузера
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\Liza\\PycharmProjects\\pythonLessons\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/buttons'
driver.get(base_url)
driver.maximize_window()
time.sleep(2)
driver.close #закрыть

# КЛИКИ
from selenium.webdriver import ActionChains
action = ActionChains(driver)  #переменная экшен хранит в себе экземпляр класса акшнЧейнс, туда поместили экхемпляр драйвера хром
click = driver.find_element(By.XPATH, "//*[@id='doubleClickBtn']")
action.double_click(click).perform()  #сделать дабл клик по кнопке
action.context_click(click).perform() #нажать правой клавишей мыши

# ПЕРЕМЕЩЕНИЕ В БРАУЗЕРНЫХ КНОПКАХ
driver.back() # назад
driver.forward() # вперед
driver.refresh() # рефреш

# ПЕРЕМЕЩЕНИЕ К ЭЛЕМЕНТУ (КОТОРЫЙ ВНИЗУ)
action.move_to_element(click).perform()

# ПОЛЯ
click.send_keys("abebeb") # если поле инпут - вставится текст
click.clear() # очистить поле
value_click = click.text # получить значение поля

# СДЕЛАТЬ СКРИНШОТ
import datetime
now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S") #название скриншота будет уникальным по дате и времени
name_screenshot = 'screenshot' + now_date + '.png'
driver.save_screenshot('.\\screen\\' + name_screenshot)

# НАЖАТИЕ НА КЛАВЕ
from selenium.webdriver import Keys
click.send_keys(Keys.RETURN) # клавиша энтер
click.send_keys(Keys.BACKSPACE*10)  # стереть один символ или 10 символов
click.send_keys(Keys.PAGE_DOWN) # в самый низ открытого списка
click.send_keys(Keys.DOWN) # на один пункт вниз открытого списка
click.send_keys(Keys.CONTROL + "a") # выделить всю строку в инпуте и потом ее можно стереть

# XPATH
new_date = driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day--today')]") # XPATH contains

# получить следующий день
import datetime
now_date = datetime.datetime.utcnow().strftime("%d")
print(now_date)  # сегоднящнее число

now_date = datetime.datetime.now()
print(now_date)
now_10 = now_date+datetime.timedelta(days=10)  # прибавить 10 дней
print(now_10)

# хуй пойми что
now_date = datetime.datetime.now()
print("Сегодня = " + str(now_date))
now_10 = now_date+datetime.timedelta(days=10)
print("Сегодня плюс 10 дней = " + str(now_10))
now_10_date = now_10.date()
print("Сегодня плюс 10 дней без времени = " + str(now_10_date))
now_10_date_str = str(now_10_date.month) + "/" + str(now_10_date.day) +"/" + str(now_10_date.year)
print("Сегодня плюс 10 дней без времени в формате строки месяц/день/год= " + str(now_10_date_str))

# ПОЛЗУНОК на сайте https://html5css.ru/howto/howto_js_rangeslider.php
actions = ActionChains(driver) #переменная экшен хранит в себе экземпляр класса акшнЧейнс, туда поместили экхемпляр драйвера хром
polz =  driver.find_element(By.XPATH, "//*[@id='id1']")
actions.click_and_hold(polz).move_by_offset(20, 0).release().perform()
# Х по горизонтали, Y по вертикали. если -20, то тянет влево. release - отпускаем мышь, сохраняем - сохраняем то, что сделали

# EXCEPTIONS
from selenium.common import NoSuchElementException
try:
    visible_after_button = driver.find_element(By.XPATH, "//*[@id='visibleAfter']")
    visible_after_button.click()
except NoSuchElementException as exception: #или except AssertionError as exception
    print("NoSuchElementException exception")

# ОЖИДАНИЕ
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.implicitly_wait(10) # на каждое действие будет ждать 10сек пока элемент не появится в DOMe. пишем один раз, далее на каждый клик ждет. неявное ожидание
# явное - для отдельного элемента. например визибл или кликабл
visible_button = WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='visibleAfter']")))
visible_button.click()

# ВЛОЖЕННЫЙ СЛОВАРЬ
dic = [
   {
      'id': 1,
      'name': 'Sauce Labs Backpack',
      'price': driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div"),
      'add_to_cart': driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
   },
   {
      'id': 2,
      'name': 'Sauce Labs Bike Light',
      'price': driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div"),
      'add_to_cart': driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']")
   }]
product = input() #выбираем продукт с клавы
print(product)
id = int(product) - 1  #доступ к dic[0], dic[1]
name_p = dic[id]
print("Вы выбрали " + str(name_p['name']))
price_p = name_p['price'].text
print("Товар стоит " + str(price_p))
name_p['add_to_cart'].click()
cart = driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']")
cart.click()
print("Товар добавляется в корзину и открывается страница корзины")

# ДАННЫЕ ПОСЛЕ СИМВОЛОВ
value_price_2 = "$15.55"
price2_float = float(value_price_2.partition('$')[2]) # получить символы после $
f[::-1].find('.') # получить колиество(инт) символов после . f - строка

# ЗАПУСТИТЬ ТЕСТ ИЗ ТЕРМИНАЛА - открыть терминал и в нем ввести
# python -m pytest -s -v
# python -m pytest -v   -отображает passed с процентами
#  python -m pytest -s -отображает passed с выводом принтов из теста. без процентов
# python -m pytest -s sstest_mail.py  -запускает один выбранный тест

# ПОРЯДОК ВЫПОЛНЕНИЯ ТЕСТОВ
import pytest
@pytest.mark.run(order=1)  # писать перед def test_buy_product_2():

# запуск python -m pytest -s -v test_buy_product.py
# Запуск отдельного тестового метода из файла. писать в терминале
# python -m pytest -s -v -k test_buy_product_3

# ФИКСТУРЫ
@pytest.fixture()
def set_up():
    print("Start test (fixture)") # перед каждым тестом
    yield
    print("Finish test (fixture)")


@pytest.fixture(scope="module") # фикстура под модуль. пишется до запуска самого первого теста. можно вписать в один тест, будет использоваться ко всем в файле
#  По факту, set group можно разместить только в первом тесте и тогда сообщение "Enter system" появится в начале 1ого теста, а "Exit system" в конце последнего теста в файле
def set_group():
    print("Enter system")
    yield
    print("Exit system")
