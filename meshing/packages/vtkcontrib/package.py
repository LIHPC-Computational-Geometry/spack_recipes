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
    url = 'https://github.com/LIHPC-Computational-Geometry/vtkcontrib/archive/refs/tags/0.0.0.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/vtkcontrib.git' 
    maintainers = ['meshing_team']

    depends_on('guitoolkitsvariables@:1.4.3', type=('build'))
    # On écarte ici la possibilité de VTK v 8 qui ne présente pas d'intérêt particulier, et on retient
    # vtk-maillage (VTK 7.1.1, backend OpenGL1 compatible GLX) ou vtk (VTK 9.*, open GL2, version en vigueur).
    depends_on('vtk-maillage@=7.1.1 ~opengl2 +mpi', type=('build', 'link'), when='+vtk7 +mpi')
    depends_on('vtk-maillage@=7.1.1 ~opengl2 ~mpi', type=('build', 'link'), when='+vtk7 ~mpi')
    depends_on('vtk@8.99: +mpi', type=('build', 'link'), when='~vtk7 +mpi')
    depends_on('vtk@8.99: ~mpi', type=('build', 'link'), when='~vtk7 ~mpi')
 #   depends_on('mpi', type=('build', 'link'))

# for undefined reference in util-linux/libmount to intl_....
#    depends_on('gettext')

    version('5.4.2', sha256='5d93d8051f4a1546932f201368bc2d4222ec617c1344dbc9ee1413beb7e24ec2')
    version('5.4.1', sha256='de31db5778628eb8b01a67517379b2abe524944a038a348c00d65b1935ad0081')
    version('5.4.0', sha256='c3c7d6b9491cbb273084ef1f5795e88599d23a041b568b61d1da426277cefcea')

    variant('shared', default=True, description='Creation de bibliotheques dynamiques (defaut:shared, annuler le defaut par ~shared)')
    variant('vtk7', default=True, description='Utilisation de VTK 7/backend open GL compatible GLX (défaut : True)')
    variant('mpi', default=False, description='Utilisation de VTK parallèle MPI (défaut : False)')

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant('BUILD_SHARED_LIBS', 'shared'))

        return args
