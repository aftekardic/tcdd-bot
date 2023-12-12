import custom_tools
import XPATHS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import chromedriver_autoinstaller

from time import sleep
from datetime import datetime
import re
import sys

ct = custom_tools.Tools


class RPA():
    def __init__(self, _from=None, _to=None, _departure_date=None, _clock_start=None, _clock_end=None, _exist_business=None):
        self._from = _from
        self._to = _to
        self._departure_date = _departure_date
        self._clock_start = datetime.strptime(_clock_start, '%H:%M').time()
        self._clock_end = datetime.strptime(_clock_end, '%H:%M').time()
        self._exist_business = _exist_business.lower() == "true"

        if ct.getOsName() == "Windows" or ct.getOsName() == "Linux":
            chromedriver_autoinstaller.install()
            self.driver = webdriver.Chrome()
            self.driver.fullscreen_window()

        else:
            self.driver = webdriver.Safari()
            self.driver.fullscreen_window()

        self.action_chains = ActionChains(self.driver)

        self.driver.get(
            "https://ebilet.tcddtasimacilik.gov.tr/view/eybis/tnmGenel/tcddWebContent.jsf")

    def setRotation(self):

        ct.retry(self.driver.find_element(
            By.XPATH, XPATHS.FROM).send_keys(self._from))
        ct.retry(self.driver.find_element(By.XPATH, XPATHS.FROM_DROP).find_element(
            By.XPATH, XPATHS.FROM_FIRST).click())

        ct.retry(self.driver.find_element(
            By.XPATH, XPATHS.TO).send_keys(self._to))
        ct.retry(self.driver.find_element(By.XPATH, XPATHS.TO_DROP).find_element(
            By.XPATH, XPATHS.TO_FIRST).click())

    def setDates(self):
        ct.retry(self.driver.find_element(
            By.XPATH, XPATHS.DEPARTURE_DATE).clear())
        ct.retry(self.driver.find_element(
            By.XPATH, XPATHS.DEPARTURE_DATE).send_keys(self._departure_date))
        ct.retry(self.driver.find_element(
            By.XPATH, XPATHS.CLOSE_CALENDAR_BUTTON).click())

    def searchTravel(self):
        ct.retry(self.driver.find_element(
            By.XPATH, XPATHS.SEARCH_BUTTON).click())

    def findAvailableTravels(self):
        sleep(5)
        available_seats = [
            {
                "ECONOMY": [],
                "BUSINESS": []
            }
        ]
        tbody = self.driver.find_element(By.XPATH, XPATHS.TBODY)
        rows = tbody.find_elements(By.TAG_NAME, "tr")
        index = 0
        for row in rows:
            time = datetime.strptime(row.find_element(
                By.XPATH, "./td[1]/span").get_attribute("innerText"), '%H:%M').time()
            if self._clock_end >= time and time >= self._clock_start:

                if self._exist_business:
                    res_business = self.driver.find_element(
                        By.XPATH, f"//*[@id='mainTabView:gidisSeferTablosu:{index}:j_idt109:0:somVagonTipiGidis1_panel']/div/ul/li[2]").text
                    available_business = re.search(r'\((\d+)\)', res_business)
                    try:
                        available_business = re.search(
                            r'\((\d+)\s*\)', res_business).group(1)
                    except:
                        available_business = re.search(
                            r'\((\d+.+)\)', res_business).group(1)

                    if int(available_business[0]) != 0:
                        available_seats[0]["BUSINESS"].append({
                            self._departure_date + " -> "+time.strftime("%H:%M"): available_business
                        })

                res_economy = self.driver.find_element(
                    By.XPATH, f"//*[@id='mainTabView:gidisSeferTablosu:{index}:j_idt109:0:somVagonTipiGidis1_panel']/div/ul/li[1]").text
                try:
                    available_economy = re.search(
                        r'\((\d+)\s*\)', res_economy).group(1)
                except:
                    available_economy = re.search(
                        r'\((\d+.+)\)', res_economy).group(1)

                if int(available_economy[0]) != 0:
                    available_seats[0]["ECONOMY"].append(
                        {
                            self._departure_date + " -> "+time.strftime("%H:%M"): available_economy
                        })

            index += 1
        return available_seats

    def closeDriver(self):
        self.driver.close()

    def runner(self):
        self.setRotation()
        self.setDates()
        self.searchTravel()
        availables = self.findAvailableTravels()
        self.closeDriver()

        return availables
