import glob
import re
import sys

def listVersions(source_path):
    recipes = glob.glob(source_path + '/**/package.py', recursive=True)
    for recipe in recipes:
        print("file:", recipe)
        with open(recipe) as f:
            line = ' '.join(f.readlines())
            product = re.search("class (.*)\(", line)
            print("   ", product.group(1).strip())
            version = re.search("version\([\'\"]([0-9]+(\.[0-9]+)*)[\'\"]", line)
            if version is None:
                print("      No VERSION")
            else:
                print("      ", version.group(1))
            
if __name__ == "__main__":
        project_path = sys.argv[1]
        listVersions(project_path)
