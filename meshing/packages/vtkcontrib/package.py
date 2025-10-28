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

# Rem : peu de variants pour VTK au regard de ce qui pourrait etre fait : opengl2, python, xdmf, qt, mpi, ffmpeg
# On veut dans cette version un VTK 7.*
#    depends_on('vtk@7.1:7.99~opengl2~python~xdmf+qt', type=('build', 'link'))
#    depends_on('qt@5.9.1', type=('build', 'link'))
    depends_on('guitoolkitsvariables@1.5.99:', type=('build', 'link'))
    depends_on('vtk-maillage', type=('build', 'link'))
#   depends_on('mpi', type=('build', 'link'))

# for undefined reference in util-linux/libmount to intl_....
#    depends_on('gettext')

    patch('vtkcontrib-4.6.0_calc_mpi.patch', when='@4.6.0')

    version('5.13.1', sha256='baf8db650a705d1dfc72a48da38e272c0ef72024a029e982ceef1d35d6ef3422')
    version('5.13.0', sha256='c2df1b2171fd72216e6279fa234e71203a7d3904e850bc3342fa2cee4f67e385')
    version('5.12.0', sha256='6cbd668f33c3df5f48aa34687239ad3fdf76d0d5f3e71b20893b2ae3fcef34c9')
    version('5.11.0', sha256='cdf69401fbb16f5d02546193ba49377852cdb6328a4bb00c0268869e05827e03')
    version('5.10.0', sha256='7d2a940d43827eff135fbcd51345876ed10354656a8fffee455702b130a1e853')
    version('5.9.0', sha256='eb6440b9c6cb386352f12faa420a61ed889c13c675856ed9846ffeaee259a632')
    version('5.8.0', sha256='a8da685e29f302a5e2c78fd53eb9b8eb81d1d62b3a60dc03a9fab0e0f9fb196b')
    version('5.7.1', sha256='000ff5ef5f2eb5873b110c479dff63a1705251c77275ae55fbaa5243aa8433e2')
    version('5.7.0', sha256='71fdb9f29538fcf4076c8238f8ceb369c20e5a548982837d3b5543852a66a03a')
    version('5.6.1', sha256='ef20de3d076e4b55b9e10aadfa2d5f1b25e21934b439c9c8afe00fa88e0164fa')
    version('5.6.0', sha256='848c2576f870b3e3dc5cb1d84d3f073f676497d865109642c7ab05f355d5a4c4')
    version('5.5.0', sha256='cb3056a9448fed7e738febc1382a5d1b6ae9ed29c0e1340f99dd03d0af913eba')
    version('5.4.3', sha256='80f8b6e2f29f8d79e16f96874d4b5b336ca7e16e86d21f69376b285a0cd70469')
    version('5.4.2', sha256='5d93d8051f4a1546932f201368bc2d4222ec617c1344dbc9ee1413beb7e24ec2')
    version('5.4.1', sha256='de31db5778628eb8b01a67517379b2abe524944a038a348c00d65b1935ad0081')
    version('5.4.0', sha256='c3c7d6b9491cbb273084ef1f5795e88599d23a041b568b61d1da426277cefcea')
    version('4.6.4', sha256='1fce68d5c9342f90ff54aae75248679d52e303cf1954cdcf2ed0bf9bc6157a4c')
    version('4.6.1', sha256='8d32ff953f61addd0a40fa6a92c2ba8fe11f7431cc01608f45b8f7f681a7de76')
    version('4.6.0', sha256='269220824875c4945bdbdd78589d460b5a5ca806d78166c38079bb228e933e11')
    version('4.0.1', sha256='ea186d906ed63c9be0328067d08889dfe72b4fc1710831fc8234496f048003af')
    version('4.0.0', sha256='3ddcb0b3f5c06c93a8fc3ea9b7cb03e93d3f5ed4ec0d2ea2a48eab7c68529305')

    variant('shared', default=True, description='Creation de bibliotheques dynamiques (defaut:shared, annuler le defaut par ~shared)')

    def cmake_args(self):
        # Since version 5.4.0 VtkContrib uses common_vtk.cmake of GUIToolkitsVariables which
        # sets VTK 7, VTK 8 or VTK 9 to ON.
        args = []
        args.append(self.define_from_variant('BUILD_SHARED_LIBS', 'shared'))

        # if OFF does vtkcontrib uses OPENGL2 ?
        # see VTK_OPENGL_BACKEND in src/VtkContrib/CMakeLists.txt
        args.append('-DUSE_OPENGL_BACKEND:BOOL=ON')

        return args
