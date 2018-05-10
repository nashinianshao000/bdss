from openpyxl import load_workbook
import re
wb = load_workbook('shenzhensgxk.xlsx')
with open('test6.txt','a+',encoding='utf-8') as f:
    i = 1
    while i < 13676:
        # print(str(wb['Sheet1']['C{}'.format(i)].value)[0:2])
        # if str(wb['Sheet1']['C{}'.format(i)].value)[0:2] == '提前':
        #     f.write(wb['Sheet1']['C{}'.format(i)].value+'\n')
        # else:
        #     f.write(wb['Sheet1']['B{}'.format(i)].value+'\n')
        f.write(wb['Sheet1']['A{}'.format(i)].value+'\t'+
                str(wb['Sheet1']['B{}'.format(i)].value.replace('编码:', ''))+'\t'+
                wb['Sheet1']['B{}'.format(i)].value +'\t'+
                wb['Sheet1']['C{}'.format(i)].value +'\t'+
                wb['Sheet1']['D{}'.format(i)].value +'\t'+
                wb['Sheet1']['E{}'.format(i)].value +'\t'+
                wb['Sheet1']['F{}'.format(i)].value +'\t'+
                wb['Sheet1']['G{}'.format(i)].value +'\t'+
                wb['Sheet1']['H{}'.format(i)].value +'\t'+
                wb['Sheet1']['I{}'.format(i)].value +'\t'+
                wb['Sheet1']['J{}'.format(i)].value +'\t'+
                wb['Sheet1']['K{}'.format(i)].value +'\t'+
                wb['Sheet1']['L{}'.format(i)].value +'\t'+
                wb['Sheet1']['M{}'.format(i)].value +'\t'+
                wb['Sheet1']['N{}'.format(i)].value +'\t'+
                wb['Sheet1']['O{}'.format(i)].value +'\t'+
                wb['Sheet1']['P{}'.format(i)].value +'\t'+
                wb['Sheet1']['Q{}'.format(i)].value +'\t'+
                wb['Sheet1']['R{}'.format(i)].value +'\t'+
                wb['Sheet1']['S{}'.format(i)].value +'\t'+
                wb['Sheet1']['T{}'.format(i)].value +'\t'+
                wb['Sheet1']['U{}'.format(i)].value +'\t'+
                wb['Sheet1']['V{}'.format(i)].value +'\t'+
                wb['Sheet1']['W{}'.format(i)].value +'\t'+
                wb['Sheet1']['X{}'.format(i)].value +'\t'+
                wb['Sheet1']['Y{}'.format(i)].value +'\n'
                )
        i += 1
        # print(i.value)
        # if i.value == 'url':
        #     continue
        # bianma = re.findall('instanceGuid=(.*?)&',i.value)
        # print(bianma)
        # bianmas = '编码:'+bianma[0]
        # f.write(bianmas+'\n')


















