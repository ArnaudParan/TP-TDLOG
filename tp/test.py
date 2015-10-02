#!/usr/bin/python3.4
#-*-coding:utf-8-*

# These functions are Python versions of functions described in chapter 8 of Numerical Recipes.
# Original functions can be found at:
# http://www2.units.it/ipl/students_area/imm2/files/Numerical_Recipes.pdf for C
# 


#Tache 1
def intToStr(casted):
    cipherChars = []
    while casted != 0:
        cipher = casted % 10
        casted = casted // 10
        cipherChar = cipherToChar(cipher)
        cipherChars.append(cipherChar)
    cipherChars = rev(cipherChars)
    return concat(cipherChars)


def rev(list):
    orderedList = []
    listLen = len(list)
    for elemId in range(1, listLen + 1):
        actualElem = list[listLen - elemId]
        orderedList.append(actualElem)

    return orderedList


def concat(charList):
    mergedWord = ""
    for carac in charList:
        mergedWord = mergedWord + carac
    return mergedWord


def cipherToChar(casted):
    if casted == 0:
        return "0"
    elif casted == 1:
        return "1"
    elif casted == 2:
        return "2"
    elif casted == 3:
        return "3"
    elif casted == 4:
        return "4"
    elif casted == 5:
        return "5"
    elif casted == 6:
        return "6"
    elif casted == 7:
        return "7"
    elif casted == 8:
        return "8"
    elif casted == 9:
        return "9"





def insertion_sort(toSort):
    lenArr = len(toSort)

    for actualNumberId in range(1, lenArr):
        actualNumber = toSort[actualNumberId]
        insert_in_list(toSort, actualNumber, actualNumberId)
    return toSort


def insert_in_list(insertIn, toInsert, listLength):
    actualElemId = listLength - 1
    while (actualElemId >= 0 and
                insertIn[actualElemId] > toInsert):
        insertIn[actualElemId + 1] = insertIn[actualElemId]
        actualElemId -= 1

    insertIn[actualElemId + 1] = toInsert
