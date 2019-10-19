from tkinter import Tk,Label
from random import choice


def Exit(event=None):
    root.destroy()
    quit()

def formation():
    global L_object,color,temp1,temp2,counter,flag,index

    if flag:
        c=choice(temp1)
        temp1.remove(c)
        temp2.append(c)
        L_object[c].config(bg=color[index])
        counter+=1
        if counter==850: flag=False
    else:
        L_object[temp2[counter-1]].config(bg='black')
        counter-=1
        if counter==0:
            flag=True
            temp1=list(range(850))
            index+=1
            if index>=len(color): index=0
        
        
    root.after(2,formation)

root=Tk()
root.geometry('1600x900')
root.state('zoomed')
root.overrideredirect(True)
root.config(background='black')
root.bind('<Escape>',Exit)


L_object=[]
color=['dark red','navy blue','gold3','dark green']
index=0
temp1=list(range(850))
temp2=[]
counter=0
flag=True


X=8
Y=11


for i in range(25):
    for j in range(34):
        h=Label(root,bg='black',width=3)
        h.place(x=X,y=Y)
        L_object.append(h)

        X+=40
    X=8
    Y+=30

formation()

root.mainloop()



