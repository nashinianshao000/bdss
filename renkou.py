from openpyxl import load_workbook
import requests
import re
from lxml import etree
def get_quxian(excel):
    wb = load_workbook(excel)
    for i in wb['SQL Results']['F']:
        if i.value != '区县名称':
            yield i.value
def baidu_ss(arg):
    url1 = 'https://www.baidu.com/s?wd='+str(arg)+'人口'
    url2 = 'https://www.baidu.com/s?wd='+str(arg)+'面积'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'baike.baidu.com',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    response = requests.get(url1,headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    html = etree.HTML(html)
    renkou = html.xpath('//div[@class="op_exactqa_s_area c-span18 c-span-last"]/div[@class="op_exactqa_s_answer"]/text()')

    # a2 = ''.join(a).replace('\n','')
    # mianji = re.findall('(\d+.\d+)平方千米|(\d+)平方公里',a2)
    # renkou = re.findall('(\d+.\d+)万.*?（\d+年常住人口）|(\d+)万.*?（\d+年常住人口）|(\d+.\d+)万.*?（\d+年）|(\d+)万.*?（\d+年）|(\d+)万人|(\d+.\d+)万人',a2)
    response2 = requests.get(url2,headers=headers)
    response2.encoding = 'utf-8'
    html = response2.text
    html = etree.HTML(html)
    mianji = html.xpath('//div[@class="op_exactqa_s_area c-span18 c-span-last"]/div[@class="op_exactqa_s_answer"]/text()')
    print(url1)
    renkou = ''.join(renkou).replace('\n','').replace(' ','').replace('\t','').replace(' ','')
    mianji = ''.join(mianji).replace('\n','').replace(' ','').replace('\t','').replace(' ','')
    print(renkou,mianji)
    return mianji,renkou
def write_excel(mianji,renkou):
    with open('test4.xlsx','a',encoding='utf-8') as f:
        f.write(mianji+'\t'+renkou+'\n')
def main():
    for i in get_quxian('基准价覆盖城市行政区详情.xlsx'):
        mianji,renkou = baidu_ss(i)
        write_excel(str(mianji),str(renkou))
if __name__ == '__main__':
    main()





