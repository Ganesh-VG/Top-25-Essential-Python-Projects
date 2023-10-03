from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver = Service("<YOUR CHROMEDRIVER.EXE FILE PATH>")
driver = webdriver.Chrome(service=chrome_driver, options=chrome_options)


def score():

    clicker = driver.find_element(By.CSS_SELECTOR, value="#buyCursor b")
    cl = clicker.text
    clicker_no = (int(cl.rsplit()[2].strip()))

    grand = driver.find_element(By.CSS_SELECTOR, value="#buyGrandma b")
    gr = grand.text
    grand_no = (int(gr.rsplit()[2].strip()))

    facto = driver.find_element(By.CSS_SELECTOR, value="#buyFactory b")
    fa = facto.text
    facto_no = (int(fa.rsplit()[2].strip()))

    miner = driver.find_element(By.CSS_SELECTOR, value="#buyMine b")
    mi = miner.text
    miner_no = (mi.rsplit()[2].strip())
    miner_no = int(miner_no.replace(",", ""))

    ship = driver.find_element(By.CSS_SELECTOR, value="#buyShipment b")
    sh = ship.text
    ship_no = (sh.rsplit()[2].strip())
    ship_no = int(ship_no.replace(",", ""))

    alchemy = driver.find_element(By.ID, value="buyAlchemy lab")
    al = alchemy.text
    alchemy_no = (al.rsplit()[3].strip())
    alchemy_no = int(alchemy_no.replace(",", ""))

    port = driver.find_element(By.CSS_SELECTOR, value="#buyPortal b")
    po = port.text
    port_no = (po.rsplit()[2].strip())
    port_no = int(port_no.replace(",", ""))

    timee = driver.find_element(By.ID, value="buyTime machine")
    ti = timee.text
    time_no = (ti.rsplit()[3].strip())
    time_no = int(time_no.replace(",", ""))

    money = driver.find_element(By.ID, value="money")
    money_no = money.text.strip()

    if "," in money_no:
        money_no = int(money_no.replace(",", ""))
    else:
        money_no = int(money_no)

    if clicker_no < money_no:
        cursor = driver.find_element(By.ID, value="buyCursor")
        cursor.click()
    elif grand_no < money_no:
        grandma = driver.find_element(By.ID, value="buyGrandma")
        grandma.click()
    elif facto_no < money_no:
        factory = driver.find_element(By.ID, value="buyFactory")
        factory.click()
    elif miner_no < money_no:
        mine = driver.find_element(By.ID, value="buyMine")
        mine.click()
    elif ship_no < money_no:
        shipment = driver.find_element(By.ID, value="buyShipment")
        shipment.click()
    elif alchemy_no < money_no:
        alchemy_lab = driver.find_element(By.ID, value="buyAlchemy lab")
        alchemy_lab.click()
    elif port_no < money_no:
        portal = driver.find_element(By.ID, value="buyPortal")
        portal.click()
    elif time_no < money_no:
        time_machine = driver.find_element(By.ID, value="buyTime machine")
        time_machine.click()


driver.get("http://orteil.dashnet.org/experiments/cookie/")

a = 0
click = True
while click:
    time.sleep(0.01)
    a += 1
    if a > 15:
        score()
        a = 0
    else:
        cookies = driver.find_element(By.ID, value="cookie")
        cookies.click()
