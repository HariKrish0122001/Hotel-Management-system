from tkinter import *
import check_in_ui
import check_out
import get_info
import customer_info

class Hotel:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry('700x700')
        
        # create mainframe to add message
        top = Frame(self.root)
        top.pack(side="top")

        # create frame to add buttons
        bottom = Frame(self.root)
        bottom.pack(side="top")


        # display message
        self.label = Label(top, font=('Algerian', 50, 'bold'), text="LEXUS CROSS", fg="#000000", anchor="center")
        self.label.grid(row=0, column=3)

        # create check in button
        self.check_in_button = Button(bottom, text="CHECK IN", font=('', 20), bg="white", relief=RIDGE, height=1,
                                      width=30,
                                      fg="magenta", anchor="center",
                                      command=check_in_ui.check_in_ui_fun)
        # call check_in_ui_fun from check_in_ui.py file
        self.check_in_button.grid(row=0, column=2, padx=5, pady=5)

        # create check out button
        self.check_out_button = Button(bottom, text="CHECK OUT", font=('', 20), bg="white", height=1,
                                       width=30, fg="magenta", anchor="center",activebackground="yellow",activeforeground="Red",
                                       command=check_out.check_out_ui)   # call check_out_ui function from check_out.py file
        self.check_out_button.grid(row=1, column=2, padx=5, pady=5)

        # create show list button
        self.room_info_button = Button(bottom, text="INFORMATION OF ROOMS", font=('', 20), bg="white", relief=RIDGE,
                                       height=1,
                                       width=30, fg="magenta", anchor="center",
                                       command=get_info.get_info_ui)  # call get_info_ui function from get_info.py file
        self.room_info_button.grid(row=2, column=2, padx=5, pady=5)

        # create get information of all the guest
        self.get_info_button = Button(bottom, text="INFORMATION OF ALL GUEST", font=('', 20), bg="white",
                                      relief=RIDGE,
                                      height=1, width=30, fg="magenta", anchor="center",
                                      command=customer_info.customer_info_ui)
        # call customer_info_ui function from customer_info.py file
        self.get_info_button.grid(row=3, column=2, padx=5, pady=5)

        # button to exit the program
        self.exit_button = Button(bottom, text="EXIT", font=('', 20), bg="white", relief=RIDGE, height=1, width=30,
                                  fg="magenta",
                                  anchor="center", command=quit)
        self.exit_button.grid(row=4, column=2, padx=5, pady=5)


def home_ui():
    root = Tk()
    w=Label(root,text="WELCOME TO ",fg="red",font=("Times New Roman",30,'italic'))
    w.pack()
    frontimage= PhotoImage(file="hotel_img.png")
    front_image = Label(root, image=frontimage)
    
    front_image.pack()
    application = Hotel(root)
    root.mainloop()

if __name__ == '__main__':
    home_ui()
