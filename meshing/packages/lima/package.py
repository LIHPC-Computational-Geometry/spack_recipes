# -*- coding: utf-8 -*-

##############################################################################
# Project Lima (Logiciel Interface MAillage)
#
# REPLACE_NAME_SERVICE_LABO, 2020
##############################################################################

# From version 7.11.0 writing support for the mli format is no longer provided.

from spack import *


class Lima(CMakePackage):
    """Logiciel Interface MAillage"""

    homepage = 'https://github.com/LIHPC-Computational-Geometry/lima'
    url = 'https://github.com/LIHPC-Computational-Geometry/lima/archive/refs/tags/0.0.0.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/lima.git'
    maintainers = ['meshing_team']

    extends("python", when='+scripting')		# For the PYTHONPATH in the generated modules

#    depends_on('sumesh +shared', type=('build', 'link'))
    depends_on('swig', type=('build'), when='+scripting')
    depends_on('python +shared', type=('build', 'link'), when='+scripting')
#    depends_on('hdf145', type=('build', 'link'))
#    depends_on('hdf5 +shared +cxx', type=('build', 'link'))
    depends_on('hdf5 +shared +cxx', type=('build', 'link'))

    variant('scripting', default=False, description='Build python binding')
    variant('shared', default=True, description='Build shared library')
    variant('xlmlima', default=True,
            description='Build xlmlima tool (converts and prepares meshes, necessary for non-regression tests)')
    variant('mli2', default=True, description='Build Lima with mli2 format support (requires HDF5 >=1.10.0)')

    variant('i4', default=False, description="int_type=int32 instead of int64")
    variant('r4', default=False, description="real=float instead of double")
    variant('tests', default=True,
            description="Builds the mesh comparison tool (necessary for non-regression tests)")
    variant('disable_mli_warning',
            default=False, description="Disables warning messages displayed when reading or writing a file in mli format (obsolete)")

    patch('cmake.patch', when='@7.4.3')
    patch('cmake-7.6.0.patch', when='@7.6.0')

    version('main', branch='main')
    version('7.11.2', sha256='87105227d07484feb5a4cf8aef75734165abd478f205e3723a2573ef4ef904aa')
    version('7.11.1', sha256='a1b0397ce668cb473775fd1f5e2adc30880680042b623e63e9a6b855ecf03591')
    version('7.11.0', sha256='9fcce72a37e1e3f71745482d17c357739a094fd31283fde7f79d898f2922230d')
    version('7.10.3', sha256='ccd943aeeee3cf28e9e12a5596b94adfe7d63bb8514858556481494fd8b2cdcd')
    version('7.10.2', sha256='60975df285defe7f8aee8f5858b4ab2c917053279db4b4b2adab7ce25f1aeb9c')
    version('7.10.1', sha256='27480c4df5ddba0738f5f916cf3c53b054feeae78d14cc669bb633ba745f4ca0')
    version('7.10.0', sha256='95d6d0f3d696945fd88a70572eb3ec769f484e2315017566f3b971f9048632bb')
    version('7.9.6', sha256='650f071afb420cab80cfb4f25913b59f2cff68f6ceb921ea91f58d6985460cba')
    version('7.9.5', sha256='48d06f71cefb7253d24b4ae5f9803219ab861281806521d97f335d6a2a209ccd')
    version('7.9.4', sha256='ab2fae0938b08c86685b0b2809dff5f6f69bb139e50179c952b391447d5833ec')
    version('7.9.3', sha256='4ef65333269ad9ba3a522a4b82d621b4a9ae6d920042a67361fe0a404c4fd0c1')
    version('7.9.2', sha256='fee1d16d12b6b2beaa6680903f67feba0fe10a0b1159a61dd926816f89e635fa')
    version('7.9.1', sha256='da517fa87a6df3b07e793d8a6a300865614803fa84cf1d3ec1994605e69b4571')
    version('7.9.0', sha256='7849219cf1de94c63fe019187a4a8dec61447d1b726fac90f43d871293f55315')
    version('7.8.1', sha256='a54de52e7414d820c5ba081cf6693e753e92993f0d250f56fd215cc2fbe28b65')
    version('7.7.9', sha256='e251a6732a2cdafb7f2851be3c5f5dba41d937fe253a9ebbf50fb81a7ddbd11f')
    version('7.4.2', sha256='7bbcd876f8c6c4330583e281707777f3142d469c248c0b0e0c6dcbda6621e8d0')
    version('7.5.1', sha256='91ef19f6f48d6795a776fea4ceabfc6e19f21f9dbb7dd489191f0ef9ff5c040a')
    version('7.6.0', sha256='6c8c963c487430de1f00bba0cd7fe1a6ec5f2ee07d1b465b74f29d71fb45fe48')
    version('7.6.3', sha256='4039ebbf3f7e047b6cb75393c6a3d4a86be635c03798bb2eb69760c2b760a508')

    conflicts('~shared', '+scripting')

    def cmake_args(self):
        args = [self.define_from_variant('BUILD_SHARED_LIBS', 'shared'),
                self.define_from_variant('BUILD_SCRIPTING', 'scripting'),
                self.define_from_variant('BUILD_XLMLIMA', 'xlmlima'),
                self.define_from_variant('BUILD_TESTS', 'tests'),
                self.define_from_variant('DISABLE_MLI_WARNING', 'disable_mli_warning'),
                self.define_from_variant('FORMAT_MLI2', 'mli2')]

        args.append(self.define('MACHINE_TYPES', False))
        args.append(self.define('FORMAT_MLI', False))
        args.append(self.define('SUMESH', False))

        if '+i4' in self.spec:
            args.append(self.define('INT_8', False))
        else:
            args.append(self.define('INT_8', True))

        if '+r4' in self.spec:
            args.append(self.define('REAL_8', False))
        else:
            args.append(self.define('REAL_8', True))

        if '+scripting' in self.spec:
            py = self.spec['python']
            args.extend([
                self.define('USE_PYTHON_3', int(py.version[0]) >= 3),
                self.define('USE_PYTHON_2', int(py.version[0]) < 3),
                # find_package(Python) under cmake_minimum_required < 3.15 (CMP0094)
                self.define('Python_EXECUTABLE', py.command.path),
                # find_package(Python2/3) under cmake_minimum_required < 3.15 (CMP0094)
                self.define('Python{}_EXECUTABLE'.format(py.version[0]),
                            py.command.path),
            ])

        return args
