# A repository for Spack recipes

![CI check-spec-magix3d](https://github.com//LIHPC-Computational-Geometry/spack_recipes/actions/workflows/check-spec-magix3d.yml/badge.svg)
![CI check-magix3d](https://github.com//LIHPC-Computational-Geometry/spack_recipes/actions/workflows/check-magix3d.yml/badge.svg)

Spack package manager (https://github.com/spack/spack) is used by LIHPC-CG projects. Spack packages are described in recipes. Two repositories of recipes are currently defined here:
- **meshing** contains the recipes of our meshing components;
- **meshing_supersede** contains recipes present in upstream spack but with modifications to suit our needs. It should be kept minimal and these modifications should be integrated into upstream when possible, and removed when they make their way into a spack release.

The **config** directory contains configuration files that can be added to the spack instance we will be using.

The **dockerfiles** directory contains various dockerfiles used by Github workflows.

This project also contains workflows used by the magix3d project and its dependencies (tkutil, qtutil...).

## Development in magix3d ecosystem projects

**Good practices**

Try to follow the following rules:
- develop on a branch and submit a pull-request on main branch at the end,
- do not versionize project using Github interface: use tags (see below).

**CI**

All magix3d ecosystem projects conform to the same spack CI. It:
- pulls the `spack_recipes` main branch,
- builds the current project branch using Spack,
- executes unit tests (registered in `CMakeLists.txt`),
- builds and runs the content of `test_link` directory.

**Versioning**

Version number are of the `X.Y.Z` form: please do not tag your project with a `v` prefix to share the same release name between Github and Spack.

Do not versionize project using Github interface. Tag your project and push the tag. It will trigger a workflow that checks rules and publishes the project release.
```bash
git tag X.Y.Z && git push origin X.Y.Z
```

Once the project is released, the workflow computes the project SHA and inserts it in the release documentation, for example in [release 6.2.2 of the preferences project](https://github.com/LIHPC-Computational-Geometry/preferences/releases/tag/6.2.2). Do not forget to copy the line and insert it in the Spack recipe of your project (the release documentation contains a link on it).

Adding a new tag on the `spack_recipes` project:
- builds a new release with the list of [its products version](https://github.com/LIHPC-Computational-Geometry/spack_recipes/releases/tag/1.1.2),
- creates both Spack and Cmake docker images conforming to this list of products version. These images have the same version number than the project release.

*Consequently, check that CI passes before taging `spack_recipes`: a release of this project is considered as a reference.*

## Docker images

This repository contains docker images available in the [Packages section](https://github.com/orgs/LIHPC-Computational-Geometry/packages?repo_name=spack_recipes) on the right of the main page.

The dockerfiles used to create those images are available in the [dockerfiles](./dockerfiles) directory. The dockerfile in charge of creating a `xxx` image is named `Dockerfile.xxx`, for example `Dockerfile.cmake-cgcore` for `cmake-cgcore` image. The name of image is suffixed with the OS name if different from ubuntu, for example `spack-gmds-macos`.

If you need some help to use available containers, you can read [this document](./docs/container-development.md).

**Automatic images**

At first, two core images:
- `spack-cgcore`: LIHPC-CG core image based on Ubuntu and built with Spack. It contains Qwt, CGNS, VTK, Open Cascade...
- `cmake-cgcore`: LIHPC-CG core image based on Ubuntu and built with Cmake. It contains Qwt, Mesquite, CGNS, VTK and Open Cascade.

These images are built when `spack-cgcore`/`cmake-cgcore` branches are tagged. The tag defines the version number of the image. It must be prefixed with `spack-cgcore`/`cmake-cgcore` to prevent conflicts with main branch tags.

Two images based on above core images:
- `spack-cgcore-magix3d`: magix3d image based on `spack-cgcore` and built with Spack. It contains magix3d release and all its dependencies.
- `cmake-cgcore-magix3d`: magix3d image based on `cmake-cgcore` and built with Cmake. It contains magix3d release and all its dependencies.

These images are built when the `main` branch is tagged. The tag defines the version number of the image. These images are used to provide both a development environment for all magix3d ecosystem projects and an executable magix3d product.

**Handmade images**

The others images, like `spack-magix3d`, can be created thanks to the `create-docker-image` workflow available [in the actions tab](https://github.com/LIHPC-Computational-Geometry/spack_recipes/actions/workflows/create-docker-image.yml): click on "Run workflow" button on the right and select the desired image.

## Build a mirror for sites that do not have an internet connection

To build a mirror for sites that do not have an internet connection, download [this script](./dockerfiles/mirror.sh) and type the following command :

```bash
mirror.sh mirror-releases x.y.z # x.y.z is a release number of spack_recipes repository
```

It will clone all repositories needed by magix3d and will prepare Spack mirrors and recipes in a *well-defined* directory structure.

If you just need to compile magix3d (no mirroring of github repositories), you can also use [Spack mirroring feature](./docs/spack-mirroring.md).



