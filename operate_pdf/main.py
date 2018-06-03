# /usr/bin/python3
# -*- coding: utf-8 -*-
"""
author: Lu
doc:
    1. split_pdf_1-->制定页范围内切分
    2. split_pdf_2-->制定切分份数进行切分
    3. split_pdf_3-->制定多少页为一份进行切分
    4. merge_pdf-->合并，按照列表中元素的先后顺序
parames：
    infn：输入文件
    outfn：输出文件
    outfn_name：输出文件名
    page_count：pdf总页数
"""
from PyPDF2 import PdfFileReader, PdfFileWriter


def split_pdf_1(infn, startpage, endpage):
    """
    infn: 切分的pdf
    startpage: 从startpage页开始切分，默认从第一页开始切分
    endpage：直到endpage页切分结束
    """
    pdf_output = PdfFileWriter()
    pdf_input = PdfFileReader(open(infn, 'rb'))
    page_count = pdf_input.getNumPages()

    # endpage必须大于startpage，endpage必须小于总页数
    if startpage > endpage:
        print("startpage > endpage")
        return
    if endpage > page_count:
        print("endpage > page_count")
        return
    # 读取对应页进行保存
    for i in range(startpage, endpage):
        pdf_output.addPage(pdf_input.getPage(i))
    pdf_output.write(open("".join(infn.split(".")[:-1]) + "_result.pdf", "wb"))


def split_pdf_2(infn, outfnnum=2):
    """
    infn: 切分的pdf
    outfnnum: 切分后的pdf数量,默认两份
    """
    # 判断切分份数是否大于1
    if outfnnum < 2:
        print(u"切分份数必须大于一份")
        return
    pdf_input = PdfFileReader(open(infn, 'rb'))
    page_count = pdf_input.getNumPages()

    # 每份的页数
    outfn_page = page_count // outfnnum
    # 进行切分
    for num in range(1, outfnnum + 1):
        pdf_output = PdfFileWriter()
        outfn_name = "".join(infn.split(".")[:-1]) + "_" + str(num) + ".pdf"
        for i in range(outfn_page * (num - 1), outfn_page * num if num != outfnnum else page_count):
            pdf_output.addPage(pdf_input.getPage(i))
        pdf_output.write(open(outfn_name, 'wb'))


def split_pdf_3(infn, outfnpage):
    """
    infn: 切分的pdf
    outfnpage：切分之后每份pdf的页数
    """
    pdf_input = PdfFileReader(open(infn, 'rb'))
    page_count = pdf_input.getNumPages()
    if page_count <= outfnpage:
        print(u"切分的页数必须大于1")
        return
    # 切分份数
    outfn_counts = page_count // outfnpage + 1 if page_count % outfnpage else 0
    # 进行切分
    for num in range(1, outfn_counts + 1):
        pdf_output = PdfFileWriter()
        outfn_name = "".join(infn.split(".")[:-1]) + "_" + str(num) + ".pdf"
        for i in range(outfnpage * (num - 1), outfnpage * num if num != outfn_counts else page_count):
            pdf_output.addPage(pdf_input.getPage(i))
        pdf_output.write(open(outfn_name, 'wb'))


def merge_pdf(infnList, outfn):
    """
    infnList: 需要合并的pdf列表
    outfn：合并之后的pdf名
    """
    pdf_output = PdfFileWriter()
    for infn in infnList:
        pdf_input = PdfFileReader(open(infn, 'rb'))
        page_count = pdf_input.getNumPages()

        for i in range(page_count):
            pdf_output.addPage(pdf_input.getPage(i))

    pdf_output.write(open(outfn, 'wb'))


if __name__ == '__main__':
    infn = "1.pdf"
    outfn = "result.pdf"
    infnList = ["1.pdf", "2.pdf"]
    # split_pdf_1(infn, startpage=10, endpage=20)
    # split_pdf_2(infn, outfnnum=4)
    # split_pdf_3(infn, outfnpage=90)
    # merge_pdf(infnList, outfn)
