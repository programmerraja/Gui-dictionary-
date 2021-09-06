""" this is simple online dictionary"""

import tkinter as t
import requests as r
from bs4 import BeautifulSoup as soup
from tkinter import messagebox
from tkinter import scrolledtext as scroll

class dictnaroy:
    def __init__(self):
        root=t.Tk()
        root.geometry("280x240"+"+"+str(int(root.winfo_screenwidth()/5))+"+"+str(int(root.winfo_screenheight()/5)))
        root.title("Dictionary")
        root.resizable(0,0)
        t.Label(root,text="Enter the word here: ").place(x=10,y=20)
        self.word=t.Entry()
        self.word.place(x=130,y=20)
        self.text_word=scroll.ScrolledText(root,width=30,height=10,wrap="word")
        self.text_word.place(x=10,y=50)
        self.word.bind("<Return>",self.search)
        
        root.mainloop()
    def search(self,event):
        if(self.word.get()):
            try:
                self.text_word.delete("1.0")
                self.text_word["state"]="normal"
                msg=soup( r.get("https://lexico.com/en/definition/"+self.word.get()).text,"html.parser").find("meta")["content"]
                self.text_word.insert("1.0",msg)
                self.text_word["state"]="disabled"
                
            except:
                messagebox.showinfo("Error","Plse connect to internet")

app=dictnaroy()

