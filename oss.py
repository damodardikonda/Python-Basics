import os
#print(dir(os))
print("\n\nget current direction");
print(os.getcwd());

print("\n\nprinting a list of directories");
print(os.listdir());

print("\n\ncreate a directory")
#print(os.mkdir("newdir"))# it creates only top level directory
#print(os.makedirs("nnndir/su-dir"))#it create a bottomlevvel diretory

print("\n\nfor deleting directory")
#print(os.rmdir("newdir"))
#print(os.removedirs(nnndir))


print("\n\nRenaming old file newdir")
#print(os.rename('newdir','mydirr'))

print('\n\nprinting information relate to folder')
print(os.stat('newdir,sub-dir1'))

print('\n\nprinting six]ze related info')
print(os.stat('newdir,sub-dir1').st_size)

print('mode relation information');
print(os.stat('newdir,sub-dir1').st_mode)
print("as like this we  can display all information")


#from datetime import datetime

#mod_time=os.stat('newdir,sub_dir1').st_mtime
#mt=datetime.fromtimestamp(mod_time)
#print(mt)

print('home location');
print(os.environ.get('Dektop'));

print('setting path')
#file_path=os.path.join(os.environ.get('Desktop'),'abc.txt')
#print(file_path)
