import os

def read (folder):
    for root,subroot,file in os.walk(folder):

        level= root.count(os.sep)
        indent= " " * 4 * level
        subindent = " " * 4 * (level+1)

        print(f'{indent} [{os.path.basename(root)}] ')
        for i in file:
            print(f' {subindent}{i}')

        # print(root,subroot,file, indent)

read('folder')

#
# a = os.walk('folder')
# for i in a:
#     print(i)
