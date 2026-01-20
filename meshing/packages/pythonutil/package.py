# -*- coding: utf-8 -*-
##############################################################################

from spack import *


class Pythonutil(CMakePackage):
    """Utilitaires python-cpp."""

    homepage = 'https://github.com/LIHPC-Computational-Geometry/pythonutil'
    url = 'https://github.com/LIHPC-Computational-Geometry/pythonutil/archive/refs/tags/0.0.0.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/pythonutil.git'
    maintainers = ['meshing_team']

    depends_on('guitoolkitsvariables', type=('build'))
    depends_on('tkutil')
    depends_on('python', type=('build', 'link'))
    # On a besoin de swig >= 3.0.0 :
    depends_on('swig@3:', type='build')

    variant('shared', default=True, description='Creation de bibliotheques dynamiques (defaut:shared, annuler le defaut par ~shared)')

    version('6.2.4', sha256='eeb7cd9740bfc1af6771a0c7b99b8cf51839eca409a01b2f6ba565bb36c89de6')
    version('6.2.3', sha256='dc0e2bb9289e51b9678433cfc50385d5529e9b44f1b784d6ac9857be6d6089bf')
    version('6.2.2', sha256='71d74499b53cbf865cc0d161e59358c5d535be407bde44e7fbca30e9232051b0')
    version('6.2.1', sha256='14425325f2627bb410d9effb022aa0d1f7d7ee490766093668e3552630809acb')
    version('6.2.0', sha256='6c513802336821be8895bc7f46bc580d80a564e2d7ec6c4ee2b1c7d6383a383f')
    version('5.6.6', sha256='6edd64ff6ac22ea3483a551c49e490f77071aebe50d5586ece6f8ff929d6e84f')

    depends_on("cxx", type="build")  # generated

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant('BUILD_SHARED_LIBS', 'shared'))

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
