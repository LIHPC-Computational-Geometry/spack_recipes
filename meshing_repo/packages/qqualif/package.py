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
    url = 'https://github.com/LIHPC-Computational-Geometry/qqualif/archive/refs/tags/v3.9.1.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/qqualif.git'
    maintainers = ['meshing_team']

# On a besoin de 5.0 <= tkutil :
    depends_on('qwtcharts@4: ~shared', type=('build', 'link'), when='~shared')
    depends_on('qwtcharts@4: +shared', type=('build', 'link'), when='+shared')
    depends_on('vtkcontrib@4: ~shared', type=('build', 'link'), when='~shared+vtk')
    depends_on('vtkcontrib@4: +shared', type=('build', 'link'), when='+shared+vtk')
    depends_on('qualif@2: ~shared', type=('build', 'link'), when='~shared')
    depends_on('qualif@2: +shared', type=('build', 'link'), when='+shared')
    depends_on('gmds', type=('build', 'link'), when='+gmds')
    depends_on('lima', type=('build', 'link'), when='+lima')
    depends_on('vtk-maillage', type=('build', 'link'))

# necessary because it is probably missing in the lima cmake files
#    depends_on('machine-types', type=('build', 'link'), when='+lima')

    # patch in order to compile the hexagen test
  #  patch('qqualif-3.7.1_missing_lima_in_test.patch')

    variant('shared', default=True, description='Creation de bibliotheques dynamiques')
    variant('lima', default=True, description='Utilisation de la structure de maillages Lima')
    variant('gmds', default=True, description='Utilisation de la structure de maillages GMDS')
    variant('vtk', default=True, description='Utilisation de la structure de maillages VTK')

    version('3.9.1')
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
        args.append ('-DVTK_7:BOOL=ON')	# ATTENTION : si vtk, et la version dépend de la version majeure de vtk-maillage

        return args
