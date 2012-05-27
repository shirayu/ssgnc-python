#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""

from distutils.core import setup, Extension

ext_module = Extension('_ssgnc',
                       sources=[ 'ssgnc_wrap.cxx'],
                       libraries=["stdc++"],
                       extra_objects = ['/usr/local/lib/libssgnc.a'],
                       include_dirs = ['/usr/local/include'],
                       )

#ext_module = Extension('_ssgnc',
#                       sources=[ 'ssgnc.i'],
#                       libraries=["stdc++"],
#                       extra_objects = ['/usr/local/lib/libssgnc.a'],
#                       include_dirs = ['/usr/local/include'],
#                       swig_opts=["-Wall", "-c++", "-shadow", "-I/usr/local/include"],
#                       )


setup(name='ssgnc-python',
      version='0.1',
      author='Yuta Hayashibe',
#      author_email='',
      ext_modules=[ext_module],
      py_modules=['ssgnc'],
      )

