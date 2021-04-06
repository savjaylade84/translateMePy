from translate import Translator

#     get the user prefer file and language to translate

print("example: file.txt")
filename=input(">>>[Enter Filename]:")

print("example:german")
language=input(">>>[Enter Language]:")

#    create translate object and set prefer language to use to translate
#    the original language 

translator = Translator(to_lang=language)

#     try to extract all the file text then print it
#     to show user the original then translate the text
#     to the prefer language then print the so that the user
#     know that the translation works

try:
    with open(filename,'r') as reader:
        for line in reader:
            line.strip()
            print(">>>[original]:{0}",line)
            translation=translator.translate(line)
            print(">>>[translated]:{0}",translation)
except:
   print("[File Not Exist Or Wrong Path File]")