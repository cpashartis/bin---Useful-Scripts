# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:16:17 2015
Author: christoforos

This code was written by Christopher Pashartis, cpashartis@gmail.com

Code Overview:
This is a class that is meant to handle all creation of directories as well as
files required for simulations.
"""


class GenerateSimulation():
    from os import getcwd, makedirs, path
    from itertools import product
    from shutil import copy

    def __init__(self, var_dict, copy_file_list, target_dir, overwrite = False):
        """var_dict: dictionary of variable name keyword with a list of numbers
        to run over
        copy_file_list: list of files to copy to target directory
        target_dir: target directory"""
        self.var_dict = var_dict
        self.copy_file_list = copy_file_list
        self.owd = getcwd()
        self.overwrite = overwrite
        print self.owd
        if target_dir.count('/') == 0:
            print "Assuming target directory is to be created in cwd"
            self.twd = self.owd + '/' + self.twd
        else:
            self.twd = target_dir

    def GenerateDir(self):
        """Generates the trees as well as moves the files to that tree,
        keeps an updated copy of what was run in the directory as well as
        what was just run"""

        with open('direc_run.txt', 'w') as datafile: #overwrite file always
            with open('total_run.txt', 'a') as totalfile:
                for param in product(*self.var_dict.values()):
                    #create format of 1_2
                    new_dir = '_'.join(str(param).strip('()'))
                    makedirs(self.twd + '/' + new_dir, exist_ok = self.overwrite)
                    datafile.writeline(new_dir) #add files to twd filelist

                    #append to total file if didn't exist
                    if path.isdir(self.twd + '/' + new_dir) == False:
                        totalfile.writeline(new_dir)

                    #copy the base files here
                    for copy_file in copy_file_list:
                        copy(copy_file_list,self.twd + '/' + new_dir + '/' )

                        ModifyOtherScripts(self)

    def ModifyOtherScripts(self):

        return 0