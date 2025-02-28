this script will take in input SDF and/or PDB files, creating one .mae file per input provided (i.e., for each input file, one output file is generated).

the script expects that your input files are within a folder "./inputs/"

to run the script, you will first need to ensure that RDKit is installed

```
pip install rdkit
```
a common alternative to the above is:

```
python3 -m pip install rdkit
```
once your packages are installed and inputs have been placed into the correct folder, run the script in terminal using
```
python3 rdkit_convert_to_mae.py
```

outputs will be stored in the newly-created folder "./outputs/"
