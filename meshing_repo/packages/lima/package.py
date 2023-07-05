# -*- coding: utf-8 -*-

##############################################################################
# Project Lima (Logiciel Interface MAillage)
#
# REPLACE_NAME_SERVICE_LABO, 2020
##############################################################################

##############################################################################
# Version 7.4.2
# Tests de non régression (hors spack) OK dans les environnements suivants :
# - CentOS 7 : HDF5 1.10.4, Python 2.7, Swig 3.0, GNU 8.3 ou Intel 19.0.5
# - Atos 7 : HDF5 1.10.4, Python 2.7, Swig 3.0, GNU 4.8 ou Intel 17.0.6
# - Rhel_8 : HDF5 1.10.4, Python 2.7, Swig 3.0, GNU 8.3 ou Intel 20.0.0
# Il est recommandé d'installer également l'utilitaire xlmlima afin de
# vérifier le bon fonctionnement de lima et notamment des lecteurs aux
# différents formats de fichiers de maillage.
##############################################################################

from spack import *


class Lima(CMakePackage):
    """Logiciel Interface MAillage"""

    homepage = 'https://github.com/LIHPC-Computational-Geometry/lima'
    url = 'https://github.com/LIHPC-Computational-Geometry/lima/archive/refs/tags/7.7.9.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/lima.git' 
    maintainers = ['meshing_team']


#    depends_on('sumesh +shared', type=('build', 'link'))
    depends_on('swig', type=('build'), when='+scripting')
    depends_on('python@2.7:3.0 +shared', type=('build', 'link'), when='+scripting')
#    depends_on('hdf145', type=('build', 'link'))
#    depends_on('hdf5 +shared +cxx', type=('build', 'link'))
    depends_on('hdf5 +shared +cxx', type=('build', 'link'))

    variant('scripting', default=False, description='Build python binding')
    variant('shared', default=True, description='Build shared library')
    variant('xlmlima', default=False,
            description='Build xlmlima tool (converts and prepares meshes)')
    variant('i4', default=False, description="int_type=int32 instead of int64")
    variant('r4', default=False, description="real=float instead of double")

    patch('cmake.patch', when='@7.4.3')
    patch('cmake-7.6.0.patch', when='@7.6.0')

    version('main', branch='main')
    version('7.7.9', sha256='483fae8106f97222bb5ed096a2a47e3ccbe9f3506ef7bb0aed1180d7deac00c2')
    version('7.4.2', sha256='7bbcd876f8c6c4330583e281707777f3142d469c248c0b0e0c6dcbda6621e8d0')
    version('7.5.1', sha256='91ef19f6f48d6795a776fea4ceabfc6e19f21f9dbb7dd489191f0ef9ff5c040a')
    version('7.6.0', sha256='6c8c963c487430de1f00bba0cd7fe1a6ec5f2ee07d1b465b74f29d71fb45fe48')
    version('7.6.3', sha256='4039ebbf3f7e047b6cb75393c6a3d4a86be635c03798bb2eb69760c2b760a508')

    conflicts('~shared', '+scripting')
    

    def cmake_args(self):
        args = [self.define_from_variant('BUILD_SHARED_LIBS', 'shared'),
                self.define_from_variant('BUILD_SCRIPTING', 'scripting'),
                self.define_from_variant('BUILD_XLMLIMA', 'xlmlima'),
               ]

        if '+i4' in self.spec:
            args.append(self.define('INT_8', False))
        else:
            args.append(self.define('INT_8', True))

        if '+r4' in self.spec:
            args.append(self.define('REAL_8', False))
        else:
            args.append(self.define('REAL_8', True))

        return args
