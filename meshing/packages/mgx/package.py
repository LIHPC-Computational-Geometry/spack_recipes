# -*- coding: utf-8 -*-
##############################################################################
# Project Magix3D
#
# CEA/DAM/DSSI, 2020
##############################################################################

from spack import *


class Mgx(CMakePackage):
    """Mailleur 3D"""

    homepage = 'https://github.com/LIHPC-Computational-Geometry/mgx'
    url = 'https://github.com/LIHPC-Computational-Geometry/mgx/archive/refs/tags/1.0.0.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/mgx.git'
    maintainers = ['meshing_team']
    
    variant('dkoc', default=False, description='Utilisation du lecteur Catia DKOC pour OpenCascade')
    variant('mdlparser', default=False, description='Utilisation du lecteur du format mdl')
    variant('meshgems', default=False, description='Utilisation de la bibliotheque de maillage volumique MeshGems')
    variant('sepa3d', default=False, description='Utilisation du celebre outil de separatrices 3D')
    # 2023/06/02 - BL: Waiting for a GitHub smooth3d version, True ==> False
    variant('smooth3d', default=False, description='Utilisation de la bibliotheque de lissage volumique Smooth3D')
    variant('triton2', default=True, description='Utilisation du mailleur tetraedrique Tetgen')

    version('1.0.0', sha256='1c52c5d0760adc69c392c70c7d88b5824aa9dfaf9d7b68f7bffbb80cd147f81e')
    
    depends_on('tkutil')
    depends_on('vtkcontrib@4: +shared', type=('build', 'link'))
    depends_on('preferences@5: +shared', type=('build', 'link'))
    depends_on('pythonutil@5: +shared', type=('build', 'link'))
    depends_on('qqualif@3: +shared', type=('build', 'link'))
    depends_on('qtpython@4: +shared', type=('build', 'link'))
    depends_on('qtvtk@7: +shared', type=('build', 'link'))
    depends_on('cgns', type=('build', 'link'))
    depends_on('gmds@0.7.2:', type=('build', 'link'))
    depends_on('gmdscea@2: +shared', type=('build', 'link'))
    depends_on('gts', type=('build', 'link'))
    depends_on('glib', type=('build', 'link'))
    depends_on('pcre', type=('build', 'link'))
#    depends_on('mdl-parser@1.5.2: +shared', type=('build', 'link'))
#    depends_on('opencascade@7.1.0+foundationclasses+dataexchange+visualization', type=('build', 'link'))
    depends_on('opencascade@7.1.0+foundationclasses+dataexchange', type=('build', 'link'))
   # depends_on('dkoc', type=('build', 'link'), when='+dkoc')
   # depends_on('meshgems', type=('build', 'link'), when='+meshgems')
   # depends_on('separatrice3d +shared', type=('build', 'link'), when='+sepa3d')
    depends_on('smooth3d +shared', type=('build', 'link'), when='+smooth3d')
    depends_on('swig', type='build')
    depends_on('triton2 +shared', type=('build', 'link'), when='+triton2')
    depends_on('mesquite')
    depends_on('python')
    depends_on('qt')
    depends_on('doxygen')
    depends_on('lima')
  #  depends_on('experimentalroom')
    depends_on('pkgconfig', type=('build'))
 
    def cmake_args(self):
        args=  [      
            self.define_from_variant('USE_DKOC', 'dkoc'),
            self.define_from_variant('USE_MDLPARSER', 'mdlparser'),
            self.define_from_variant('USE_MESHGEMS', 'meshgems'),
            self.define_from_variant('USE_SEPA3D', 'sepa3d'),
            self.define_from_variant('USE_SMOOTH3D', 'smooth3d'),
            self.define_from_variant('USE_TRITON', 'triton2'),
            self.define('BUILD_SHARED_LIBS', True),
            self.define('PRODUCTION', True),
            self.define('BUILD_MAGIX3D', True),
            self.define('BUILD_MAGIX3DBATCH', True),
            self.define('T_INTERNAL_EXTENSION', 'not_defined'),
            self.define('ERD_INTERNAL_EXTENSION', 'not_defined'),
            self.define('USER_TEAM', 'undef_user_team'),
            self.define('DOXYGEN_PATH', 'not_defined'),
            self.define('DKOC_LICENCE', 'unavailable')
        ]


        if self.spec.satisfies('%intel'):
            args.append('-DCMAKE_CXX_FLAGS="-std=c++11"')


        if self.spec['python'].version < Version('3'):
            args.append('-DUSE_PYTHON_3:BOOL=OFF')
        else: 
            args.append('-DUSE_PYTHON_3:BOOL=ON')

        if self.spec['vtk-maillage'].version < Version('8'):
            args.append('-DVTK_7:BOOL=ON')
        elif self.spec['vtk-maillage'].version < Version('9'):
            args.append('-DVTK_8:BOOL=ON')
        else:
            args.append('-DVTK_9:BOOL=ON')

        return args
