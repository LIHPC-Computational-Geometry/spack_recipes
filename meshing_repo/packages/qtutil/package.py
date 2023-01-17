# -*- coding: utf-8 -*-
##############################################################################
# Project QtUtil
#
# REPLACE_NAME_SERVICE_LABO, 2020
##############################################################################

from spack import *


class Qtutil(CMakePackage):
    """Bibliotheque d'utilitaires Qt"""

    homepage = 'https://github.com/LIHPC-Computational-Geometry/qtutil'
    url = 'https://github.com/LIHPC-Computational-Geometry/qtutil/archive/refs/tags/v5.7.8.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/qtutil.git'
    maintainers = ['meshing_team']

# On a besoin de 5.0 <= tkutil :
    depends_on('tkutil@5: +shared', type=('build', 'link'), when='+shared')
    depends_on('tkutil@5: ~shared', type=('build', 'link'), when='~shared')
    depends_on('qt@5.9:', type=('build', 'link'))
    version('5.7.8')
    version('5.7.0')# sha256='a62fd6e85a8e45f42c3382edeb9a094e873cc479abf6f70efd3df0fb8188cc02')
    version('5.1.0', sha256='b3f1825ed7a4fb2039d47fad235ac819d61adc8faf4f1a70d8a3ed226bceb625')
    version('5.0.3', sha256='0368caf97f15683799423eb05f605884d187f3ad7e675855073840d49cccd269')
    version('5.0.2', sha256='9ca1d5fd687d90398ca45ca3e1a07f9d7c0b591943d231e8c088e026cb4d7cc2')
    version('5.0.0', sha256='c15f4c25a3db68ed90dc7ded6b53085a3f66181972936cdc247818b17f94dc21')

    variant('shared', default=True, description='Creation de bibliotheques dynamiques')

# to avoid QtWebEngine or QtWebkit
    variant('qtbrowser', default=True, description='Use Qt base browser')

    def cmake_args(self):
        args = []
        args = [self.define_from_variant('BUILD_SHARED_LIBS', 'shared')]
        args = [self.define_from_variant('USE_QT_TEXT_BROWSER', 'qtbrowser')]

        return args
