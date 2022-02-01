CC=gcc
CXX=g++
CXXFLAGS=-std=c++11 -Wall -pedantic -w
SHELL=/bin/bash

all: build

build:
	#cp config/trace.config .
	${CXX} ${CXXFLAGS} -o adm.x adm.cpp

test:
	./adm.x < scores

clean:
	rm -f *.o *.x core.* *.result

%.x : %.ctest_stack.x
	$(CC) -o $@ $<
%.x : %.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<