import subprocess
import sys

def upgrade_pip():
    """
    Upgrades pip to the latest version.
    """
    print("Upgrading pip...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

def upgrade_all_packages():
    """
    Upgrades all installed packages to the latest versions.
    """
    print("Upgrading all installed packages...")
    # Get the list of outdated packages
    outdated = subprocess.check_output([sys.executable, "-m", "pip", "list", "--outdated"]).decode("utf-8")
    for line in outdated.split("\n")[2:]:  # Skip the header lines
        if line:
            package = line.split()[0]
            print(f"Upgrading package: {package}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])

if __name__ == "__main__":
    try:
        upgrade_pip()
        upgrade_all_packages()
        print("All packages are up to date.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
