#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
script to convert the JMeter script's all simple controller to transaction controller
'''

import sys, re


def sim2Trann(jmxFile):
    printStart()  # print ASCII art start

    newFilenName = raw_input("Enter the new filename:")

    if newFilenName:  # change foo to foo.jmx name style
        newFilenName = setNameFull(newFilenName)
        while jmxFile == newFilenName:
            print "Please input an other name differ from the original name!"
            newFilenName = raw_input("Enter the new filename:")
            # if newFilenName == '':
            #     print "Please enter an name:"
            #
            # else:
            #     pass
            newFilenName = setNameFull(newFilenName)
    else:  # set a default name to the new jmx
        newFilenName = "newjmx.jmx"

    jmxFile = open(jmxFile, 'r')

    newFile = open(newFilenName, "w")

    removed = jmxFile.read()


    # change the simple contoller name
    removed = re.sub(
        r'<GenericController guiclass=\"LogicControllerGui\" testclass=\"GenericController\"',
        '<TransactionController guiclass=\"TransactionControllerGui\" testclass=\"TransactionController\"', removed)

    GuysNeedToReplace = re.findall(r'<TransactionController guiclass.+?\"/>', removed)

    # replace "/>" to the ">" at the end of the controller, and add 3 lines at the end
    for guys in GuysNeedToReplace:
        reguy = guys[:-2] + "><boolProp name=\"TransactionController.includeTimers\">false</boolProp><boolProp name=\"TransactionController.parent\">false</boolProp></TransactionController>"
        removed = re.sub(guys, reguy, removed)

    newFile.write(removed)  # write in the new file

    jmxFile.close()  # close the original file

    newFile.close()  # close the output file

    printFinish()  # print ASCII art Finish


def setNameFull(FileName):
    if '.jmx' in FileName:
        pass
    else:
        returnName = FileName + ".jmx"
        return returnName


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

    sim2Trann(fileName)


if __name__ == '__main__':
    main()