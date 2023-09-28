# -*- coding: utf-8 -*-

from spack import *
import os

class Magix3d(CMakePackage):
    """Mailleur 3D"""

    homepage = 'https://github.com/LIHPC-Computational-Geometry/magix3d'
    url = 'https://github.com/LIHPC-Computational-Geometry/magix3d/archive/refs/tags/2.2.4.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/magix3d.git'
    maintainers = ['meshing_team']
    
    variant('dkoc', default=False, description='Utilisation du lecteur Catia DKOC pour OpenCascade')
    variant('mdlparser', default=False, description='Utilisation du lecteur du format mdl')
    variant('meshgems', default=False, description='Utilisation de la bibliotheque de maillage volumique MeshGems')
    variant('sepa3d', default=False, description='Utilisation du celebre outil de separatrices 3D')
    # 2023/06/02 - BL: Waiting for a GitHub smooth3d version, True ==> False
    variant('smooth3d', default=False, description='Utilisation de la bibliotheque de lissage volumique Smooth3D')
    variant('triton2', default=True, description='Utilisation du mailleur tetraedrique Tetgen')
    variant('pythonaddon', default=False, description='Additional python modules to enrich PYTHONPATH')
    variant('doc', default=False, description='Installation de la documentation utilisateur')

    version('2.2.6', sha256='5917142b8467f3d47529908884260cdf263604fbecb4a513f364381f82111b3f')
    version('2.2.5')

    depends_on('tkutil')
    depends_on('vtkcontrib@4: +shared', type=('build', 'link'))
    depends_on('preferences@5: +shared', type=('build', 'link'))
    depends_on('pythonutil@5: +shared', type=('build', 'link'))
    depends_on('qqualif@3: +shared', type=('build', 'link'))
    depends_on('qtpython@4: +shared', type=('build', 'link'))
    depends_on('qtvtk@7: +shared', type=('build', 'link'))
    depends_on('cgns', type=('build', 'link'))
    depends_on('gmds@0.7.2:', type=('build', 'link'))
    depends_on('gmdscea@2: +shared', type=('build', 'link'))
    depends_on('gts', type=('build', 'link'))
    depends_on('glib', type=('build', 'link'))
    depends_on('pcre', type=('build', 'link'))
#    depends_on('mdl-parser@1.5.2: +shared', type=('build', 'link'))
#    depends_on('opencascade@7.1.0+foundationclasses+dataexchange+visualization', type=('build', 'link'))
    depends_on('opencascade@7.1.0+foundationclasses+dataexchange', type=('build', 'link'))
   # depends_on('dkoc', type=('build', 'link'), when='+dkoc')
   # depends_on('meshgems', type=('build', 'link'), when='+meshgems')
   # depends_on('separatrice3d +shared', type=('build', 'link'), when='+sepa3d')
    depends_on('smooth3d +shared', type=('build', 'link'), when='+smooth3d')
    depends_on('swig', type='build')
    depends_on('triton2 +shared', type=('build', 'link'), when='+triton2')
    depends_on('mesquite')
    depends_on('python')
    depends_on('qt')
    depends_on('doxygen')
    depends_on('lima')
  #  depends_on('experimentalroom')
    depends_on('pkgconfig', type=('build'))

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

    # documentation
    depends_on("libpng", when="+doc")
    depends_on("graphviz", when="+doc")
    depends_on("py-breathe", when="+doc")
    depends_on("py-rst2pdf", when="+doc")
    depends_on("py-sphinx@5.3.0", when="+doc")
    depends_on("py-sphinx-rtd-theme", when="+doc")
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
        args = []

        args.append('-DBUILD_SHARED_LIBS:BOOL=ON')  # Toujours en mode shared, pour le scripting
        args.append('-DPRODUCTION:BOOL=ON')         # On installe => mode production pour les scripts fixant l'environnement python d'execution
        if self.spec.satisfies('%intel'):
            args.append('-DCMAKE_CXX_FLAGS="-std=c++11"')

        args.append(self.define_from_variant('DKOC', 'dkoc'))
        args.append(self.define_from_variant('MDLPARSER', 'mdlparser'))
        args.append(self.define_from_variant('MESHGEMS', 'meshgems'))
        args.append(self.define_from_variant('SEPA3D', 'sepa3d'))
        args.append(self.define_from_variant('SMOOTH3D', 'smooth3d'))
        args.append(self.define_from_variant('TRITON', 'triton2'))
        args.append(self.define_from_variant('PYTHONADDON', 'pythonaddon'))
        args.append(self.define_from_variant('WITH_DOC', 'doc'))

        args.append(self.define('T_INTERNAL_EXTENSION', 'not_defined'))
        args.append(self.define('ERD_INTERNAL_EXTENSION', 'not_defined'))
        args.append(self.define('USER_TEAM', 'not_defined'))
        args.append(self.define('DOXYGEN_PATH', 'not_defined'))
        args.append(self.define('DKOC_LICENCE', 'unavailable'))
        args.append(self.define('URL_WIKI', 'url_wiki'))
        args.append(self.define('URL_TUTORIAL', 'url_tuto'))
        args.append(self.define('URL_QUALIF', 'url_doc_qualif'))

        args.append('-DBUILD_MAGIX3D:BOOL=ON')
        args.append('-DBUILD_MAGIX3DBATCH:BOOL=OFF')

        if ('+doc' in self.spec.variants):
            args.append('-DSPHINX_WARNINGS_AS_ERRORS=OFF')

        if self.spec['python'].version < Version('3'):
            args.append('-DUSE_PYTHON_3:BOOL=OFF')
        else:
            args.append('-DUSE_PYTHON_3:BOOL=ON')

        # only py-numpy py-matplotlib py-scipy are necessary
        # the rest are here because we are not in an environment
        if "+pythonaddon" in self.spec:
            python_version = self.spec['python'].version.up_to(2)
            py_depends = ['py-numpy', 'py-matplotlib', 'py-scipy',
                          'py-cycler', 'py-kiwisolver',
                          'py-pillow', 'py-pyparsing', 'py-python-dateutil',
                          'py-pytz', 'py-setuptools', 'py-setuptools-scm',
                          'py-six']
            python_path = []
            for py_dep in py_depends:
                python_path.append(os.path.join(self.spec[py_dep].prefix, 'lib',
                                                'python' + str(python_version),
                                                'site-packages'))
            args.append('-DADDPYTHONPACKAGES='+':'.join(python_path)+':')

        return args
