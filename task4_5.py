"""Скопировать из файла F1 в файл F2 строки, начиная с четвертой по порядку.
Подсчитать количество символов в последнем слове F2."""

startLine = 4
filename1 = "F1.txt"
filename2 = "F2.txt"


def copyFile():
     with open(filename1,"r") as file1:
         with open(filename2, "w") as file2:
            for line in file1.readlines()[startLine-1:]:
                file2.write(line)


def lastword(filename):
    with open(filename,"r") as file:
        lastline=file.readlines()[-1]
    lastw=lastline.split()[-1]
    print("Длина последнего слова = " + str(len(lastw)))


copyFile()
lastword(filename2)