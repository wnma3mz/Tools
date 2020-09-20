# coding: utf-8
import win32com.client as win32
import os


class PDF2Word(object):
    def __init__(self, rootDir):
        self.rootDir = rootDir
        self.word = win32.gencache.EnsureDispatch('Word.Application')
        self.word.Visible = False

    def run(self):
        try:
            self.walkdir(self.rootDir)
        finally:
            self.word.Quit()

    def walkdir(self, dir_):
        for filename in os.listdir(dir_):
            pathname = os.path.join(dir_, filename)
            if os.path.isdir(pathname):
                self.convert_files_folder(pathname)
                self.walkdir(pathname)
            else:
                self.covert_files(pathname)

    def covert_files(self, f):
        if f.endswith('.pdf'):
            fullpath = os.path.join(f)
            head, pdf_name = os.path.split(fullpath)
            save_path = os.path.join(head, pdf_name.replace('.pdf', '.docx'))
            if not os.path.exists(save_path):
                self.pdf_to_word(fullpath)

    def convert_files_folder(self, folder):
        files = os.listdir(folder)
        for f in files:
            self.covert_files(os.path.join(folder, f))

    def pdf_to_word(self, pdf_path):
        head, pdf_name = os.path.split(pdf_path)
        save_path = os.path.join(head, pdf_name.replace('.pdf', '.docx'))
        try:
            doc = self.word.Documents.Open(pdf_path)
            self.word.ActiveDocument.SaveAs(save_path)
            print('File "{}" transfer Complete'.format(pdf_name))
        except Exception as e:
            print(e)
            print("%s conver failed" % pdf_path)


def pdf_to_word(word, pdf_path):
    head, pdf_name = os.path.split(pdf_path)
    save_path = os.path.join(head, pdf_name.replace('.pdf', '.docx'))
    doc = word.Documents.Open(pdf_path)
    word.ActiveDocument.SaveAs(save_path)
    print('File "{}" transfer Complete'.format(pdf_name))


if __name__ == '__main__':
    dir_ = 'D:\\pdf_dir'
    pdf2word = PDF2Word(dir_)
    pdf2word.run()
