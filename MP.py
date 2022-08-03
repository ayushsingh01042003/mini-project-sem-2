from tkinter import *
from tkinter import messagebox
from  tkinter import ttk
import csv
from matplotlib import pyplot as plt


global sum_dry_total,sum_wet_total
sum_dry_total=0
sum_wet_total=0

# starting of the first function
    

    
def first():
        
    #window design
    root=Tk()
    root.geometry('1366x768')
    root.title('Main')
    root.resizable(False,False)
    
    

    canvas1=Canvas(root,width=1366,height=800)
    canvas1.grid(row=0,column=0)
    canvas1.configure(background="#add8e6")
    text1=canvas1.create_text((400,10),text="WASTE WEIGHT COLLECTOR PROGRAM",font=('arial',20,'bold'),anchor="nw")

    def second():
    
        root1=Tk()
        root1.geometry('1366x768')
        root1.title('New User')
        root1.resizable(False,False)
        #root1.iconbitmap('2.ico')
        root1.configure(background="#add8e6")
        
            


        def ratio():
            file1=open('data.csv','a+',newline='')
            with open('data.csv', newline='', encoding='utf_8') as gg:
                reader = csv.reader(gg)
                content = list(reader)
            len_content=len(content)
            check=1
            if check==1:
                if len_content>1:
                    for qaz in content:
                        if qaz[10]==f:
                            messagebox.showerror('Error','Entry already exists')
                            check=0
            if check==1:
                xy=(a,'',b,'',c,'',d,'',e,'',f)
                zz=csv.writer(file1)
                zz.writerow(xy)
                popup1()
                

           
            
            


        def table():
            file1=open('data.csv','a+',newline='')
            with open('data.csv', newline='', encoding='utf_8') as f:
                reader = csv.reader(f)
                content = list(reader)
            if content==[]:
                xyz=('Drivers Name','','Phone Number','','Address','','Dry Waste','','Wet Waste','','House Code')
                zz=csv.writer(file1)
                zz.writerow(xyz)
            
                
                
            file1.close()
            ratio()

     
                               
            
        

        def getvals():
            global a,b,c,d,e,f
            a=entry1.get()
            b=entry2.get()
            c=entry3.get()
            d=entry4.get()
            e=entry5.get()
            f=entry6.get()
            table()

       
        #labels
        label1=Label(root1,text='DRIVERS NAME',font=('arial',16,'bold')).place(x=5,y=50)
        label2=Label(root1,text='DRIVERS PHONE NUMBER',font=('arial',16,'bold')).place(x=5,y=100)
        label3=Label(root1,text="HOUSE NUMBER AND ADDRESS",font=('arial',16,'bold')).place(x=5,y=150)
        label4=Label(root1,text='AMOUNT OF DRY WASTE COLLECTED',font=('arial',16,'bold')).place(x=5,y=200)
        label5=Label(root1,text='AMOUNT OF WET WASTE COLLECTED',font=('arial',16,'bold')).place(x=5,y=250)
        label6=Label(root1,text='HOUSE CODE',font=('arial',16,'bold')).place(x=5,y=300)

    

    


        #entry
  
        entry1=Entry(root1,width=40,fg='red',font=('helvetica',16,'normal'))
        entry1.place(x=650,y=50)
        entry2=Entry(root1,width=40,fg='blue',font=('helvetica',16,'normal'))
        entry2.place(x=650,y=100)
        
        entry3=Entry(root1,width=40,fg='green',font=('helvetica',16,'normal'))
        entry3.place(x=650,y=150)
        entry4=Entry(root1,width=40,fg='purple',font=('helvetica',16,'normal'))
        entry4.place(x=650,y=200)
        entry5=Entry(root1,width=40,fg='brown',font=('helvetica',16,'normal'))
        entry5.place(x=650,y=250)
        entry6=Entry(root1,width=40,fg='orange',font=('helvetica',16,'normal'))
        entry6.place(x=650,y=300)



        def popup1():
            messagebox.showinfo("Message",'Entry Added Successfully')
          
        
        
        button7=Button(root1,text='Submit',padx=20,pady=20,font=('helvetica',16,'normal'),command=lambda:[getvals(),root1.destroy(),errorSort(),first()])
        button7.place(x=600,y=500)



    
    def third():
        root2=Tk()
        root2.geometry('800x600')
        root2.title('Existing User')
        root2.resizable(False,False)
        #root2.iconbitmap('2.ico')
        root2.configure(background="#add8e6")



    
        
 
        def read():
            global x
            x=entry7.get()
            
            file1=open('data.csv','a+',newline='')
            with open('data.csv', newline='', encoding='utf_8') as f:
                reader = csv.reader(f)
                content = list(reader)
            for i in content:
                if x==i[10]:
                    root3=Tk()
                    root3.geometry('1366x768')
                    root3.title('Edit User')
                    root3.resizable(False,False)
                    #root3.iconbitmap('2.ico')

                    def delete():
                        line=[]
                            
                            
                        with open('data.csv', 'r') as rf:
                            reader=csv.reader(rf)
                            for i in reader:
                                line.append(i)
                                
                                
                        flist=[]
                        for ii in line:
                            if x==ii[10]:
                                pass
                            else:
                                flist=[ii]+flist
                        print(flist)
                            
                           
                        lissst=[aa,'',bb,'',cc,'',dd,'',ee,'',x]
                        flist=[lissst]+flist
                        flist.reverse()

                        file4=open('data.csv','w+',newline='')
                        writer4=csv.writer(file4)
                        writer4.writerows(flist)
                    
 

                    def getvals1():
                        global aa,bb,cc,dd,ee
                        aa=entry8.get()
                        bb=entry9.get()
                        cc=entry10.get()
                        dd=entry11.get()
                        ee=entry12.get()
                           
                        delete()
                            
                        print('Success')


                    label8=Label(root3,text='DRIVERS NAME',font=('arial',16,'bold')).place(x=5,y=50)
                    label9=Label(root3,text='DRIVERS PHONE NUMBER',font=('arial',16,'bold')).place(x=5,y=100)
                    label10=Label(root3,text="HOUSE NUMBER AND ADDRESS",font=('arial',16,'bold')).place(x=5,y=150)
                    label11=Label(root3,text='AMOUNT OF DRY WASTE COLLECTED',font=('arial',16,'bold')).place(x=5,y=200)
                    label12=Label(root3,text='AMOUNT OF WET WASTE COLLECTED',font=('arial',16,'bold')).place(x=5,y=250)



                    entry8=Entry(root3,width=40,fg='red',font=('helvetica',16,'normal'))
                    entry8.place(x=650,y=50)
                    entry9=Entry(root3,width=40,fg='blue',font=('helvetica',16,'normal'))
                    entry9.place(x=650,y=100)
                    entry10=Entry(root3,width=40,fg='green',font=('helvetica',16,'normal'))
                    entry10.place(x=650,y=150)
                    entry11=Entry(root3,width=40,fg='purple',font=('helvetica',16,'normal'))
                    entry11.place(x=650,y=200)
                    entry12=Entry(root3,width=40,fg='brown',font=('helvetica',16,'normal'))
                    entry12.place(x=650,y=250)

                    def popup3():
                        messagebox.showinfo('Info','Entries have been updated successfully')

                    btn=Button(root3,text='Edit',command=lambda:[getvals1(),root3.destroy(),first(),popup3()])
                    btn.place(x=650,y=400)




            
        label7=Label(root2,text="House Code",font=('arial',16,'bold')).place(x=150,y=200)  
        entry7=Entry(root2,font=('arial',16,'bold'))
        entry7.place(x=350,y=200)

        button4=Button(root2,text='Continue',padx=10,pady=10,font=('helvetica',16,'bold'),command=lambda:[read(),root2.destroy(),errorSort()]).place(x=350,y=400)

                    
        
    def errorSort():
        global unqt
        file5=open('data.csv','a+',newline='')
        with open('data.csv', newline='', encoding='utf_8') as fff:
            reader5 = csv.reader(fff)
            content5 = list(reader5)
        dry_waste=0
        wet_waste=0
        LLL=[]
        stop=0
        length=len(content5)

            
        for y in range(1,length):
            recheck=content5[y]
            reconstant=recheck[0]
            LLL=LLL+[reconstant]

                
        lengthL=len(LLL)
        reoccuring=[]

        for i in range(0,lengthL):
            check=LLL[i]
            constant=check[0]
            for ii in range(0,lengthL):
                check1=LLL[ii]
                constant1=check1[0]
                if constant==constant1:
                    if i!=ii:
                        reoccuring=reoccuring+[i]

        newlist=[]
        lis=[]
        content5.pop(0)
        for j in reoccuring:
            newlist=newlist+[content5[j]]
        newlength=len(newlist)

        unq=[]
        for x in newlist:
            unq=unq+[x[0]]

        unqt=[]
        for xx in unq:
            if xx not in unqt:
                unqt.append(xx)


        dlength=len(unqt)
        global sum1,sum11,sum2,sum22,sum3,sum33,sum4,sum44,sum5,sum55
        sum1=0
        sum11=0
        sum2=0
        sum22=0
        sum3=0
        sum33=0
        sum4=0
        sum44=0
        sum5=0
        sum55=0
        if dlength==1:
            for w in content5:
                if w[0]==unqt[0]:
                    sum1=sum1+float(w[6])
                    sum11=sum11+float(w[8])
            error()
                
        if dlength==2:
            for w in content5:
                if w[0]==unqt[0]:
                    sum1=sum1+float(w[6])
                    sum11=sum11+float(w[8])

                if w[0]==unqt[1]:
                    sum2=sum2+float(w[6])
                    sum22=sum22+float(w[8])


                error()

        if dlength==3:
            for w in content5:
                if w[0]==unqt[0]:
                    sum1=sum1+float(w[6])
                    sum11=sum11+float(w[8])

                if w[0]==unqt[1]:
                    sum2=sum2+float(w[6])
                    sum22=sum22+float(w[8])

                if w[0]==unqt[2]:
                    sum3=sum3+float(w[6])
                    sum33=sum33+float(w[8])

                error()


        if dlength==4:
            for w in content5:
                if w[0]==unqt[0]:
                    sum1=sum1+float(w[6])
                    sum11=sum11+float(w[8])

                if w[0]==unqt[1]:
                    sum2=sum2+float(w[6])
                    sum22=sum22+float(w[8])

                if w[0]==unqt[2]:
                    sum3=sum3+float(w[6])
                    sum33=sum33+float(w[8])

                if w[0]==unqt[3]:
                    sum4=sum4+float(w[6])
                    sum44=sum44+float(w[8])

                error()


        if dlength==5:
             for w in content5:
                if w[0]==unqt[0]:
                    sum1=sum1+float(w[6])
                    sum11=sum11+float(w[8])

                if w[0]==unqt[1]:
                    sum2=sum2+float(w[6])
                    sum22=sum22+float(w[8])

                if w[0]==unqt[2]:
                    sum3=sum3+float(w[6])
                    sum33=sum33+float(w[8])

                if w[0]==unqt[3]:
                    sum4=sum4+float(w[6])
                    sum44=sum44+float(w[8])

                if w[0]==unqt[4]:
                    sum5=sum5+float(w[6])
                    sum55=sum55+float(w[8])

                error()

            
            

    def error():
        if sum1>50 and sum11>50:
            messagebox.showwarning('Overflow','Both dry and wet waste overflow in one or many trucks')
            print(unqt[0],'has crossed the limit for both dry waste and wet waste')
        elif sum1>50:
            messagebox.showwarning('Overflow','Dry waste overflow in one or many trucks')
            print(unqt[0],'has crossed the limit for dry waste')
        elif sum11>50:
            messagebox.showwarning('Overflow','Wet waste overflow in one or many trucks')
            print(unqt[0],'has crossed the limit for wet waste ')


        if sum2>50 and sum22>50:
            messagebox.showwarning('Overflow','Both dry and wet waste overflow in one or many trucks')
            print(unqt[1],'has crossed the limit for both dry waste and wet waste')
        elif sum2>50:
            messagebox.showwarning('Overflow','Dry waste overflow in one or many trucks')
            print(unqt[1],'has crossed the limit for dry waste')
        elif sum22>50:
            messagebox.showwarning('Overflow','Wet waste overflow in one or many trucks')
            print(unqt[1],'has crossed the limit for wet waste')


        if sum3>50 and sum33>50:
            messagebox.showwarning('Overflow','Both dry and wet waste overflow in one or many trucks')
            print(unqt[2],'has crossed the limit for both dry waste and wet waste')
        elif sum3>50:
            messagebox.showwarning('Overflow','Dry waste overflow in one or many trucks')
            print(unqt[2],'has crossed the limit for dry waste')
        elif sum33>50:
            messagebox.showwarning('Overflow','Wet waste overflow in one or many trucks')
            print(unqt[2],'has crossed the limit for wet waste')

        if sum4>50 and sum44>50:
            messagebox.showwarning('Overflow','Both dry and wet waste overflow in one or many trucks')
            print(unqt[3],'has crossed the limit for both dry waste and wet waste')
        elif sum4>50:
            messagebox.showwarning('Overflow','Dry waste overflow in one or many trucks')
            print(unqt[3],'has crossed the limit for dry waste')
        elif sum44>50:
            messagebox.showwarning('Overflow','Wet waste overflow in one or many trucks')
            print(unqt[3],'has crossed the limit for wet waste')


        if sum5>50 and sum55>50:
            messagebox.showwarning('Overflow','Both dry and wet waste overflow in one or many trucks')
            print(unqt[4],'has crossed the limit for both dry and wet waste')
        if sum5>50:
            messagebox.showwarning('Overflow','Dry waste overflow in one or many trucks')
            print(unqt[4],'has crossed the limit for dry waste')
        if sum55>50:
            messagebox.showwarning('Overflow','Wet waste overflow in one or many trucks')
            print(unqt[4],'has crossed the limit for wet waste')


                
                           

                        
    def fourth():
        file5=open('data.csv','a+',newline='')
        sum_dry_total=0
        sum_wet_total=0
        with open('data.csv', newline='', encoding='utf_8') as fff:
            reader5 = csv.reader(fff)
            content5 = list(reader5)
        length=len(content5)
        content5=content5[1:]
        for i in content5:
            sum_dry_total=sum_dry_total+float(i[6])
            sum_wet_total=sum_wet_total+float(i[8])
        dwaste=sum_dry_total
        wwaste=sum_wet_total
        plt.style.use('fivethirtyeight')
        slices=[dwaste,wwaste]
        labels=['DRY WASTE','WET WASTE']
        explode=[0,0.1]
        plt.pie(slices,labels=labels,explode=explode)
        plt.title('Dw v/s Ww')
        plt.tight_layout()
        plt.show()

        slices1=[]
        labels1=[]
        slices2=[]
        for o in content5:
            slices1.append(o[6])
            labels1.append(o[4])
            slices2.append(o[8])
        
        plt.pie(slices1,labels=labels1)
        plt.title('DRY WASTE')
        plt.tight_layout()
        plt.show()
        
        plt.pie(slices2,labels=labels1)
        plt.title('WET WASTE')
        plt.tight_layout()
        plt.show()




    def fifth():
        root5=Tk()
        root5.geometry('800x600')
        root5.title('Delete Entry')
        root5.resizable(False,False)
        #root5.iconbitmap('2.ico')
        root5.configure(background="#add8e6")
        
        def five1():
            g=1
            abc=entry22.get()
            root5.destroy()
            updated_list=[]
            file1=open('data.csv','a+',newline='')
            with open('data.csv', newline='', encoding='utf_8') as gg:
                reader = csv.reader(gg)
                content = list(reader)
            len_content=len(content)
            for i in content:
                if i[10]==abc:
                    messagebox.showinfo('Info','Entries have been Deleted successfully.')
                    g=0
                else:
                    updated_list=updated_list+[i]
            if g==1:
                messagebox.showerror('Error','No entries with entered house code was found.')
                 
                                
            file1.close()
            file1=open('data.csv','w+',newline='')
            writer=csv.writer(file1)
            writer.writerows(updated_list)
            

        label22=Label(root5,text="House code",font=('arial',16,'bold')).place(x=150,y=200)               
        entry22=Entry(root5,font=('arial',16,'italic'))
        entry22.place(x=350,y=200)

       
                
        button22=Button(root5,text='Delete',padx=10,pady=10,font=('helvetica',16,'bold'),command=lambda:[five1(),first()]).place(x=350,y=400)   
        
  

        
    #buttons 
    button1=Button(canvas1,text='New Entry',font=('arial',25,'bold'),fg='gold',command=lambda:[second(),root.destroy()])
    button1.place(x=550,y=200)

    button2=Button(canvas1,text='Existing Entry',font=('arial',20,'bold'),fg='blue',command=lambda:[third(),root.destroy()])
    button2.place(x=550,y=300)

    button3=Button(canvas1,text='Generate Pie Chart',font=('arial',20,'bold'),fg='green',command=lambda:[fourth(),root.destroy()])
    button3.place(x=550,y=400)

    button8=Button(canvas1,text='Delete Record',font=('arial',20,'bold'),fg='purple',command=lambda:[fifth(),root.destroy()])
    button8.place(x=550,y=500)

    button9=Button(canvas1,text='Send message',font=('arial',20,'bold'),fg='red',command=lambda:[sixth(),root.destroy()])
    button9.place(x=550,y=600)
    def sixth():
        import os
        from twilio.rest import Client
        a='AC0f6aec06a0aef534eed04e0be9bbdf71'
        b='dd85ac2421281190011975a12ade6a8e'
        client = Client(a,b)
        call = client.calls.create(
                twiml='<Response><Say>useful message</Say></Response>',
                to='+919113876984',
                from_='+18437382534'
            )

        
        message = client.messages \
                    .create(
                         body='useful message',
                         from_='+18437382534',
                         to='+917829284472'
                        
            )
        
    

first()


