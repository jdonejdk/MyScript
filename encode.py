import os
import sys
import codecs
import chardet


def list_files(path):
    """
    该程序用于将目录下的文件从指定格式转换到指定格式，默认的是GBK转到utf-8
    :param path:    文件路径
    :return:list_ffiles 文件列表
    """
    list_files = []
    for root,dirs,files in os.walk(path):
        for file in files:
            file_name = os.path.join(root,file)
            if(file_name.endswith('.c') or file_name.endswith('.h') or file_name.endswith('.txt')):
                list_files.append(file_name)
                print(file_name)
    # print(list_files)
    return list_files

def convert(file, in_enc="gb18030", out_enc="utf-8-sig"):
    """
    该函数用于将目录下的文件从指定格式转换到指定格式，默认的是GBK转到utf-8
    :param file:    文件路径
    :param in_enc:  输入文件格式
    :param out_enc: 输出文件格式
    :return:
    """
    in_enc = in_enc.upper()
    out_enc = out_enc.upper()
    try:
        print("convert [ " + file.split('\\')[-1] + " ].....From " + in_enc + " --> " + out_enc )
        f = codecs.open(file, 'rb', in_enc, errors="ignore")
        new_content = f.read()
        codecs.open(file, 'w', out_enc).write(new_content)
    except IOError as err:
        print("I/O error: {0}".format(err))

if __name__ == "__main__":
    path = r'..\\'
    path = sys.argv[1]
    print(path)
    list_files = list_files(path)

    for fileName in list_files:
        with open(fileName, "rb") as f:
            data = f.read()
            codeType = chardet.detect(data)['encoding']
            if(codeType == None):
                continue
            print(fileName+' encode is '+codeType)
            if(codeType == "GB2312"):
                convert(fileName, codeType, 'utf-8')
            # if(codeType == "utf-8"):
            #     convert(fileName, codeType, 'utf-8-sig')



