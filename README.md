# FibPhoFlow

FibPhoFlow is an open-source fiber photometry data analysis package compatible with data obtained from [TdT fiber photometry](https://www.tdt.com/system/behavior-and-fiber-photometry/) hardware and software.

## How to download

This package is currently available on PyPi for download with pip, but certain dependency issues associated with the HDF5 data storage package Tables are currently being troubleshooted. 

Until that is resolved, one must download the fibphoflow.py file present in the github src folder, and use it as a local script. One can place fibphoflow.py in your python working directory or add its path with sys.path.append(). Also note that this package applies experimental metadata from a user-provided excel sheet, so at some step the user will need Microsoft Excel.

## Overview of Workflow

* Note that a well documented practice analysis walkthrough will be added soon.

1. The raw fiber photometry data streams from TdT photometry recording directories are loaded using the TdT python package. TdT recording files need to be located in the working directory or its subdirectories for them to be located while running fibphoflow.py. The script is currently only compatible with a GCaMP and UV/Isosbestic stream.

2. A simple low pass filtering step (a moving average) is applied to help smooth out signal noise

3. The streams (GCaMP and UV) are downsampled based on the hz value one sets.

4. A normalization of the calcium stream is performed using the isosbestic stream

5. From here, based on the experimental metadata found in the experiment's excel file, the processed streams from step 3 are chopped up into specific "epoch" traces for analysis and these traces are normalized to user-defined recording baseline periods to obtain traces in terms of delta F/F.


## To-do's

1. Fix package dependency issues and allow for download with conda-forge

2. Add option for butterworth low pass filtering step.

3. Make things more Jupyter compatible so that report printouts can be made easier

4. Clean up code commenting/documentation, along with error messages

5. Add third red calcium channel

6. Add z-scoring