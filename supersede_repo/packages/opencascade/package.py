# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Opencascade(CMakePackage):
    """Open CASCADE Technology is a software development kit (SDK)
    intended for development of applications dealing with 3D CAD data,
    freely available in open source. It includes a set of C++ class
    libraries providing services for 3D surface and solid modeling,
    visualization, data exchange and rapid application development."""


##############################################
# WARNING this supersedes the upstream recipe 
##############################################

    homepage = "https://www.opencascade.com"
    url      = "https://git.dev.opencascade.org/gitweb/?p=occt.git;a=snapshot;h=refs/tags/V7_1_0;sf=tgz"

#    version('7.4.0', extension='tar.gz',
#            sha256='1eace85115ea178f268e9d803ced994b66b72455b5484074b6ad7f643261f0a0')
    version('7.1.0', extension='tar.gz')#,
 #           sha256='f28ca30bf939158c192df571d78b9dae0e34ab8d8ec9a8b2e8274acd81e138c8')

    # Opencascade depends on xlocale.h from glibc-headers but it was removed in 2.26.
    # This patch is a tentative backport from v7.4.0
    patch('xlocale-7_1.patch', when='@7.1.0')

    # modifications for internal use
    patch('opencascade-7.1.0_a.patch', when='@7.1.0')
    
    variant('tbb', default=False,
            description='Build with Intel Threading Building Blocks')
    variant('vtk', default=False,
            description='Enable VTK support')
    variant('freeimage', default=False,
            description='Build with FreeImage')
    variant('rapidjson', default=False,
            description='Build with rapidjson')
    variant('gl2ps', default=False,
            description='Build with gl2ps (only in 7.1.0)')

    # optionnal modules
    variant('documentation', default=False,
            description='Sets BUILD_DOC_Overview (uses doxygen)')
    variant('applicationframework', default=False,
            description='Sets BUILD_MODULE_ApplicationFramew')
    variant('dataexchange', default=False,
            description='Sets BUILD_MODULE_DataExchange')
    variant('draw', default=False,
            description='Sets BUILD_MODULE_Draw')
    variant('foundationclasses', default=False,
            description='Sets BUILD_MODULE_FoundationClasses (probably always ON)' )
    variant('modelingalgorithm', default=False,
            description='Sets BUILD_MODULE_ModelingAlgorithm')
    variant('modelingdata', default=False,
            description='Sets BUILD_MODULE_ModelingData')
    variant('visualization', default=False,
            description='Sets BUILD_MODULE_Visualization')
    

    depends_on('intel-tbb', when='+tbb')
    depends_on('vtk', when='+vtk')
    depends_on('freeimage', when='+freeimage')
    depends_on('rapidjson', when='+rapidjson')
    depends_on('gl2ps', when='@7.1.0+gl2ps')
    depends_on('doxygen', when='+documentation')


    depends_on('freetype')
    depends_on('tcl')

    # OCC does not care for the X screensaver variant of tk so we leave
    # it as indifferent
    # We should probably have ~xss as default in the tk recipe
    depends_on('tk')

    depends_on('gl')

    # those two libraries are always used at link phase, but it could be a 
    # remnant of the optionnal gl2ps module. We might be able to remove 
    # those dependencies in a future release of OCC.
    depends_on('libxmu', type=('build','link'))
    depends_on('libxi', type=('build','link'))

    def cmake_args(self):
        args = []

        if '+tbb' in self.spec:
            args.append('-DUSE_TBB=ON')
            args.append('-D3RDPARTY_VTK_DIR=%s' %
                        self.spec['intel-tbb'].prefix)
        else:
            args.append('-DUSE_TBB=OFF')

        if '+vtk' in self.spec:
            args.append('-DUSE_VTK=ON')
            args.append('-D3RDPARTY_VTK_DIR=%s' %
                        self.spec['vtk'].prefix)
        else:
            args.append('-DUSE_VTK=OFF')

        if '+freeimage' in self.spec:
            args.append('-DUSE_FREEIMAGE=ON')
            args.append('-D3RDPARTY_FREEIMAGE_DIR=%s' %
                        self.spec['freeimage'].prefix)
        else:
            args.append('-DUSE_FREEIMAGE=OFF')

        if '+rapidjson' in self.spec:
            args.append('-DUSE_RAPIDJSON=ON')
            args.append('-D3RDPARTY_RAPIDJSON_DIR=%s' %
                        self.spec['rapidjson'].prefix)
        else:
            args.append('-DUSE_RAPIDJSON=OFF')

        if '+gl2ps' in self.spec:
            args.append('-DUSE_GL2PS=ON')
            args.append('-D3RDPARTY_GL2PS_DIR=%s' %
                        self.spec['gl2ps'].prefix)
        else:
            args.append('-DUSE_GL2PS=OFF')

        
        if '+documentation' in self.spec:
            args.append('-DBUILD_DOC_Overview=ON')
        else:
            args.append('-DBUILD_DOC_Overview=OFF')

        if '+applicationframework' in self.spec:
            args.append('-DBUILD_MODULE_ApplicationFramew=ON')
        else:
            args.append('-DBUILD_MODULE_ApplicationFramew=OFF')

        if '+dataexchange' in self.spec:
            args.append('-DBUILD_MODULE_DataExchange=ON')
        else:
            args.append('-DBUILD_MODULE_DataExchange=OFF')

        if '+draw' in self.spec:
            args.append('-DBUILD_MODULE_Draw=ON')
        else:
            args.append('-DBUILD_MODULE_Draw=OFF')
        
        if '+foundationclasses' in self.spec:
            args.append('-DBUILD_MODULE_FoundationClasses=ON')
        else:
            args.append('-DBUILD_MODULE_FoundationClasses=OFF')

        if '+modelingalgorithm' in self.spec:
            args.append('-DBUILD_MODULE_ModelingAlgorithm=ON')
        else:
            args.append('-DBUILD_MODULE_ModelingAlgorithm=OFF')

        if '+modelingdata' in self.spec:
            args.append('-DBUILD_MODULE_ModelingData=ON')
        else:
            args.append('-DBUILD_MODULE_ModelingData=OFF')

        if '+visualization' in self.spec:
            args.append('-DBUILD_MODULE_Visualization=ON')
        else:
            args.append('-DBUILD_MODULE_Visualization=OFF')

        return args
