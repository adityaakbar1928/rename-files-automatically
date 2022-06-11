import os

def menu():
    global before_ext, after_ext
    print("Welcome to Rename tools\n"
          "Made with Love by Aditya\n"
          "Put this exe to main folder where the images is located (it will change files in subfolder too)\n")
    before_ext = str(input("Type your file extension (eg, jfif or jpg): "))
    after_ext = str(input("Type extension you want (eg, png): "))
    confirmation = str(input("You want to change your "+before_ext+" files to "+after_ext+" ? (Y/N) "))
    if confirmation.lower() == "y":
        convert(before_ext, after_ext)
    else:
        print("error")

def convert(bext, aext):
    os.system('for /r %x in (*.'+bext+') do ren "%x" *.'+aext)

menu()