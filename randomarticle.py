from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import random


class randomarticle:
    ssc_url = "https://slatestarcodex.com/archives/"
    acx_url = "https://astralcodexten.substack.com/archive"

    def __init__(self):
        def get_ssc_links(self):
            # load html and parse using bs4
            req = Request(self.ssc_url, headers={'User-Agent': 'Mozilla/5.0'})
            html_page = urlopen(req)
            soup = BeautifulSoup(html_page, "lxml")
            # create empty list with links and fill
            links = []
            for link in soup.findAll('a'):
                current_link = link.get('href')
                # check that the link satisfies some conditions
                condition = (
                    (current_link is not None) and
                    ("wp-login.php" not in current_link) and
                    ("slatestarcodex" in current_link) and
                    ("#comment" not in current_link) and
                    ("open-thread" not in current_link) and
                    ("open-thresh" not in current_link))
                if condition:
                    # add more flltering to get rid of some summary page links
                    manual_filter = [
                        "https://slatestarcodex.com/",
                        "https://slatestarcodex.com/",
                        "https://slatestarcodex.com/about/",
                        "https://slatestarcodex.com/archives/",
                        "https://slatestarcodex.com/2021/",
                        "https://slatestarcodex.com/2020/",
                        "https://slatestarcodex.com/2019/",
                        "https://slatestarcodex.com/2018/",
                        "https://slatestarcodex.com/2017/",
                        "https://slatestarcodex.com/2016/",
                        "https://slatestarcodex.com/2015/",
                        "https://slatestarcodex.com/2014/",
                        "https://slatestarcodex.com/2013/"
                        ]
                    if current_link not in manual_filter:
                        links.append(current_link)
            return links

        logger.info("Looking up the full list of Astral Codex Ten articles")

        def get_acx_links(self):
            # set up a headless selenium browser
            options = Options()
            options.headless = True
            self.driver = webdriver.Firefox(options=options)
            self.driver.get(self.acx_url)
            self.driver.maximize_window()
            # scroll to the bottom of the page
            # first get current scroll height
            last_height = self.driver.execute_script(
                "return document.body.scrollHeight")
            while True:
                # Scroll down to bottom
                self.driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                # Wait to load page
                time.sleep(3)
                # Calculate new scroll height and compare with last height
                new_height = self.driver.execute_script(
                    "return document.body.scrollHeight")
                if new_height == last_height:
                    time.sleep(10)
                    break
                last_height = new_height
            # get the fully loaded page and parse it
            html_page = self.driver.page_source
            soup = BeautifulSoup(html_page, "lxml")
            links = []
            # find all div containers that are a post preview
            preview_class = "post-preview portable-archive-post "\
                            "has-image has-author-line"
            divs = [divs for divs in soup.findAll(
                "div", {"class": preview_class})]
            # iterate over all post previews to get the link and to
            # check whether the link is behind a paywall
            for div in divs:
                linkdiv = div.find(
                    "a", {"class": "post-preview-title newsletter"})
                link = linkdiv.get('href')
                article_attributes = div.find(
                    "table", {"class": "post-meta post-preview-meta custom"})
                paywalled = article_attributes.find(
                    "td", {"class": "post-meta-item audience-lock"})
                if ((paywalled is None) and ("open-thread" not in link)):
                    links.append(link)

            self.driver.close()
            return links

        self.all_links = get_acx_links(self) + get_ssc_links(self)
        self.link = random.choice(self.all_links)
        print(self.link)

    def write_tweet(self):
        message = [
            "Here is your daily article from Astral Codex Ten "
            "/ Slate Star Codex:",
            f"{self.link}"
        ]
        message = " \n".join(message)
        return message
