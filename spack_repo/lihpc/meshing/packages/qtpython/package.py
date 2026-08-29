# -*- coding: utf-8 -*-
##############################################################################
# Project QtPython
#
# CEA/DAM/DSSI, 2020
##############################################################################

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Qtpython(CMakePackage):
    """Bibliotheque d'utilitaires Qt/Python pour executer des scripts dans une console."""

    homepage = "https://github.com/LIHPC-Computational-Geometry/qtpython"
    url = "https://github.com/LIHPC-Computational-Geometry/qtpython/archive/refs/tags/0.0.0.tar.gz"
    git = "https://github.com/LIHPC-Computational-Geometry/qtpython.git"
    maintainers = ["meshing_team"]

    depends_on("guitoolkitsvariables", type=("build", "link"))
    depends_on("qtutil@5: +shared", type=("build", "link"), when="+shared")
    depends_on("qtutil@5: ~shared", type=("build", "link"), when="~shared")
    depends_on("pythonutil@5: +shared", type=("build", "link"), when="+shared")
    depends_on("pythonutil@5: ~shared", type=("build", "link"), when="~shared")
    depends_on("qt")

    depends_on("python", type=("build", "link"))
    depends_on("swig@3:", type="build")

    variant("shared", default=True, description="Creation de bibliotheques dynamiques")

    version("6.4.7", sha256="7ff52e3bf8f8b83636d76b6a9a1a9b5a296e5110081511703b5ef2bb99749db8")
    version("6.4.6", sha256="9f5acd88f4dbcc47fa1929a26466ab3aea0554ba87bfcd562bef701fefe7a1f5")
    version("6.4.5", sha256="0a787b2b3ffc8c9a02cf134dd408b135d71b72ccaa2bef725aeb86440af4f0d8")
    version("6.4.4", sha256="d70158ab0605623deeef24ca71e9ddbce1478afcf000b2ee5aa2fa922e3a59c2")
    version("6.4.3", sha256="dcfee932c873f8d35b86e19bff95fca2aada7a2a631da2393546a9ed010fa5b4")
    version("6.4.2", sha256="1a1967412fa11dcbac9e5eeb7361c1b5e013beb97dfa3c0717dee8e211206299")
    version("6.4.1", sha256="439274455fe500d1f1bca2cef53433d2f4428ad96a57b060c4345872c04f9c64")
    version("6.4.0", sha256="0ec68d7699450ef924cd1ab4c333cd1045451aa698a09184af56cc2f3db89c04")
    version("6.3.3", sha256="060eb5832f39e1bd4c78e1abab7fad7dbcff2b098c9ac0764b6015bf46209d5b")
    version("6.3.2", sha256="9abf42ee139fa392179e4b969b7bcf70cde9436ac7b02f3fb07e4e0077b17624")
    version("6.3.1", sha256="9191f353d63008f84aeebf9267202ad45ce7a6a04ee05b55bb076916c99de287")
    version("6.3.0", sha256="c6ccdb952ed6b9dfb393579eb82748e3c3c213da4ff8c254ec8e9eaea18ae338")
    version("5.1.10", sha256="ef9258f94a10c4124ad08ddac1824dfd616fc13e81bf3dabe8e8022578ed84fb")

    depends_on("cxx", type="build")  # generated

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant("BUILD_SHARED_LIBS", "shared"))

        args.append("-DBUILD_PY_CONSOLE:BOOL=ON")

        # Fix cmake taking python3 even if `which python` is python2
        py = self.spec["python"]
        args.extend(
            [
                # find_package(PythonInterp) # Deprecated, but used by pybind11
                self.define("PYTHON_EXECUTABLE", py.command.path),
                # find_package(Python) under cmake_minimum_required < 3.15 (CMP0094)
                self.define("Python_EXECUTABLE", py.command.path),
                # find_package(Python2/3) under cmake_minimum_required < 3.15 (CMP0094)
                self.define("Python{}_EXECUTABLE".format(py.version[0]), py.command.path),
            ]
        )

        return args
