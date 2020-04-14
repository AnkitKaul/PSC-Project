from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image
import sqlite3
from tkinter import ttk

root= Tk() #root window is created
root.title('Coding Database') #Title name of the project
root.geometry("450x650") #Size of application
conn = sqlite3.connect('coders.db') #To connect to sqlite3
c = conn.cursor() #To get a cursor 
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='ccdata' ''') #To check whether ccdata table exist then return 1 or 0
if c.fetchone()[0]!=1 : { #IF count!=1 will create a new table
	c.execute("""CREATE TABLE ccdata (
        first_name text,
        last_name text,
        phnum integer,
        mail text,
        cf_id text,
        cf_rat integer,
        earth_id text,
        earth_rat integer,
        rank_id text,
        rank_rat integer,
        cc_id text,
        cc_rat integer,
        atco_id text,
        atco_rat integer
        )""")       
}
def edit():
    conn = sqlite3.connect('coders.db')
    c = conn.cursor()
    record_id=update_box.get()
    c.execute("""UPDATE ccdata SET
        first_name= :first,
        last_name= :last,
        phnum= :phone,
        mail= :mail,
        cf_id= :cf_id,
        cf_rat= :cf_rat,
        earth_id= :earth_id,
        earth_rat= :earth_rat,
        rank_id= :rank_id,
        rank_rat= :rank_rat,
        cc_id= :cc_id,
        cc_rat= :cc_rat,
        atco_id= :atco_id,
        atco_rat= atco_rat
        WHERE oid= :oid""",
        {   'first': f_name_upd.get(), 
            'last': l_name_upd.get(),
            'phone': phnumber_upd.get(),
            'mail': mail_upd.get(),
            'cf_id': cf_id_upd.get(),
            'cf_rat': cf_rat_upd.get(),
            'earth_id': earth_id_upd.get(),
            'earth_rat': earth_rat_upd.get(),
            'rank_id': rank_id_upd.get(),
            'rank_rat': rank_rat_upd.get(),
            'cc_id': cc_id_upd.get(),
            'cc_rat': cc_rat_upd.get(),
            'atco_id': atco_id_upd.get(),    
            'atco_rat': atco_rat_upd.get(),
            'oid': record_id
        })
    conn.commit()
    conn.close()
    amd.destroy()
    upd.destroy()

def update_now():
    global amd
    amd=Tk()
    amd.geometry("400x1000")
    amd.title("Update Page")
    conn = sqlite3.connect('coders.db')
    c = conn.cursor() 
    record_id=update_box.get()
    c.execute("SELECT * FROM ccdata WHERE oid=" + record_id)
    records=c.fetchall()
    #Create Global variables for text box names
    global f_name_upd
    global l_name_upd
    global phnumber_upd
    global mail_upd
    global cf_id_upd
    global cf_rat_upd
    global earth_id_upd
    global earth_rat_upd
    global rank_id_upd
    global rank_rat_upd
    global cc_id_upd
    global cc_rat_upd
    global atco_id_upd
    global atco_rat_upd
    f_name_upd= Entry(amd, width=30)
    f_name_upd.grid(row=2, column=1, padx=40, pady=(10,0))
    l_name_upd= Entry(amd, width=30)
    l_name_upd.grid(row=3, column=1, padx=40, pady=(10,0))
    phnumber_upd= Entry(amd, width=30)
    phnumber_upd.grid(row=4, column=1,padx=40,pady=(10,0))
    mail_upd= Entry(amd, width=30)
    mail_upd.grid(row=5, column=1, padx=40, pady=(10,0))
    cf_id_upd= Entry(amd, width=30)
    cf_id_upd.grid(row=6, column=1, padx=40, pady=(10,0))
    cf_rat_upd= Entry(amd, width=30)
    cf_rat_upd.grid(row=7, column=1, padx=40, pady=(10,0))
    earth_id_upd= Entry(amd, width=30)
    earth_id_upd.grid(row=8, column=1, padx=40, pady=(10,0))
    earth_rat_upd= Entry(amd, width=30)
    earth_rat_upd.grid(row=9, column=1, padx=40, pady=(10,0))
    rank_id_upd= Entry(amd, width=30)
    rank_id_upd.grid(row=10, column=1, padx=40, pady=(10,0))
    rank_rat_upd= Entry(amd, width=30)
    rank_rat_upd.grid(row=11, column=1, padx=40, pady=(10,0))
    cc_id_upd= Entry(amd, width=30)
    cc_id_upd.grid(row=12, column=1, padx=40, pady=(10,0))
    cc_rat_upd= Entry(amd, width=30)
    cc_rat_upd.grid(row=13, column=1, padx=40, pady=(10,0))
    atco_id_upd= Entry(amd, width=30)
    atco_id_upd.grid(row=14, column=1, padx=40, pady=(10,0))
    atco_rat_upd= Entry(amd, width=30)
    atco_rat_upd.grid(row=15, column=1, padx=40, pady=(10,0))
    #To Create Text Box Labels
    f_name_upd_label= Label(amd,text="First Name")
    f_name_upd_label.grid(row=2, column=0, pady=(10,0))
    l_name_upd_label= Label(amd,text="Last Name")
    l_name_upd_label.grid(row=3, column=0, pady=(10,0))
    phnumber_upd_label= Label(amd,text="Phone Number")
    phnumber_upd_label.grid(row=4, column=0, pady=(10,0))
    mail_upd_label= Label(amd,text="Email")
    mail_upd_label.grid(row=5, column=0, pady=(10,0))
    cf_id_upd_label= Label(amd,text="Codeforces Id")
    cf_id_upd_label.grid(row=6, column=0, pady=(10,0))
    cf_rat_upd_label= Label(amd,text="Codeforces Rating")
    cf_rat_upd_label.grid(row=7, column=0, pady=(10,0))
    earth_id_upd_label= Label(amd,text="Hackerearth Id")
    earth_id_upd_label.grid(row=8, column=0, pady=(10,0))
    earth_rat_upd_label= Label(amd,text="Hackerearth Rating")
    earth_rat_upd_label.grid(row=9, column=0, pady=(10,0))
    rank_id_upd_label= Label(amd,text="Hackerrank Id")
    rank_id_upd_label.grid(row=10, column=0, pady=(10,0))
    rank_rat_upd_label= Label(amd,text="Hackerrank Rating")
    rank_rat_upd_label.grid(row=11, column=0, pady=(10,0))
    cc_id_upd_label= Label(amd,text="Codechef Id")
    cc_id_upd_label.grid(row=12, column=0, pady=(10,0))
    cc_rat_upd_label= Label(amd,text="Codchef Rating")
    cc_rat_upd_label.grid(row=13, column=0, pady=(10,0))
    atco_id_upd_label= Label(amd,text="Atcoder Id")
    atco_id_upd_label.grid(row=14, column=0, pady=(10,0))
    atco_rat_upd_label= Label(amd,text="Atcoder Rating")
    atco_rat_upd_label.grid(row=15, column=0, pady=(10,0))

    #Loop through Results
    for record in records:
        f_name_upd.insert(0, record[0])
        l_name_upd.insert(0, record[1])
        phnumber_upd.insert(0, record[2])
        mail_upd.insert(0, record[3])
        cf_id_upd.insert(0, record[4])
        cf_rat_upd.insert(0, record[5])
        earth_id_upd.insert(0, record[6])
        earth_rat_upd.insert(0, record[7])
        rank_id_upd.insert(0, record[8])
        rank_rat_upd.insert(0, record[9])
        cc_id_upd.insert(0, record[10])
        cc_rat_upd.insert(0, record[11])
        atco_id_upd.insert(0, record[12])
        atco_rat_upd.insert(0, record[13])
    #Create a save button
    update_btn= Button(amd,text="Save Update",command=edit)
    update_btn.grid(row=16,column=0,columnspan=2,pady=10,padx=10,ipadx=135)
    conn.commit()
    conn.close()

def update():
    global upd
    upd= Tk()
    upd.title('Update Page')
    upd.geometry("400x300")
    conn = sqlite3.connect('coders.db')
    c = conn.cursor() 
    global update_box 
    update_box= Entry(upd)
    update_box.grid(row=0,column=1,padx=10,pady=10)
    update_box_label=Label(upd,text="Enter Id Number")
    update_box_label.grid(row=0,column=0,padx=10,pady=10)
    update_button= Button(upd,text="Update Customer",command=update_now)
    update_button.grid(row=1,column=0,ipadx=10)
    

def add():
    conn = sqlite3.connect('coders.db')
    c = conn.cursor()
    c.execute("INSERT INTO ccdata VALUES(:f_name, :l_name, :phnumber, :mail, :cf_id, :cf_rat, :earth_id, :earth_rat, :rank_id, :rank_rat, :cc_id, :cc_rat, :atco_id, :atco_rat)", 
        {   'f_name': f_name.get(),
            'l_name': l_name.get(),
            'phnumber': phnumber.get(),   
            'mail': mail.get(),
            'cf_id': cf_id.get(),
            'cf_rat': cf_rat.get(),
            'earth_id': earth_id.get(),
            'earth_rat': earth_rat.get(),
            'rank_id': rank_id.get(),
            'rank_rat': rank_rat.get(),
            'cc_id': cc_id.get(),
            'cc_rat': cc_rat.get(),
            'atco_id': atco_id.get(),
            'atco_rat': atco_rat.get()
        })
    conn.commit()
    conn.close()
    #Clear the Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    phnumber.delete(0, END)
    mail.delete(0, END)
    cf_id.delete(0, END)
    cf_rat.delete(0, END)
    earth_id.delete(0, END)
    earth_rat.delete(0, END)
    rank_id.delete(0, END)
    rank_rat.delete(0, END)
    cc_id.delete(0, END)
    cc_rat.delete(0, END) 
    atco_id.delete(0, END)
    atco_rat.delete(0, END)

def query():
    ad=Tk()
    ad.geometry("1500x300")
    conn = sqlite3.connect('coders.db')
    c = conn.cursor()
    ad.title("Display Page")
    label=Label(ad, text="Coding Database Table\n\n", font=("Arial",15)).grid(row=0,column=0,columnspan=3)
    #Query the database
    c.execute("SELECT oid,* FROM ccdata")
    records=c.fetchall()
    #Loop through Result
    lookup_label=Label(ad, text="ID")
    lookup_label.grid(row=0,column=0,pady=(10,0))
    lookup_label=Label(ad, text="First Name")
    lookup_label.grid(row=0,column=1,pady=(10,0))
    lookup_label=Label(ad, text="Last Name")
    lookup_label.grid(row=0,column=2,pady=(10,0))
    lookup_label=Label(ad, text="Phone Number")
    lookup_label.grid(row=0,column=3,pady=(10,0))
    lookup_label=Label(ad, text="Email")
    lookup_label.grid(row=0,column=4,pady=(10,0))
    lookup_label=Label(ad, text="Codeforces Id")
    lookup_label.grid(row=0,column=5,pady=(10,0))
    lookup_label=Label(ad, text="Codeforces Rank")
    lookup_label.grid(row=0,column=6,pady=(10,0))
    lookup_label=Label(ad, text="Hackerearth Id")
    lookup_label.grid(row=0,column=7,pady=(10,0))
    lookup_label=Label(ad, text="Hackerearth Rank")
    lookup_label.grid(row=0,column=8,pady=(10,0))
    lookup_label=Label(ad, text="Hackerrank Id")
    lookup_label.grid(row=0,column=9,pady=(10,0))
    lookup_label=Label(ad, text="Hackerrank Rank")
    lookup_label.grid(row=0,column=10,pady=(10,0))
    lookup_label=Label(ad, text="Codechef Id")
    lookup_label.grid(row=0,column=11,pady=(10,0))
    lookup_label=Label(ad, text="Codechef Rank")
    lookup_label.grid(row=0,column=12,pady=(10,0))
    lookup_label=Label(ad, text="AtCoder Id")
    lookup_label.grid(row=0,column=13,pady=(10,0))
    lookup_label=Label(ad, text="Atcoder Rank")
    lookup_label.grid(row=0,column=14,pady=(10,0))
    lookup_label=Label(ad, text="")
    for index,record in enumerate(records):
        num=0
        for i in record:
            if i=='':
                lookup_label=Label(ad, text="NULL")
                lookup_label.grid(row=index+1,column=num,pady=(10,0))
            else :
                lookup_label=Label(ad, text=i)
                lookup_label.grid(row=index+1,column=num,pady=(10,0))
            num+=1
    conn.commit()
    conn.close()
def clear():
    f_name.delete(0, END)
    l_name.delete(0, END)
    phnumber.delete(0, END)
    mail.delete(0, END)
    cf_id.delete(0, END)
    cf_rat.delete(0, END)
    earth_id.delete(0, END)
    earth_rat.delete(0, END)
    rank_id.delete(0, END)
    rank_rat.delete(0, END)
    cc_id.delete(0, END)
    cc_rat.delete(0, END) 
    atco_id.delete(0, END)
    atco_rat.delete(0, END)

def search():
    ad=Tk()
    ad.geometry("500x300")
    conn = sqlite3.connect('coders.db')
    c = conn.cursor()
    ad.title("Search Page")
    def search_now():
        md=Tk()
        md.geometry("1500x300")
        md.title("Output Page")
        conn = sqlite3.connect('coders.db')
        c = conn.cursor()
        searched= search_box.get()
        c.execute("SELECT oid,* FROM ccdata")
        records=c.fetchall()
        s=0
        lookup_label=Label(md, text="ID")
        lookup_label.grid(row=0,column=0,pady=(10,0))
        lookup_label=Label(md, text="First Name")
        lookup_label.grid(row=0,column=1,pady=(10,0))
        lookup_label=Label(md, text="Last Name")
        lookup_label.grid(row=0,column=2,pady=(10,0))
        lookup_label=Label(md, text="Phone Number")
        lookup_label.grid(row=0,column=3,pady=(10,0))
        lookup_label=Label(md, text="Email")
        lookup_label.grid(row=0,column=4,pady=(10,0))
        lookup_label=Label(md, text="Codeforces Id")
        lookup_label.grid(row=0,column=5,pady=(10,0))
        lookup_label=Label(md, text="Codeforces Rank")
        lookup_label.grid(row=0,column=6,pady=(10,0))
        lookup_label=Label(md, text="Hackerearth Id")
        lookup_label.grid(row=0,column=7,pady=(10,0))
        lookup_label=Label(md, text="Hackerearth Rank")
        lookup_label.grid(row=0,column=8,pady=(10,0))
        lookup_label=Label(md, text="Hackerrank Id")
        lookup_label.grid(row=0,column=9,pady=(10,0))
        lookup_label=Label(md, text="Hackerrank Rank")
        lookup_label.grid(row=0,column=10,pady=(10,0))
        lookup_label=Label(md, text="Codechef Id")
        lookup_label.grid(row=0,column=11,pady=(10,0))
        lookup_label=Label(md, text="Codechef Rank")
        lookup_label.grid(row=0,column=12,pady=(10,0))
        lookup_label=Label(md, text="AtCoder Id")
        lookup_label.grid(row=0,column=13,pady=(10,0))
        lookup_label=Label(md, text="Atcoder Rank")
        lookup_label.grid(row=0,column=14,pady=(10,0))
        lookup_label=Label(md, text="")
        for index,record in enumerate(records):
            if record[1]==searched:
                num=0
                s+=1
                for i in record:
                    if i=='':
                        lookup_label=Label(md, text="NULL")
                        lookup_label.grid(row=index+1,column=num,pady=10)
                    else:
                        lookup_label=Label(md, text=i)
                        lookup_label.grid(row=index+1,column=num,pady=10)
                    num+=1
        if s==0:
            lookup_label=Label(md,text="No Record Found")
            lookup_label.grid(row=4,column=0)
        ad.destroy()
        
    search_box= Entry(ad)
    search_box.grid(row=0,column=1,padx=10,pady=10)
    search_box_label=Label(ad,text="Enter First Name")
    search_box_label.grid(row=0,column=0,padx=10,pady=10)
    search_button= Button(ad,text="Search Customer", command=search_now)
    search_button.grid(row=1,column=0,padx=10)
    conn.commit()
    conn.close()

def delete():
    ad=Tk()
    ad.title("Delete Page")
    ad.geometry("300x100")
    conn = sqlite3.connect('coders.db')
    c = conn.cursor()
    def delete_now():
        conn = sqlite3.connect('coders.db')
        c = conn.cursor()
        c.execute("DELETE from ccdata WHERE oid=" + delete_box.get())
        delete_box.delete(0, END)
        conn.commit()
        conn.close()
        ad.destroy()
    delete_box= Entry(ad)
    delete_box.grid(row=0,column=1,padx=10,pady=10)
    delete_box_label=Label(ad,text="Enter Id Number")
    delete_box_label.grid(row=0,column=0,padx=10,pady=10)
    delete_button= Button(ad,text="Delete Customer",command=delete_now)
    delete_button.grid(row=1,column=0,ipadx=10)
    conn.commit()
    conn.close()

#To Create Text Boxes
f_name= Entry(root, width=30)
f_name.grid(row=2, column=1,  pady=(10,0))
l_name= Entry(root, width=30)
l_name.grid(row=3, column=1,  pady=(10,0))
phnumber= Entry(root, width=30)
phnumber.grid(row=4, column=1,  pady=(10,0))
mail= Entry(root, width=30)
mail.grid(row=5, column=1,  pady=(10,0))
cf_id= Entry(root, width=30)
cf_id.grid(row=6, column=1,  pady=(10,0))
cf_rat= Entry(root, width=30)
cf_rat.grid(row=7, column=1,  pady=(10,0))
earth_id= Entry(root, width=30)
earth_id.grid(row=8, column=1,  pady=(10,0))
earth_rat= Entry(root, width=30)
earth_rat.grid(row=9, column=1,  pady=(10,0))
rank_id= Entry(root, width=30)
rank_id.grid(row=10, column=1,  pady=(10,0))
rank_rat= Entry(root, width=30)
rank_rat.grid(row=11, column=1,  pady=(10,0))
cc_id= Entry(root, width=30)
cc_id.grid(row=12, column=1,  pady=(10,0))
cc_rat= Entry(root, width=30)
cc_rat.grid(row=13, column=1,  pady=(10,0))
atco_id= Entry(root, width=30)
atco_id.grid(row=14, column=1,  pady=(10,0))
atco_rat= Entry(root, width=30)
atco_rat.grid(row=15, column=1,  pady=(10,0))
#To Create Text Box Labels
f_name_label= Label(root,text="First Name")
f_name_label.grid(row=2, column=0, pady=(10,0))
l_name_label= Label(root,text="Last Name")
l_name_label.grid(row=3, column=0, pady=(10,0))
phnumber_label= Label(root,text="Phone Number")
phnumber_label.grid(row=4, column=0, pady=(10,0))
mail_label= Label(root,text="Email")
mail_label.grid(row=5, column=0, pady=(10,0))
cf_id_label= Label(root,text="Codeforces Id")
cf_id_label.grid(row=6, column=0, pady=(10,0))
cf_rat_label= Label(root,text="Codeforces Rating")
cf_rat_label.grid(row=7, column=0, pady=(10,0))
earth_id_label= Label(root,text="Hackerearth Id")
earth_id_label.grid(row=8, column=0, pady=(10,0))
earth_rat_label= Label(root,text="Hackerearth Rating")
earth_rat_label.grid(row=9, column=0, pady=(10,0))
rank_id_label= Label(root,text="Hackerrank Id")
rank_id_label.grid(row=10, column=0, pady=(10,0))
rank_rat_label= Label(root,text="Hackerrank Rating")
rank_rat_label.grid(row=11, column=0, pady=(10,0))
cc_id_label= Label(root,text="Codechef Id")
cc_id_label.grid(row=12, column=0, pady=(10,0))
cc_rat_label= Label(root,text="Codchef Rating")
cc_rat_label.grid(row=13, column=0, pady=(10,0))
atco_id_label= Label(root,text="Atcoder Id")
atco_id_label.grid(row=14, column=0, pady=(10,0))
atco_rat_label= Label(root,text="Atcoder Rating")
atco_rat_label.grid(row=15, column=0, pady=(10,0))

#Create Submit Button
submit_btn= Button(root,text="Add Record to Database", command=add)
submit_btn.grid(row=16, column=0, pady=10)

query_btn= Button(root,text="Display Record",command=query)
query_btn.grid(row=16, column=2,pady=10)

searc_btn= Button(root,text="Search the Entry", command=search)
searc_btn.grid(row=17,column=0, pady=10)

delete_btn= Button(root,text="Delete Entry", command=delete)
delete_btn.grid(row=17,column=2,pady=10)

update_btn= Button(root,text="Update the Record",command=update)
update_btn.grid(row=18,column=0,pady=10)


clear_btn= Button(root,text="Clear the Record",command=clear)
clear_btn.grid(row=18,column=2,pady=10)

button_quit= Button(root,text="Exit Program",command=root.quit)
button_quit.grid(row=17,column=1)

conn.close()
root.mainloop()