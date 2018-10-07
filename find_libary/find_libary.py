# coding: utf-8

import os


def filter_libary(libary):
    for l in libary.split('.'):
        if l and l not in import_lst:
            return l.strip()
    return ''


def filter_libary2(string):
    return (i.split('.')[0].strip().split('#')[0] for i in string.split(' as ')[0].split(','))


def walkdir(rootDir):
    for filename in os.listdir(rootDir):
        pathname = os.path.join(rootDir, filename)
        if (os.path.isdir(pathname)):
            walkdir(pathname)
        elif pathname.endswith('.py'):
            with open(pathname, 'r', encoding='utf-8') as f:
                for line in f.readlines():
                    if 'import ' in line:
                        word_lst = line.split(' ')
                        if word_lst[0] == 'from':
                            import_lst.append(filter_libary(word_lst[1]))
                        elif word_lst[0] == 'import':
                            for item in filter_libary2(' '.join(word_lst[1:])):
                                if item not in import_lst:
                                    import_lst.append(item.strip())


if __name__ == '__main__':
    # rootDir = 'F:\\mitmproxy-master'
    rootDir = ''
    global import_lst
    import_lst = []

    walkdir(rootDir)

    import_lst = sorted(list(set(import_lst)))[1:]
