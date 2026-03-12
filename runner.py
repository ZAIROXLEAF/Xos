#XOS Interpeter V0.2
import sys
log =[sys.argv]
def executer(Keyword,word):
  if Keyword=="yap":
      #print("code output:\n")
      if word == " ":
        word = "Error blank space before \'(\'"
      print("code output:\n \n"+word)
Keyword=""
ret = 0
block=True
space_error_detect = True
Word=""
SCRIPT = sys.argv[1]
#SCRIPT= input("Enter script name with xos extension: ")
with open(SCRIPT,"r") as code:
  code = code.read()
for i in range(len(code)):
  block=True
  if code[i]=="(":
    space_error_detect = False
  if i<3:
    Keyword+=code[i]
    block=False
  elif code[i]!="(" and code[i]!=")" and block:
    Word+=code[i]
    #elif code[i]=="(" or code[i]==")":
    #block=True
  elif code[i]==")":
    executer(Keyword,Word)
    ret=1
    break
  if space_error_detect:
    if code[i]==" ":
      executer(Keyword," ")
      ret=0
      break
if ret == 0:
  print("\nRun unsuccessfully")
elif ret==1:
  print("\nRun successfully")