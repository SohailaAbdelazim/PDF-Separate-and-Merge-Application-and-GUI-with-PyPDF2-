# PDF merging, extracting and spliting application with its GUI Using tiknter library and PyPDF2
# Authors: Basmala Gad, Sohaila Khalifa and Sara Walid
import os.path
import PyPDF2

def file_merger():

    mergered_file = PyPDF2.PdfFileMerger()
    files_number = int(input("Please enter files number you want to merge: "))
    pdf_files = []
    # loop for appending files names to the list
    for i in range(0, files_number):
        pdf_file = input("Please enter files name: ")+".pdf"
        if not os.path.isfile(pdf_file):
            pdf_file = input("Can not find this file in directory, Please enter correct files name: ") + ".pdf"
        pdf_files.append(pdf_file)
    # loop to marge files
    for pdf in pdf_files:
        mergered_file.append(PyPDF2.PdfFileReader(pdf, 'rb'))
    mergered_file.write("Merged File.pdf")
    mergered_file.close()


def page_extractor():

    file_name = input("Please enter file name you want to extract page from: ")
    pdf_file_name = file_name + ".pdf"
    if not os.path.isfile(pdf_file_name):
        file_name = input("Can not find this file in directory, Please enter correct file name: ")
        pdf_file_name = file_name + ".pdf"
    pdf_file = PyPDF2.PdfFileReader(pdf_file_name, 'rb')
    page_number = int(input("Please enter page number you want to extract: "))
    pdf_length = pdf_file.getNumPages()
    if page_number > pdf_length:
        page_number = int(input("Invalid Page Number, Please enter page number you want to extract: "))
    pdf_extract = PyPDF2.PdfFileWriter()
    # (page_number-1) because getPage start counting form 0
    pdf_extract.addPage(pdf_file.getPage(page_number - 1))
    with open(file_name + '-' + str(page_number) + '.pdf', 'wb') as outputstream:
        pdf_extract.write(outputstream)


def file_split():

    file_name = input("Please enter file name you want to split: ")
    pdf_file_name = file_name+".pdf"
    if not os.path.isfile(pdf_file_name):
        file_name = input("Can not find this file in directory, Please enter file name you want to split: ")
        pdf_file_name = file_name + ".pdf"
    page_number = int(input("Please enter page number you want to be start of second file: "))
    main_pdf = PyPDF2.PdfFileReader(pdf_file_name, 'rb')
    pdf_length = main_pdf.getNumPages()         # to get how many pages in pdf file
    if page_number > pdf_length:
        page_number = int(input("Invalid Page Number, Please enter  correct page number you want to be start of second file: "))

    file1_output = PyPDF2.PdfFileWriter()
    # loop starts from 1 because getPage counting from 0
    for page in range(1, page_number):
        file1_output.addPage(main_pdf.getPage(page-1))
    with open(file_name + '-' + '1' + '.pdf', 'wb') as outputstream:
        file1_output.write(outputstream)

    file2_output = PyPDF2.PdfFileWriter()
    for page in range(page_number, pdf_length+1):
        file2_output.addPage(main_pdf.getPage(page-1))
    with open(file_name + '-' + '2' + '.pdf', 'wb') as outputstream:
        file2_output.write(outputstream)
    # we used with open to give name to the new file
    # as function addPage returns object so outputstream used to define this object


from distutils.cmd import Command
import tkinter.font 
from tkinter import *

app = Tk()
app.geometry("1200x650")   # setting window size & not allowing to resize. window title and background colour 
app.resizable(width=False, height=False)
app.title("SBS PDF") 
app.configure(bg = "#efefef") 
# seting buttons and labels font. 
button_font = tkinter.font.Font(family = "Comic Sans MS" , size = 30 )
message_font = tkinter.font.Font(family = "Comic Sans MS" , size = 30 )

welcome = Label(app, text=" - Welcome To SBS PDF Application - " , font = message_font , fg = "#dd5a69" )
welcome.pack()
# functions to chnage the text displayed on the button after clicking on it.
def Change_merge(): 
    merge_button["text"] = "Merged"


merge_button = tkinter.Button(app, text="Merge files", command=lambda:[Change_merge(), file_merger()], width= 24 ,height= 1 ,  font = button_font , 
 background= "#c28475" )

merge_button.pack()
merge_button.place( x = 300  , y = 60 ) # setting the button place using the x and y axis dimenssions. 

def Change_extract(): 
    extract_button["text"] = "Extracted"

extract_button = tkinter.Button(app, text="Extract a page from file" , command=lambda:[Change_extract(), page_extractor()] ,  width= 24 ,height= 1 , 
 font = button_font ,  background= "#7ca3a0")
extract_button.pack()
extract_button.place( x = 10  , y = 200 )

def Change_split(): 
    split_button["text"] = "Splited"

split_button = tkinter.Button(app, text="Split file into separate pages" , command = lambda: [Change_split() ,file_split()],  width= 24 ,height= 1  , 
 font = button_font ,  background= "#619d9b" )
split_button.pack()
split_button.place( x = 600  , y = 200 )

def Change_exit(): 
    exit_button["text"] = "Bye Bye"

exit_button = tkinter.Button(app, text="Exit" , command = lambda:[Change_exit(), app.destroy()],  width= 24 ,height= 1 , 
 font = button_font ,  background= "#e8c3a8")
exit_button.pack()
exit_button.place( x = 300  , y = 340 )

thankyou = Label(app, text=" - Thank you for using SBS PDF Application - " , font = message_font , fg = "#dd5a69" )
thankyou.pack()
thankyou.place( x = 180  , y = 450 )
app.mainloop()

