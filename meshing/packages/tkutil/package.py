# -*- coding: utf-8 -*-
##############################################################################
# Project TkUtil
#
# CEA/DAM/DSSI, 2020
##############################################################################

from spack import *


class Tkutil(CMakePackage):
    """Bibliothèque d'utilitaires C++"""

    homepage = 'https://github.com/LIHPC-Computational-Geometry/tkutil'
    url = 'https://github.com/LIHPC-Computational-Geometry/tkutil/archive/refs/tags/0.0.0.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/tkutil.git'
    maintainers = ['meshing_team']

    extends("python")		# For the PYTHONPATH in the generated modules

    depends_on('guitoolkitsvariables', type=('build', 'link'))
    # 5.7.6 is the last python2 only version
    depends_on('python@:2.999', type=('build', 'link'), when='@:5.7.6')
    depends_on('python', type=('build', 'link'), when='@5.7.7:')
    # On a besoin de swig >= 3.0.0 :
    depends_on('swig@3:', type=('build'))
    depends_on('libiconv', type=('build', 'link'))

    version('main', branch='main')
    version('6.13.1', sha256='8c548d1bb57c8d84c42ec4f8643edd323a2cbd22a9180cd0822c10bcf49ca2c5')
    version('6.13.0', sha256='c6df0badfaaa6b77cacdcd85aef79a628980a7367dc90c88df9959859d12af15')
    version('6.12.1', sha256='8d53dca70dda7d8e28effde8d4dbd67eb215c27c3935db7cc75b09231cda469d')
    version('6.12.0', sha256='459281ff909ce856a3641a8ea331a8d8801321ac5d20a2b3067ecb4a3afecbde')
    version('6.11.0', sha256='51b6934c847e3728183abd3260829b5b0fb31f75d4f6e43422e271c2c09ea3b8')
    version('6.10.3', sha256='d13279c80cc77902daecc5175429da703a85085a6a60fb839ccc3a428a10bed0')
    version('6.10.2', sha256='d4ef63fa7e7357fc8bdaecab4d69c9a3c36ba479e5aa842628bf8b32e0edbcbf')
    version('6.10.1', sha256='4f841f062b93465248c9a5e651080d40c621047422a04458dd87f81f1d5ad094')
    version('6.10.0', sha256='a1521faa5123c569b93ece8874127996976f8ef44eb8d3f57280afb3a80e385d')
    version('6.9.0', sha256='1fd2d1d525dac45277a8e9370252251f746946cd9b7b2b6440241e0f13aa27a0')
    version('6.8.0', sha256='f9c1326f2725fec482db691ceda00882eba31c4db326bdddaf0f510a8b857afb')
    version('6.7.0', sha256='5d610804c9061b09bad2cf799839a24a4de87667680943cc2bd8958f92bcf703')
    version('6.6.1', sha256='1f65b2628992d455cdd0fb9b1e3e791432a3051ac2b138d4a7ef73dabc9e5d76')
    version('6.6.0', sha256='9ae89bf5da6ed5af88e11325862df528c16166df49419b518c1c51a80019d0b8')
    version('6.5.1', sha256='877ca71cc84cb4d948db8f5ecf65bae775cd33d83b2208c2d8260313238cc285')
    version('6.5.0', sha256='a1f1dc27fd0f5bcb8ddeee3f9d895c793f97e21d1cf395d1f607e29a47d0363e')
    version('5.14.0', sha256='e9fdc04f5a8efa4a95648a80422cfaccbb6733b79af2d49fe1af3ace4c748cb3')
    # versions below are deprecated as sources are in the infinite void of space
    version('5.7.7', sha256='a9ed789f4088ba2bb3f1807d6317f74904fd10911b92cdb50f5c0e7f7ae61dea', deprecated=True)
    version('5.7.5', sha256='335300ae3b441b45327d9b0fa4591c096509381b4c355d61fb407cb2eeea62fd', deprecated=True)
    version('5.7.2', sha256='36406ad50fb73b07216f19ef34958abcf17171cc32a1d0fb44a7176aa97c03f3', deprecated=True)
    version('5.1.0', sha256='949b97c14fcdddfc524978b472aa5129fe140049ada2b1e94717158c1a22b700', deprecated=True)
    version('5.0.3', sha256='1fe8250cfd83c640266c54cc15687927f702cebd7d5e0a8396ea318e171f6b9a', deprecated=True)
    version('5.0.2', sha256='7ca880377d069af81160458131c4c9c3d57bb24a7c1077f57d681abb02871669', deprecated=True)
    version('5.0.0', sha256='9e049bbdf61ce49ff6e8bf246b94bc61a76896146f48b7aa5d5305346c6f9d50', deprecated=True)

    depends_on("cxx", type="build")  # generated

    variant('shared', default=True, description='Creation de bibliotheques dynamiques')

    def cmake_args(self):
        args = []
        args = [self.define_from_variant('BUILD_SHARED_LIBS', 'shared')]
        args.append('-DCMAKE_CXX_FLAGS="-std=c++17"')

        args.append(self.define('USE_PYTHON_3', int(self.spec['python'].version[0]) >= 3))
        args.append(self.define('USE_PYTHON_2', int(self.spec['python'].version[0]) < 3))

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
