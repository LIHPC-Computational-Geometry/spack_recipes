import glob
import re
import sys
import os

# Parse the list of recipes and create a markdown file
# containing each product name and associated last version.
# Used in CI when a new is release is creted to comment it.
def listVersions(source_path):
    print("Extracting products name and version from Spack recipes")
    recipes = glob.glob(source_path + '/**/package.py', recursive=True)
    products = {}
    for recipe in recipes:
        with open(recipe) as f:
            product_name = os.path.basename(os.path.dirname(recipe))
            line = ' '.join(f.readlines())
            version = re.search("version\([\'\"]([0-9]+(\.[0-9]+)*)[\'\"]", line)
            version_name = 'undefined' if version is None else version.group(1)
            products[product_name] = version_name
    print(products)

    file_name = source_path + '/recipes.md'
    print("Creating markdown file:", file_name)
    with open(file_name, 'w') as md:
        md.write('**Below the last version of products contained in Spack recipes for this release.**\n')
        md.write('| Product | Version |\n')
        md.write('| ------- | ------- |\n')
        for product in products.items():
            product_name = product[0]
            version = product[1]
            md.write('| ' + product_name + ' | ' + version + ' |\n')
    print("File created:", file_name)
            
    file_name = source_path + '/recipes.sh'
    print("Creating bash file:", file_name)
    with open(file_name, 'w') as md:
        md.write('#!/bin/bash\n\n')
        md.write('declare -A products\n')
        for product in products.items():
            product_name = product[0]
            version = product[1]
            md.write('products[' + product_name + ']=' + version + '\n')
    print("File created:", file_name)

if __name__ == "__main__":
    project_path = sys.argv[1]
    listVersions(project_path)
