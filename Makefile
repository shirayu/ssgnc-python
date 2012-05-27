_ssgnc.so: ssgnc_wrap.o
	gcc -shared ssgnc_wrap.o /usr/local/lib/libssgnc.a  -o _ssgnc.so  -lstdc++

ssgnc_wrap.o: ssgnc_wrap.cxx
	gcc -fPIC -c ssgnc_wrap.cxx -I/usr/include/python2.6  -lstdc++

ssgnc_wrap.cxx: ssgnc.i
	swig -Wall -c++ -python -shadow -c++ -I/usr/local/include ssgnc.i

test: _ssgnc.so
	python ./test__ssgnc.py
all:
clean:
	rm ssgnc_wrap.o _ssgnc.so ssgnc_wrap.cxx ssgnc.py*
