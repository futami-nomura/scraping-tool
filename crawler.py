# import modules to crawl images
from icrawler.builtin import GoogleImageCrawler

crawler = GoogleImageCrawler(storage={"root_dir": "images"})
crawler.crawl(keyword="稲熱病", max_num = 10)
