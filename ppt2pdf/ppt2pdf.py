#-*- coding:utf-8 -*-
import comtypes.client
import os


def init_powerpoint():
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1
    return powerpoint


def ppt_to_pdf(powerpoint, inputFileName, outputFileName, formatType=32):
    if outputFileName[-3:] != 'pdf':
        outputFileName = outputFileName + '.pdf'
    try:
        deck = powerpoint.Presentations.Open(inputFileName)
        deck.SaveAs(outputFileName, formatType)
        deck.Close()
    except Exception as e:
        print("%s conver failed" % inputFileName)


def convert_files_folder(powerpoint, folder):
    files = os.listdir(folder)
    pptfiles = [f for f in files if f.endswith(
        (".ppt", ".pptx", ".PPT", ".PPTX"))]
    for pptfile in pptfiles:
        fullpath = os.path.join(folder, pptfile)
        if not os.path.exists(fullpath + '.pdf'):
            ppt_to_pdf(powerpoint, fullpath, fullpath)


def walkdir(rootDir, powerpoint):
    for filename in os.listdir(rootDir):
        pathname = os.path.join(rootDir, filename)
        if (os.path.isdir(filename)):
            convert_files_folder(powerpoint, pathname)
            walkdir(pathname, powerpoint)


def rmsamepdf(rootDir):
    for filename in os.listdir(rootDir):
        pathname = os.path.join(rootDir, filename)
        if (os.path.isdir(pathname)):
            rmsamepdf(pathname)
        if (filename.endswith('.pdf')):
            for pre in [".ppt", ".pptx", ".PPT", ".PPTX"]:
                if pre in filename:
                    os.remove(pathname)


def mvpdf(rootDir):
    import sys
    import shutil
    split_char = "\\" if sys.platform == 'win32' else '/'
    for filename in os.listdir(rootDir):
        pathname = os.path.join(rootDir, filename)
        if (os.path.isdir(pathname)):
            mvpdf(pathname)
        pdf_dir = rootDir.split(split_char)[-1]
        if not os.path.exists(os.path.join(rootDir, pdf_dir)):
            os.mkdir(os.path.join(rootDir, pdf_dir))
        if (filename.endswith('.pdf')):
            shutil.move(pathname, os.path.join(rootDir, pdf_dir))

if __name__ == '__main__':
    try:
        powerpoint = init_powerpoint()
        cwd = os.getcwd()
        # 以当前文件位置为root，不断遍历文件夹中的ppt文件，转换为pdf
        walkdir(cwd, powerpoint)
        # 整理pdf文件
        # os.mkdir("pdf")
        mvpdf(cwd)
        # 删除同名pdf
        # rmsamepdf(cwd)
    finally:
        powerpoint.Quit()
