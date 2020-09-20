#-*- coding:utf-8 -*-
import comtypes.client
import os


class PPT2PDF(object):
    def __init__(self, rootDir):
        self.rootDir = rootDir
        self.powerpoint = comtypes.client.CreateObject(
            "Powerpoint.Application", dynamic=True)
        self.powerpoint.Visible = 1
        self.end_tuple = (".ppt", ".pptx", ".PPT", ".PPTX")

    def run(self):
        try:
            self.walkdir(self.rootDir)
        finally:
            self.powerpoint.Quit()

    def walkdir(self, dir_):
        for filename in os.listdir(dir_):
            pathname = os.path.join(dir_, filename)
            if os.path.isdir(pathname):
                self.convert_files_folder(pathname)
                self.walkdir(pathname)
            else:
                self.covert_files(pathname)

    def _replace_name(self, name):
        for ends in self.end_tuple:
            name = name.replace(ends, '.pdf')
        return name

    def covert_files(self, f):
        if f.endswith(self.end_tuple):
            fullpath = os.path.join(f)
            head, fname = os.path.split(fullpath)
            save_path = os.path.join(head, self._replace_name(fname))
            if not os.path.exists(save_path):
                self.ppt_to_pdf(fullpath, save_path)

    def convert_files_folder(self, folder):
        files = os.listdir(folder)
        for f in files:
            self.covert_files(os.path.join(folder, f))

    def ppt_to_pdf(self, inputFileName, outputFileName, formatType=32):
        try:
            deck = self.powerpoint.Presentations.Open(inputFileName)
            deck.SaveAs(outputFileName, formatType)
            deck.Close()
            print('File "{}" transfer Complete'.format(inputFileName))
        except Exception as e:
            print(e)
            print("%s conver failed" % inputFileName)


if __name__ == '__main__':
    ppt_dir = 'D:\\ppt_dir'
    ppt2pdf = PPT2PDF(ppt_dir)
    ppt2pdf.run()
