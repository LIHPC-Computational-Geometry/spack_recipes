# -*- coding: utf-8 -*-
##############################################################################
# Project QtPython
#
# CEA/DAM/DSSI, 2020
##############################################################################

from spack import *


class Qtpython(CMakePackage):
    """Bibliotheque d'utilitaires Qt/Python permettant d'executer des scripts dans une console avec mode pas a pas."""

    homepage = 'https://github.com/LIHPC-Computational-Geometry/qtpython'
    url = 'https://github.com/LIHPC-Computational-Geometry/qtpython/archive/refs/tags/v5.1.10.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/qtpython.git'
    maintainers = ['meshing_team']

    depends_on('qtutil@5: +shared', type=('build', 'link'), when='+shared')
    depends_on('qtutil@5: ~shared', type=('build', 'link'), when='~shared')
    depends_on('pythonutil@5: +shared', type=('build', 'link'), when='+shared')
    depends_on('pythonutil@5: ~shared', type=('build', 'link'), when='~shared')
    depends_on('qt')

# 5.0.2 is the last python2 only version
    depends_on('python@:2.999', type=('build', 'link'), when='@:5.0.2')
    depends_on('python', type=('build', 'link'), when='@5.0.3:')
#    depends_on('python@:2.999', type=('build', 'link'))	# ==================== A REVOIR
# On a besoin de swig >= 3.0.0 :
    depends_on('swig@3:', type='build')

    variant('shared', default=True, description='Creation de bibliotheques dynamiques (defaut:shared, annuler le defaut par ~shared)')

    version('5.1.10')
    version('5.1.1')# sha256='c6fe52a87cf38d28ed711dc47cd31ca3411cf5db962fe09531758340e7045844')
    version('5.0.3', sha256='2602f10437cdd1293caffbefefcdf104c146456d81f61b13ea0356533c63a2e0')
    version('5.0.2', sha256='587a91778f6797f056da3f54272e362b155ab427f63a7efd36db9fb739591881')
    version('4.1.0', sha256='870101ed2ef4e3424e3e9e03e83676186785dcd4e88e1ab6618f2bcbc9766112')
    version('4.0.2', sha256='f0b0749e26df7a01f70a30facbfeaad4eb410d1d9db6a78d731c1c35d2a97571')

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant('BUILD_SHARED_LIBS', 'shared'))

        if self.spec['python'].version < Version('3'):
            args.append('-DUSE_PYTHON_3:BOOL=OFF')
        else:
            args.append('-DUSE_PYTHON_3:BOOL=ON')

        args.append('-DBUILD_PY_CONSOLE:BOOL=ON')

        return args
