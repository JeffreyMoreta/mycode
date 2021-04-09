#!/usr/bin/env python3
import shutil
import os

os.chdir('/home/student/mycode/')
shutil.move('raynor.obj', 'ceph_storage/')

xname = input('What is the new name for kerrigan.obj?')
shutil.move('../ceph_storage/kerrigan.obj', 'cepg_storage/' + xname)
