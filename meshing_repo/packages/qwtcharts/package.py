# -*- coding: utf-8 -*-
##############################################################################
# Project QwtCharts
#
# REPLACE_NAME_SERVICE_LABO, 2020
##############################################################################

from spack import *


class Qwtcharts(CMakePackage):
    """Bibliotheque d'utilitaires Qwt"""

    homepage = 'https://github.com/LIHPC-Computational-Geometry/qwtcharts'
    url = 'https://github.com/LIHPC-Computational-Geometry/qwtcharts/archive/refs/tags/v4.4.13.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/qwtcharts.git'
    maintainers = ['meshing_team']
 
# On a besoin de 5.0 <= tkutil :
    depends_on('qtutil@5: +shared', type=('build', 'link'), when='+shared')
    depends_on('qtutil@5: ~shared', type=('build', 'link'), when='~shared')
#    depends_on('qt@5.9:', type=('build', 'link'))
    depends_on('qwt@6.1:', type=('build', 'link'))

    version('4.4.13', sha256='e73544b6f94e2a3f989b74827bac5afbbf9c9a8899d991528d6f101f4fbc34d4')
    version('4.4.7', sha256='e22528b70830e6ffa819ef032ab72307f218a65fa925a4c5f78a8510deedbae4')
    version('4.4.6', sha256='7e5e6d072e4ef01fc88d7cd7084a4eb8316ee03970536e0fc08598c07663d89e')
    version('4.1.0', sha256='47ecedb95db452edfde1efd8392e096ad5357517ddef17d09af6082df397ce12')
    version('4.0.3', sha256='03c2b1da97179c1702b75f48343eb4a36b5f8e516ed82cfeb32e4c29b7177e03')
    version('4.0.2', sha256='259164fbf009a275b90bf497362c5db42ad83f562a6747d22310c0eac4761f14')
    version('4.0.0', sha256='490c33b251b03ace8dd192cf775563fe9fd79ade51ebb8f30fcf023fd77ba000')

    variant('shared', default=True, description='Creation de bibliotheques dynamiques')

    def cmake_args(self):
        args = []
        args = [self.define_from_variant('BUILD_SHARED_LIBS', 'shared')]

        return args
