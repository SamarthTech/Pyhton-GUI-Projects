from tkinter import * 
import tkinter as tk
from datetime import datetime
from tkinter import messagebox
import pyshorteners
import pyperclip  # Added import

class url_shortner:

    def create(self):
        if self.url.get() == "":
            messagebox.showerror("Error","Please Paste an URL")
        else:
            self.urls = self.url.get()
            self.s = pyshorteners.Shortener()
            self.short_url = self.s.tinyurl.short(self.urls)

            self.output = Entry(self.root,font=('verdana',10,'bold'),fg="purple",width=30,relief=GROOVE,borderwidth=2,border=2)
            self.output.insert(END,self.short_url)
            self.output.place(x=80,y=120)

            # Add the Copy button
            self.copy_button = Button(self.root, text="Copy", font=('verdana',8,'bold'), bg="purple", fg="white", command=self.copy_url)
            self.copy_button.place(x=310, y=118)

    def copy_url(self):
        # Copy the generated URL to clipboard
        pyperclip.copy(self.short_url)
        messagebox.showinfo("Copied", "URL copied to clipboard")

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x200')
        self.root.title('Url Shortner')
        self.root['bg'] = "white"

        # Allow both horizontal and vertical resizing
        self.root.resizable(True, True)

        self.title = Label(self.root,text="URL Shortner",font=('verdana',15,'bold'),bg="white",fg="purple")
        self.title.place(x=180,y=5)

        self.date = Label(self.root,text=datetime.now().date(),fg="purple",font=('verdana',10,'bold'))
        self.date.place(x=400,y=5)

        Label(self.root,text="Paste Your Url Here ..",font=('verdana',10,'bold'),fg="purple").place(x=50,y=50)

        self.url = Entry(self.root,width=50,bg="lightgrey",relief=GROOVE,borderwidth=2,border=2)
        self.url.place(x=50,y=80)

        self.button = Button(self.root,relief=GROOVE,text="Create",font=('verdana',8,'bold'),bg="purple",fg="white",command=self.create)
        self.button.place(x=360,y=78)
        self.root.mainloop()

if __name__ == '__main__':
    url_shortner()
