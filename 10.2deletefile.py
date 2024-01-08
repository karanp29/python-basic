# -----DELETE FILE------------
# use OS module 
import os

os.remove("sample.txt")

#
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")