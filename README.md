1. pip install virtualenv
2. virtualenv env
3. source env/bin/activate
4. pip install requirements.txt
5. cd shop
6. scrapy crawl shop_shorts -o extract_shorts_data.json
7. scrapy crawl shop_shorts -o extract_shorts_data.csv