# Book Web Scraper

A Python web scraping project that collects book information from [Books to Scrape](https://books.toscrape.com/), cleans the collected data, and saves it to a CSV file.

## Features

- Fetches webpage HTML using Requests.
- Retries failed HTTP requests.
- Parses book titles, prices, and URLs using BeautifulSoup.
- Scrapes multiple pages automatically.
- Removes duplicate records.
- Exports the results to `books.csv`.
- Checks data quality, including missing values and duplicates.
- Includes automated tests using pytest.

## Technologies Used

- Python
- Requests
- BeautifulSoup4
- CSV
- pytest
- Git and GitHub (for version control and project sharing)

## Installation

1. Clone or download this project.
2. Open a terminal in the project folder.
3. Install the required packages:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the scraper:

```bash
python run_scraper.py
```

This collects book information and saves it to `books.csv`.

Check the data quality:

```bash
python check_data.py
```

Run the automated tests:

```bash
python -m pytest test_web_data_extractor.py -v
```

## Output

The scraper currently collects 1,000 book records.

The generated CSV file contains these columns:

- `name`
- `price`
- `url`

The latest data quality check reported 1,000 unique records, zero duplicates, and zero missing values.

## Project Structure

```text
provider_results_2/
├── web_data_extractor.py
├── run_scraper.py
├── check_data.py
├── test_web_data_extractor.py
├── requirements.txt
├── README.md
└── books.csv
```

## What I Learned

- Making HTTP requests and handling request failures.
- Parsing HTML and extracting structured information.
- Navigating multiple pages on a website.
- Cleaning and validating collected data.
- Writing automated tests with mocks.
- Saving structured data to CSV files.

## Disclaimer

This project is intended for learning and demonstration purposes. Always respect website terms of service, access restrictions, and applicable scraping policies.
