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
    url = 'https://github.com/LIHPC-Computational-Geometry/qtvtk/archive/refs/tags/0.0.0.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/qtvtk.git'
    maintainers = ['meshing_team']

    depends_on('guitoolkitsvariables', type=('build'))
    depends_on('qtutil@5: +shared', type=('build', 'link'), when='+shared')
    depends_on('qtutil@5: ~shared', type=('build', 'link'), when='~shared')
    depends_on('vtkcontrib@4: +shared', type=('build', 'link'), when='+shared')
    depends_on('vtkcontrib@4: ~shared', type=('build', 'link'), when='~shared')
    depends_on('preferences', type=('build', 'link'))
    depends_on('qt')
    depends_on('vtk-maillage +qt', type=('build', 'link'))

    variant('shared', default=True, description='Creation de bibliotheques dynamiques (defaut:shared, annuler le defaut par ~shared)')

    version('8.8.2', sha256='be755be155304572c7c2eae81a67c5ecbcd3dcd3aa6372d7f4afeb7ffaad6356')
    version('8.8.1', sha256='bdbc864a487a1aede2a538e94db4182b787412bcdc75ef9f3fd602a35e7e58fa')
    version('8.8.0', sha256='fd80c02a12628aba7a214dd23589028f2d8a1e4088a9140c661ee0d63b63dee7')
    version('8.7.0', sha256='929bef89cf5a04c9214500667f741eba66c5885a2aeaedd7d05fc0f935146ad1')
    version('8.6.0', sha256='95968e9fb03e6fe229efbbc70056a4e3184d4bb6879abdbeb7e84fc17695d869')
    version('8.5.1', sha256='6a9ee744bde29ecdd157c23aff6036e614b03907dc05a6a3098fa1465e7360bc')
    version('8.5.0', sha256='134ecd42a13e2409f3cbc9a634ec8d1ab0ed763cdb9c6c05a4ca72586af8b0b7')
    version('8.4.1', sha256='8b5b0f74a27fd0664b4c94229d8488fb62fa34b2fd7a7367085215a2f850f786')
    version('8.4.0', sha256='851bcf977d03f514dec6e1c220f3585e80ad043c4b11ef45805a5916b1c16d64')
    version('7.14.8', sha256='2d9cb54c14afc38e849a25fe8fe534481402f64352c690454671e0e61a9fe0c4')
    version('7.14.0', sha256='ff72228ae9762551e8c7be0def0a5e3289cb8c29427870beb34a375e02fec396')
    version('7.13.1', sha256='09c7d5b25ea6254650e994a0bfe97f96a3cd0c7e90df74f536d8b2e5b2f9e5d8')
    version('7.13.0', sha256='413b9776a81c51a9b3912d9de95ab04b4e3324a3e371f4759e690948bc9b8227')
    version('7.1.0', sha256='d70a3511cac971c0f18cbb322d32e1ef7dfae41816d1c189a7167289e89091d3')
    version('7.0.1', sha256='c5342f195c9f79fed62c572f405fdf67d009b89ce12e80e6fad80674dab92c06')
    version('7.0.0', sha256='75abca1906b3c6a535515a29be8fddbe1e1ff39c1bb609fe423d5bd309b8d61b')

    def cmake_args(self):
        # Since version 5.4.0 VtkContrib uses common_vtk.cmake of GUIToolkitsVariables which
        # sets VTK 7, VTK 8 or VTK 9 to ON.
        args = []
        # Sous spack on est en mode "production", ce qui conditionne le repertoire ou est l'aide :
        args.append('-DPRODUCTION=ON')
        args.append(self.define_from_variant('BUILD_SHARED_LIBS', 'shared'))

        return args
