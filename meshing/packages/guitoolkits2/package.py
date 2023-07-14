# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install guitoolkits2
#
# You can edit this file again by typing:
#
#     spack edit guitoolkits2
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

#
# Exemple d'installation : spack install --j 16 guitoolkits2 +plugin +qtvtk +qwtcharts +annotations +qtnetwork +qtpython ^qt+opengl
#

from spack.package import *


class Guitoolkits2(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    homepage = 'https://github.com/LIHPC-Computational-Geometry/guitoolkits2'
    url = 'https://github.com/LIHPC-Computational-Geometry/guitoolkits2/archive/refs/tags/v1.0.0.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/guitoolkits2.git' 
    maintainers = ["meshing_team"]

    version('1.0.0')

    variant('tkutil', default=True, description='Classes C++ utilitaires')
    variant('pythonutil', default=True, description='Classes pour exécuter des scripts python dans un code C++.')
    variant('qtutil', default=True, description='Classes C++ utilitaires')
    variant('qtpython', default=True, description='Classes C++ utilitaires')
    variant('qtvtk', default=True, description='Classes C++ utilitaires')
    variant('qtnetwork', default=True, description='Classes C++ utilitaires')
    variant('vtkcontrib', default=True, description='Classes C++ utilitaires')
    variant('preferences', default=True, description='Classes C++ utilitaires')
    variant('plugin', default=True, description='Classes C++ utilitaires')
    variant('annotations', default=True, description='Classes C++ utilitaires')
    variant('qtvtk', default=True, description='Classes C++ utilitaires')
    variant('qwtcharts', default=True, description='Classes C++ utilitaires')
    variant('qqualif', default=True, description='Classes C++ utilitaires')
    variant('gmds', default=True, description='Support de GMDS (par QQualif)')
    variant('lima', default=True, description='Support de Lima++ (par QQualif)')
    variant('vtk', default=True, description='Support de VTK (par QQualif)')
    variant('corbautil', default=False, description='Classes C++ utilitaires')

# Les composantes à installer :
# ne pas changer manuellement. Elles sont positionées en fonction des variants
    tkutil		= False
    pythonutil	= False
    qtutil		= False
    qtpython	= False
    vtkcontrib	= False
    qtvtk		= False
    qtnetwork	= False
    preferences	= False
    plugin		= False
    annotations	= False
    qwtcharts	= False
    qqualif		= False
    corbautil	= False

                                            
    depends_on('libiconv', type=('build', 'link'))
    for deppython in ['+tkutil', '+pythonutil', '+qtutil', '+qtpython', '+preferences', '+plugin', '+qwtcharts', '+qqualif', '+qtvtk', '+qtnetwork', '+corbautil']:
        depends_on ('python', type=("build", "link", "run"), when=deppython)
        depends_on ('swig', type=("build"), when=deppython)
        
    for depqt in ['+qtutil', '+qtpython', '+qtvtk', '+qtnetwork', '+preferences', '+plugin', '+annotations', '+qwtcharts', '+qqualif']:
	    depends_on('qt@5.9:', type=("build", "link"), when=depqt)
	    
    for depxercesc in ['+preferences', '+plugin']:
        depends_on ('xerces-c', type=("build", "link"), when=depxercesc)
        
    for depqwt in ['+qwtcharts', '+qqualif']:
        depends_on ('qwt@6.1:', type=("build", "link"), when=depqwt)
        
    for depvtk in ['+vtkcontrib', '+qtvtk', '+annotations']:
        depends_on('vtk-maillage@7.1:', type=('build', 'link'), when=depvtk)	# => Force vtk-maillage d'une version connue. On affine les dépendances ci-dessous.
        depends_on('vtk-maillage~opengl2+qt+mpi', type=('build', 'link'), when=depvtk + " ^vtk-maillage@7.1:7.99")
        depends_on('vtk-maillage+opengl2+qt+mpi', type=('build', 'link'), when=depvtk + " ^vtk-maillage@8:")
        depends_on('vtk-maillage+opengl2+qt+mpi', type=('build', 'link'), when=depvtk + " ^vtk-maillage@9:")

    for depqualif in ['+qqualif']:
        depends_on ('qualif', type=("build", "link"), when=depqualif)
        depends_on ('lima', type=("build", "link"), when=depqualif + " +lima")
        depends_on ('gmds', type=("build", "link"), when=depqualif + " +gmds")
        depends_on ('vtk-maillage', type=("build", "link"), when=depqualif + " +vtk")
        
    depends_on('omniorb-anl', type=('build', 'link'), when='+corbautil')
 
    # to avoid QtWebEngine or QtWebkit
    variant('qtbrowser', default=True, description='Use Qt base browser')
    
#    depends_on('doxygen')

    def cmake_args(self):

        if self.spec.satisfies('+tkutil'):
            self.tkutil		= True
            
        if self.spec.satisfies('+pythonutil'):
            self.tkutil		= True
            self.pythonutil	= True
    
        if self.spec.satisfies('+qtutil'):
            self.tkutil		= True
            self.qtutil		= True
            
        if self.spec.satisfies('+qtpython'):
            self.tkutil		= True
            self.qtutil		= True
            self.qtpython	= True

        if self.spec.satisfies('+preferences'):
            self.tkutil		= True
            self.qtutil		= True
            self.preferences	= True

        if self.spec.satisfies('+plugin'):
            self.tkutil		= True
            self.qtutil		= True
            self.preferences	= True
            self.plugin		= True

        if self.spec.satisfies('+qwtcharts'):
            self.tkutil		= True
            self.qtutil		= True
            self.qwtcharts	= True
                                  
        if self.spec.satisfies('+qqualif'):
            self.tkutil		= True
            self.qtutil		= True
            self.qwtcharts	= True
            self.qqualif	= True
 
        if self.spec.satisfies('+qtnetwork'):
            self.tkutil		= True
            self.qtutil		= True
            self.qtnetwork	= True
                       
        if self.spec.satisfies('+vtkcontrib'):
            self.vtkcontrib	= True
            
        if self.spec.satisfies('+qtvtk'):
            self.tkutil		= True
            self.qtutil		= True
            self.vtkcontrib	= True    
            self.qtvtk		= True        

        if self.spec.satisfies('+annotations'):
            self.tkutil		= True
            self.qtutil		= True
            self.vtkcontrib	= True
            self.qtvtk		= True        
            self.annotations= True

        if self.spec.satisfies('+corbautil'):
            self.tkutil		= True
            self.corbautil	= True
            
        args = [
            self.define('BUILD_SHARED_LIBS', True),
            self.define_from_variant('USE_QT_TEXT_BROWSER', 'qtbrowser')
        ]

        if self.spec.satisfies('%intel'):
            args.append('-DCMAKE_CXX_FLAGS="-std=c++11"')

        if self.tkutil:
            args.append('-DTK_UTIL:BOOL=ON')

        if self.vtkcontrib:
            args.append('-DVTKCONTRIB:BOOL=ON')
            
        if self.pythonutil:
            args.append('-DPYTHON_UTIL:BOOL=ON')
            
        if self.qtutil:
            args.append('-DQT_UTIL:BOOL=ON')
            
        if self.qtpython:
            args.append('-DQT_PYTHON:BOOL=ON')
            
        if self.qtnetwork:
            args.append('-DQT_NETWORK:BOOL=ON')
            
        if self.qtvtk:
            args.append('-DQT_VTK:BOOL=ON')
            
        if self.preferences:
            args.append('-DPREFERENCES:BOOL=ON')
            
        if self.plugin:
            args.append('-DPLUGIN:BOOL=ON')
            
        if self.qwtcharts:
            args.append('-DQWT_CHARTS:BOOL=ON')
            
        if self.qqualif:
            args.append('-DQQUALIF:BOOL=ON')
            if self.spec.satisfies('+lima'):
                args.append('-DBUILD_GQLima:BOOL=ON')
            if self.spec.satisfies('+gmds'):
                args.append('-DBUILD_GQGMDS:BOOL=ON')
            if self.spec.satisfies('+vtk'):
                args.append('-DBUILD_GQVtk:BOOL=ON')
                                            
        if self.annotations:
            args.append('-DANNOTATIONS:BOOL=ON')

        if self.corbautil:
            args.append('-DCORBA_UTIL:BOOL=ON')

        if self.spec['python'].version < Version('3'):
            args.append('-DUSE_PYTHON_2:BOOL=ON')
        else:
            args.append('-DUSE_PYTHON_3:BOOL=ON')

        return args

