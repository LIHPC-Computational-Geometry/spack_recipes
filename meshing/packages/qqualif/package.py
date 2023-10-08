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
    url = 'https://github.com/LIHPC-Computational-Geometry/qqualif/archive/refs/tags/4.2.1.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/qqualif.git'
    maintainers = ['meshing_team']

    depends_on('guitoolkitsvariables', type=('build'))
    depends_on('qwtcharts@4: ~shared', type=('build', 'link'), when='~shared')
    depends_on('qwtcharts@4: +shared', type=('build', 'link'), when='+shared')
    depends_on('vtkcontrib@4: ~shared', type=('build', 'link'), when='~shared+vtk')
    depends_on('vtkcontrib@4: +shared', type=('build', 'link'), when='+shared+vtk')
    depends_on('qualif@2: ~shared', type=('build', 'link'), when='~shared')
    depends_on('qualif@2: +shared', type=('build', 'link'), when='+shared')
    depends_on('gmds', type=('build', 'link'), when='+gmds')
    depends_on('lima', type=('build', 'link'), when='+lima')
    depends_on('vtk-maillage', type=('build', 'link'), when='+vtk')

# necessary because it is probably missing in the lima cmake files
#    depends_on('machine-types', type=('build', 'link'), when='+lima')

    # patch in order to compile the hexagen test
  #  patch('qqualif-3.7.1_missing_lima_in_test.patch')

    variant('shared', default=True, description='Creation de bibliotheques dynamiques')
    variant('lima', default=True, description='Utilisation de la structure de maillages Lima')
    variant('gmds', default=True, description='Utilisation de la structure de maillages GMDS')
    variant('vtk', default=True, description='Utilisation de la structure de maillages VTK')

    version('4.2.1', sha256='616f7411c1e07deb7257ee6ac398082e779d691d63b52d8e4eda382625d96380')
    version('4.2.0', sha256='753182217c65ec4408fc5ea1e1d2a392ea0a662d5a977838ac5be2b09ff5af81')
    version('3.9.1', sha256='bcc2a63ff842e59483bcafe68b09da17834f18b0bc6fecbad68638f85ba8f3e1')
    version('3.9.0')
    version('3.7.3', sha256='26c7abf2bf4af3608a3777cfa33b67a017965d20681d2e38532aa67e4327442a')
    version('3.7.1', sha256='88f767746ec679990b6ca957825d58f374ab322caae53b60f1e48887bcb0c59d')
    version('3.1.0', sha256='51405815a2f7cf1472d98ba77836da7aa85abec035c7ac3da9f7f0178aae234e')
    version('3.0.5', sha256='400b8d308c6813d236b380742793a27c7169e8c89b894a6397c583fee52730cf')
    version('3.0.4', sha256='bcfa1f54962c9681417382155a5f7c2a2addfe01096804919cb0619ecbfd64ea')
    version('3.0.2', sha256='975bbe849a780e4d9edfbd25ecfde9db651b35a295a7939b3b243467cc6ab6e5')
    version('3.0.1', sha256='9a942e63fbcce101e8231215bd52fff00bca8106b3c9d0ffd01dbacd606c988c')

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant('BUILD_SHARED_LIBS', 'shared'))
        args.append(self.define_from_variant('BUILD_GQLima', 'lima'))
        args.append(self.define_from_variant('BUILD_GQGMDS', 'gmds'))
        args.append(self.define_from_variant('BUILD_GQVtk', 'vtk'))
       
        if '+vtk' in self.spec:
            if self.spec['vtk-maillage'].version < Version('8'):
                args.append('-DVTK_7:BOOL=ON')
            elif self.spec['vtk-maillage'].version < Version('9'):
                args.append('-DVTK_8:BOOL=ON')
            else:
                args.append('-DVTK_9:BOOL=ON')

        return args
