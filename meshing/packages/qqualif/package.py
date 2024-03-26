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
    # Rem à propos de VTK : peu importe que ce soit VTK 7 (vtk-maillage) ou VTK 9 (vtk), on suit le mouvement :
    depends_on('vtkcontrib@5.4.0: ~shared', type=('build', 'link'), when='~shared+vtk')
    depends_on('vtkcontrib@5.4.0: +shared', type=('build', 'link'), when='+shared+vtk')
    depends_on('qualif@2: ~shared', type=('build', 'link'), when='~shared')
    depends_on('qualif@2: +shared', type=('build', 'link'), when='+shared')
    depends_on('gmds', type=('build', 'link'), when='+gmds')
    depends_on('lima', type=('build', 'link'), when='+lima')

# necessary because it is probably missing in the lima cmake files
#    depends_on('machine-types', type=('build', 'link'), when='+lima')

    # patch in order to compile the hexagen test
    # patch('qqualif-3.7.1_missing_lima_in_test.patch')

    variant('shared', default=True, description='Creation de bibliotheques dynamiques')
    variant('lima', default=True, description='Utilisation de la structure de maillages Lima')
    variant('gmds', default=True, description='Utilisation de la structure de maillages GMDS')
    variant('vtk', default=True, description='Utilisation de la structure de maillages VTK')

    version('4.3.0', sha256='4f7cfd222c207f634837ba93e319f0f57a18fcead04d1aa265ae825031c59537')

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant('BUILD_SHARED_LIBS', 'shared'))
        args.append(self.define_from_variant('BUILD_GQLima', 'lima'))
        args.append(self.define_from_variant('BUILD_GQGMDS', 'gmds'))
        args.append(self.define_from_variant('BUILD_GQVtk', 'vtk'))

        return args
