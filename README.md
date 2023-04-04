# Webpage to PNG Converter

This command-line tool captures entire webpages as PNG images. It allows you to input single URLs or process multiple URLs from a text file. The resulting images are saved in the specified directory with the provided file names.

## Installation

Make sure you have Python 3 installed on your system.
Install the required packages:

```
pip install selenium
pip install webdriver-manager
```

Clone the repository or download the website_converter.py script.

## Usage

Run the script using the following command:


```
python website_converter.py -u <url> -n <name> -d <destination> -f <file> -t <threads>

Arguments

    -u, --url: URL of the website to capture.
    -n, --name: Output file name without extension.
    -d, --destination: Destination directory for the output file (default: current directory).
    -f, --file: File containing a list of URLs and names, one per line.
    -t, --threads: Number of threads for parallel processing (default: 5).
```

## Examples

    Capture a single webpage:


```
python website_converter.py -u https://www.example.com -n example -d screenshots
```

This command captures the entire webpage at https://www.example.com, saves it as a PNG image in the "screenshots" directory, and names the output file "example.png".

Capture multiple webpages from a file:

Create a text file with one URL and name per line, separated by a space, like this:

```
https://www.example1.com example1
https://www.example2.com example2
```

Then, run the script:

```
python website_converter.py -f urls.txt -d screenshots
```

This command processes each URL in the urls.txt file, captures the webpages, and saves them as PNG images in the "screenshots" directory with the specified names.    

## Dependencies

Python 3  
Selenium  
WebDriver  
Manager for Python
