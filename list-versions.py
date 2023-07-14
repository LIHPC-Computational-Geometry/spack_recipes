import glob
import re
import sys
import os

def listVersions(source_path):
    recipes = glob.glob(source_path + '/**/package.py', recursive=True)
    with open(source_path + '/recipes.md', 'w') as md:
        md.write('**Below the last version of products contained in Spack recipes for this release.**\n')
        md.write('| Product | Version |\n')
        md.write('| ------- | ------- |\n')
        for recipe in recipes:
            with open(recipe) as f:
                product_name = os.path.basename(os.path.dirname(recipe))
                line = ' '.join(f.readlines())
                version = re.search("version\([\'\"]([0-9]+(\.[0-9]+)*)[\'\"]", line)
                version_name = 'undefined' if version is None else version.group(1)
                md.write('| ' + product_name + ' | ' + version_name + ' |\n')

            
if __name__ == "__main__":
        project_path = sys.argv[1]
        listVersions(project_path)
