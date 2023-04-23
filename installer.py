import os

directory = "kulak_ver"

parent_dir = "C:/"

path = os.path.join(parent_dir,directory)
os.mkdir(path)

os.chdir(path)


os.mkdir(os.path.join(path,"toplantilar"))
os.mkdir(os.path.join(path,"avatarlar"))
os.mkdir(os.path.join(path,"ozetler"))


f = open('test.txt','w')
f.write("abe installer")