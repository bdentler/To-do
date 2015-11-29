#!/usr/local/bin/python3.4
# -*- coding: utf-8

import os, sys
from datetime import datetime
from datetime import timedelta

def delete(num):
    file = open('/users/dentlerb/dropbox/Admin/todo.txt', 'r')
    text = file.read()
    file.close
    list = text.split('\n')
    ct = len(list)
    file = open('/users/dentlerb/dropbox/Admin/todo.txt', 'w')
    for l in range(0, num-1):
        file.write(list[l])
        if not(num == ct and l == num-2): file.write('\n')
    for l in range(num, ct):
        file.write(str(l) + ' - ' + list[l][list[l].find('-')+2:])
        if (l < ct-1): file.write('\n')
    file.close    

def insert(num, item):
    file = open('/users/dentlerb/dropbox/Admin/todo.txt', 'r')
    text = file.read()
    file.close
    list = text.split('\n')
    ct = len(list)
    file = open('/users/dentlerb/dropbox/Admin/todo.txt', 'w')
    for l in range(0, num-1):
        file.write(list[l] + '\n')
    
    file.write(str(num) + ' - ' + item + '\n')
    
    for l in range(num, ct):
        file.write(str(l+1) + ' - ' + list[l-1][list[l-1].find('-')+2:] + '\n')
    file.write(str(ct+1) + ' - ' + list[ct-1][list[ct-1].find('-')+2:])
    file.close    

def add(item, dayt):
    fn = dayt + '.txt'
    file = open('/users/dentlerb/dropbox/Admin/' + fn, 'a')
    file.write('\n- '+item)
    file.close
    renum()

def renum():
    file = open('/users/dentlerb/dropbox/Admin/todo.txt', 'r')
    text = file.read()
    file.close
    list = text.split('\n')
    ct = len(list)
    file = open('/users/dentlerb/dropbox/Admin/todo.txt', 'w')
    for l in range(ct):
        file.write(str(l+1) + ' - ' + list[l][list[l].find('-')+2:])
        if l != ct-1: file.write('\n')
    file.close

def move(num1, num2):
    file = open('/users/dentlerb/dropbox/Admin/todo.txt', 'r')
    text = file.read()
    file.close
    list = text.split('\n')
    ct = len(list)
    temp = list.pop(num1-1)     # pick off the right one from the list: num1-1 save it to a temp variable
    list.insert(num2-1, temp)   # insert it in the list at the new place: num2-1
    file = open('/users/dentlerb/dropbox/Admin/todo.txt', 'w')
    for l in range(ct):
        file.write(str(l+1) + ' - ' + list[l][list[l].find('-')+2:])
        if l != ct-1: file.write('\n')
    file.close

def ccat():
    dayt = datetime.now().strftime("%Y-%m-%d")
    cmd = "cat /users/dentlerb/dropbox/Admin/todo.txt /users/dentlerb/dropbox/Admin/"+dayt+".txt > /users/dentlerb/dropbox/Admin/tmp.txt"
    os.system(cmd)
    os.system("mv /users/dentlerb/dropbox/Admin/tmp.txt /users/dentlerb/dropbox/Admin/todo.txt")
    cmd = "rm /users/dentlerb/dropbox/Admin/"+dayt+".txt"
    os.system(cmd)

def convertDate(dayt):

    today = datetime.now()
    today_dow = datetime.now().strftime("%w")
    dayt = dayt.upper()
    
    if dayt[0:2] == "SU":
        adjustment = ( 7 - int(today_dow)) % 7
    elif dayt[0:2] == "MO":
        adjustment = ( 8 - int(today_dow)) % 7
    elif dayt[0:2] == "TU":
        adjustment = ( 9 - int(today_dow)) % 7
    elif dayt[0:2] == "WE":
        adjustment = ( 10 - int(today_dow)) % 7
    elif dayt[0:2] == "TH":
        adjustment = ( 11 - int(today_dow)) % 7
    elif dayt[0:2] == "FR":
        adjustment = ( 12 - int(today_dow)) % 7
    elif dayt[0:2] == "SA":
        adjustment = ( 13 - int(today_dow)) % 7
    elif dayt[0:1] == "D":
        adjustment = eval(dayt[1:])
    elif dayt[0:1] == "W":
        adjustment = eval(dayt[1:])*7
    elif dayt[0:1] == "M":
        adjustment = eval(dayt[1:])*30
    elif dayt[-1:] == "D":
        adjustment = eval(dayt[:-1])
    elif dayt[-1:] == "W":
        adjustment = eval(dayt[:-1])*7
    elif dayt[-1:] == "M":
        adjustment = eval(dayt[:-1])*30
          
    theDate = (today + timedelta(days=adjustment)).strftime("%Y-%m-%d")
    return theDate

choice = sys.argv[1]
if choice == 'd' or choice == 'D':     # delete an item
    num = eval(sys.argv[2])
    delete(num)
elif choice == 'i' or choice == 'I':   # insert an item at a location
    num = eval(sys.argv[2])
    item = sys.argv[3]
    insert(num, item)
elif choice == 'r' or choice == 'R':   # renumber the list
    renum()
elif choice == 'm' or choice == 'M':   # move an item to a different location
    num1 = eval(sys.argv[2])
    num2 = eval(sys.argv[3])
    move(num1, num2)
elif choice == 'a' or choice == 'A':
    item = sys.argv[2]
    if len(sys.argv) == 4:
    	dayt = convertDate(sys.argv[3])
    else:
    	dayt = "todo"
    add(item,dayt)
elif choice == 'c' or choice == 'C':   # concatenate two files
    ccat()
else:
    print("I don't know what to do")