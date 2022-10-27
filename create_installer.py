import os
import subprocess
import shutil

def rm_dir(folder):
    if os.path.exists(folder):
        print(f"remove folder '{folder}'")
        shutil.rmtree(folder)
        print("remove succeeded")

def make_installer(onefile=False, project_name="HSPR",installer_root_folder="installer"):
    rm_dir("build")
    rm_dir("dist")
    cmd = ["pyinstaller", "--clean", "src/main.py", "-n", project_name]
    if onefile:
        cmd.append("--onefile")
    subprocess.check_call(cmd)

    input_folder = "dist"
    if not onefile:
        input_folder = os.path.join(input_folder, project_name)

    output_filename = os.path.join(installer_root_folder, "hspr")
    if onefile:
        output_filename += "_onefile"

    shutil.make_archive(output_filename, "zip", input_folder) # .zip extension will be attach by make_archive

def main():
    installer_folder = "installer"
    rm_dir(installer_folder)
    os.makedirs(installer_folder)

    onefile = [True, False]
    for o in onefile:
        make_installer(
            onefile=o,
            installer_root_folder=installer_folder
        )

if __name__ == "__main__":
    main()