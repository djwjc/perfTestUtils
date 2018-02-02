#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, re


def tran2Sim(jmxFile):
    printStart()  # print ASCII art start

    newFilenName = raw_input("Enter the new filename:")
    if newFilenName:
        if '.jmx' in newFilenName:
            pass
        else:
            newFilenName = newFilenName + ".jmx"
    else:
        newFilenName = "newjmx.jmx"

    jmxFile = open(jmxFile, 'r')

    newFile = open(newFilenName, "w")

    removed = jmxFile.read()

    # print ">>>>>>>>>>>>>>>>>>>>Processing>>>>>>>>>>>>>>>>>>>>"

    # remove three lines in Transaction conntroller
    removed = re.sub(r' +<boolProp name="TransactionController.includeTimers">false</boolProp>\n', '', removed)
    removed = re.sub(r' +<boolProp name="TransactionController.parent">false</boolProp>\n', '', removed)
    removed = re.sub(r' +</TransactionController>\n', '', removed)

    # change the transaction contoller name
    removed = re.sub(
        r'<TransactionController guiclass=\"TransactionControllerGui\" testclass=\"TransactionController\"',
        '<GenericController guiclass=\"LogicControllerGui\" testclass=\"GenericController\"', removed)

    GuysNeedToReplace = re.findall(r'<GenericController guiclass.+?\">', removed)

    for guys in GuysNeedToReplace:  # replace ">" to the "/>" at the end of the controller
        reguy = guys[:-1] + "/>"
        removed = re.sub(guys, reguy, removed)

    newFile.write(removed)  # write in the new file

    jmxFile.close()  # close the original file
    newFile.close()  # close the output file

    printFinish()  # print ASCII art Finish


def printStart():
    print "███████╗████████╗ █████╗ ██████╗ ████████╗"
    print "██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝"
    print "███████╗   ██║   ███████║██████╔╝   ██║   "
    print "╚════██║   ██║   ██╔══██║██╔══██╗   ██║   "
    print "███████║   ██║   ██║  ██║██║  ██║   ██║   "
    print "╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   "


def printFinish():
    print "███████╗██╗███╗   ██╗██╗███████╗██╗  ██╗"
    print "██╔════╝██║████╗  ██║██║██╔════╝██║  ██║"
    print "█████╗  ██║██╔██╗ ██║██║███████╗███████║"
    print "██╔══╝  ██║██║╚██╗██║██║╚════██║██╔══██║"
    print "██║     ██║██║ ╚████║██║███████║██║  ██║"
    print "╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝╚═╝  ╚═╝"


def main():
    try:
        fileName = sys.argv[1]
    except IndexError:
        try:
            fileName = raw_input("Please input file name:")
        except IndexError:
            print "File is not exist!!!"
            exit()

    tran2Sim(fileName)


if __name__ == '__main__':
    main()
