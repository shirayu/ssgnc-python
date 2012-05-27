SSGNC wrapper for python
==========================

ssgnc-python is a python wrapper module for SSGNC. Search System for Giga-scale N-gram Corpus.

Detailed information of SSGNC can be found at
http://code.google.com/p/ssgnc/

Install Dependencies
--------------------

You need to install SSGNC before build.
You have to "configure" with the following environment variables.

    CFLAGS="-fPIC -O3" CXXFLAGS="-fPIC -O3" ./configure
    make && sudo make install

To build ssgnc-python, run
--------------------
  (If you want to install, run)

    % python ./setup.py build
    % sudo python ./setup.py install


  (If you fail to make, please try to install SWIG and run)

    % make ssgnc_wrap.cxx


How to use?
--------------------

  See 'test__ssgnc.py' as a sample program.

License
--------------------

GPL version3
