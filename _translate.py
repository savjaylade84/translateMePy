from translate import Translator

print("<example: file.txt")
filename=input("[Enter Filename]:")

translator = Translator(to_lang="german")

try:
    with open(filename,'r') as reader:
        for line in reader:
            line.strip()
            print(line)
            translation=translator.translate(line)
            print(translation)
except:
   print("[File Not Exist Or Wrong Path File]")