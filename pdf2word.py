# coding: utf-8
import win32com.client as win32
import os


def pdf2word(word, pdf_path):
    head, pdf_name = os.path.split(pdf_path)
    save_path = os.path.join(head, pdf_name.replace('.pdf', '.docx')) 
    doc = word.Documents.Open(pdf_path)
    word.ActiveDocument.SaveAs(save_path)
    print('File "{}" transfer Complete'.format(pdf_name))

if __name__ == '__main__':
    word = win32.gencache.EnsureDispatch('Word.Application')
    word.Visible = False

    # pdf目录的绝对路径
    pdfdir_path = ''

    f_lst = os.listdir(pdfdir_path)
    for f in f_lst:
        if f.endswith('.pdf'):
            pdf_path = os.path.join(pdfdir_path, f)
            try:
                pdf2word(word, pdf_path)
            except:
                print('File "{}" transfer failed'.format(pdf_path))
                continue

    word.Quit()
