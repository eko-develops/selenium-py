from browser import Browser
from timer_group import TimerGroup
from selenium.common.exceptions import TimeoutException
from constants import *


class Test:
    @staticmethod
    def page_load(url):
        """Test the page load based on ready state of document"""
        timers = TimerGroup("load")
        chrome = Browser()
        try:
            """Test how long the page takes to completely load"""
            chrome.clean_up()

            """Open the website and start the timer"""
            timers.start_timer("load")
            chrome.get(url)

            """Wait for the page to load completely then end timer"""
            chrome.exec_script("return document.readyState == 'complete'")
            timers.end_timer("load")

            timers.display_full()
            print("Homepage loaded successfully")
        finally:
            chrome.quit(f"Exiting page load test for {url}")

    @staticmethod
    def login_page(user, password, home_url):
        """Test login page fields"""
        timers = TimerGroup("home_load", "login_btn_load", "login_load")
        chrome = Browser()
        try:
            """Test how long the page takes to completely load"""
            chrome.clean_up()

            """Open the website and start the timer"""
            timers.start_timer("home_load")
            chrome.get(home_url)
            """Wait for the page to load completely then end timer"""
            chrome.exec_script("return document.readyState == 'complete'")
            timers.end_timer("home_load")

            """Wait for login button then click"""
            timers.start_timer("login_btn_load")
            chrome.wait_for_visibility(LOGIN_BUTTON, True)
            timers.end_timer("login_btn_load")

            """Testing login page load time.
                Waits for page to be loaded then for input fields to be visible.
            """
            timers.start_timer("login_load")
            chrome.exec_script("return document.readyState == 'complete'")
            chrome.wait_for_visibility(USERNAME_INPUT)
            timers.end_timer("login_load")

            """Fill in inputs"""
            chrome.find_element_send_keys(USERNAME_INPUT, user)
            chrome.find_element_send_keys(PASSWORD_INPUT, password)

            timers.display_full()
            print("Login Page fields are viewable and can be written to.")
        except TimeoutException as TOE:
            print(TOE)
        finally:
            chrome.quit(f"Exiting login test for {user} at {home_url}")
