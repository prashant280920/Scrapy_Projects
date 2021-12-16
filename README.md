# Scrapy Projects
Using Scrapy a Python framework that give all tools you need to efficiently extract data for large scale web scraping. Here are some web scarpe scripts I have done on some website.

## Setting Up the Environment

1. Fork The repo
2. Clone it in your local machine using the forked repo
3. Create a virtual enviornment in your local machine in the folder you cloned the repo,

    ```bash
    pip install virtualenv
    virtualenv env
    ```
4. Activate the virtual env<br>
   For Windows run
   ```bash
   .\env\Scripts\activate
   ```
   For Linux run
   ```bash
   source env/bin/activate
   ```
   Follow the instructions given after you create a env successfully .
5. Now install requirements using
   ```bash
   pip install -r requirements.txt
   ```
6. Now move to any project directory - `cd <Project Directory>`. For example `cd shop`.
7. Now to webcrawl the website find the NAME_OF_SPIDER from the python file in the spiders directory. In **shop** project NAME_OF_SPIDER = `shop_shorts` from the shop_shorts.py in the spiders directory.
    ```bash
    scrapy crawl NAME_OF_SPIDER
    ```
8. To get the output in simple json file
    ```bash
    scrapy crawl NAME_OF_SPIDER -o output.json
    ```
9. To get the output in simple csv file
    ```bash
    scrapy crawl NAME_OF_SPIDER -o output.csv
    ```