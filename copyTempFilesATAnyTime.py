import subprocess
import glob




cmd = "mkdir -p savedFiles"
p = subprocess.call([cmd], shell=True)

while (True):
    files = glob.glob(".Xil/Vivado-26835-caslab-srv2/dcp4/*.xdc")
    if (len(files) > 0):
        cmd = "cp -r .Xil/Vivado-26835-caslab-srv2/dcp4 savedFiles/"
        p = subprocess.call([cmd], shell=True)
        break
















