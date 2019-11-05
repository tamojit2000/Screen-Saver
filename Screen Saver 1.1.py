from tkinter import Tk,Label
from random import choice


def Exit(event=None):
    root.destroy()
    quit()

def formation():
    global L_object,color,temp1,temp2,counter,flag,index,h,w

    if flag:
        c=choice(temp1)
        temp1.remove(c)
        temp2.append(c)
        L_object[c].config(bg=color[index])
        counter+=1
        if counter==(h//30)*(w//40): flag=False
    else:
        L_object[temp2[counter-1]].config(bg='black')
        counter-=1
        if counter==0:
            flag=True
            temp1=list(range((h//30)*(w//40)))
            index+=1
            if index>=len(color): index=0
        
        
    root.after(2,formation)

root=Tk()
root.state('zoomed')
root.overrideredirect(True)
root.config(background='black')

w=root.winfo_screenwidth()
h=root.winfo_screenheight()



L_object=[]
color=['dark orange','purple','dark red','navy blue','gold3','dark green']
index=0
temp1=list(range((h//30)*(w//40)))
temp2=[]
counter=0
flag=True


X=8
Y=11


for i in range(h//30):
    for j in range(w//40):
        p=Label(root,bg='black',width=3)
        p.place(x=X,y=Y)
        L_object.append(p)

        X+=40
    X=8
    Y+=30

formation()

root.bind_all('<Any-KeyPress>',Exit)
root.bind_all('<Any-Button>',Exit)
root.bind_all('<Button-1>',Exit)
root.bind_all('<Motion>',Exit)

root.mainloop()



