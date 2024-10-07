import threading
import time
from selenium import webdriver

URLS = [
    "https://www.google.com",
    "https://github.com",
    "https://www.python.org",
    "https://selenium-python.readthedocs.io"
]

def open_browser(thread_name: str, url: str, headless: bool = False):
    """
    Function that creates and handles a chromedriver driver in a thread
    
    Args:
        thread_name (str): _description_
        url (str): _description_
        headless (bool, optional): _description_. Defaults to False.
    """
    
    print(f"Starting browser in {thread_name}")
    
    # Browser options
    options = webdriver.ChromeOptions()
    
    if headless:
        options.add_argument("--headless=old")
        options.add_argument("--disable-gpu")
        
    options.add_argument("--blink-settings=imagesEnabled=false")
    options.add_argument("--disable-images")
    options.add_argument("--incognito")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-automation")
    options.add_argument("--disable-extensions")
    options.add_argument("--start-maximized")
    options.add_argument("--auto-open-devtools-for-tabs")
    # Avoid SSL errors
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    
    try:
        # Create a new instance of the Chrome browser 
        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(15)
        driver.get(url)
        
        # Simulate the browser staying open for a while
        time.sleep(5)
    except Exception as e:
        print(f"Error in {thread_name}: {e}")
    
    finally:
        # Close the browser
        driver.quit()
        
        print(f"Browser closed on {thread_name}")

# Create multiple threads
threads = []

for i in range(4):  # Create 4 threads, one for each browser
    thread = threading.Thread(target=open_browser, args=(f"Hilo-{i}", URLS[i], True))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All browsers have ended.")
