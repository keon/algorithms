import os

fnc_list = "<!--fnc_list-->\n" # prefix + implemented functions list
for (path, dir, folders) in sorted(os.walk("./algorithms"))[1:]: # first folder is 'algorithms' so skiped that
    
    if '.py' not in path.split(os.path.sep)[-1]:
        fnc_list += (path.count(os.sep)-1) * "  " + '* [' + path.split(os.path.sep)[-1] + '](' + path + ')\n'
    for filename in sorted(folders):       
        ext = os.path.splitext(filename)[-1]
        if ext == '.py' and filename != '__init__.py':
            fnc_list += path.count(os.sep) * "  " + '* [' + filename + '](' + os.path.join(path, filename) + ')\n'
            
fnc_list += "<!--/fnc_list-->\n" # suffix
  
f = open("README.md", 'r')
README = f.read() # read existing README.md
f.close()

f = open("README.md", 'w')
# change existing implemented functions list to new list
replace_str = '<!--fnc_list-->' + README.split('<!--fnc_list-->')[1].split('<!--/fnc_list-->')[0] + '<!--/fnc_list-->\n'
README = README.replace(replace_str, fnc_list) 
f.write(README) # update README.md
f.close()

