# -*- coding: utf-8 -*-
##############################################################################
# Project Qualif
#
# REPLACE_NAME_SERVICE_LABO, 2020
##############################################################################

from spack import *


class Qualif(CMakePackage):
    """Bibliotheque/utilitaire de mesure de qualite de maillage"""

    homepage = 'https://github.com/LIHPC-Computational-Geometry/qualif'
    url = 'https://github.com/LIHPC-Computational-Geometry/qualif/archive/refs/tags/v2.3.5.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/qualif.git'

    depends_on('cmake', type='build')
# On a besoin de 7.2 <= Lima :
    depends_on('lima', type=('build', 'link'))
    version('2.3.5', sha256='84529d811c74454b695f4432e1c8a1af6af4ab422c3dd8f4e2d8e6e5aa7f8c31')
    version('2.3.4')
    version('2.3.2', sha256='c5049581fb01c240b6ea0662129d8a2ee9002901090e5be8805ed738ea1e34a7')
    version('2.3.1', sha256='b2a4f936539db69de061e5552bea780b098eca8221b40204a0888b9f9a3f7718')
    version('2.1.0', sha256='8ab87dd38752ecab4b4af73c8405d57b0daf5301a63e59f088649039ac4eb525')
    version('2.0.2', sha256='3ffcf3dee735a5d631f6e0f16422df9c22910156d0cbd82aa99b7733c89a7c41')
    version('2.0.1', sha256='28f01315224e4174c6ba44717afdfc3799560ec14488493f7d738122179092be')
    version('2.0.0', sha256='470cb7d25d34f2b19458c6a43e9ca5e3e2def7f3f4f0efdf0dbef5bbfe8dc9cc')

    variant('shared', default=True, description='Creation de bibliotheques dynamiques (defaut:shared, annuler le defaut par ~shared)')

    def cmake_args(self):
        args = []
        if '~shared' in self.spec:
            args.append('-DBUILD_SHARED_LIBS:BOOL=OFF')

        return args
