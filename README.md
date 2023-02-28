# A repository for the spack recipes of our meshing software

In order to develop and in our CI we can use the spack package manager (https://github.com/spack/spack), where packages are described in recipes. We will usually be based on the latest release from spack.

two repos are currently defined here:
- **meshing_repo** contains the recipes of our meshing components;
- **supersede_repo** contains recipes present in upstream spack but with modifications to suit our needs. It should be kept minimal and these modifications should be integrated into upstream when possible, and removed when they make their way into a spack release.

The **config** directory contains configuration files that can be added to the spack instance we will be using.
