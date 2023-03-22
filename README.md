## web-testing

Uses Selenium for automated web testing.

View `requirements.txt` for full list of packages used.

### How to Install

Currently working with Python `3.11.2`.

Create a virtual enviroment then activate it and use the `pip` command to install the packages for the virtual enviroment.

```
py -m venv <venv_name>

source <env_name>/Scripts/activate

pip install -r requirements.txt
```

### Main Packages

- Web Scraping - `Selenium`
- Chrome Driver - `webdriver-manager`
- Linting - `pylint`
- Formatting - `black`

### Working On

- Export results to text file, CSV, or Google Sheets
- Better reporting logs
- `Matplotlib` for graphs for data and results

### References

[Command Line Switches for Chromium](https://peter.sh/experiments/chromium-command-line-switches/) - Chrome driver options arguments  
[Chrome Driver Capabilities](https://chromedriver.chromium.org/capabilities) - Options to customize and configure a `ChromeDriver` session
