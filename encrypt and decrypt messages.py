from tkinter import messagebox,simpledialog,Tk
def even(number):
    if(number%2==0):
        return True
    return False
def odd(number):
    if(number%2!=0):
        return True
    return False
def evenlist(message):
    el=[]
    for i in range(len(message)):
        if even(i):
            el.append(message[i])
    return el
def oddlist(message):
    ol=[]
    for i in range(len(message)):
        if odd(i):
            ol.append(message[i])
    return ol
def encryptedmessage(message):
    res=''
    if(odd(len(message))):
        message+='x'
    el=evenlist(message)
    ol=oddlist(message)
    for i in range(int(len(message)/2)):
        res+=ol[i]
        res+=el[i]
    return res
def get_task():
    task=simpledialog.askstring('Task','Do you want to encrypt or decrypt?')
    return task
def get_message():
    message=simpledialog.askstring('Message','Enter the secret message')
    return message
tk=Tk()
while True:
    task=get_task()
    if(task=='encrypt'):
        message=get_message()
        cipher=encryptedmessage(message)
        messagebox.showinfo('cipher text of the secret message is ',cipher)
    elif(task=='decrypt'):
        message=get_message()
        plain=encryptedmessage(message)
        messagebox.showinfo('plain text of the secret message is ',plain)
    else:
        break
tk.mainloop()
