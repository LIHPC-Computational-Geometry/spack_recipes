If you need to use magix3d on sites that do not have an internet connection and youcan use [Spack mirrors](https://spack.readthedocs.io/en/latest/mirrors.html).

# Build the mirror

*Step 1*

Open a bash terminal on the [spack-magix3d](https://github.com/LIHPC-Computational-Geometry/lihpccg-ci/pkgs/container/spack-magix3d) image and mount a volume of the container to your local file system, for example `/magix3d-mirror` on the container points to `/tmp/magix3d-mirror` on your local machine.

    podman run -v /tmp/magix3d-mirror:/magix3d-mirror --rm -it ghcr.io/lihpc-computational-geometry/spack-magix3d bash

*Step 2*

Activate the Spack environment used to build the image and create the mirror.

    source /spack/share/spack/setup-env.sh
    spack env activate meshing-env
    spack mirror create -a

*Step 3*

Go to the `/spack/var/spack`, tar the cache directory of the previously created mirror (with h option to follow symlinks) in your local file system through the mounting point, `/magix3d-mirror`in this example.

    cd /spack/var/spack
    tar cvfz /magix3d-mirror/cache.tar.gz cache

Then, you can exit from the container and go the previously mounted directory on your computer, `/tmp/magix3d-mirror`in this example.
Do not forget to download the last release of [spack LIHPC-CG recipes](https://github.com/LIHPC-Computational-Geometry/spack_recipes/releases) in the same directory.

# Use the mirror

On the site with no internet connection, you need to import the `cache.tar.gz` file created above and the last release of spack LIHPC-CG recipes.
Untar the 2 files in a directory and add the mirror and the recipes to Spack. If your site has predefined Spack configurations, you can not add the mirror and the recipes in using `spack mirror add` and `spack repo add` as they will be added at the end of the previously configured mirror and repo lists. Instead you need to directly edit the configuration files. To know the place of the configuration files, use the following commands:

    spack config blame repos    # for recipes
    spack config blame mirrors  # for mirrors

Edit the repos and mirrors configuration files and add the LIHPC-CG repositories and mirror.




