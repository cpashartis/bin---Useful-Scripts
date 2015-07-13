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

    def __init__(self, var_dict, copy_file_list, target_dir, overwrite = True):
        """var_dict: dictionary of variable name keyword with a list of numbers
        to run over
        copy_file_list: list of files to copy to target directory
        target_dir: target directory"""

        from os import getcwd

        self.var_dict = var_dict
        self.copy_file_list = copy_file_list
        self.owd = getcwd()
        self.overwrite = overwrite
        if target_dir.count('/') == 0:
            print "Assuming target directory is to be created in cwd"
            self.twd = self.owd + '/' + target_dir.strip('/')
        else:
            self.twd = target_dir

        self.GenerateDir()

    def GenerateDir(self):
        """Generates the trees as well as moves the files to that tree,
        keeps an updated copy of what was run in the directory as well as
        what was just run"""

        from itertools import product
        from shutil import copytree, rmtree
        from os import path,makedirs

        try: #ignore if exists
            makedirs(self.twd)
        except OSError:
            pass

        with open(self.twd + '/direc_run.txt', 'w') as datafile: #overwrite file always

            #check if total file exists, otherwise, make it and mark ordering
            if path.isfile(self.twd + '/total_run.txt') == False:
                with open(self.twd + '/total_run.txt', 'w') as totalfile:
                    totalfile.write('#' + '\t'.join(self.var_dict.keys()) + '\n')
            with open(self.twd + '/total_run.txt', 'a') as totalfile:
                for param in product(*self.var_dict.values()):
                    #create format of 1_2
                    new_dir = '_'.join([str(i) for i in param])

                    if path.exists(self.twd + '/' + new_dir) == self.overwrite and self.overwrite == True:
                        rmtree(self.twd + '/' + new_dir)

                    #append to total file if didn't exist
                    if path.exists(self.twd + '/' + new_dir) == False:
                        totalfile.write(new_dir + '\n')

                    #copy the base files here
                    for copy_file in self.copy_file_list:
                        copytree(copy_file,self.twd + '/' + new_dir + '/' )
                    datafile.write(new_dir + '\n') #add files to twd filelist

        self.ModifyOtherScripts() #call this with inheritance to do what you want


    def ModifyOtherScripts(self):

        return 0