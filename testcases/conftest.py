import pytest as pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class", autouse=True)
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.yatra.com/")
    driver.maximize_window()

    # disponibiliza los objetos que se instancian para la clase que llama al fixture
    request.cls.driver = driver

    yield
    driver.close()


