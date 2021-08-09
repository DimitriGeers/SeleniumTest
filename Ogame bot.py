from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import datetime as dt

driver = webdriver.Chrome()
driver.get('https://lobby.ogame.gameforge.com/en_GB/hub')
driver.maximize_window()
time.sleep(3)

planet_1 = "https://s176-en.ogame.gameforge.com/game/index.php?page=ingame&component=supplies&cp=33643696"
planet_2 = "https://s176-en.ogame.gameforge.com/game/index.php?page=ingame&component=supplies&cp=33645455"
planet_3 = "https://s176-en.ogame.gameforge.com/game/index.php?page=ingame&component=supplies&cp=33647417"
planet_4 = "https://s176-en.ogame.gameforge.com/game/index.php?page=ingame&component=supplies&cp=33648154"
planet_5 = "https://s176-en.ogame.gameforge.com/game/index.php?page=ingame&component=supplies&cp=33650332"
planet_6 = "https://s176-en.ogame.gameforge.com/game/index.php?page=ingame&component=supplies&cp=33653192"
planet_7 = "https://s176-en.ogame.gameforge.com/game/index.php?page=ingame&component=supplies"
def login():
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/ul/li[1]/span").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/form/div[1]/div/input").send_keys("Put login here")
    time.sleep(0.5)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/form/div[2]/div/input").send_keys("Put password here")
    time.sleep(0.5)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/form/p/button[1]").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/a/button").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/section[1]/div[2]/div/div/div[1]/div[2]/div/div/div[11]/button").click()



def check_resource(resource="all"):
    resource_energy_stock = float(driver.find_element_by_id("resources_energy").text)
    try:
        resource_metal_stock = int(driver.find_element_by_id("resources_metal").text)*1000
        resource_crystal_stock = float(driver.find_element_by_id("resources_crystal").text)*1000
        resource_deuterium_stock = float(driver.find_element_by_id("resources_deuterium").text)*1000
        resource_darkmatter_stock = float(driver.find_element_by_id("resources_darkmatter").text)*1000
    except:
        pass

    try:
        if resource == "all":
            return [resource_metal_stock, resource_crystal_stock, resource_deuterium_stock, resource_darkmatter_stock, resource_energy_stock]
        elif resource == "metal":
            return resource_metal_stock
        elif resource == "crystal":
            return resource_crystal_stock
        elif resource == "deuterium":
            return resource_deuterium_stock
        elif resource == "darkmatter":
            return resource_darkmatter_stock
    except:
        pass

    if resource == "energy":
        return resource_energy_stock

def upgrade(planet=1):
    if planet == 1:
        driver.get(planet_1)
    elif planet == 2:
        driver.get(planet_2)
    elif planet == 3:
        driver.get(planet_3)
    elif planet == 4:
        driver.get(planet_4)
    elif planet == 5:
        driver.get(planet_5)
    elif planet == 6:
        driver.get(planet_6)
    elif planet == 7:
        driver.get(planet_7)
    else:
        driver.get("https://s176-en.ogame.gameforge.com/game/index.php?page=ingame&component=supplies")

    time.sleep(3)

    metal_mine = driver.find_element_by_css_selector("span[class='icon sprite sprite_medium medium metalMine']")
    crystal_mine = driver.find_element_by_css_selector("span[class='icon sprite sprite_medium medium crystalMine']")
    deuterium_mine = driver.find_element_by_css_selector("span[class='icon sprite sprite_medium medium deuteriumSynthesizer']")

    metal_storage = driver.find_element_by_css_selector("span[class='icon sprite sprite_small small metalStorage']")
    crystal_storage = driver.find_element_by_css_selector("span[class='icon sprite sprite_small small crystalStorage']")
    deuterium_storage = driver.find_element_by_css_selector("span[class='icon sprite sprite_small small deuteriumStorage']")

    solar_plant = driver.find_element_by_css_selector("span[class='icon sprite sprite_medium medium solarPlant']")
    fusion_reactor = driver.find_element_by_css_selector("span[class='icon sprite sprite_medium medium fusionPlant']")
    solar_sat = driver.find_element_by_css_selector("span[class='icon sprite sprite_medium medium solarSatellite']")


    metal_mine_level = int(driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div/div[2]/ul/li[1]/span/span/span[1]").text)
    crystal_mine_level = int(driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div/div[2]/ul/li[2]/span/span/span[1]").text)
    deuterium_mine_level = int(driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div/div[2]/ul/li[3]/span/span/span[1]").text)

    metal_storage_level = int(driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div/div[2]/ul/li[8]/span/span/span[1]").text)
    crystal_storage_level = int(driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div/div[2]/ul/li[9]/span/span/span[1]").text)
    deuterium_storage_level = int(driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div/div[2]/ul/li[10]/span/span/span[1]").text)

    solar_plant_level = int(driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div/div[2]/ul/li[4]/span/span/span[1]").text)
    fusion_reactor_level = int(driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div/div[2]/ul/li[5]/span/span/span[1]").text)

    if check_resource("energy") < 0:
        try:
            print("Energy low, trying to improve energy plants/sats on ", dt.datetime.now())
            if solar_plant_level <= 16:
                solar_plant.click()
                time.sleep(3)
            elif fusion_reactor_level <= 10:
                fusion_reactor.click()
                time.sleep(3)
            else:
                solar_sat.click()
                time.sleep(3)
                driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/input").send_keys("5")
                time.sleep(3)

            improve_button = driver.find_element_by_css_selector("span[class='tooltip']")
            time.sleep(5)
            if improve_button.text == "Improve":
                improve_button.click()
                print("Starting iprovement of energy source at", dt.datetime.now())
            elif improve_button.text == "Build":
                improve_button.click()
                print("Building sat at", dt.datetime.now())


        except:
            print("Unable to upgrade solar plant")

        finally:
            pass

    elif deuterium_mine_level <= metal_mine_level-6:

        try:
            print("Trying to upgrade deuterium plant on ", dt.datetime.now())
            deuterium_mine.click()
            time.sleep(5)
            improve_button = driver.find_element_by_css_selector("span[class='tooltip']")
            time.sleep(5)
            if improve_button.text == "Improve":
                improve_button.click()

        except:
            print("unable to upgrade deuterium mine")

        finally:
            pass

    elif crystal_mine_level <= metal_mine_level-4:
        try:
            print("Trying to upgrade crystal mine on ", dt.datetime.now())
            crystal_mine.click()
            time.sleep(5)
            improve_button = driver.find_element_by_css_selector("span[class='tooltip']")
            time.sleep(5)
            if improve_button.text == "Improve":
                improve_button.click()


        except:
            print("unable to upgrade crystal mine")

        finally:
            pass

    else:
        try:
            print("Trying to upgrade metal mine on ", dt.datetime.now())
            metal_mine.click()
            time.sleep(5)
            improve_button = driver.find_element_by_css_selector("span[class='tooltip']")
            time.sleep(5)
            if improve_button.text == "Improve":
                improve_button.click()

        except:
            print("unable to upgrade metal mine")

def main():
    while True:
            # print("Starting iprovement of planet 1 on ", dt.datetime.now())
            # upgrade(1)
            # print("Starting iprovement of planet 2 on ", dt.datetime.now())
            # upgrade(2)
            # print("Starting iprovement of planet 3 on ", dt.datetime.now())
            # upgrade(3)
            # print("Starting iprovement of planet 4 on ", dt.datetime.now())
            # upgrade(4)
            # print("Starting iprovement of planet 5 on ", dt.datetime.now())
            # upgrade(5)
            # print("Starting iprovement of planet 6 on ", dt.datetime.now())
            # upgrade(6)
            print("Starting iprovement of planet 7 on ", dt.datetime.now())
            upgrade(7)

login()
time.sleep(2)
main()
