import Tkinter
import csv
from xml.dom.minidom import parse
import xml.dom.minidom
import sys
sys.path.append('C:\Users\dell\AppData\Local\Programs\Python\Python36\Lib\site-packages')
from csvfileread import csvfile,csvfiletransform,csvfileload
from textfileread import textfile,textfiletransform,textfileload
from xmlfileread import xmlfile,xmlfiletransform,xmlfileload
class ETL_interface(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        button = Tkinter.Button(self,text=u"EXTRACT",
                                command=self.extract,height=1,width=20)
        button.grid(column=0,row=1)
        button.config(font=('times',20,'bold'))

        button1 = Tkinter.Button(self,text=u"TRANSFORM",
                                command=self.transform,height=1,width=20)
        button1.grid(column=1,row=1)
        button1.config(font=('times',20,'bold'))

        button2 = Tkinter.Button(self,text=u"LOAD",
                                command=self.load,height=1,width=20)
        button2.grid(column=2,row=1)
        button2.config(font=('times',20,'bold'))

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=0,columnspan=3,sticky='EW')
        self.labelVariable.set(u"You gave no command!!")

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())       

    def extract(self):
        self.labelVariable.set( "You gave a command to EXTRACT data!!" )
        print("CSV FILE IS -->")
        csvfile()
        print("TEXT FILE IS -->")
        textfile()
        print("XML FILE IS -->")
        xmlfile()

    def transform(self):
        self.labelVariable.set( "You gave a command to TRANSFORM data!!" )
        print("TRANSFORMED CSV FILE IS -->")
        csvfiletransform()
        print("TRANSFORMED TEXT FILE IS -->")
        textfiletransform()
        print("TRANSFORMED XML FILE IS -->")
        xmlfiletransform()

    def load(self):
        self.labelVariable.set( "You gave a command to LOAD data!!" )
        csvfileload()
        textfileload()
        xmlfileload()

if __name__ == "__main__":
    app = ETL_interface(None)
    app.title('EXTRACT, TRANSFORM, LOAD')
    app.mainloop()