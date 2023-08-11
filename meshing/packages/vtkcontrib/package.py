# -*- coding: utf-8 -*-
##############################################################################
# Project VtkContrib
#
# CEA/DAM/DSSI, 2020
##############################################################################

from spack import *


class Vtkcontrib(CMakePackage):
    """Bibliotheque d'utilitaires VTK"""

    homepage = 'https://github.com/LIHPC-Computational-Geometry/vtkcontrib'
    url = 'https://github.com/LIHPC-Computational-Geometry/vtkcontrib/archive/refs/tags/5.4.1.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/vtkcontrib.git' 
    maintainers = ['meshing_team']

# Rem : peu de variants pour VTK au regard de ce qui pourrait etre fait : opengl2, python, xdmf, qt, mpi, ffmpeg
# On veut dans cette version un VTK 7.*
#    depends_on('vtk@7.1:7.99~opengl2~python~xdmf+qt', type=('build', 'link'))
#    depends_on('qt@5.9.1', type=('build', 'link'))
    depends_on('guitoolkitsvariables', type=('build', 'link'))
    depends_on('vtk-maillage', type=('build', 'link'))
 #   depends_on('mpi', type=('build', 'link'))

# for undefined reference in util-linux/libmount to intl_....
#    depends_on('gettext')

    patch('vtkcontrib-4.6.0_calc_mpi.patch', when='@4.6.0')

    version('5.4.1', sha256='de31db5778628eb8b01a67517379b2abe524944a038a348c00d65b1935ad0081')
    version('5.4.0', sha256='c3c7d6b9491cbb273084ef1f5795e88599d23a041b568b61d1da426277cefcea')
    version('4.6.4', sha256='1fce68d5c9342f90ff54aae75248679d52e303cf1954cdcf2ed0bf9bc6157a4c')
    version('4.6.1', sha256='8d32ff953f61addd0a40fa6a92c2ba8fe11f7431cc01608f45b8f7f681a7de76')
    version('4.6.0', sha256='269220824875c4945bdbdd78589d460b5a5ca806d78166c38079bb228e933e11')
    version('4.0.1', sha256='ea186d906ed63c9be0328067d08889dfe72b4fc1710831fc8234496f048003af')
    version('4.0.0', sha256='3ddcb0b3f5c06c93a8fc3ea9b7cb03e93d3f5ed4ec0d2ea2a48eab7c68529305')

    variant('shared', default=True, description='Creation de bibliotheques dynamiques (defaut:shared, annuler le defaut par ~shared)')

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant('BUILD_SHARED_LIBS', 'shared'))

        if self.spec['vtk-maillage'].version < Version('8'):
            args.append('-DVTK_7:BOOL=ON')
        elif self.spec['vtk-maillage'].version < Version('9'):
            args.append('-DVTK_8:BOOL=ON')
        else:
            args.append('-DVTK_9:BOOL=ON')

        # if OFF does vtkcontrib uses OPENGL2 ?
        # see VTK_OPENGL_BACKEND in src/VtkContrib/CMakeLists.txt
        args.append('-DUSE_OPENGL_BACKEND:BOOL=ON')

        return args
