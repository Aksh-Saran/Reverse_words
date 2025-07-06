import os
import re

def update_version_in_file(file_path, build_num_key, build_num):
    #Update build number in file using regular expressions
    with open(file_path, 'r') as file_in:
        file_content = file_in.read()
        updated_content = re.sub(fr'({build_num_key}=)(\s*\d+)', rf'\1 {build_num}', file_content)

    with open(file_path, 'w') as file_out:
        file_out.write(updated_content)

def update_sconstruct(source_path, build_num):
    #Update build number in SConstruct file
    sconstruct_path = os.path.join(source_path, "develop", "global", "src", "SConstruct")
    update_version_in_file(sconstruct_path, "point", build_num)

def update_version_file(source_path, build_num):
    #Update build number in VERSION file
    version_path = os.path.join(source_path, "develop", "global", "src", "VERSION")
    update_version_in_file(version_path, "ADLMSDK_VERSION_POINT", build_num)

def main():
    source_path = os.environ.get("SourcePath")
    build_num = os.environ.get("BuildNum")
    
    #If no Src path or Buildnum found then try and except block is used to catch any exception
    if not source_path or not build_num:
        print("Error: SourcePath or BuildNum environment variable not set.")
        return

    try:
        update_sconstruct(source_path, build_num)
        update_version_file(source_path, build_num)
        print("Version numbers updated successfully.")
    except Exception as e:
        print(f"An error occurred while updating version numbers: {e}")

if __name__ == "__main__":
    main()
