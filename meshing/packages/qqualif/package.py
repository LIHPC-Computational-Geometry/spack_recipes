# -*- coding: utf-8 -*-
##############################################################################
# Project QQualif
#
# CEA/DAM/DSSI, 2020
##############################################################################

from spack import *


class Qqualif(CMakePackage):
    """Bibliotheque d'utilitaires de qualite de maillage."""

    homepage = 'https://github.com/LIHPC-Computational-Geometry/qqualif'
    url = 'https://github.com/LIHPC-Computational-Geometry/qqualif/archive/refs/tags/0.0.0.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/qqualif.git'
    maintainers = ['meshing_team']

    depends_on('guitoolkitsvariables', type=('build'))
    depends_on('qwtcharts@4: ~shared', type=('build', 'link'), when='~shared')
    depends_on('qwtcharts@4: +shared', type=('build', 'link'), when='+shared')
#    depends_on('vtkcontrib@4: ~shared', type=('build', 'link'), when='~shared+vtk')
#    depends_on('vtkcontrib@4: +shared', type=('build', 'link'), when='+shared+vtk')
    depends_on('qualif@2: ~shared', type=('build', 'link'), when='~shared')
    depends_on('qualif@2: +shared', type=('build', 'link'), when='+shared')
    depends_on('gmds', type=('build', 'link'), when='+gmds')
    depends_on('lima', type=('build', 'link'), when='+lima')
    depends_on('vtk-maillage', type=('build', 'link'), when='+vtk7')
    depends_on('vtk', type=('build', 'link'), when='+vtk9')

# necessary because it is probably missing in the lima cmake files
#    depends_on('machine-types', type=('build', 'link'), when='+lima')

    # patch in order to compile the hexagen test
    # patch('qqualif-3.7.1_missing_lima_in_test.patch')

    variant('shared', default=True, description='Creation de bibliotheques dynamiques')
    variant('lima', default=True, description='Utilisation de la structure de maillages Lima')
    variant('gmds', default=True, description='Utilisation de la structure de maillages GMDS')
# The difficulty with QQualif is that we do or do not want VTK, and that, for VtkContrib and 
# QtVtk, we can use vtk-maillage or vtk 9.
# The use here of the 2 variants vtk7 and vtk9 allows us to cover these 3 cases.
    variant('vtk7', default=True, description='Utilisation de la structure de maillages vtkUnstructuredGrid de VTK 7')
    variant('vtk9', default=False, description='Utilisation de la structure de maillages vtkUnstructuredGrid de VTK 9')
    conflicts('+vtk7', when='+vtk9')

    version('4.6.0', sha256='78fbbbd4919b5b6a96ee684e66baafa074c2a36328829ac120625e1a6540da14')
    version('4.5.0', sha256='ae16c1e0c44a5ad3843e9bc7e6beca3d800ce0c887faf646e06b8f0dfb40363e')
    version('4.4.0', sha256='0d8d315c1131ec36af92b6455880c4071ef3b06c36bebca55075c94b3e347224')
    version('4.3.2', sha256='3be7b1615df727fecd8d590048745ea4fe51922c1745e0e78fe449a57aa28ab3')
    version('4.3.1', sha256='93bf0c9cce52c7bc7157f3e728063d9699a88fb84875e649c31386cbab230b47')
    version('4.3.0', sha256='4f7cfd222c207f634837ba93e319f0f57a18fcead04d1aa265ae825031c59537')
    version('4.2.1', sha256='616f7411c1e07deb7257ee6ac398082e779d691d63b52d8e4eda382625d96380')
    version('4.2.0', sha256='753182217c65ec4408fc5ea1e1d2a392ea0a662d5a977838ac5be2b09ff5af81')
    version('3.9.1', sha256='bcc2a63ff842e59483bcafe68b09da17834f18b0bc6fecbad68638f85ba8f3e1')
    # versions below are deprecated as sources are in the infinite void of space
    version('3.7.3', sha256='26c7abf2bf4af3608a3777cfa33b67a017965d20681d2e38532aa67e4327442a', deprecated=True)
    version('3.7.1', sha256='88f767746ec679990b6ca957825d58f374ab322caae53b60f1e48887bcb0c59d', deprecated=True)
    version('3.1.0', sha256='51405815a2f7cf1472d98ba77836da7aa85abec035c7ac3da9f7f0178aae234e', deprecated=True)
    version('3.0.5', sha256='400b8d308c6813d236b380742793a27c7169e8c89b894a6397c583fee52730cf', deprecated=True)
    version('3.0.4', sha256='bcfa1f54962c9681417382155a5f7c2a2addfe01096804919cb0619ecbfd64ea', deprecated=True)
    version('3.0.2', sha256='975bbe849a780e4d9edfbd25ecfde9db651b35a295a7939b3b243467cc6ab6e5', deprecated=True)
    version('3.0.1', sha256='9a942e63fbcce101e8231215bd52fff00bca8106b3c9d0ffd01dbacd606c988c', deprecated=True)

    depends_on("cxx", type="build")  # generated

    def cmake_args(self):
        # Since version 5.4.0 VtkContrib uses common_vtk.cmake of GUIToolkitsVariables which
        # sets VTK 7, VTK 8 or VTK 9 to ON.
        args = []
        args.append(self.define_from_variant('BUILD_SHARED_LIBS', 'shared'))
        args.append(self.define_from_variant('BUILD_GQLima', 'lima'))
        args.append(self.define_from_variant('BUILD_GQGMDS', 'gmds'))
        if self.spec.satisfies('+vtk7') or self.spec.satisfies('+vtk9'):
            args.append('-DBUILD_GQVtk:BOOL=ON')

        return args
