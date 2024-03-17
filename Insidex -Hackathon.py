import pickle
from tkinter.ttk import Combobox
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import askyesno
import yaml
from PIL import ImageTk,Image
import mysql.connector


root=Tk()
root.title("INSIDEX")
root.geometry("1200x900")
root.state('zoomed')
def canvas(a,file):
        global my_canvas,new_bg
        my_canvas=Canvas(a,width=800,height=500) 
        my_canvas.pack(fill="both",expand=True)
        ico=ImageTk.PhotoImage(Image.open(r"Images\ins.jpeg"))
        root.iconphoto(False,ico)
        def resizer(e):
                global bg1,resized_bg,new_bg
                bg1=Image.open(file)
                resized_bg=bg1.resize((e.width,e.height),Image.ANTIALIAS)
                new_bg=ImageTk.PhotoImage(resized_bg)
                my_canvas.create_image(0,0,image=new_bg,anchor="nw")    
        my_canvas.bind("<Configure>",resizer)
        root.geometry("1200x900")
status=1
#establishing connection to the SQL Table
m=mysql.connector.connect(host='localhost',user='root',passwd='Sanju@1712',database='sanjay')
c=m.cursor()
logo=Image.open("Images\logo2.jpeg")
resized=logo.resize((300,100),Image.ANTIALIAS)
new_pic=ImageTk.PhotoImage(resized)
f=open("Areas1.dat",'rb')
temp={}
temp=pickle.load(f)
f.close()
login_btn=PhotoImage(file=r"Images\login.png").subsample(3,3)
def admin():#for admin operations
        def back1():
                frame.place_forget()
                my_canvas.destroy()
                admin()
        def login():
                user=un.get()
                password=pw.get()
                userpw={'Sai Sanjay':'Sanju@1712','MR sparky':'suryaisadhonifan','Sumukesh':'Sumu!@123'}
                if user in userpw and userpw[user]==password:
                        global status
                        status=0
                else:
                        messagebox.showerror('WARNING BY INSIDEX','You have entered the wrong username/password')
                        status=1
                
                if status==0:
                        frame1.place_forget()
                        global frame
                        frame=Frame(my_canvas,width=500,height=400,bg='#00ddff',highlightbackground='#ff00d4',highlightthickness=3,relief=RAISED)
                        Label(frame,text="ADMIN OPERATIONS",font=("Castellar",25,"bold"),bg="#ee2a7b",fg="white").place(x=75,y=10)
                        insertbutton=Button(frame,text="Insert",font="Castellar 15",command=insert,padx=30,pady=30,bg="#FF5349")
                        insertbutton.place(x=50,y=100)
                        deletebutton=Button(frame,text="Delete",font="Castellar 15",command=delete,padx=30,pady=30,bg="#0555c3")
                        deletebutton.place(x=300,y=100)
                        updatebutton=Button(frame,text="Update",font="Castellar 15",command=update,padx=30,pady=30,bg="#69e09b")
                        updatebutton.place(x=175,y=250)
                        Button(frame,text='Back',command=back1).place(x=50,y=300)
                        frame.place(x=725,y=200) 
        my_canvas.destroy()
        canvas(root,r'Images\admin.jpg')
        frame1=Frame(my_canvas,width=500,height=400,bg='#00ddff',highlightbackground='#ff00d4',highlightthickness=3)
        def back():
                frame1.place_forget()
                my_canvas.destroy()
                home()
        lab=Label(frame1,text="ADMIN LOGIN PAGE",font=("Castellar",25,"bold"),bg="#ee2a7b",fg="white")
        lab.place(x=70,y=5)
        def on_enter(e):
                un.delete(0,'end')
        def on_leave(e):
                if un.get()=='':
                        un.insert(0,'Username')
        un=Entry(frame1,width=25,fg='black',bg='#00ddff',border=0,font=('Microsoft Yahei UI Light',11))
        un.place(x=30,y=80)
        un.insert(0,'Username')
        un.bind('<FocusIn>',on_enter)
        un.bind('<FocusOut>',on_leave)
        Frame(frame1,width=295,height=2,bg='black').place(x=25,y=107)
        def on_enter(e):
                pw.delete(0,'end')
                pw.config(show='*')
        def on_leave(e):
                if pw.get()=='':
                        pw.insert(0,'Password')
        pw=Entry(frame1,width=25,fg='black',bg='#00ddff',border=0,font=('Microsoft Yahei UI Light',11))
        pw.place(x=30,y=130)
        pw.insert(0,'Password')
        pw.bind('<FocusIn>',on_enter)
        pw.bind('<FocusOut>',on_leave)
        Frame(frame1,width=295,height=2,bg='black').place(x=25,y=157)
        def toggle_password():
                if pw.cget('show') == '':
                        pw.config(show='*')
                        toggle_btn.config(text='Show Password')
                else:
                        pw.config(show='')
                        toggle_btn.config(text='Hide Password')
        toggle_btn =Button(frame1, text='Show Password',command=toggle_password,bg='#cc8899')
        toggle_btn.place(x=350,y=137)   
        Button(frame1,image=login_btn,command=login,borderwidth=0).place(x=150,y=200)
        Button(frame1, text="Back", command=back).place(x=80,y=200)
        frame1.place(x=750,y=200)
        
        def insert():
                frame.place_forget()
                root.title("Insert")
                ins=Frame(my_canvas,width=500,height=400,bg='#00ddff',highlightbackground='#ff00d4',highlightthickness=3)
                Label(ins,text='INSERTION OF RECORDS',font=("Castellar",25,"bold"),bg="#ee2a7b",fg="white").place(x=25,y=0)
                f=open('Areas1.dat','rb')
                options=[]
                l=pickle.load(f)
                for i in l:
                        options.append(i)
                f.close() 
                def check(e):
                        typed=e.widget.get()
                        if typed == '':
                                combo_box['values']=options
                        else:
                                data=[] 
                                for i in options:
                                        if typed.lower() in i.lower():
                                                data.append(i)
                                combo_box['values']=data
                area=Label(ins,text="Enter Area to insert:",font="Algeria 11",bg="white",fg="red")
                area.place(x=25,y=75)
                combo_box=Combobox(ins,value=options)
                combo_box.place(x=200,y=75)
                combo_box.bind("<KeyRelease>",check)
                fac=Label(ins,text="Enter Facility to insert:",font="Algeria 11",bg="white",fg="red")
                fac.place(x=25,y=150)
                l=['Hotels and eateries','Hospitals','Shopping','Temples','Entertainment']  
                listbox=Listbox(ins) 
                listbox.place(x=200,y=150)
                for i in range(len(l)):
                        listbox.insert(END,l[i])
                global a
                a=[]
                for i in listbox.curselection():
                        a.append(listbox.get(i))      
                ins.place(x=750,y=200)
                f2=Frame(my_canvas,width=500,height=600,bg='#00ddff',highlightbackground='#ff00d4',highlightthickness=3)
                def undo():
                        f2.place_forget()
                        insert()
                def undo1():
                        ins.place_forget()
                        frame.place(x=750,y=200)     
                def show():
                        global g,p,q,r,a,b
                        a=[]
                        for i in listbox.curselection():
                                a.append(listbox.get(i))
                        if combo_box.get() and a:
                                f2.place(x=750,y=50)
                                ins.place_forget()
                                root.title("Insert 2")
                                root.configure(bg="#7018D3")
                                Label(f2,text=str(combo_box.get()),font=('Arial,30')).place(x=25,y=10)
                                g=[]
                                for i in listbox.curselection(): 
                                        b=listbox.get(i)                
                                Label(f2,text=b,font=('Arial,30')).place(x=150,y=10)
                                Label(f2,text='Enter new '+b+' name',font="Algeria 11",bg="white",fg="red").place(x=25,y=50)
                                p=Entry(f2,width=25,insertwidth=2)
                                p.place(x=300,y=50)
                                Label(f2,text="Enter new "+b+' open timings',font="Algeria 11",bg="white",fg="red").place(x=25,y=100)
                                q=Entry(f2,width=25,insertwidth=2)
                                q.place(x=300,y=100)
                                Label(f2,text='Enter new '+b+' phone details',font="Algeria 11",bg="white",fg="red").place(x=25,y=150)
                                r=Entry(f2,width=25,insertwidth=2)
                                r.place(x=300,y=150)
                                
                                back=Button(f2,text="Back",command=undo)
                                back.place(x=25,y=250)
                        else:
                                messagebox.showerror('WARNING BY INSIDEX','Please fill all the fields')
                
                def clickins():
                        global a
                        #print(value)
                        if p.get() and q.get() and r.get():
                                g.append(p.get()+',')
                                g.append('Open:'+q.get()+',')
                                g.append('Contact:'+r.get())
                        for i in a:
                                s=''
                                for j in g:
                                        s+= j
                                temp[combo_box.get()][i].append(s)
                        l=Text(f2,height=10,width=50)
                        l.place(x=25,y=300)
                        for i in a:
                                l.insert(END,yaml.dump([combo_box.get(),i,temp[combo_box.get()][i]]
                                ,sort_keys=False,default_flow_style=False))
                        
                        inse.config(state="disabled",text="inserted")
                        messagebox.showinfo("INFO BY INSIDEX!","You have successfully inserted "+b+" in "+combo_box.get())
                        f.close()
                inse=Button(f2,text="Insert the selected area and facility",font="Castellar 13",command=clickins,bg="#0555c3")
                inse.place(x=25,y=200)
                             
                next=Button(ins,text='Next',padx=10,pady=10,command=show)
                next.place(x=350,y=275)
                back=Button(ins,text="Back",command=undo1)
                back.place(x=25,y=350)
                
        
        def delete():
                global a
                frame.place_forget()
                root.title("Delete")
                k=Frame(my_canvas,width=500,height=400,bg='#00ddff',highlightbackground='#ff00d4',highlightthickness=3)
                Label(k,text='DELETION OF RECORDS',font=("Castellar",25,"bold"),bg="#ee2a7b",fg="white").place(x=25,y=0)
                f=open('Areas1.dat','rb')
                options=[]
                l=pickle.load(f)
                for i in l:
                        options.append(i)
                def check(e):
                        typed=e.widget.get()
                        if typed == '':
                                combo_box['values']=options
                        else:
                                data=[] 
                                for i in options:
                                        if typed.lower() in i.lower():
                                                data.append(i)
                                combo_box['values']=data
                area=Label(k,text="Enter Area to delete:",font="Algeria 11",bg="white",fg="red")
                area.place(x=25,y=75)
                combo_box=Combobox(k,value=options)
                combo_box.place(x=200,y=75)
                combo_box.bind("<KeyRelease>",check)
                fac=Label(k,text="Enter Facility to delete:",font="Algeria 11",bg="white",fg="red")
                fac.place(x=25,y=150)
                l=['Hotels and eateries','Hospitals','Shopping','Temples','Entertainment']  
                listbox=Listbox(k) 
                listbox.place(x=200,y=150)
                for i in range(len(l)):
                        listbox.insert(END,l[i])
                a=[]
                for i in listbox.curselection():
                        a.append(listbox.get(i))      
                k.place(x=750,y=200)       
                f1=Frame(my_canvas,width=500,height=500,bg='#00ddff',highlightbackground='#ff00d4',highlightthickness=3)
                def undo():
                        f1.place_forget()
                        delete()
                def undo1():
                        k.place_forget()
                        frame.place(x=750,y=200)     
                def show():
                        global a,result,tp
                        a=[]
                        for i in listbox.curselection():
                                a.append(listbox.get(i))
                        if combo_box.get() and a:
                                f1.place(x=750,y=100)
                                k.place_forget()
                                root.title("Delete 2")
                                root.configure(bg="#7018D3")
                                Label(f1,text=combo_box.get(),font=('Arial,30')).place(x=25,y=10)
                                a=[]
                                for i in listbox.curselection():
                                        a.append(listbox.get(i)) 
                                        tp=listbox.get(i)
                                Label(f1,text=tp,font=('Arial,30')).place(x=25,y=50)
                                Label(f1,text='Select the places u want to delete:',font=('Arial,10'),bg='#FFCCCB',fg='black').place(x=200,y=10)
                                fac=Listbox(f1,selectmode="multiple",width=50)
                                fac.place(x=200,y=50)
                                #f=open("Areas1.dat",'rb')
                                #d=pickle.load(f)
                                for i in a:
                                        for j in temp[combo_box.get()][i]:
                                                fac.insert(END,j)
                                
                                def get(event):
                                        global index,value,b
                                        index,b=[],[]
                                        sel=event.widget.curselection()
                                        for i in range(len(sel)):
                                                index.append(sel[i])
                                                
                                        value=[]
                                        for i in range(len(index)):
                                                value.append(event.widget.get(index[i]))        
                                        result.set(str(value))      
                                result=StringVar()
                                fac.bind("<<ListboxSelect>>",get) 
                                back=Button(f1,text="Back",command=undo)
                                back.place(x=25,y=100)
                        else:
                                messagebox.showerror('WARNING BY INSIDEX','Please fill all the fields')
                        def clickdel():
                                #global temp
                                f=open("Areas1.dat",'rb')
                                #temp={}
                                #temp=pickle.load(f)
                                for i in a:
                                        for j in value:
                                                t={'areas':combo_box.get(),'fac':i,'name':j}
                                                temp[t['areas']][t['fac']].remove(t['name'])
  
                                l=Text(f1,height=10,width=50)
                                l.place(x=25,y=300)
                                for i in a:
                                        l.insert(END,yaml.dump([combo_box.get(),i,temp[combo_box.get()][i]]
                                        ,sort_keys=False,default_flow_style=False))
                                dele.config(state="disabled",text="deleted")
                                messagebox.showinfo("INFO BY INSIDEX!","You have successfully deleted "+tp+"from "+combo_box.get())
                                f.close()
                        dele=Button(f1,text="Delete the selected area and facility",font="Castellar 13",command=clickdel,bg="#0555c3")
                        dele.place(x=25,y=200)
                                
                next=Button(k,text='Next',padx=10,pady=10,command=show)
                next.place(x=350,y=275)
                back=Button(k,text="Back",command=undo1)
                back.place(x=25,y=350)
                
        def update():
                global a
                frame.place_forget()
                root.title("Update")
                upd=Frame(my_canvas,width=500,height=400,bg='#00ddff',highlightbackground='#ff00d4',highlightthickness=3)
                Label(upd,text='UPDATION OF RECORDS',font=("Castellar",25,"bold"),bg="#ee2a7b",fg="white").place(x=25,y=0)
                f=open('Areas1.dat','rb')
                options=[]
                l=pickle.load(f)
                for i in l:
                        options.append(i)
                def check(e):
                        typed=e.widget.get()
                        if typed == '':
                                combo_box['values']=options
                        else:
                                data=[] 
                                for i in options:
                                        if typed.lower() in i.lower():
                                                data.append(i)
                                combo_box['values']=data
                area=Label(upd,text="Enter Area to update:",font="Algeria 11",bg="white",fg="red")
                area.place(x=25,y=75)
                combo_box=Combobox(upd,value=options)
                combo_box.place(x=200,y=75)
                combo_box.bind("<KeyRelease>",check)
                fac=Label(upd,text="Enter Facility to update:",font="Algeria 11",bg="white",fg="red")
                fac.place(x=25,y=150)
                l=['Hotels and eateries','Hospitals','Shopping','Temples','Entertainment']  
                listbox=Listbox(upd) 
                listbox.place(x=200,y=150)
                for i in range(len(l)):
                        listbox.insert(END,l[i])
                a=[]
                for i in listbox.curselection():
                        a.append(listbox.get(i))      
                upd.place(x=750,y=200)
                f2=Frame(my_canvas,width=500,height=500,bg='#00ddff',highlightbackground='#ff00d4',highlightthickness=3)
                def undo():
                        f2.place_forget()
                        update()
                def undo1():
                        upd.place_forget()
                        frame.place(x=750,y=200)     
                def show():
                        global a,result,up
                        a=[]
                        for i in listbox.curselection():
                                a.append(listbox.get(i))
                        if combo_box.get() and a:
                                f2.place(x=750,y=100)
                                upd.place_forget()
                                root.title("Update 2")
                                root.configure(bg="#7018D3")
                                Label(f2,text=combo_box.get(),font=('Arial,30')).place(x=25,y=10)
                                a=[]
                                for i in listbox.curselection():
                                        a.append(listbox.get(i))
                                        up=listbox.get(i)
                                
                                x1,y1=175,50
                                for i in a:
                                        Label(f2,text=i,font=('Arial,30')).place(x=25,y=50)
                                        lo=temp[combo_box.get()][i]
                                        ent={}
                                        for j in lo:
                                                n=Entry(f2,width=40,font=('Arial 10'))
                                                n.insert(0,j)
                                                ent[j]=n
                                                n.place(x=x1,y=y1)       
                                                y1+=25
                                back=Button(f2,text="Back",command=undo)
                                back.place(x=25,y=y1+25)
                        else:
                                messagebox.showerror('WARNING BY INSIDEX','Please fill all the fields')
                        
                        def clickupd():
                                '''f=open("Areas1.dat",'rb')
                                temp={}
                                temp=pickle.load(f)'''
                                o=[]
                                for j in lo:
                                        o.append(ent[j].get())
                                for i in range(len(a)):
                                        for j in range(len(o)):
                                                temp[combo_box.get()][a[i]][j]=o[j]
                                for i in a:
                                        l=Text(f2,height=10,width=50)
                                        l.place(x=25,y=300)
                                        l.insert(END,yaml.dump([combo_box.get(),i,temp[combo_box.get()][i]]
                                        ,sort_keys=False,default_flow_style=False))
                                upda.config(state="disabled",text="updated")
                                messagebox.showinfo("INFO BY INSIDEX!","You have successfully updated "+up+" in "+combo_box.get())
                                f.close()  
                        upda=Button(f2,text="Update the selected area and facility",font="Castellar 13",command=clickupd,bg="#0555c3")
                        upda.place(x=25,y=y1+50)
                next=Button(upd,text='Next',padx=10,pady=10,command=show)
                next.place(x=350,y=275)
                back=Button(upd,text="Back",command=undo1)
                back.place(x=25,y=350)
def home():
        canvas(root,r"Images\background2.jpg")
        f=Frame(my_canvas)
        f.configure(bg="#f01e2c")
        Label(f,text="WELCOME TO INSIDEX",font=("Castellar",30,"bold"),bg="#2596be",fg="white").grid(row=0,column=1)
        
        logolab=Label(f,image=new_pic)
        logolab.grid(row=1,column=1,padx=50,pady=50)
        Button(f,text="Admin",bg="#2596be",font="Times 15",fg="white",height=2,border=2,command=admin).grid(row=4,column=1,sticky=NSEW,padx=10,pady=10)
        f.place(x=730,y=250)
home()
def confirm():
        ans=askyesno(title='Exit',message='Do you want to exit?')
        if ans:
                root.destroy()
root.protocol("WM_DELETE_WINDOW",confirm)
root.mainloop()