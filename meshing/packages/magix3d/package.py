# -*- coding: utf-8 -*-

from spack import *
import os


class Magix3d(CMakePackage):
    """Mailleur 3D"""

    homepage = 'https://github.com/LIHPC-Computational-Geometry/magix3d'
    url = 'https://github.com/LIHPC-Computational-Geometry/magix3d/archive/refs/tags/0.0.0.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/magix3d.git'
    maintainers = ['meshing_team']

    variant('dkoc', default=False, description='Utilisation du lecteur Catia DKOC pour OpenCascade')
    variant('mdlparser', default=False, description='Utilisation du lecteur du format mdl')
    variant('sepa3d', default=False, description='Utilisation du celebre outil de separatrices 3D')
    variant('smooth3d', default=False, description='Utilisation de la bibliotheque de lissage volumique Smooth3D')
    variant('triton2', default=True, description='Utilisation du mailleur tetraedrique Tetgen')
    variant('pythonaddon', default=False, description='Additional python modules to enrich PYTHONPATH')
    variant('doc', default=False, description='Installation de la documentation utilisateur')

    version('2.3.5', sha256='28808a4c5893f84e2de43c8913c6609f97b1a6b213b3bb2d7dd37a8a6c8f8d39')
    version('2.3.4', sha256='934475f0738f7f6d48eb3e33336b4ce6625811722aebc5a566b7327d9dbdd255')
    version('2.3.3', sha256='fd1fbbde688dcfd2ab5e7f102d3209c0e1da7c8bdc8cb0691a5701f9c382f4de')
    version('2.3.2', sha256='5ae3afda57218c0dd6dea8373256f353112ae9156bbef2dd84666b6e32e65b74')
    version('2.3.1', sha256='07f6cabd231777273468dc806f0c318b4520831dbcaf1fa2906c39051585410a')
    version('2.3.0', sha256='9949dac2aa3df14f0e96e94105f47d0a612a83524c8138171fb1860a00feaf36')
    version('2.2.7', sha256='4437209e1811b523c3945fda17ab6aaf2082da9c84f892955123e69465ebd250')
    version('2.2.6', sha256='9d39dd74a1b9360a5ca2790f2d9e8b17429f82833df2d633b57c866383873d05')
    version('2.2.5')

    depends_on('guitoolkitsvariables', type=('build'))
    depends_on('tkutil')
    depends_on('vtkcontrib@4: +shared', type=('build', 'link'))
    depends_on('preferences@5: +shared', type=('build', 'link'))
    depends_on('pythonutil@5: +shared', type=('build', 'link'))
    depends_on('qqualif@3: +shared', type=('build', 'link'))
    depends_on('qtpython@4: +shared', type=('build', 'link'))
    depends_on('qtvtk@7: +shared', type=('build', 'link'))
    depends_on('cgns', type=('build', 'link'))
    depends_on('gmds@1.2.1: +lima', type=('build', 'link'))
    depends_on('gts', type=('build', 'link'))
    depends_on('glib', type=('build', 'link'))
    depends_on('pcre', type=('build', 'link'))
    depends_on('opencascade@7.1.0+foundationclasses+dataexchange', type=('build', 'link'))
    depends_on('tetgen@1.6.0', when='+triton2')
    depends_on('smooth3d +shared', type=('build', 'link'), when='+smooth3d')
    depends_on('swig', type='build')
    depends_on('mesquite')
    depends_on('python')
    depends_on('qt')
    depends_on('doxygen')
    depends_on('lima')
    depends_on('pkgconfig', type=('build'))
    # depends_on('mdl-parser@1.5.2: +shared', type=('build', 'link'), when='+mdlparser')
    # depends_on('dkoc', type=('build', 'link'), when='+dkoc')
    # depends_on('separatrice3d +shared', type=('build', 'link'), when='+sepa3d')
    # depends_on('experimentalroom')

    # the limitations on the version number comes
    # when we are in python2
    depends_on('py-numpy', when='+pythonaddon')
    depends_on('py-numpy@:1.16.2', when='+pythonaddon ^python@2')
    depends_on('py-matplotlib', when='+pythonaddon')
    depends_on('py-matplotlib@:2.2.3', when='+pythonaddon ^python@2')
    depends_on('py-scipy', when='+pythonaddon')
    depends_on('py-scipy@:1.1.0', when='+pythonaddon ^python@2')
    depends_on('py-cycler', when='+pythonaddon')
    depends_on('py-kiwisolver', when='+pythonaddon')
    depends_on('py-pillow', when='+pythonaddon')
    depends_on('py-pillow@:6.2.2', when='+pythonaddon ^python@2')
    depends_on('py-pyparsing', when='+pythonaddon')
    depends_on('py-python-dateutil', when='+pythonaddon')
    depends_on('py-pytz', when='+pythonaddon')
    depends_on('py-setuptools', when='+pythonaddon')
    depends_on('py-setuptools@:44.1.0', when='+pythonaddon ^python@2')
    depends_on('py-setuptools-scm', when='+pythonaddon')
    depends_on('py-six', when='+pythonaddon')
    depends_on('py-packaging', when='+pythonaddon')

    # documentation
    depends_on("py-breathe", when="+doc")
    depends_on("py-rst2pdf", when="+doc")
    # sphinx version fixed for rtd_theme
    depends_on("py-sphinx@5.3.0", when="+doc")
    # rtd_theme version fixed to fix no module found epub3
    depends_on("py-sphinx-rtd-theme@0.5.1", when="+doc")
    depends_on("py-sphinx-copybutton", when="+doc")

    # setup PYTHON_PATH for documentation
    def setup_build_environment(self, env):
        if ('+doc' in self.spec.variants):
            python_version = str(self.spec['python'].version).split('.')
            python_dir = "python" + python_version[0] + "." + python_version[1]

            sphinx_path = self.spec['py-sphinx'].prefix
            sphinx_pythonpath = join_path(sphinx_path, 'lib', python_dir, 'site-packages')
            env.prepend_path('PYTHONPATH', sphinx_pythonpath)

    def cmake_args(self):
        return self.fill_cmake_args(False, 'undefined', 'undefined', 'undefined', 'undefined', 'unavailable')

    def fill_cmake_args(self, batch, t_ext, erd_ext, team, dox_path, dkoc_lic):
        args = []

        args.append('-DBUILD_SHARED_LIBS:BOOL=ON')  # Toujours en mode shared, pour le scripting
        args.append('-DPRODUCTION:BOOL=ON')         # On installe => mode production pour les scripts fixant l'environnement python d'execution
        if self.spec.satisfies('%intel'):
            args.append('-DCMAKE_CXX_FLAGS="-std=c++11"')

        args.append(self.define_from_variant('DKOC', 'dkoc'))
        args.append(self.define_from_variant('MDLPARSER', 'mdlparser'))
        args.append(self.define_from_variant('SEPA3D', 'sepa3d'))
        args.append(self.define_from_variant('SMOOTH3D', 'smooth3d'))
        args.append(self.define_from_variant('TRITON', 'triton2'))
        args.append(self.define_from_variant('PYTHONADDON', 'pythonaddon'))
        args.append(self.define_from_variant('WITH_DOC', 'doc'))

        args.append(self.define('T_INTERNAL_EXTENSION', t_ext))
        args.append(self.define('ERD_INTERNAL_EXTENSION', erd_ext))
        args.append(self.define('USER_TEAM', team))
        args.append(self.define('DOXYGEN_PATH', dox_path))
        args.append(self.define('DKOC_LICENCE', dkoc_lic))
        args.append(self.define('URL_WIKI', 'url_wiki'))
        args.append(self.define('URL_TUTORIAL', 'url_tuto'))
        args.append(self.define('URL_QUALIF', 'url_doc_qualif'))

        args.append(self.define('BUILD_MAGIX3D', True))
        args.append(self.define('BUILD_MAGIX3DBATCH', batch))

        if ('+doc' in self.spec.variants):
            args.append('-DSPHINX_WARNINGS_AS_ERRORS=OFF')

        args.append(self.define('USE_PYTHON_3', int(self.spec['python'].version[0]) >= 3))
        args.append(self.define('USE_PYTHON_2', int(self.spec['python'].version[0]) < 3))

        # only py-numpy py-matplotlib py-scipy are necessary
        # the rest are here because we are not in an environment
        if "+pythonaddon" in self.spec:
            python_version = self.spec['python'].version.up_to(2)
            py_depends = ['py-numpy', 'py-matplotlib', 'py-scipy',
                          'py-cycler', 'py-kiwisolver',
                          'py-pillow', 'py-pyparsing', 'py-python-dateutil',
                          'py-pytz', 'py-setuptools', 'py-setuptools-scm',
                          'py-six', 'py-packaging']
            python_path = []
            for py_dep in py_depends:
                python_path.append(os.path.join(self.spec[py_dep].prefix, 'lib',
                                                'python' + str(python_version),
                                                'site-packages'))
            args.append('-DADDPYTHONPACKAGES=' + ':'.join(python_path) + ':')

        return args
