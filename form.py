from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def start_browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('https://forms.gle/rKfhMRdiE7qRjMK38')
    browser.maximize_window()
    sleep(3)
    return browser


# Preenche o nome
def fill_name(browser, name):
    browser.find_element_by_xpath(
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(name)

# Preenche o e-mail


def fill_email(browser, email):
    browser.find_element_by_xpath(
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(email)

# preenche a fonte de venda


def fill_source(browser, source):

    if source == "Atacado":
        option = 1
    else:
        option = 2

    xpath_source = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[{option}]/label/div/div[2]/div/span"
    browser.find_element_by_xpath(xpath_source).click()

# preenche as categorias


def fill_category(browser, categories):
    # categories = "Camisa, Calça, Roupas Íntimas"
    category_list = categories.split(", ")

    for category in category_list:
        if category == "Camisa":
            option = 1
        elif category == "Calça":
            option = 2
        elif category == "Vestido":
            option = 3
        else:
            option = 4

        xpath_source = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[{option}]/label/div/div[2]/div/span"
        browser.find_element_by_xpath(xpath_source).click()


# Preenche tipo da conta
def fill_customer_type(browser, customer_type):
    xpath_type = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]"

    # customer_type = "Cadastrado"

    if customer_type == "Não Cadastrado":
        option = 3
    elif customer_type == "Cadastrado":
        option = 4
    elif customer_type == "Cliente Regular":
        option = 5
    else:
        option = 6

    xpath_customer_type = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[{option}]/span"
    browser.find_element_by_xpath(xpath_type).click()
    sleep(1)
    browser.find_element_by_xpath(xpath_customer_type).click()


# Preenche a nota
def fill_rating(browser, rating):
    # rating = 3

    xpath_rating = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[{rating}]/div[2]/div/div/div[3]/div"
    browser.find_element_by_xpath(xpath_rating).click()

# Envia o formulario


def send_form(browser):
    button_xpath = "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span"
    browser.find_element_by_xpath(button_xpath).click()


def fill_form():
    browser = start_browser()
    fill_name(browser, "Daniel Fujtia")
    fill_email(browser, "teste@teste.com")
    fill_source(browser, "Atacado")
    fill_category(browser, "Camisa, Calça, Roupas Íntimas")
    sleep(2)
    fill_customer_type(browser, "Cadastrado")
    sleep(2)
    fill_rating(browser, 3)
    sleep(2)
    # send_form(browser)
