# 用Python处理pdf文件

## 说明：

1. 使用模块pypdf2 (pip3 install pypdf2)
2. 三种切割方式，一种合并方式

## 报错1

PyPDF2.utils.PdfReadError: Multiple definitions in dictionary at byte 0x149413 for key /Type

**解决方案**

pdf_input = PdfFileReader(open(infn, 'rb'), strict=False)
