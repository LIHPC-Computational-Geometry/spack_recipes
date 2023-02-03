# -*- coding: utf-8 -*-
##############################################################################
# Project QtVTK
#
# CEA/DAM/DSSI, 2020
##############################################################################

from spack import *


class Qtvtk(CMakePackage):
    """Bibliotheque d'utilitaires Qt/VTK et permettant le parametrage d'experiences lasers ou conteneurs"""

    homepage = 'https://github.com/LIHPC-Computational-Geometry/qtvtk'
    url = 'https://github.com/LIHPC-Computational-Geometry/qtvtk/archive/refs/tags/v7.14.8.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/qtvtk.git'
    maintainers = ['meshing_team']

    maintainers = ['meshing_team']

    depends_on('qtutil@5: +shared', type=('build', 'link'), when='+shared')
    depends_on('qtutil@5: ~shared', type=('build', 'link'), when='~shared')
    depends_on('vtkcontrib@4: +shared', type=('build', 'link'), when='+shared')
    depends_on('vtkcontrib@4: ~shared', type=('build', 'link'), when='~shared')
    depends_on('xerces-c@3.1.4', type=('build', 'link'))
    depends_on('preferences', type=('build', 'link'))
    depends_on('qt')

    variant('shared', default=True, description='Creation de bibliotheques dynamiques (defaut:shared, annuler le defaut par ~shared)')

    version('7.14.8')
    version('7.14.0')#, sha256='ff72228ae9762551e8c7be0def0a5e3289cb8c29427870beb34a375e02fec396')
    version('7.13.1', sha256='09c7d5b25ea6254650e994a0bfe97f96a3cd0c7e90df74f536d8b2e5b2f9e5d8')
    version('7.13.0', sha256='413b9776a81c51a9b3912d9de95ab04b4e3324a3e371f4759e690948bc9b8227')
    version('7.1.0', sha256='d70a3511cac971c0f18cbb322d32e1ef7dfae41816d1c189a7167289e89091d3')
    version('7.0.1', sha256='c5342f195c9f79fed62c572f405fdf67d009b89ce12e80e6fad80674dab92c06')
    version('7.0.0', sha256='75abca1906b3c6a535515a29be8fddbe1e1ff39c1bb609fe423d5bd309b8d61b')

    def cmake_args(self):
        args = []
        # Sous spack on est en mode "production", ce qui conditionne le repertoire ou est l'aide :
        args.append('-DPRODUCTION=ON')
        args.append(self.define_from_variant('BUILD_SHARED_LIBS', 'shared'))

        if self.spec['vtk-maillage'].version < Version('8'):
            args.append('-DVTK_7:BOOL=ON')
        else:
            args.append('-DVTK_8:BOOL=ON')

        return args
