# A repository for Spack recipes

![CI check-spec](https://github.com//LIHPC-Computational-Geometry/spack_recipes_meshing/actions/workflows/check-spec.yml/badge.svg)
![CI check-mgx](https://github.com//LIHPC-Computational-Geometry/spack_recipes_meshing/actions/workflows/check-mgx.yml/badge.svg)

Spack package manager (https://github.com/spack/spack) is used bu LIHPC-CG projects. Spack packages are described in recipes. Two repositories of recipes are currently defined here:
- **meshing** contains the recipes of our meshing components;
- **meshing_supersede** contains recipes present in upstream spack but with modifications to suit our needs. It should be kept minimal and these modifications should be integrated into upstream when possible, and removed when they make their way into a spack release.

The **config** directory contains configuration files that can be added to the spack instance we will be using.

The **dockerfiles** directory contains various dockerfiles used by Github workflows.

This project also contains workflows used by the mgx project and its dependencies (tkutil, qtutil...).

## CI and versioning policy of mgx ecosystem projects

**Development**

Try to follow the following rules:
- develop on a branch and do a pull-request on main branch at the end,
- do not versionize project using Github interface.

**CI**

All mgx ecosystem projects conform to the same spack CI. It:
- pulls the `spack_recipes_meshing` main branch,
- builds the current project branch using Spack,
- executes unit tests (registered in `CMakeLists.txt),
- builds and runs the content of `test_link` directory.


**Versioning**

Do not versionize project using Github interface. Tag your project and push the tag. It will trigger a workflow that check rules before making the project release.
```bash
git tag X.Y.Z && git push origin X.Y.Z
```

Once the project is released, the workflow computes the project SHA and inserts it in the release documentation, for example in [release 6.2.2 of the preferences project](https://github.com/LIHPC-Computational-Geometry/preferences/releases/tag/6.2.2). Do not forget to copy the line and insert it in the Spack recipe of your project (the release documentation contains a link on it).

Adding a new tag on the `spack_recipes_meshing` project:
- builds a new release with the list of [its products version](https://github.com/LIHPC-Computational-Geometry/spack_recipes_meshing/releases/tag/1.1.2),
- creates both Spack and Cmake docker images conforming to this list of products version. These images have the same version number than the project release.

*Consequently, check that CI passes before taging `spack_recipes_meshing`: a release of this project is considered as a reference.*

## Use cases
**Development in a library like tkutil**

TODO

**Development in two dependent libraries like tkutil and qtutil**

TODO

**Development in mgx**

TODO

## Project branches

TODO

## Docker images

TODO
