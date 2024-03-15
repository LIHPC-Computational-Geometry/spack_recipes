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
    url = 'https://github.com/LIHPC-Computational-Geometry/qtpython/archive/refs/tags/0.0.0.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/qtpython.git'
    maintainers = ['meshing_team']

    depends_on('guitoolkitsvariables', type=('build'))
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

    version('6.4.1', sha256='439274455fe500d1f1bca2cef53433d2f4428ad96a57b060c4345872c04f9c64')
    version('6.4.0', sha256='0ec68d7699450ef924cd1ab4c333cd1045451aa698a09184af56cc2f3db89c04')
    version('6.3.3', sha256='060eb5832f39e1bd4c78e1abab7fad7dbcff2b098c9ac0764b6015bf46209d5b')
    version('6.3.2', sha256='9abf42ee139fa392179e4b969b7bcf70cde9436ac7b02f3fb07e4e0077b17624')
    version('6.3.1', sha256='9191f353d63008f84aeebf9267202ad45ce7a6a04ee05b55bb076916c99de287')
    version('6.3.0', sha256='c6ccdb952ed6b9dfb393579eb82748e3c3c213da4ff8c254ec8e9eaea18ae338')
    version('5.1.10', sha256='ef9258f94a10c4124ad08ddac1824dfd616fc13e81bf3dabe8e8022578ed84fb')
    version('5.1.1', sha256='c6fe52a87cf38d28ed711dc47cd31ca3411cf5db962fe09531758340e7045844')
    version('5.0.3', sha256='2602f10437cdd1293caffbefefcdf104c146456d81f61b13ea0356533c63a2e0')
    version('5.0.2', sha256='587a91778f6797f056da3f54272e362b155ab427f63a7efd36db9fb739591881')
    version('4.1.0', sha256='870101ed2ef4e3424e3e9e03e83676186785dcd4e88e1ab6618f2bcbc9766112')
    version('4.0.2', sha256='f0b0749e26df7a01f70a30facbfeaad4eb410d1d9db6a78d731c1c35d2a97571')

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant('BUILD_SHARED_LIBS', 'shared'))

        args.append(self.define('USE_PYTHON_3', int(self.spec['python'].version[0]) >= 3))
        args.append(self.define('USE_PYTHON_2', int(self.spec['python'].version[0]) < 3))

        args.append('-DBUILD_PY_CONSOLE:BOOL=ON')

        # Fix cmake taking python3 even if `which python` is python2
        py = self.spec['python']
        args.extend([
           # find_package(PythonInterp) # Deprecated, but used by pybind11
           self.define('PYTHON_EXECUTABLE', py.command.path),
           # find_package(Python) under cmake_minimum_required < 3.15 (CMP0094)
           self.define('Python_EXECUTABLE', py.command.path),
           # find_package(Python2/3) under cmake_minimum_required < 3.15 (CMP0094)
           self.define('Python{}_EXECUTABLE'.format(py.version[0]), py.command.path),
        ])

        return args
