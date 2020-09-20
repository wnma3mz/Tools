# -*- coding: utf-8 -*-
"""
author: Lu
doc:
    1. page2page-->制定页范围内切分
    2. filenum-->制定切分份数进行切分
    3. filenum-->制定多少页为一份进行切分
    4. merge_pdf-->合并，按照列表中元素的先后顺序
parames：
    infn：输入文件
    outfn：输出文件
    outfn_name：输出文件名
    page_count：pdf总页数

pip3 install pypdf2

PyPDF2.utils.PdfReadError: Multiple definitions in dictionary at byte 0x149413 for key /Type
**解决方案**
pdf_input = PdfFileReader(open(infn, 'rb'), strict=False)
"""
from PyPDF2 import PdfFileReader, PdfFileWriter


class PDFSplit(object):
    def __init__(self, infn):
        """
        infn: 切分的pdf
        """
        self.infn = infn
        self.pdf_input = PdfFileReader(open(infn, 'rb'))
        self.page_count = self.pdf_input.getNumPages()

    def page2page(self, startpage, endpage):
        """
        startpage: 从startpage页开始切分，默认从第一页开始切分
        endpage：直到endpage页切分结束
        """
        # endpage必须大于startpage，endpage必须小于总页数
        if startpage > endpage or endpage > self.page_count:
            raise ValueError("page_count > endpage > startpage")
        pdf_output = PdfFileWriter()
        # 读取对应页进行保存
        for i in range(startpage, endpage):
            pdf_output.addPage(self.pdf_input.getPage(i))
        pdf_output.write(
            open("".join(self.infn.split(".")[:-1]) + "_result.pdf", "wb"))

    def filenum(self, outfnnum=2):
        """
        outfnnum: 切分后的pdf数量,默认两份
        """
        # 判断切分份数是否大于1
        if outfnnum < 2:
            raise ValueError("切分份数必须大于一份")
        # 每份的页数
        outfn_page = self.page_count // outfnnum
        # 进行切分
        for num in range(1, outfnnum + 1):
            pdf_output = PdfFileWriter()
            outfn_name = "".join(
                self.infn.split(".")[:-1]) + "_" + str(num) + ".pdf"
            endpage = outfn_page * num if num != outfnnum else self.page_count
            for i in range(outfn_page * (num - 1), endpage):
                pdf_output.addPage(self.pdf_input.getPage(i))
            pdf_output.write(open(outfn_name, 'wb'))

    def pagenum(self, outfn_page):
        """
        outfn_page：切分之后每份pdf的页数
        """

        if self.page_count <= outfn_page:
            raise ValueError("切分的页数必须大于1")
        # 切分份数
        outfn_counts = self.page_count // outfn_page + 1 if self.page_count % outfn_page else 0
        # 进行切分
        for num in range(1, outfn_counts + 1):
            pdf_output = PdfFileWriter()
            outfn_name = "".join(
                self.infn.split(".")[:-1]) + "_" + str(num) + ".pdf"

            endpage = outfn_page * num if num != outfn_counts else self.page_count
            for i in range(outfn_page * (num - 1), endpage):
                pdf_output.addPage(self.pdf_input.getPage(i))
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
    pdfs = PDFSplit(infn)
    pdfs.page2page(startpage=10, endpage=20)
    pdfs.filenum(outfnnum=4)
    pdfs.pagenum(outfn_page=90)

    infnList = ["1.pdf", "2.pdf"]
    outfn = "result.pdf"
    # merge_pdf(infnList, outfn)
