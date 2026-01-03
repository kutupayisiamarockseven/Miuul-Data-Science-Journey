############################################
# Virtual Environment and Packet Management #
############################################
# NOTE: 'numpy' is used as an example package name below.

# -n (name)      : Specifies the name of the environment.
# -c (channel)   : Specifies the source channel to download from.
# -f (file)      : Specifies a file path to read from.
# --all          : Selects all packages in the current environment.

# --- 1. Environment Management ---

# To list all available environments: conda env list

# To create a new environment named 'myenv': conda create -n myenv

# To activate the environment: conda activate myenv

# To deactivate the current environment: conda deactivate

# To delete an environment completely: conda env remove -n myenv


# --- 2. Package Management with Conda ---

# List installed packages in the current environment: conda list

# Install a specific package: conda install numpy

# Install multiple packages at once: conda install numpy scipy pandas

# Install a specific version of a package: conda install numpy=1.20.1

# Update a specific package: conda update numpy

# Update all packages in the environment: conda update --all

# Uninstall (remove) a package: conda remove numpy

# Update Conda itself (Base environment): conda update -n base -c defaults conda


# --- 3. Package Management with Pip ---
# Pip: Python Package Index (Standard Python installer)

# Install a package via pip: pip install pandas

# Install a specific version via pip: pip install pandas==1.20.1


# --- 4. Export & Import ---

# Export the active environment to a file (Save configuration): conda env export > environment.yaml

# Create an environment from a file (Load configuration): conda env create -f environment.yaml