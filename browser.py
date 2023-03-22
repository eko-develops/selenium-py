import time

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Browser:
    """Browser class that wraps Selenium"""

    def __init__(self):
        self.options = ChromeOptions()
        self.init_options()

        """Download and install the appropriate version of the ChromeDriver"""
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=self.options,
        )

    def init_options(self):
        """Initialize options using command line switches for the driver"""
        self.options.add_argument("--incognito")
        # self.options.add_argument("--headless")
        # self.options.add_argument("--start-maximized")
        # self.options.add_experimental_option("detach", True)  # keep window open after running, doesnt always work

        """Ignore issues with Selenium"""
        self.options.add_argument("--ignore-certificate-errors")
        self.options.add_argument("--ignore-ssl-errors")
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])

    def get(self, url):
        """Loads webpage in current browser session.

        Args:
            url (str): The URL to load.
        """
        self.driver.get(url)

    def quit(self, message=""):
        """Closes browser and shuts down driver.

        Args:
            message (str, optional): A message to print before exiting. Defaults to "".
        """
        if message:
            print(message)
        self.driver.quit()

    def pause(self, seconds=2):
        """Pauses script execution for a given number of seconds

        Args:
            seconds (int, optional): The number of seconds to pause. Defaults to 2.
        """
        time.sleep(seconds)

    def page_title(self):
        """Gets page title for current webpage.

        Returns:
            str: The page title.
        """
        return self.driver.title

    def wait_for_visibility(self, element_selector, click=False, timeout=10):
        """Waits for an element with the given CSS selector to be both present in the
        DOM and visible on the page. If the `click` parameter is set to `True`,
        the element will be clicked after it becomes visible.

        Raises a `selenium.common.exceptions.TimeoutException` if timeout is exceeded.

            Args:
                element_selector (str): The element's CSS selector.
                click (bool, optional): Click the element after it is visible. Defaults to False.
                timeout (int, optional): Maximum amount of time in seconds to wait for the element to be visible. Defaults to 10.

            Returns:
                WebElement: The visible element for additional actions.
        """
        wait = WebDriverWait(self.driver, 1)
        element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, element_selector)),
            f"Timed out waiting for {element_selector}",
        )

        if click is True:
            element.click()

        return element

    def find_element_by_selector(self, element_selector):
        """Find an element by it's CSS selector.
        Element can be stored to be used for later actions.

        Example:
        -
        logo = chrome.find_element_by_selector("#header .logo")
        """
        return self.driver.find_element(By.CSS_SELECTOR, element_selector)

    def find_element_send_keys(self, element_selector, keys):
        """Finds an element by CSS selector then adds keys to element."""
        element = self.wait_for_visibility(element_selector)
        # element.send_keys(keys)
        self.slow_type(element, keys)

    def exec_script(self, script):
        """Executes a script in the browser"""
        self.driver.execute_script(script)

    def slow_type(self, element, text, delay=0.1):
        """Imitates slow typing to an element."""
        for char in text:
            element.send_keys(char)
            self.pause(delay)

    def clean_up(self):
        """Removes instance cache and cookies before running.
        This is generally always ran at the start of every Test method.
        Pauses for 2 seconds after clearing to ensure everything is removed.
        """
        self.driver.execute_cdp_cmd("Network.enable", {})
        self.driver.execute_cdp_cmd("Network.clearBrowserCache", {})
        self.driver.execute_cdp_cmd("Network.clearBrowserCookies", {})
        self.driver.execute_cdp_cmd("Network.disable", {})
        self.pause()
