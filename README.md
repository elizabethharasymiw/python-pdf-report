# report-generator
Example of how to make a PDF report using python FPDF (Free PDF)

## Python virtual environment maintenance commands
```
# Create python virtual environment
python3 -m venv python-env
```
```
# Activate python virtual environment
source python-env/bin/activate
```
```
# Deactivate python virtual environment
deactivate
```
```
# Install required dependencies to the current python virtual environment
pip install -r requirements.txt
```
```
# List current python packages in this virtual environment
pip list
```
```
# Example of installing a new python package with pip
pip install package_name
pip install fpdf
```
```
# Save the current the versions of all python packages used in this
# virtual environment. This can be used later to recreate another
# virtual environment in the future with the same dependencies.
pip freeze > requirements.txt
```
