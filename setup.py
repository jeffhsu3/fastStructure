
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy
import sys
import glob

name = 'faststructure'
version = '1.1'

# setup bed parser

cmdclass = {}
ext_modules = []
includes = []

includes.append(numpy.get_include())

ext_modules += [
        Extension("faststructure.vars.admixprop",
            sources=["faststructure/vars/admixprop.pyx", 
                     "faststructure/vars/C_admixprop.c"],
            include_dirs=includes),
        Extension("faststructure.vars.allelefreq",
            sources=["faststructure/vars/allelefreq.pyx",
                     "faststructure/vars/C_allelefreq.c"],
            libraries=["gsl", "gslcblas"],
            extra_compile_args=["-O3"],
            include_dirs=includes),
        Extension("faststructure.marglikehood",
            sources=["faststructure/vars/marglikehood.pyx", 
                     "faststructure/vars/C_marglikehood.c"],
            include_dirs=includes),
        Extension("faststructure.parse_bed", 
            ["faststructure/parse_bed.pyx"],
            include_dirs = includes,),
        Extension("faststructure.parse_str",
            ["faststructure/parse_str.pyx"],
            include_dirs=includes,),
        Extension("faststructure.fastStructure",
            ["faststructure/fastStructure.pyx"],
            include_dirs=includes),
        Extension("faststructure.vars.utils",
            ["faststructure/vars/utils.pyx"],
            include_dirs=includes,),
        ]

cmdclass.update({'build_ext': build_ext})

metadata = {
        'name': name,
        'version': version,
        'cmdclass': cmdclass,
        'ext_modules': ext_modules,
        'scripts': glob.glob('scripts/*.py'),
        'description': 'faststructure',
        'author': 'Anil Raj',
        'packages': ['faststructure',
            'faststructure.vars'],
        }
        

if __name__ == '__main__':
    dist = setup(**metadata)
