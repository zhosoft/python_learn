# alt+enter 导包快捷键

from io import StringIO
from io import open
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf


def read_pdf(pdf):
    # resource manager
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    # device
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    process_pdf(rsrcmgr, device, pdf)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    # 获取所有行
    lines = str(content).split("\n")

    units = [1, 2, 3, 5, 7, 8, 9, 11, 12, 13]
    header = '\x0cUNIT '
    # print(lines[0:100])
    count = 0
    flag = False
    text = open('words.txt', 'w+')
    for line in lines:
        if line.startswith(header):
            flag = False
            count += 1
            if count in units:
                flag = True
                print(line)
                text.writelines(line + '\n')
        if '//' in line and flag:
            text_line = line.split('//')[0].split('. ')[-1]
            print(text_line)
            text.writelines(text_line + '\n')
    text.close()


def _main():
    my_pdf = open('t1.pdf', "rb")
    read_pdf(my_pdf)
    my_pdf.close()


if __name__ == '__main__':
    _main()
