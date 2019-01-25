#!/usr/bin/python

# 遍历文件夹和文件
import os
def traverseDirByOSWalk(path):
  path = os.path.expanduser(path)
  for (dirname, subdir, subfile) in os.walk(path):
    #print('dirname is %s, subdir is %s, subfile is %s' % (dirname, subdir, subfile))
    print('[' + dirname + ']')
    for d in subdir:
      print(d)
    for f in subfile:
      print(os.path.join(dirname, f))
      
# 移动文件
import shutil
shutil.move(src, dst)
