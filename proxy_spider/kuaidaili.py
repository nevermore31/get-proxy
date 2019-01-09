import grequests
from bs4 import BeautifulSoup
from setting import headers as hd
from multiprocessing import Pool


class ProxySpider:
    def __init__(self, size=None):
        self.size = size if size else 20
        start_url = 'https://www.kuaidaili.com/free/inha/{}/'
        self.all_url = [start_url.format(int(i)) for i in range(1, 10)]
        self.headers = hd(spider_name='kuaidaili.py')

    def req(self, url):
        """
        进行第一次爬取, 保存所有请求结果
        :return: 保存失败 url与成功 text 的列表
        """
        task = [t for t in grequests.get(url, headers=self.headers)]
        g = grequests.map(task, size=self.size)
        fail = []
        succus = [i.text if i.status_code == 200 else fail.append(i.url) for i in g]
        return succus, fail

    def handle_succus(self, text):
        """
        :param text: url文本 str
        :return: 解析出需要的ip地址
        """
        soup = BeautifulSoup(text, 'lxml')
        tr = soup.body.find('div', id='content').find('tbody').find_all('tr')
        
