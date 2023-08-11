# A repository for the spack recipes of our meshing software

![CI check-spec](https://github.com//LIHPC-Computational-Geometry/spack_recipes_meshing/actions/workflows/check-spec.yml/badge.svg)
![CI check-mgx](https://github.com//LIHPC-Computational-Geometry/spack_recipes_meshing/actions/workflows/check-mgx.yml/badge.svg)

Spack package manager (https://github.com/spack/spack) is used bu LIHPC-CG projects. Spack packages are described in recipes. Two repositories of recipes are currently defined here:
- **meshing** contains the recipes of our meshing components;
- **meshing_supersede** contains recipes present in upstream spack but with modifications to suit our needs. It should be kept minimal and these modifications should be integrated into upstream when possible, and removed when they make their way into a spack release.

The **config** directory contains configuration files that can be added to the spack instance we will be using.

The **dockerfiles** directory contains various dockerfiles used by Github workflows.

This project also contains workflows used by the mgx project and its dependencies (tkutil, qtutil...).

## CI and versioning policy of mgx ecosystem projects
### CI

TODO

### Versioning

TODO

### Development use cases

TODO

## Project branches

TODO
## Docker images

TODO