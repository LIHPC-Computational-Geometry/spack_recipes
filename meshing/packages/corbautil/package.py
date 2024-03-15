# -*- coding: utf-8 -*-
##############################################################################
# Project CorbaUtil
#
# REPLACE_NAME_SERVICE_LABO, 2020
##############################################################################

from spack import *


class Corbautil(CMakePackage):
    """Bibliotheque d'utilitaires CORBA"""

    homepage = ''
    url = 'corbautil-6.2.1.tar.gz'
    git = ''
    maintainers = ['meshing_team']

    depends_on('guitoolkitsvariables', type=('build'))
    depends_on('tkutil@6: +shared', type=('build', 'link'), when='+shared')
    depends_on('tkutil@6: ~shared', type=('build', 'link'), when='~shared')
    depends_on('omniorb-anl@3.99:', type=('build', 'link', 'run'))
    version('6.2.1', sha256='41aaf5a3c582ec0fe3467aaf95eb24b72b1336ce31718153877a3bb34c775cc2')

    variant('shared', default=True, description='Creation de bibliotheques dynamiques')

    def cmake_args(self):
        args = []
        args = [self.define_from_variant('BUILD_SHARED_LIBS', 'shared')]

        return args
