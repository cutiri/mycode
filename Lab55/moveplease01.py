#!/usr/bin/env python3

import shutil, os

def main():
    os.chdir("/home/student/mycode/Lab55")    

    shutil.move("raynor.obj", "ceph_storage/")

    xname:str = input('What is the new name for kerrigan.obj? ')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


if __name__ == "__main__":
    main()

def test(n1: str, n2: int):
    pass
