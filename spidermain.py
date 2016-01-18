# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 15:49:22 2016

@author: Administrator
"""

# 调度程序

import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()        
        self.outputer = html_outputer.HtmlOutputer()
        
    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        count = 1
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print "craw %d : %s" % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 6:
                    break
                count += 1
            except:
                print "Craw Failed"

        self.outputer.output_html()
            
        
        
        
        
if __name__ == "__main__":
    root_url = "https://en.wikipedia.org/wiki/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    
        