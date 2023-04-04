import argparse
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def capture_screenshot(url, destination, filename):
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(url)

    # Set the initial window size to maximum content height or screen height
    initial_width = driver.execute_script("return document.body.scrollWidth")
    initial_height = driver.execute_script("return document.body.scrollHeight")
    screen_height = driver.execute_script("return window.innerHeight")
    final_height = max(initial_height, screen_height)
    driver.set_window_size(initial_width, final_height)

    driver.save_screenshot(os.path.join(destination, f"{filename}.png"))

    driver.quit()


def main():
    parser = argparse.ArgumentParser(
        description="Capture full webpage as PNG.")
    parser.add_argument("-u", "--url", help="URL of the website to capture.")
    parser.add_argument(
        "-n", "--name", help="Output file name without extension.")
    parser.add_argument("-d", "--destination", default=".",
                        help="Destination directory for the output file.")
    parser.add_argument(
        "-f", "--file", help="File containing a list of URLs and names, one per line.")

    args = parser.parse_args()

    if not os.path.exists(args.destination):
        os.makedirs(args.destination)

    if args.url and args.name:
        capture_screenshot(args.url, args.destination, args.name)

    if args.file:
        with open(args.file, "r") as f:
            lines = f.readlines()

        for line in lines:
            url, name = line.strip().split()
            capture_screenshot(url, args.destination, name)


if __name__ == "__main__":
    main()
