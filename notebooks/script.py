import subprocess
import os

# Change to the notebooks folder
# notebooks_folder = "./notebooks"
# os.chdir(notebooks_folder)

# Make the download_baselines.sh script executable
subprocess.run(["chmod", "+x", "C:\\Users\\Vartika\\Documents\\GitHub\\TeachMyAgent\\notebooks\\download_baselines.sh"])

# Download results using the script
subprocess.run(["./download_baselines.sh"])
