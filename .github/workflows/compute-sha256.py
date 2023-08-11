import re
import sys
import requests
import hashlib
import os

base_url = 'https://github.com/LIHPC-Computational-Geometry/'

def computeSha256(project_name, project_version, project_path):
    try:
        readable_hash = str(sha256sum(project_name, project_version))

        file_name = project_path + '/newbody.md'
        print("Creating markdown file:", file_name)
        spack_recipe_url = base_url + 'spack_recipes_meshing/blob/main/meshing/packages/' + project_name + '/package.py'
        with open(file_name, 'w') as md:
            md.write("Do not forget to update your [Spack recipe](" + spack_recipe_url + ") with the following line:\n")
            md.write("```python\n")
            md.write("    version('" + project_version + "', sha256='" + readable_hash + "')\n")
            md.write("```\n")
        print("File created:", file_name)

        return 0

    except Exception as e:
        print(e)
        return -1

def sha256sum(project_name, project_version):
    url = base_url + project_name + '/archive/refs/tags/' + project_version + '.tar.gz'

    print("Downloading", url)
    tarball = requests.get(url, allow_redirects=True)
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        file_name = "/tmp/" + project_name + "-" + project_version + ".tar.gz"
        with open(file_name, 'wb') as f:
            f.write(response.raw.read())
            print('File created:', file_name)
    else:
        raise Exception("Can not download: " + url)

    print("Computing sha256")
    readable_hash = -1
    with open(file_name,"rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest()

    return readable_hash


if __name__ == "__main__":
    project_name = sys.argv[1]
    project_version = sys.argv[2]
    project_path = sys.argv[3]
    sys.exit(computeSha256(project_name, project_version, project_path))
