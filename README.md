# FibPhoFlow

FibPhoFlow is an open-source fiber photometry data analysis package compatible with data obtained from [TdT fiber photometry](https://www.tdt.com/system/behavior-and-fiber-photometry/) hardware and software.

## Installation

This package is currently available on [PyPi](https://test.pypi.org/project/fibphoflow/) for download with [pip](https://pythonspeed.com/articles/conda-vs-pip/), but certain dependency issues associated with the HDF5 data storage related python packages, h5py and pytables, tend to cause build errors in different environments. The simplest way to use this python package is to use the python package manager, Anaconda. If you are trying to pip install this package without Conda you will need to download the C package [HDF5](https://www.hdfgroup.org/downloads/hdf5/). The instructions that follow are for the Conda installation.

### Step 1: 
- Download [Anaconda](https://www.anaconda.com/download) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- Download an IDE which allows you to see plots, such as [Spyder](https://www.spyder-ide.org/) or [Jupyterlab](https://jupyter.org/)
  - You can install Spyder or Jupyterlab once you have Conda with one of these:
    ```
    conda install -c anaconda spyder
    ```
    ```
    conda install -c conda-forge jupyterlab
    ```

### Step 2: Create Conda virtual environment for fibphoflow
- Download this repository or a Github release of this repository following [these instructions](https://blog.hubspot.com/website/download-from-github#repository)
- Open your [Terminal](https://cs.colby.edu/maxwell/courses/tutorials/terminal/)
- Feel free to move the downloaded Github folder and rename
- Navigate to the folder using your Terminal application
```
cd path/to/<folder_name>
```
- Once in the folder you created, create a Conda virtual environnment (aka 'venv' which includes needed package dependences)
```
conda env create -f environment.yml
```
- Activate this Conda venv
```
conda activate fibphoflow_venv
```
- Note: For more information on general conda venv usage, [see here](environments.html#activating-an-environment)

### Step 3: Connect the Conda venv with your IDE and run the IDE
- Configure your venv with the IDE's Spyder or Jupyter [with these instructions](https://medium.com/@apremgeorge/using-conda-python-environments-with-spyder-ide-and-jupyter-notebooks-in-windows-4e0a905aaac5)  
- Alternatively, you can install an IDE into your venv with:
```
conda install <IDE Name>
```
```
<IDE Name>
```

### Step 4: Modify tutorial_project.py to your own workflow
- The simplest way to run Fibphoflow until a Python package is eventually developed is to move all TdT photometry recordings to a directory where the parent folder contains tutorial_project.py (later to be renamed to whatever you want), Excel files where you store metadata for your traces (example tutorial_project.xlsx file included in downloaded repository), the fibphoflow.py file which is in the src subdirectory of the downloaded repository, and the fibphoflow_config.py file also in src. You can organize your recordings into subfolders within this parent folder and Fibphoflow will search those subdirectories.
- In your IDE, your working directory needs to be set to the path of the parent folder to be able to read the files mentioned above (there are other ways of doing this if you know Python better, but for simplicity just do this).

## Overview of Workflow

1. The raw fiber photometry data streams from TdT photometry recording directories are loaded using the TdT python package. TdT recording files need to be located in the working directory or its subdirectories for them to be located while running fibphoflow.py. The script is currently only compatible with a GCaMP and UV/Isosbestic stream.

2. A simple low pass filtering step (a moving average) is applied to help smooth out signal noise

3. The streams (GCaMP and UV) are downsampled based on the hz value one sets.

4. A normalization of the calcium stream is performed using the isosbestic stream, but this is optional and it is possible for the calcium and isosbestic traces to just be normalized to themselves.

5. From here, based on the experimental metadata found in the experiment's excel file, the processed streams from step 3 are chopped up into specific "epoch" traces for analysis and these traces are normalized to user-defined recording baseline periods to obtain traces in terms of delta F/F.


## To-do's

1. Fix package dependency issues and allow for download with conda-forge and PyPi

2. Add option for butterworth low pass filtering step.

3. Make things more Jupyter compatible so that report printouts can be made easier

4. Clean up code commenting/documentation, along with error messages

5. Add third red calcium channel

6. Add z-scoring
