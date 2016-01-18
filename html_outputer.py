# html_outputer
# -*- coding: utf-8 -*-


class HtmlOutputer(object):
	def __init__(self):
		self.datas = []


	def collect_data(self, data):
		if data is None:
			return
		self.datas.append(data)
		print


	def output_html(self):

		fout = open("output.txt", "w+")

		for data in self.datas:
			
			fout.write("url: %s \n" % data["url"])
			fout.write("title: %s \n" % data["title"])
			fout.write("summary: %s \n" % data["summary"])

		fout.close()


