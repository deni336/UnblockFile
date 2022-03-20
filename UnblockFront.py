import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import GUI as G
import Unblock as UB

frameStyles = {"relief": "groove",
               "bd": 3, "bg": "#4b4b4b",
               "fg": "blue", "font": ("Arial", 12, "bold")}

class UnblockFront(G.GUI):

    def __init__(self, parent, controller):

        G.GUI.__init__(self, parent)

        label1 = tk.Label(self.mainFrame, font=("Arial", 20),
                          text="Unblockers R Us", background="#4b4b4b",
                          foreground="blue")
        label1.pack(side="top")

        frame1 = tk.LabelFrame(self.mainFrame, G.frameStyles, text="Unblocked Files")
        frame1.place(rely=0.05, relx=0.01, height=820, width=800)
        frame2 = tk.LabelFrame(self.mainFrame, G.frameStyles, text="Directory Selection")
        frame2.place(rely=0.05, relx=0.45, height=200, width=200)

        def loadtemplate(self):
            filename = filedialog.askdirectory()
            outputList = UB.unblock(filename)
            tv1LoadData(list(outputList))

        ttk.Button(frame2, text = "Browse", command=lambda: loadtemplate(self)).pack()
        #ttk.Button(frame2, text="Submit", command=lambda:UB.execute()).pack()
        ttk.Button(frame2, text="Clear", command=lambda: tv1ClearData()).pack()

        tv1 = ttk.Treeview(frame1)
        columnListAccount = ("Path of file unblocked", "")
        tv1['columns'] = columnListAccount
        tv1['show'] = "headings"
        for column in columnListAccount:
            tv1.heading(column, text=column)
            tv1.column(column, width=50)
        tv1.place(relheight=1, relwidth=.995)
        treeScrollY = tk.Scrollbar(frame1)
        treeScrollY.configure(command=tv1.yview)
        tv1.configure(yscrollcommand=treeScrollY.set)
        treeScrollY.pack(side="right", fill="y")

        def tv1LoadData(outputList):
            tv1ClearData()
            for i in outputList:
                tv1.insert("", "end", values=i)

        def tv1ClearData():
            tv1.delete(*tv1.get_children())