import csv
import tkinter as tk
from tkinter import PhotoImage, ttk
from tkinter.messagebox import showinfo
from turtle import window_width

def showmenu():
    headingtext.pack(ipady=10)
    menutext.pack(ipady=5)
    menuframe.pack()
    seebutton.grid(column=0,row=0,padx=5)
    addbutton.grid(column=1,row=0,padx=5)
    updatebutton.grid(column=2,row=0,padx=5)
    exitbutton.grid(column=3,row=0,padx=5)
def hidemenu():
    headingtext.pack_forget()
    menutext.pack_forget()
    seebutton.pack_forget()
    addbutton.pack_forget()
    updatebutton.pack_forget()
    exitbutton.pack_forget()
    menuframe.pack_forget()

def see_details():
    seeframe.pack()
    identrytext.grid(column=0,row=0,sticky=tk.W,padx=(0,5),pady=(5,5))
    idbox.grid(column=1,row=0,sticky=tk.E,padx=(0,5),pady=(5,5))
    searchbutton.grid(column=2,row=0,sticky=tk.E,padx=0,pady=(5,5))
    menubutton.pack(anchor="sw")
    hidemenu()
def see_search():
    search_id=stu_id.get()
    f=open("school_records.csv","r",newline="")
    fo=csv.reader(f)
    for i in fo:
        if search_id==i[0]:
            details=i
            idfound=True
            break
    else:
        showinfo(title="info",message="Not Found")
        idfound=False
    f.close()
    menubutton.pack_forget()
    if idfound:
        idtext.config(text=f"Student ID:{details[0]}")
        idtext.grid(column=1,row=1,sticky=tk.W,padx=5)
        nametext.config(text=f"Name:{details[1]}")
        nametext.grid(column=1,row=2,sticky=tk.W,padx=5)
        classtext.config(text=f"Class:{details[2]}")
        classtext.grid(column=1,row=3,sticky=tk.W,padx=5)
        rolltext.config(text=f"Roll no:{details[3]}")
        rolltext.grid(column=1,row=4,sticky=tk.W,padx=5)
        idbox.delete(0,'end')
    else:
        idtext.pack_forget()
        nametext.pack_forget()
        classtext.pack_forget()
        rolltext.pack_forget()
    menubutton.pack(anchor="sw")

def menu():
    showmenu()
    seeframe.pack_forget()
    identrytext.pack_forget()
    idbox.pack_forget()
    searchbutton.pack_forget()
    idtext.pack_forget()
    nametext.pack_forget()
    classtext.pack_forget()
    rolltext.pack_forget()
    menubutton.pack_forget()
    addformframe.pack_forget()
    enternametext.pack_forget()
    namebox.pack_forget()
    enterclasstext.pack_forget()
    classbox.pack_forget()
    enterrolltext.pack_forget()
    rollbox.pack_forget()
    submitbutton.pack_forget()
    updateframe.pack_forget()
    update_identrytext.grid_remove()
    update_idbox.grid_remove()
    update_openbutton.grid_remove()
    

def add_details():
    addformframe.pack()
    enternametext.grid(column=0,row=0,sticky=tk.W,pady=5)
    namebox.grid(column=1,row=0,sticky=tk.W,pady=5)
    enterclasstext.grid(column=0,row=1,sticky=tk.W,pady=5)
    classbox.grid(column=1,row=1,sticky=tk.W,pady=5)
    enterrolltext.grid(column=0,row=2,sticky=tk.W,pady=5)
    rollbox.grid(column=1,row=2,sticky=tk.W,pady=5)
    submitbutton.grid(column=0,row=3,sticky=tk.W,pady=5)
    menubutton.pack(anchor="sw")
    hidemenu()
def add_submit():
    f=open("school_records.csv","r",newline="")
    fo=csv.reader(f)
    records_list=[]
    for i in fo:
        last_i=i
        records_list.append(i)
    if records_list==[]:
        stu_id=1
    else:
        stu_id=int(last_i[0])+1
    f.close()
    details=[stu_id,stu_name.get(),stu_class.get(),stu_roll.get()]
    f=open("school_records.csv","a",newline="")
    fo=csv.writer(f)
    fo.writerow(details)
    f.close()
    namebox.delete(0, "end")
    classbox.delete(0,"end")
    rollbox.delete(0,"end")
    showinfo(title="info",message="Successfully Submitted!")

def update_details():
    updateframe.pack()
    update_identrytext.grid(column=0,row=0,sticky=tk.W,padx=(0,5),pady=(5,5))
    update_idbox.grid(column=1,row=0,sticky=tk.E,padx=(0,5),pady=(5,5))
    update_openbutton.grid(column=2,row=0,sticky=tk.E,padx=0,pady=(5,5))
    menubutton.pack(anchor="sw")
    hidemenu()

def update_open():
    search_id=update_stu_id.get()
    f=open("school_records.csv","r",newline="")
    fo=csv.reader(f)
    for i in fo:
        if search_id==i[0]:
            details=i
            idfound=True
            break
    else:
        showinfo(title="info",message="Not Found")
        idfound=False
    f.close()
    menubutton.pack_forget()
    if idfound:
        update_idtext.config(text=f"Student ID:{details[0]}")
        update_idtext.grid(column=0,row=1,sticky=tk.W,padx=5)
        update_enternametext.grid(column=0,row=2,sticky=tk.W,padx=5)
        update_namebox.delete(0,'end')
        update_namebox.insert(0,f"{details[1]}")
        update_namebox.grid(column=1,row=2,sticky=tk.W,padx=5)
        update_enterclasstext.grid(column=0,row=3,sticky=tk.W,padx=5)
        update_classbox.delete(0,'end')
        update_classbox.insert(0,f"{details[2]}")
        update_classbox.grid(column=1,row=3,sticky=tk.W,padx=5)
        update_enterrolltext.grid(column=0,row=4,sticky=tk.W,padx=5)
        update_rollbox.delete(0,'end')
        update_rollbox.insert(0,f"{details[3]}")
        update_rollbox.grid(column=1,row=4,sticky=tk.W,padx=5)
        update_submitbutton.grid(column=0,row=5)
    else:
        idtext.pack_forget()
        nametext.pack_forget()
        classtext.pack_forget()
        rolltext.pack_forget()
    menubutton.pack(anchor="sw")
def update_submit():
    f=open("school_records.csv","r",newline="")
    fo=csv.reader(f)
    records_list=[]
    count=0
    for i in fo:
        records_list.append(i)
        if int(i[0])==int(update_stu_id.get()):
            index=count
        count+=1
    f.close()
    details=[update_stu_id.get(),update_stu_name.get(),update_stu_class.get(),update_stu_roll.get()]
    records_list[index]=details
    f=open("school_records.csv","w",newline="")
    fo=csv.writer(f)
    fo.writerows(records_list)
    f.close()
    update_namebox.delete(0, "end")
    update_classbox.delete(0,"end")
    update_rollbox.delete(0,"end")
    update_idbox.delete(0,'end')
    update_idtext.grid_remove()
    update_enternametext.grid_remove()
    update_namebox.grid_remove()
    update_enterclasstext.grid_remove()
    update_classbox.grid_remove()
    update_enterrolltext.grid_remove()
    update_rollbox.grid_remove()
    update_submitbutton.grid_remove()
    showinfo(title="info",message="Successfully Updated!")

root=tk.Tk()
root.title("School Records Management")
win_w=400
win_h=300
screen_w=root.winfo_screenwidth()
screen_h=root.winfo_screenheight()
center_x=int(screen_w/2-win_w/2)
center_y=int(screen_h/2-win_h/2)
root.geometry(f'{win_w}x{win_h}+{center_x}+{center_y}')
#root.resizable(False,False)

#heading
headingtext=ttk.Label(root,text="Welcome",font=("Helvetica",14))

#menu
menuframe=ttk.Frame(root)
menuframe.columnconfigure(0,weight=1)
menuframe.columnconfigure(1,weight=1)
menuframe.columnconfigure(2,weight=1)
menuframe.columnconfigure(3,weight=1)
menutext=ttk.Label(root,text="what do you want to you?")
seebutton=ttk.Button(menuframe,text="See Details",command=see_details)
addbutton=ttk.Button(menuframe,text="Add Details",command=add_details)
updatebutton=ttk.Button(menuframe,text="Update Details",command=update_details)
exitbutton=ttk.Button(menuframe,text="Exit",command=exit)


#see details
seeframe=ttk.Frame(root)
seeframe.columnconfigure(0)
seeframe.columnconfigure(1)
seeframe.columnconfigure(2)
identrytext=ttk.Label(seeframe,text="Enter student id:")
stu_id=tk.StringVar()
idbox=ttk.Entry(seeframe,textvariable=stu_id)
searchbutton=ttk.Button(seeframe,text="Search",command=see_search)
#searchbutton.bind('<KeyPress-Enter>',see_search)
idtext=ttk.Label(seeframe,text="Student ID:")
nametext=ttk.Label(seeframe,text="Name:")
classtext=ttk.Label(seeframe,text="Class:")
rolltext=ttk.Label(seeframe,text="Roll no:")

#menu button
back_arrow_image=PhotoImage(file="back-arrow-icon.png")
back_arrow_icon=back_arrow_image.subsample(25,25)
menubutton=ttk.Button(root,text="Menu",command=menu,image=back_arrow_icon,compound="left")


#add details
addformframe=ttk.Frame(root)
addformframe.columnconfigure(0)
addformframe.columnconfigure(1)
enternametext=ttk.Label(addformframe,text="Enter name:")
stu_name=tk.StringVar()
namebox=ttk.Entry(addformframe,textvariable=stu_name)
enterclasstext=ttk.Label(addformframe,text="Enter class:")
stu_class=tk.StringVar()
classbox=ttk.Entry(addformframe,textvariable=stu_class)
enterrolltext=ttk.Label(addformframe,text="Enter roll no:")
stu_roll=tk.StringVar()
rollbox=ttk.Entry(addformframe,textvariable=stu_roll)
submitbutton=ttk.Button(addformframe,text='Submit',command=add_submit)

#updatedetails
updateframe=ttk.Frame(root)
updateframe.columnconfigure(0)
updateframe.columnconfigure(1)
update_identrytext=ttk.Label(updateframe,text="Enter student ID:")
update_stu_id=tk.StringVar()
update_idbox=ttk.Entry(updateframe,textvariable=update_stu_id)
update_openbutton=ttk.Button(updateframe,text="Open",command=update_open)
update_idtext=ttk.Label(updateframe)
update_enternametext=ttk.Label(updateframe,text="Name:")
update_stu_name=tk.StringVar()
update_namebox=ttk.Entry(updateframe,textvariable=update_stu_name)
update_enterclasstext=ttk.Label(updateframe,text="Class:")
update_stu_class=tk.StringVar()
update_classbox=ttk.Entry(updateframe,textvariable=update_stu_class)
update_enterrolltext=ttk.Label(updateframe,text="Roll no:")
update_stu_roll=tk.StringVar()
update_rollbox=ttk.Entry(updateframe,textvariable=update_stu_roll)
update_submitbutton=ttk.Button(updateframe,text='Submit',command=update_submit)


showmenu()

root.mainloop()