from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
time.sleep(3)

def login():

    driver.get("https://www.playinitium.com/")
    time.sleep(5)
    driver.find_element_by_class_name("login-signup-switch").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[3]/div/form/div[1]/input").send_keys("Enter login here")
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[3]/div/form/div[2]/input").send_keys("Enter password here")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[3]/div/form/div[3]/a").click()
    time.sleep(7)
def get_ui_info(request):

    if request == "health_current":
        hp = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div/div/div/div[6]/div/div[1]/div/p').text
        hp = hp.split("/")
        return float(hp[0])
    elif request == "health_max":
        hp = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div/div/div/div[6]/div/div[1]/div/p').text
        hp = hp.split("/")
        return float(hp[1])
    elif request == "location":
        location = driver.find_element_by_id("locationName").text
        return location

    elif request == "enemy_hp":
        try:
            enemy_hp = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div/div/div/div[7]/div/div[1]/div/p").text
            enemy_hp = enemy_hp.split("/")
            return int(enemy_hp[0])
        except:
            return None
def get_next_destination(destination):
    print("looking for:", destination)
    current_location = get_ui_info('location')
    location_high_road = ["Aera inn", "Aera", "North West Hills", "The Fork", "High Road", "High Road: Swampland"]

    if destination == "Aera Inn":
        if current_location == "Aera":
            go_to_location("Aera Inn")

        else:
            index = location_high_road.index(current_location)
            return location_high_road[index - 1]


    if destination == "High Road: Swampland":
        if current_location == "Aera Inn":
            return "North West Hills"

        else:
            index = location_high_road.index(current_location)
            return location_high_road[index+1]

def go_to_location(destination):
    print("Trying to go to location:", destination)
    try:

        location_labels = driver.find_elements_by_class_name("label")
        indoor_locations = driver.find_elements_by_class_name("path-overlay-link")

        for location in location_labels:
            if location.text == destination:
                location.click()

        for location in indoor_locations:
            if location.text == destination:
                location.click()

    except:
        pass
def fight():
    tags = driver.find_elements_by_tag_name("a")

    if get_ui_info("enemy_hp") != None:
        if get_ui_info("health_current") < get_ui_info("health_max")*0.50:
            actions = ActionChains(driver)
            actions.send_keys("3")
            actions.perform()
            time.sleep(1)
            main()

        try:
            if get_ui_info("enemy_hp") > 0:
                actions = ActionChains(driver)
                actions.send_keys("1")
                actions.perform()
                time.sleep(1)
        except:
            pass

    try:
        for tag in tags:
            if "Show loot" in tag.text:
                try:
                    tag.click()
                except:
                    pass
            if "Collect 0 gold" in tag.text:
                actions = ActionChains(driver)
                actions.send_keys("w")
                actions.perform()
                time.sleep(12)
                break

            if "Collect" in tag.text:
                tag.click()

    except:
        pass
def experiment():
    tags = driver.find_elements_by_tag_name("a")

    for tag in tags:
        if tag.text == "Begin Experiments":
            tag.click()
            break

    time.sleep(5)
def main():
    if "Combat" in get_ui_info("location"):
        fight()

    while get_ui_info("health_current") > get_ui_info("health_max")*0.60:
        if "Combat" in get_ui_info("location"):
            fight()

        else:
            current_location = get_ui_info('location')

            if current_location == "High Road: Swampland":
                actions = ActionChains(driver)
                actions.send_keys("w")
                print("Exploring the ", current_location)
                actions.perform()
                time.sleep(30)

            else:
                go_to_location(get_next_destination("High Road: Swampland"))
                time.sleep(10)




    if get_ui_info("health_current") < get_ui_info("health_max")*0.60:
        current_location = get_ui_info('location')

        if current_location == "Aera Inn":
            go_to_location("Rest")
            time.sleep(40)
        else:
            go_to_location(get_next_destination("Aera Inn"))
            time.sleep(10)

login()
while keyboard.is_pressed('q') == False:
    main()
















