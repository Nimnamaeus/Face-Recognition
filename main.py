############################################# IMPORTING ################################################
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2,os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time
from PIL import Image, ImageTk

############################################# FUNCTIONS ################################################

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

##################################################################################

def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200,tick)

###################################################################################

def contact():
    mess._show(title='Contact us', message="Please contact us on : 'xxxxxxxxxxxxx@gmail.com' ")

###################################################################################

def check_haarcascadefile():
    exists = os.path.isfile("haarcascade_frontalface_default.xml")
    if exists:
        pass
    else:
        mess._show(title='Some file missing', message='Please contact us for help')
        window.destroy()

###################################################################################

def save_pass():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel\psd.txt")
    if exists1:
        tf = open("TrainingImageLabel\psd.txt", "r")
        key = tf.read()
    else:
        master.destroy()
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            tf = open("TrainingImageLabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered', message='New password was registered successfully!!')
            return
    op = (old.get())
    newp= (new.get())
    nnewp = (nnew.get())
    if (op == key):
        if(newp == nnewp):
            txf = open("TrainingImageLabel\psd.txt", "w")
            txf.write(newp)
        else:
            mess._show(title='Error', message='Confirm new password again!!!')
            return
    else:
        mess._show(title='Wrong Password', message='Please enter correct old password.')
        return
    mess._show(title='Password Changed', message='Password changed successfully!!')
    master.destroy()

###################################################################################

def change_pass():
    global master
    master = tk.Tk()
    master.geometry("400x160")
    master.resizable(False,False)
    master.title("Change Password")
    master.configure(background="white")
    lbl4 = tk.Label(master,text='    Enter Old Password',bg='white',font=('times', 12, ' bold '))
    lbl4.place(x=10,y=10)
    global old
    old=tk.Entry(master,width=25 ,fg="black",relief='solid',font=('times', 12, ' bold '),show='*')
    old.place(x=180,y=10)
    lbl5 = tk.Label(master, text='   Enter New Password', bg='white', font=('times', 12, ' bold '))
    lbl5.place(x=10, y=45)
    global new
    new = tk.Entry(master, width=25, fg="black",relief='solid', font=('times', 12, ' bold '),show='*')
    new.place(x=180, y=45)
    lbl6 = tk.Label(master, text='Confirm New Password', bg='white', font=('times', 12, ' bold '))
    lbl6.place(x=10, y=80)
    global nnew
    nnew = tk.Entry(master, width=25, fg="black", relief='solid',font=('times', 12, ' bold '),show='*')
    nnew.place(x=180, y=80)
    cancel=tk.Button(master,text="Cancel", command=master.destroy ,fg="black"  ,bg="red" ,height=1,width=25 , activebackground = "white" ,font=('times', 10, ' bold '))
    cancel.place(x=200, y=120)
    save1 = tk.Button(master, text="Save", command=save_pass, fg="black", bg="#3ece48", height = 1,width=25, activebackground="white", font=('times', 10, ' bold '))
    save1.place(x=10, y=120)
    master.mainloop()

#####################################################################################

def psw():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel\psd.txt")
    if exists1:
        tf = open("TrainingImageLabel\psd.txt", "r")
        key = tf.read()
    else:
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            tf = open("TrainingImageLabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered', message='New password was registered successfully!!')
            return
    password = tsd.askstring('Password', 'Enter Password', show='*')
    if (password == key):
        TrainImages()
    elif (password == None):
        pass
    else:
        mess._show(title='Wrong Password', message='You have entered wrong password')

######################################################################################

def clear():
    txt.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    message3.configure(text=res)


def clear2():
    txt2.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    message3.configure(text=res)

#######################################################################################

def TakeImages():
    check_haarcascadefile()
    columns = ['SERIAL NO.', '', 'ID', '', 'NAME']
    assure_path_exists("StudentDetails/")
    assure_path_exists("TrainingImage/")
    serial = 0
    exists = os.path.isfile("StudentDetails\StudentDetails.csv")
    if exists:
        with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                serial = serial + 1
        serial = (serial // 2)
        csvFile1.close()
    else:
        with open("StudentDetails\StudentDetails.csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(columns)
            serial = 1
        csvFile1.close()
    Id = (txt.get())
    name = (txt2.get())
    if ((name.isalpha()) or (' ' in name)):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                sampleNum = sampleNum + 1
                cv2.imwrite("TrainingImage\\" + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                            gray[y:y + h, x:x + w])
                cv2.imshow('Taking Images', img)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif sampleNum > 30:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Taken for ID : " + Id
        row = [serial, '', Id, '', name]
        with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message3.configure(text=res)
    else:
        if (name.isalpha() == False):
            res = "Enter Correct name"
            message.configure(text=res)

########################################################################################

def TrainImages():
    check_haarcascadefile()
    assure_path_exists("TrainingImageLabel/")
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, ID = getImagesAndLabels("TrainingImage")
    try:
        recognizer.train(faces, np.array(ID))
    except:
        mess._show(title='No Registrations', message='Please Register someone first!!!')
        return
    recognizer.save("TrainingImageLabel\Trainner.yml")
    res = "Profile Saved Successfully"
    message3.configure(text=res)
    message.configure(text='Total Registrations till now  : ' + str(ID[0]))

############################################################################################3

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    Ids = []
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        try:
            ID = int(os.path.split(imagePath)[-1].split(".")[2])
            faces.append(imageNp)
            Ids.append(ID)
        except (ValueError, IndexError):
            print(f"Skipping invalid image file: {imagePath}")
            continue
    return faces, Ids

###########################################################################################

def TrackImages():
    check_haarcascadefile()
    assure_path_exists("Attendance/")
    assure_path_exists("StudentDetails/")
    for k in tv.get_children():
        tv.delete(k)
    msg = ''
    i = 0
    j = 0
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    exists3 = os.path.isfile("TrainingImageLabel\Trainner.yml")
    if exists3:
        recognizer.read("TrainingImageLabel\Trainner.yml")
    else:
        mess._show(title='Data Missing', message='Please click on Save Profile to reset data!!')
        return
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);

    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
    exists1 = os.path.isfile("StudentDetails\StudentDetails.csv")
    if exists1:
        df = pd.read_csv("StudentDetails\StudentDetails.csv")
    else:
        mess._show(title='Details Missing', message='Students details are missing, please check!')
        cam.release()
        cv2.destroyAllWindows()
        return
    
    attendance_marked = False  # Flag to track if attendance was marked
    
    while True:
        ret, im = cam.read()
        if not ret:  # Check if camera read was successful
            break
            
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                ID = str(ID)
                ID = ID[1:-1]
                bb = str(aa)
                bb = bb[2:-2]
                attendance = [str(ID), '', bb, '', str(date), '', str(timeStamp)]
                attendance_marked = True  # Set flag when attendance is marked

            else:
                Id = 'Unknown'
                bb = str(Id)
            cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
        cv2.imshow('Taking Attendance', im)
        
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    
    # Properly release resources
    cam.release()
    cv2.destroyAllWindows()
    
    # Only save attendance if it was actually marked
    if attendance_marked:
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
        exists = os.path.isfile("Attendance\Attendance_" + date + ".csv")
        if exists:
            with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(attendance)
            csvFile1.close()
        else:
            with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(col_names)
                writer.writerow(attendance)
            csvFile1.close()
        with open("Attendance\Attendance_" + date + ".csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for lines in reader1:
                i = i + 1
                if (i > 1):
                    if (i % 2 != 0):
                        iidd = str(lines[0]) + '   '
                        tv.insert('', 0, text=iidd, values=(str(lines[2]), str(lines[4]), str(lines[6])))
        csvFile1.close()

######################################## USED STUFFS ############################################
    
global key
key = ''

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day,month,year=date.split("-")

mont={'01':'January',
      '02':'February',
      '03':'March',
      '04':'April',
      '05':'May',
      '06':'June',
      '07':'July',
      '08':'August',
      '09':'September',
      '10':'October',
      '11':'November',
      '12':'December'
      }

######################################## GUI FRONT-END ###########################################

# Add these color constants at the top of the file
DARK_BG = "#2C3333"  # Dark background
ACCENT_COLOR = "#00ADB5"  # Teal accent
TEXT_COLOR = "#EEEEEE"  # Light text
BUTTON_COLOR = "#395B64"  # Button background
FRAME_BG = "#2E4F4F"  # Frame background

window = tk.Tk()
window.geometry("1280x720")
window.resizable(True, False)
window.title("Attendance System")
window.configure(background=DARK_BG)

frame1 = tk.Frame(window, bg=FRAME_BG, relief='flat')
frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

frame2 = tk.Frame(window, bg=FRAME_BG, relief='flat')
frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

message3 = tk.Label(window, text="Face Recognition Based Attendance System",
                   fg=TEXT_COLOR, bg=DARK_BG, width=55, height=1,
                   font=('Helvetica', 29, 'bold'))
message3.place(x=10, y=10)

frame3 = tk.Frame(window, bg=FRAME_BG)
frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)

frame4 = tk.Frame(window, bg=FRAME_BG)
frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)

datef = tk.Label(frame4, text=day+"-"+mont[month]+"-"+year+"  |  ",
                 fg=ACCENT_COLOR, bg=DARK_BG, width=55, height=1,
                 font=('Helvetica', 22, 'bold'))
datef.pack(fill='both', expand=1)

clock = tk.Label(frame3, fg=ACCENT_COLOR, bg=DARK_BG, width=55, height=1,
                font=('Helvetica', 22, 'bold'))
clock.pack(fill='both', expand=1)
tick()

head2 = tk.Label(frame2, text="New Registration",
                 fg=TEXT_COLOR, bg=ACCENT_COLOR,
                 font=('Helvetica', 17, 'bold'),
                 padx=20, pady=10)
head2.grid(row=0, column=0)

head1 = tk.Label(frame1, text="Already Registered",
                 fg=TEXT_COLOR, bg=ACCENT_COLOR,
                 font=('Helvetica', 17, 'bold'),
                 padx=20, pady=10)
head1.place(x=0, y=0)

lbl = tk.Label(frame2, text="Enter LRN No.", width=20, height=1,
               fg=TEXT_COLOR, bg=FRAME_BG,
               font=('Helvetica', 17, 'bold'))
lbl.place(x=80, y=55)

txt = tk.Entry(frame2, width=25, fg=TEXT_COLOR, bg=DARK_BG,
               font=('Helvetica', 15), relief='flat',
               insertbackground=TEXT_COLOR)
txt.place(x=30, y=110)

clearButton = tk.Button(frame2, text="Clear", command=clear,
                       fg=TEXT_COLOR, bg="#ea2a2a",
                       width=8, height=1,
                       relief='flat', cursor='hand2',
                       font=('Helvetica', 11, 'bold'))
clearButton.place(x=335, y=110)

lbl2 = tk.Label(frame2, text="Enter Name", width=20, height=1,
                fg=TEXT_COLOR, bg=FRAME_BG,
                font=('Helvetica', 17, 'bold'))
lbl2.place(x=80, y=160)

txt2 = tk.Entry(frame2, width=25, fg=TEXT_COLOR, bg=DARK_BG,
                font=('Helvetica', 15), relief='flat',
                insertbackground=TEXT_COLOR)
txt2.place(x=30, y=215)

clearButton2 = tk.Button(frame2, text="Clear", command=clear2,
                        fg=TEXT_COLOR, bg="#ea2a2a",
                        width=8, height=1,
                        relief='flat', cursor='hand2',
                        font=('Helvetica', 11, 'bold'))
clearButton2.place(x=335, y=215)

message = tk.Label(frame2, text="",
                  bg=FRAME_BG, fg=TEXT_COLOR,
                  width=39, height=1,
                  font=('Helvetica', 15, 'bold'))
message.place(x=7, y=450)

# Update the image loading function with larger size
def load_and_resize_image(path, size=(35, 35)):  # Increased size from 25x25 to 35x35
    img = Image.open(path)
    img = img.resize(size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)

# Update the message frame layout
message_frame = tk.Frame(frame2, bg=FRAME_BG)
message_frame.place(x=7, y=490)

try:
    camera_icon = load_and_resize_image("icons/camera.png")
    save_icon = load_and_resize_image("icons/save.png")
except:
    camera_icon = None
    save_icon = None

# Place text first, then icon with adjusted padding
text1_label = tk.Label(message_frame, text="1.) Take Images",
                      bg=FRAME_BG, fg=TEXT_COLOR,
                      font=('Helvetica', 15, 'bold'))
text1_label.grid(row=0, column=0, sticky='w', pady=5)

if camera_icon:
    camera_label = tk.Label(message_frame, image=camera_icon, bg=FRAME_BG)
    camera_label.image = camera_icon
    camera_label.grid(row=0, column=1, padx=(15, 0), pady=5)

text2_label = tk.Label(message_frame, text="2.) Save Profile",
                      bg=FRAME_BG, fg=TEXT_COLOR,
                      font=('Helvetica', 15, 'bold'))
text2_label.grid(row=1, column=0, sticky='w', pady=5)

if save_icon:
    save_label = tk.Label(message_frame, image=save_icon, bg=FRAME_BG)
    save_label.image = save_icon
    save_label.grid(row=1, column=1, padx=(15, 0), pady=5)

lbl3 = tk.Label(frame1, text="Attendance",
                width=20, fg=TEXT_COLOR, bg=ACCENT_COLOR,
                height=1, font=('Helvetica', 17, 'bold'))
lbl3.place(x=100, y=115)

res=0
exists = os.path.isfile("StudentDetails\StudentDetails.csv")
if exists:
    with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for l in reader1:
            res = res + 1
    res = (res // 2) - 1
    csvFile1.close()
else:
    res = 0
message.configure(text='Total Registrations till now  : '+str(res))

##################### MENUBAR #################################

menubar = tk.Menu(window,relief='ridge')
filemenu = tk.Menu(menubar,tearoff=0)
filemenu.add_command(label='Change Password', command = change_pass)
filemenu.add_command(label='Contact Us', command = contact)
filemenu.add_command(label='Exit',command = window.destroy)
menubar.add_cascade(label='Help',font=('times', 29, ' bold '),menu=filemenu)

################## TREEVIEW ATTENDANCE TABLE ####################

tv= ttk.Treeview(frame1,height =13,columns = ('name','date','time'))
tv.column('#0',width=82)
tv.column('name',width=130)
tv.column('date',width=133)
tv.column('time',width=133)
tv.grid(row=2,column=0,padx=(0,0),pady=(150,0),columnspan=4)
tv.heading('#0',text ='LRN')
tv.heading('name',text ='NAME')
tv.heading('date',text ='DATE')
tv.heading('time',text ='TIME')

###################### SCROLLBAR ################################

scroll=ttk.Scrollbar(frame1,orient='vertical',command=tv.yview)
scroll.grid(row=2,column=4,padx=(0,100),pady=(150,0),sticky='ns')
tv.configure(yscrollcommand=scroll.set)

###################### BUTTONS ##################################

takeImg = tk.Button(frame2, text="Take Images",
                   command=TakeImages,
                   fg=TEXT_COLOR, bg=BUTTON_COLOR,
                   width=34, height=1,
                   activebackground=ACCENT_COLOR,
                   font=('Helvetica', 15, 'bold'),
                   relief='flat', cursor='hand2')
takeImg.place(x=30, y=300)
trainImg = tk.Button(frame2, text="Save Profile",
                    command=psw,
                    fg=TEXT_COLOR, bg=BUTTON_COLOR,
                    width=34, height=1,
                    activebackground=ACCENT_COLOR,
                    font=('Helvetica', 15, 'bold'),
                    relief='flat', cursor='hand2')
trainImg.place(x=30, y=380)
trackImg = tk.Button(frame1, text="Take Attendance", command=TrackImages  ,fg="black"  ,bg="yellow"  ,width=35  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
trackImg.place(x=30,y=50)
quitWindow = tk.Button(frame1, text="Quit", command=window.destroy  ,fg="black"  ,bg="red"  ,width=35 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
quitWindow.place(x=30, y=450)

##################### END ######################################

def on_enter(e):
    e.widget['background'] = ACCENT_COLOR

def on_leave(e):
    e.widget['background'] = BUTTON_COLOR

# Add these bindings before window.mainloop()
takeImg.bind("<Enter>", on_enter)
takeImg.bind("<Leave>", on_leave)
trainImg.bind("<Enter>", on_enter)
trainImg.bind("<Leave>", on_leave)

# Add hover effects for clear buttons
clearButton.bind("<Enter>", on_enter)
clearButton.bind("<Leave>", on_leave)
clearButton2.bind("<Enter>", on_enter)
clearButton2.bind("<Leave>", on_leave)

window.configure(menu=menubar)
window.mainloop()
