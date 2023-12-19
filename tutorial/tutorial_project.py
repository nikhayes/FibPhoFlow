#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 14:28:11 2023

@author: nikolashayes
"""


from fibphoflow import *

import os
import pandas as pd
import xlsxwriter
import numpy as np
import seaborn as sns


file = "Fibphoflow_Tutorial.xlsx" # Should be in working directory
exp_df = xlsx2dataframe(file, sheet_list= ["Experiment Group 1"]) 
sub_df = exp_df[exp_df["Experiment"].isin([1])] # You can use this to subset data on your excel sheet

# To set your channel config, you need to know what these values are from your
# TdT settings. Go to your recording folder and look at the StoresListing.txt to check.
# The settings shown below are for shown for a setup where multiple mice recordings are done
channel_config = {
        "colors" : ["gcamp", "isos"],  #needs to stay in this order
        "gcamp" : {1 : {"_465A"}, 
                   2 : {"_465B"},
                   3 : {"_465C"}},
        "isos" : {1 : {"_405A"}, 
                  2 : {"_405B"},
                  3 : {"_405C"}}}
       
# The below function retrieves metadata from the excel file then downsamples your recordings
# to the frequency indicated by down_hz. The downsampled data will be stored in a compressed
# file format known as hdf5. If know hdf5 file for "Fibphoflow_Tutorial" exists yet, it will be 
# generated when running this function. The name can be different.
recordings = extract_experiment(sub_df, channel_config, hdf5_name="Fibphoflow_Tutorial", down_hz=1)

# For our own experiments, we have multiple parts of a full recording where we want to 
# hone in and create an Epoch window just for that part of the recording. Epoch names and
# start times are retrieved from the Excel sheet.
injection_epoch = ["Injection", 45, 5, 3] # ['Name of Epoch on excel file", Length of Epoch not including baseline before, length of time for baseline, baseline offset from Epoch start]
fooddrop_epoch = ["Food Drop", 15, 5, 1]

epoch_list = [injection_epoch, fooddrop_epoch]

epoch_dict, r_epoch_dict = group_epochs_extraction(sub_df, recordings, epoch_list, ema_smooth=False)

inspect_recordings(sub_df, r_epoch_dict) # This plots individual traces

groups2compare = sub_df['Group'].tolist() #all groups in sub_df
#groups2compare = ["PBS_then_PBS", "PBS_then_InterventionA]

# This will average together traces if the mouse is the same and the experimental group is the same
avg_epoch_dict = average_epochs(sub_df, epoch_dict, epoch_list, channel="gcamp_isocorr") #gcamp_isocorr, gcamp, or isos
plot_averagedepochs(avg_epoch_dict, groups2compare)

# Generate Heatmaps
# https://seaborn.pydata.org/tutorial/color_palettes.html https://medium.com/@morganjonesartist/color-guide-to-seaborn-palettes-da849406d44f
my_cmap = sns.color_palette("ch:s=-.2,r=.6", as_cmap=True) 
epochs = dict({"IP Injection":(20, -60)}) # "Epoch name" (max, min) of % delta fluorescence 
heatmap_dim = (10, 10) #width, height of figure
plot_averagedepochs_with_heat(epochs, avg_epoch_dict, groups2compare, heatmap_dim)

# This generates an excel file with your data. Each Epoch is on a different sheet
averagedepochs_to_excel("epochdata.xlsx", avg_epoch_dict, groups2compare)

