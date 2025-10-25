# Cycloidal-Drive-Animation
Based on matplotlib

## Quick Setup with Virtual Environment

### Option 1: Automated Setup (Recommended)
Run one of the following scripts to automatically set up a virtual environment:

**For PowerShell:**
```powershell
.\setup_venv.ps1
```

**For Command Prompt:**
```cmd
setup_venv.bat
```

### Option 2: Manual Setup
If you prefer to set up manually:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1
# On Windows Command Prompt:
venv\Scripts\activate.bat

# Install dependencies
pip install -r requirements.txt
```

## Manual Installation
If you prefer not to use a virtual environment:

```bash
pip install numpy
pip install matplotlib
```

Here is the demo vedio
Cycloid Drives Animation https://youtu.be/wV8ygmoxS0c via @YouTube 

Hope anybody else to improve the scripits!

Got the idea from the following:
https://woodencaliper.hatenablog.com/entry/2018/11/19/003515

You can use the paramaters from the GUI and draw your own cycloid drives in 3D software from the following steps.
https://www.youtube.com/watch?v=guvatctnjww

or put the paramaters into the formula mentioned in the following pdf:
https://blogs.solidworks.com/teacher/wp-content/uploads/sites/3/Building-a-Cycloidal-Drive-with-SOLIDWORKS.pdf
