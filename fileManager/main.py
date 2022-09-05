#!/usr/bin/env python3

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
import shutil
import os
import easygui

# Open a file box window
def open_window():
    read = easygui.fileopenbox()
    return read

# Open file function
def open_file():
    string = open_window()
    try:
        os.startfile(string)
    except:
        mb.showinfo("confirmation", "File not Found!")

# Copy file function
def copy_file():
    source = open_window()
    destination = filedialog.askdirectory()
    shutil.copy(source, destination)
    mb.showinfo("confirmation", "File Copied!")

# Delete file function
def delete_file():
    del_file = open_window()
    if os.path.exists(del_file):
        os.remove(del_file)
    else:
        mb.showinfo("confirmation", "File not Found!")

# Rename file function
def rename_file():
    chosenFile = open_window()
    path1 = os.path.dirname(chosenFile)
    extension = os.path.splitext(chosenFile)[1]
    print("Enter new name for the chosen file")
    newName = input()
    path = os.path.join(path1, newName+extension)
    print(path)
    os.rename(chosenFile,path)
    mb.showinfo('confirmation', "File Renamed !")

# Move file function
def move_file():
    source = open_window()
    destination = filedialog.askdirectory()
    if(source==destination):
        mb.showinfo('confirmation', "Source and destination are same")
    else:
        shutil.move(source, destination)
        mb.showinfo('confirmation', "File Moved !")

# Function to make a new folder
def make_folder():
    newFolderPath = filedialog.askdirectory()
    print("Enter name of new folder")
    newFolder = input()
    path = os.path.join(newFolderPath, newFolder)
    os.mkdir(path)
    mb.showinfo('confirmation', "Folder created !")

# Function to remove a folder
def remove_folder():
    delFolder = filedialog.askdirectory()
    os.rmdir(delFolder)
    mb.showinfo('confirmation', "Folder Deleted !")

# Function to list all the files in folder
def list_files():
    folderList = filedialog.askdirectory()
    sortlist = sorted(os.listdir(folderList))
    i=0
    print("Files in ", folderList, "folder are:")
    while(i<len(sortlist)):
        print(sortlist[i]+'\n')
        i+=1

def main():
    root = Tk()
    # creating label and buttons to perform operations
    Label(root, text="File Manager", font=("Helvetica", 16), fg="blue").grid(row = 5, column = 2)
    Button(root, text = "Open a File", command = open_file).grid(row=15, column =2)
    Button(root, text = "Copy a File", command = copy_file).grid(row = 25, column = 2)
    Button(root, text = "Delete a File", command = delete_file).grid(row = 35, column = 2)
    Button(root, text = "Rename a File", command = rename_file).grid(row = 45, column = 2)
    Button(root, text = "Move a File", command = move_file).grid(row = 55, column =2)
    Button(root, text = "Make a Folder", command = make_folder).grid(row = 75, column = 2)
    Button(root, text = "Remove a Folder", command = remove_folder).grid(row = 65, column =2)
    Button(root, text = "List all Files in Directory", command = list_files).grid(row = 85,column = 2)
    root.mainloop()

if __name__ == "__main__":
    main()
