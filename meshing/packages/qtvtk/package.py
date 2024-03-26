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

    depends_on('guitoolkitsvariables@:1.4.3', type=('build'))
    depends_on('qtutil@5: +shared', type=('build', 'link'), when='+shared')
    depends_on('qtutil@5: ~shared', type=('build', 'link'), when='~shared')
    depends_on('vtkcontrib@5.4.0: +shared', type=('build', 'link'), when='+shared')
    depends_on('vtkcontrib@5.4.0: ~shared', type=('build', 'link'), when='~shared')
    depends_on('vtkcontrib@5.4.0: +vtk7', type=('build', 'link'), when='+vtk7')
    depends_on('vtkcontrib@5.4.0: ~vtk7', type=('build', 'link'), when='~vtk7')
    depends_on('xerces-c@3.1.4', type=('build', 'link'))
    depends_on('preferences', type=('build', 'link'))
    depends_on('qt')
    # On écarte ici la possibilité de VTK v 8 qui ne présente pas d'intérêt particulier :
    depends_on('vtk-maillage@=7.1.1 +qt', type=('build', 'link'), when='+vtk7')
    depends_on('vtk@8.99: +qt', type=('build', 'link'), when='~vtk7')

    variant('shared', default=True, description='Creation de bibliotheques dynamiques (defaut:shared, annuler le defaut par ~shared)')
    variant('vtk7', default=True, description='Utilisation de VTK 7/backend open GL compatible GLX')
    
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
        args = []
        # Sous spack on est en mode "production", ce qui conditionne le repertoire ou est l'aide :
        args.append('-DPRODUCTION=ON')
        args.append(self.define_from_variant('BUILD_SHARED_LIBS', 'shared'))

        return args
