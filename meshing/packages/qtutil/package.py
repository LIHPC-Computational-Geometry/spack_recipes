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
    url = 'https://github.com/LIHPC-Computational-Geometry/qtutil/archive/refs/tags/0.0.0.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/qtutil.git'
    maintainers = ['meshing_team']

    depends_on('guitoolkitsvariables', type=('build'))
    depends_on('tkutil@5: +shared', type=('build', 'link'), when='+shared')
    depends_on('tkutil@5: ~shared', type=('build', 'link'), when='~shared')
    depends_on('qt@5.9:', type=('build', 'link'))

    version('6.6.0', sha256='84f639df33b1b2f697c0af6cd226adba3d36c211fee7d490b759b7fa6eb4a8c8')
    version('6.5.0', sha256='113808d85915957e34777ab7a207830b5916d0db19c3f009a035ccc43940a27b')
    version('6.4.2', sha256='e11596c5ccfbca313d628bbdadba0c59c5c8a24164f39525078e163012fa870f')
    version('6.4.1', sha256='65a46bbd7818bf04f0addef12e9a35bdef118161cf46c75d0bbea929bed90373')
    version('6.4.0', sha256='568f09a12c92810e27457ae1c589a0a9e89d3dd605194e5e1a429a0a3e18c96b')
    version('6.3.0', sha256='183642b97f60053b3643a097124a8e4cad04447f5934f21d66715d9f17cdfa86')
    version('6.2.1', sha256='0e8f0a75dca6574d4f348c4c2db3b5689a21cea94e6345a146235053ad4bbc4c')
    version('6.2.0', sha256='74a85acee94a676060197ac49179d82a9544f2baba871d4b2c1b1633317886bb')
    version('5.7.8', sha256='7073195a2cbfdae00840412d54ef7d8b8d60a6b28d9520a34e9b34fd3779bc5d')
    version('5.7.0', sha256='a62fd6e85a8e45f42c3382edeb9a094e873cc479abf6f70efd3df0fb8188cc02')
    version('5.1.0', sha256='b3f1825ed7a4fb2039d47fad235ac819d61adc8faf4f1a70d8a3ed226bceb625')
    version('5.0.3', sha256='0368caf97f15683799423eb05f605884d187f3ad7e675855073840d49cccd269')
    version('5.0.2', sha256='9ca1d5fd687d90398ca45ca3e1a07f9d7c0b591943d231e8c088e026cb4d7cc2')
    version('5.0.0', sha256='c15f4c25a3db68ed90dc7ded6b53085a3f66181972936cdc247818b17f94dc21')

    variant('shared', default=True, description='Création de bibliothèques dynamiques')

# to avoid QtWebEngine or QtWebkit
    variant('qtbrowser', default=True, description='Use Qt base browser')

    def cmake_args(self):
        args = []
        args += [self.define_from_variant('BUILD_SHARED_LIBS', 'shared')]
        args += [self.define_from_variant('USE_QT_TEXT_BROWSER', 'qtbrowser')]

        return args
