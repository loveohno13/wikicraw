# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser(object):

	def _get_new_urls(self, url, soup):
		new_urls = []

		links = soup.find_all("a", href=re.compile(r"^/wiki/\w*"))
		for link in links:
			new_url = link["href"]
			new_full_url = urlparse.urljoin(url, new_url)
			new_urls.append(new_full_url)
		return new_urls

	def _get_new_data(self, url, soup):
	
		new_data = {}

		new_data["url"] = url

		title_node = soup.find("div", id="content").find("h1")
		new_data["title"] = title_node.get_text()

		summary_node = soup.find("div", id="mw-content-text").find("p")
		new_data["summary"] = summary_node.get_text()

		return new_data


	def parse(self, url, html_cont):

		soup = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")
		new_urls = self._get_new_urls(url, soup)
		new_data = self._get_new_data(url, soup)

		return new_urls, new_data


