# A repository for the spack recipes of our meshing software

![CI check-spec](https://github.com//LIHPC-Computational-Geometry/spack_recipes_meshing/actions/workflows/check-spec.yml/badge.svg)
![CI check-mgx](https://github.com//LIHPC-Computational-Geometry/spack_recipes_meshing/actions/workflows/check-mgx.yml/badge.svg)

In order to develop and in our CI we can use the spack package manager (https://github.com/spack/spack), where packages are described in recipes. We will usually be based on the latest release from spack.

Two repos are currently defined here:
- **meshing** contains the recipes of our meshing components;
- **meshing_supersede** contains recipes present in upstream spack but with modifications to suit our needs. It should be kept minimal and these modifications should be integrated into upstream when possible, and removed when they make their way into a spack release.

The **config** directory contains configuration files that can be added to the spack instance we will be using.
