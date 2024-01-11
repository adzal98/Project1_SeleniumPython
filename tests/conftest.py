import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service



# Putem alege in ce browser sa ruleze testele noastre, alegand din terminal:
# py.test --select_browser chrome
# !!!Aceasta metoda nu functioneaza cu DriverManager, trebuie sa avem chromedriver-ul local!!!
def pytest_addoption(parser):
    parser.addoption("--select_browser", action="store", default="chrome")

# Acest fixture se poate aplica unei clase
# Initializeaza browser-ul
@pytest.fixture(scope="class")
def setup_browser(request):
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)  # Pastreaza fereastra deschisa
    select_browser = request.config.getoption("select_browser")

    if select_browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)  # Pastreaza fereastra deschisa
        driver = webdriver.Chrome(service=Service(r"D:\Python\Chrome Driver\chromedriver.exe"), options=options)

    elif select_browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference("detach", True)  # Pastreaza fereastra deschisa, DIFERIT fata de chrome si edge

        driver = webdriver.Firefox(service=Service(r"D:\Python\Firefox Driver\geckodriver.exe"), options=options)
    elif select_browser == "edge":
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)  # Pastreaza fereastra deschisa
        driver = webdriver.Edge(service=Service(r"D:\Python\Firefox Driver\msedgedriver.exe"), options=options)
    driver.get("https://magento.softwaretestingboard.com/")
    request.cls.driver = driver  # Se foloseste pentru a importa driver-ul in teste
