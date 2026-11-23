import PyQt5.QtWidgets as w
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from functools import partial
import sys
import numpy as np
import random as rd
import math as m
import copy as c
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


def bubbleSort(arr):
    time = 'O(n^2)'
    count = 0
    swap = 0
    passes = []  # har traverse ky baat kaisa array aya
    n = len(arr)
    for i in range(n):
        flag = True
        count += 1
        passes.append(c.copy(arr))
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swap += 1
                flag = False
        if flag:
            if (count == 1):
                time = 'O(n)'
            break
    answers = (arr, swap, count, time, passes)
    return answers


def SelectionSort(arr):
    n = len(arr)
    count = 0
    swap = 0
    passes = []
    for i in range(n - 1):
        min_idx = i
        count += 1
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[min_idx], arr[i] = arr[i], arr[min_idx]
            swap += 1
        passes.append(arr.copy())
    time = 'O(n^2)'
    answers = (arr, swap, count, time, passes)
    return answers


def InsertionSort(arr):
    n = len(arr)
    count = 0
    swap = 0
    passes = []
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        count += 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            swap += 1
        arr[j + 1] = key
        passes.append(arr.copy())
    time = 'O(n^2)'
    answers = (arr, swap, count, time, passes)
    return answers


def Insertion(arr, n, pos, val):
    checkn(n)
    checkn(pos)
    checkn(val)
    passes = []
    count = 0
    for i in reversed(range(pos, n)):
        arr[i + 1] = arr[i]
        passes.append(arr.copy())
        count += 1
    arr[pos] = val
    passes.append(arr.copy())
    time = 'O(n)'
    answers = (arr, 0, count, time, passes)
    return answers


def Deletion(arr, pos):
    checkpos(pos)
    passes = []
    n = len(arr)
    count = 0
    for i in range(pos, n - 1):
        arr[i] = arr[i + 1]
        count += 1
        passes.append(c.copy(arr))
    time = 'O(n)'
    answers = (arr[:n - 1], 0, count, time, passes)
    return answers


def LinearSearch(arr, val):
    checkval(val)
    msg = w.QMessageBox()
    msg.setWindowTitle('Information')
    msg.setStandardButtons(w.QMessageBox.Ok)
    count = 0
    flag = False
    passes = []
    for i in range(len(arr)):
        count += 1
        passes.append(c.copy(arr))
        if arr[i] == val:
            flag = True
            ans = 'Value Found at Index: ' + str(i)
            msg.setText(ans)
            msg.exec_()
            break
    if not flag:
        print('Value not Found')
    time = 'O(n)'
    answers = (arr, 0, count, time, passes)
    return answers


def BinarySearch(arr, val):
    checkval(val)
    msg = w.QMessageBox()
    msg.setWindowTitle('Information')
    msg.setStandardButtons(w.QMessageBox.Ok)
    low = 0
    passes = []
    high = len(arr) - 1
    count = 0
    while low <= high:
        mid = (low + high) // 2
        count += 1
        passes.append(c.copy(arr[low:high]))
        if arr[mid] == val:
            ans = 'Value Found at Index: ' + str(mid)
            msg.setText(ans)
            msg.exec_()
            break
        elif arr[mid] < val:
            low = mid + 1
        else:
            high = mid
    answers = (arr, 0, count, "O(Logn)", passes)
    return answers


class Node:
    def _init_(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def _init_(self):
        self.head = None

    def InsertionAtBeginning(self, val):
        checkval(val)
        count = 0
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        time = 'O(1)'
        answers = (self.LinkedListToArray(), 0, count, time, [self.LinkedListToArray().copy()])
        return answers

    def InsertionAtMiddle(self, pos, val):
        checkpos(pos)
        checkval(val)
        count = 0
        if pos == 0:
            return self.InsertionAtBeginning(val)
        else:
            new_node = Node(val)
            curr = self.head
            prev = None
            while curr and count < pos:
                prev = curr
                curr = curr.next
                count += 1
            if curr:
                new_node.next = curr
                prev.next = new_node
            else:
                print("Position out of range.")
            time = 'O(n)'
            answers = (self.LinkedListToArray(), 0, count, time, [self.LinkedListToArray().copy()])
            return answers

    def InsertionAtEnd(self, val):
        checkval(val)
        if self.head == None:
            self.head = Node(val)
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = Node(val)

    def DeletionAtBeginning(self):

        count = 0
        if self.head:
            self.head = self.head.next
        else:
            print("Linked list is empty.")
        time = 'O(1)'
        answers = (self.LinkedListToArray(), 0, count, time, [self.LinkedListToArray().copy()])
        return answers

    def DeletionAtMiddle(self, pos):
        checkpos(pos)
        count = 0
        if pos == 0:
            return self.DeletionAtBeginning()
        else:
            curr = self.head
            prev = None
            while curr and count < pos:
                prev = curr
                curr = curr.next
                count += 1
            if curr:
                prev.next = curr.next
            else:
                print("Position out of range.")
            time = 'O(n)'
            answers = (self.LinkedListToArray(), 0, count, time, [self.LinkedListToArray().copy()])
            return answers

    def Updation(self, pos, val):
        checkpos(pos)
        checkval(val)
        count = 0
        curr = self.head
        while curr and count < pos:
            curr = curr.next
            count += 1
        if curr:
            curr.data = val
        else:
            print("Position out of range.")
        time = 'O(n)'
        answers = (self.LinkedListToArray(), 0, count, time, [self.LinkedListToArray().copy()])
        return answers

    def LlLinearSearch(self, val):
        msg = w.QMessageBox()
        msg.setWindowTitle('Information')
        msg.setStandardButtons(w.QMessageBox.Ok)
        passes = []
        checkval(val)
        count = -1
        curr = self.head
        flag = False
        while curr:
            count += 1
            ptr = self.head
            arr = []
            while ptr != None:
                arr.append(ptr.data)
                ptr = ptr.next
            passes.append(arr)
            if curr.data == val:
                flag = True
                ans = 'Value Found at Index: ' + str(count)
                msg.setText(ans)
                msg.exec_()
                break
            curr = curr.next

        if not flag:
            ans = 'Value Not Found'
            msg.setText(ans)
            msg.exec_()
        time = 'O(n)'
        answers = (arr, 0, count, time, passes)
        return answers

    def LinkedListToArray(self):
        array = []
        ptr = self.head
        while ptr != None:
            array.append(ptr.data)
            ptr = ptr.next
        return array


class Stack:
    def _init_(self):
        self.top = -1
        self.arr = np.array([0 for i in range(500)])

    def push(self, val):
        checkval(val)
        if self.top == 499:
            print("Stack Overflow: Cannot push element, stack is full.")
        else:
            self.top += 1
            self.arr[self.top] = val
        count = 0
        time = 'O(1)'
        answers = (self.arr[:self.top + 1], 0, count, time, [self.arr[:self.top + 1].copy()])
        return answers

    def pop(self):
        count = 0
        if self.top == -1:
            print("Stack Underflow: Cannot pop element, stack is empty.")
            return None
        else:
            popped_val = self.arr[self.top]
            self.top -= 1
            time = 'O(1)'
            answers = (self.arr[:self.top + 1], 0, count, time, [self.arr[:self.top + 1].copy()])
            return answers


class Queue:
    def _init_(self):
        self.arr = [0] * 500
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        checkval(value)
        if self.rear == 499:
            print("Queue Overflow: Cannot enqueue element, queue is full.")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.arr[self.rear] = value
        count = 0
        time = 'O(1)'
        answers = (self.arr[self.front:self.rear + 1], 0, count, time, [self.arr[self.front:self.rear + 1].copy()])
        return answers

    def dequeue(self):
        count = 0
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow: Cannot dequeue element, queue is empty.")
            return None
        else:
            dequeued_val = self.arr[self.front]
            self.front += 1
            if self.front > self.rear:
                self.front = -1
                self.rear = -1
            time = 'O(1)'
            answers = (self.arr[self.front:self.rear + 1], 0, count, time, [self.arr[self.front:self.rear + 1].copy()])
            return answers


def checkpos(pos):
    msg = w.QMessageBox()
    msg.setWindowTitle('Information')
    msg.setStandardButtons(w.QMessageBox.Ok)
    if pos == -1:
        msg.setText('Please Enter the Valid Position')
        msg.exec_()


def checkn(n):
    msg = w.QMessageBox()
    msg.setWindowTitle('Information')
    msg.setStandardButtons(w.QMessageBox.Ok)
    if n == -1:
        msg.setText('Please Enter the Valid Position')
        msg.exec_()


def checkval(val):
    msg = w.QMessageBox()
    msg.setWindowTitle('Information')
    msg.setStandardButtons(w.QMessageBox.Ok)
    if val == -1:
        msg.setText('Please Enter the Valid Position')
        msg.exec_()


# screen class widget inherit with Qdialog class dialog is ui screen
class GetStarted(w.QDialog):
    def _init_(self):  # Constructor
        super(GetStarted,
              self)._init_()  # super constructor. super means parent class current QDialog is that . in this we pass Getstarted class
        # above line telling to parents class Qdialog now we are creating get started screen
        loadUi('get started.ui', self)  # now we load start page ui
        self.gtB.clicked.connect(self.switchUI)

    def switchUI(self):  # main page ko call kar na ka method hai yeh
        uif = MainWindow()
        self.close()
        uif.exec_()


class MainWindow(w.QDialog):
    def _init_(self):
        super(MainWindow, self)._init_()
        loadUi('Main Window.ui', self)

        self.t1 = 0  # timecomplex calculate
        self.t2 = 0  # timecomplex calculate
        # Sorting Methods
        self.arraysorts = np.array(
            ['Insertion', 'Deletion', 'Linear Search', 'Binary Search', 'Bubble Sort', 'Insertion Sort',
             'Selection Sort'])
        self.linkedListsorts = np.array(
            ['Insertion at Begining', 'Insertion at Middle', 'Deletion at Begining', 'Deletion at Middle',
             'Linked List Linear Search', 'Updation'])
        self.stacksorts = np.array(['Push', 'Pop'])
        self.Queuesorts = np.array(['Enqueue', 'Dequeue'])

        self.compare.clicked.connect(self.Compare)
        self.category = self.array.text()
        self.array.clicked.connect(self.setAttributes)
        self.linked.clicked.connect(self.setAttributes)
        self.stack.clicked.connect(self.setAttributes)
        self.queue.clicked.connect(self.setAttributes)

        for i in range(len(self.arraysorts)):
            self.c1.addItem(self.arraysorts[i])
            self.c2.addItem(self.arraysorts[i])

        layout = w.QVBoxLayout()  # widget mein layout

        self.figure = plt.figure()  # figure show kar ga lines , numbers

        self.canvas = FigureCanvas(self.figure)  # white area
        self.compare = w.QPushButton("Compare", self)
        self.compare.clicked.connect(self.Compare)
        layout.addWidget(self.compare)
        layout.addWidget(self.canvas)  # qvbox mein canvas

        self.w2.setLayout(layout)  # phir layout ko widget mein w2

    # for graph
    def plot_graph(self, t1, t2):
        self.figure.clear()

        ax = self.figure.add_subplot(111)  # normal argument kuch bhi insert

        x = [i for i in range(1, len(self.intarr))]  # x axis array ki lenght tak chaly ga
        if t1 == 3:
            y1 = [m.log(i) for i in range(1, len(self.intarr))]
        else:
            y1 = [(i - 1) ** t1 for i in range(1, len(self.intarr))]

        if t2 == 3:
            y2 = [m.log(i) for i in range(1, len(self.intarr))]
        else:
            y2 = [i ** t2 for i in range(1, len(self.intarr))]

        ax.plot(x, y1, label=self.c1.currentText())  # to write name of selected c1 - blue
        ax.plot(x, y2, label=self.c2.currentText())  # to write name of selected c2 - red

        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_title('Comparasion Graph')

        ax.legend()  # means jo hum ny value insert kare hain ous ko plot kar dy na line

        self.canvas.draw()  # then draw line in canvas #call this method in initui1 and 2

    # its check value is given or generated random by clicking it
    def Compare(self):
        if self.randomval.isChecked():
            text = self.no.toPlainText()
            if text == "":
                msg = w.QMessageBox()  # message box store in msg var
                msg.setIcon(w.QMessageBox.Warning)  # and icon of it is warning
                msg.setText('Please Enter the Number of Random Values You want to Enter')
                msg.setWindowTitle('No Values')
                msg.setStandardButtons(w.QMessageBox.Ok)
                msg.exec_()
            else:
                self.intarr = np.array([rd.randrange(1, 100) for i in range(int(text))])
                self.SortingCall()
        else:
            text = str(self.valbox.toPlainText())
            if (text == ""):
                msg = w.QMessageBox()
                msg.setIcon(w.QMessageBox.Warning)
                msg.setText('Please Enter Values to Perform Operation')
                msg.setWindowTitle('No Values')
                msg.setStandardButtons(w.QMessageBox.Ok)
                msg.exec_()
            else:
                text = text.split(',')
                self.intarr = np.array([int(x) for x in text])  # value in text store in x and save in intarr
                self.SortingCall()

    def SortingCall(self):
        list, list2 = LinkedList(), LinkedList()  # objects for operations
        stack, stack2 = Stack(), Stack()
        queue, queue2 = Queue(), Queue()
        arr1 = self.intarr
        arr2 = c.copy(arr1)
        if self.category == 'Linked List':
            for i in range(len(self.intarr)):
                list.InsertionAtEnd(self.intarr[i])  # user input value insert in list 1 and list 2
            list2 = c.deepcopy(list)  # obj ky attributes copy hoky var mein save ho ry
        elif self.category == 'Stack':  # user input value insert in stack
            for i in range(len(self.intarr)):
                stack.push(self.intarr[i])
            stack2 = c.copy(stack)  # array ky elements copy ho ry
        elif self.category == 'Queue':  # user input value insert in Queue
            for i in range(len(self.intarr)):
                queue.enqueue(self.intarr[i])
            queue2 = c.copy(queue)
        my_val = self.Addval()
        my_n = self.Addn()
        my_pos = self.Addpos()
        mapping1 = {
            # value
            'Linear Search': partial(LinearSearch, arr1, my_val)
            , 'Binary Search': partial(BinarySearch, arr1, my_val)
            , 'Insertion at Begining': partial(list.InsertionAtBeginning, my_val)
            , 'Linked List Linear Search': partial(list.LlLinearSearch, my_val)
            , 'Push': partial(stack.push, my_val)
            , 'Enqueue': partial(queue.enqueue, my_val)
            # Position
            , 'Deletion': partial(Deletion, arr1, my_pos)
            , 'Deletion at Middle': partial(list.DeletionAtMiddle, my_pos)
            # position and value
            , 'Insertion': partial(Insertion, arr1, my_n, my_pos, my_val)
            , 'Insertion at Middle': partial(list.InsertionAtMiddle, my_pos, my_val)
            , 'Updation': partial(list.Updation, my_pos, my_val)
            # Noting
            , 'Bubble Sort': partial(bubbleSort, arr1)
            , 'Insertion Sort': partial(InsertionSort, arr1)
            , 'Selection Sort': partial(SelectionSort, arr1)
            , 'Deletion at Begining': partial(list.DeletionAtBeginning)
            , 'Pop': partial(stack.pop)
            , 'Dequeue': partial(queue.dequeue)
        }
        mapping2 = {
            # value
            'Linear Search': partial(LinearSearch, arr2, my_val)
            , 'Binary Search': partial(BinarySearch, arr2, my_val)
            , 'Insertion at Begining': partial(list2.InsertionAtBeginning, my_val)
            , 'Linked List Linear Search': partial(list2.LlLinearSearch, my_val)
            , 'Push': partial(stack2.push, my_val)
            , 'Enqueue': partial(queue2.enqueue, my_val)
            # Position
            , 'Deletion': partial(Deletion, arr2, my_pos)
            , 'Deletion at Middle': partial(list2.DeletionAtMiddle, my_pos)
            # position and value
            , 'Insertion': partial(Insertion, arr2, my_n, my_pos, my_val)
            , 'Insertion at Middle': partial(list2.InsertionAtMiddle, my_pos, my_val)
            , 'Updation': partial(list2.Updation, my_pos, my_val)
            # Noting
            , 'Bubble Sort': partial(bubbleSort, arr2)
            , 'Insertion Sort': partial(InsertionSort, arr2)
            , 'Selection Sort': partial(SelectionSort, arr2)
            , 'Deletion at Begining': partial(list2.DeletionAtBeginning)
            , 'Pop': partial(stack2.pop)
            , 'Dequeue': partial(queue2.dequeue)
        }
        ui1 = self.c1.currentText()  # Current Selected Operation 1
        ui2 = self.c2.currentText()  # Current Selected Operation 2
        method1 = mapping1[
            ui1]()  # now he go in mapping 1 and search current selected operation & pass its paramerters
        method2 = mapping2[
            ui2]()  # now he go in mapping 2 and search current selected operation & pass its paramerters
        # Blue
        self.initUI1(method1)
        # Red
        self.initUI2(method2)

    # for blue initUI1 & for RED initUI2
    def initUI1(self, abc):
        self.scroll = self.panel  # Assuming self.panel is the scroll area widget
        self.widget = w.QWidget()
        self.vbox = w.QVBoxLayout()
        for i in range(len(abc[4])):
            a = abc[4]
            object = w.QLabel(str(a[i]))
            object.setStyleSheet(
                'font: 15pt "Ink Free";color: rgb(255, 255, 255);background-color: rgb(107, 131, 167);margin:5px;padding: 5px;')
            object.height = 65
            object.width = 280
            self.vbox.addWidget(object)
        self.widget.setLayout(self.vbox)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        # Add the rest of your code here
        self.pass1.setText(str(abc[2]))
        self.swap1.setText(str(abc[1]))
        self.time1.setText(abc[3])
        self.val1.setText(str(len(abc[0])))
        if abc[3] == 'O(n)':
            self.t1 = 1
        elif abc[3] == 'O(n^2)':
            self.t1 = 2
        elif abc[3] == 'O(1)':
            self.t1 = 0
        elif abc[3] == 'O(Logn)':
            self.t1 = 3

    def initUI2(self, abc):
        self.scroll = self.panel2
        self.widget = w.QWidget()
        self.vbox = w.QVBoxLayout()
        for i in range(len(abc[4])):
            a = abc[4]
            object = w.QLabel(str(a[i]))
            object.setStyleSheet(
                'font: 15pt "Ink Free";color: rgb(255, 255, 255);background-color: rgb(159, 54, 54);;margin:5px;padding: 5px;')
            object.height = 65
            object.width = 280
            self.vbox.addWidget(object)
        self.widget.setLayout(self.vbox)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        # Add the rest of your code here
        self.pass2.setText(str(abc[2]))
        self.swap2.setText(str(abc[1]))
        self.time2.setText(abc[3])
        self.val2.setText(str(len(abc[0])))
        if abc[3] == 'O(n)':
            self.t2 = 1
        elif abc[3] == 'O(n^2)':
            self.t2 = 2
        elif abc[3] == 'O(1)':
            self.t2 = 0
        elif abc[3] == 'O(Logn)':
            self.t2 = 3
        self.plot_graph(self.t1, self.t2)

    def Addpos(self):
        txt = self.pos.toPlainText()
        if txt == "":
            return -1
        else:
            return int(txt)

    def Addn(self):
        txt = self.sizen.toPlainText()
        if txt == "":
            return -1
        else:
            return int(txt)

    def Addval(self):
        txt = self.val.toPlainText()
        if txt == "":
            return -1
        else:
            return int(txt)

    # Array List Stack Queue py jab hum click karain tou yeh Attr set hon
    def setAttributes(self):
        self.array.setStyleSheet('border: 5px solid rgb(40, 75, 99);color: rgb(255, 255, 255);')
        self.linked.setStyleSheet('border: 5px solid rgb(40, 75, 99);color: rgb(255, 255, 255);')
        self.stack.setStyleSheet('border: 5px solid rgb(40, 75, 99);color: rgb(255, 255, 255);')
        self.queue.setStyleSheet('border: 5px solid rgb(40, 75, 99);color: rgb(255, 255, 255);')
        btn = self.sender()
        self.c1.clear()
        self.c2.clear()
        self.category = btn.text()
        if self.category == 'Array':
            for i in range(len(self.arraysorts)):
                self.c1.addItem(self.arraysorts[i])
                self.c2.addItem(self.arraysorts[i])
        elif self.category == 'Linked List':
            for i in range(len(self.linkedListsorts)):
                self.c1.addItem(self.linkedListsorts[i])
                self.c2.addItem(self.linkedListsorts[i])
        elif self.category == 'Stack':
            for i in range(len(self.stacksorts)):
                self.c1.addItem(self.stacksorts[i])
                self.c2.addItem(self.stacksorts[i])
        elif self.category == 'Queue':
            for i in range(len(self.Queuesorts)):
                self.c1.addItem(self.Queuesorts[i])
                self.c2.addItem(self.Queuesorts[i])
        btn.setStyleSheet('background-color: rgb(40, 75, 99);color: rgb(255, 255, 255);')


if _name_ == "_main_":
    # app bana ry hum app var mein hum ny w.Qapp likh ry or ous mein sys.argv pass kar ra ry system ko app bana na ka bol ly
    app = w.QApplication(sys.argv)
    ui = GetStarted()
    ui.show()
    app.exec_()  # phir jo humein screen show kar waya ous ko application bana dou
    # Qdialog is screen and app is diff in app there is work coding.