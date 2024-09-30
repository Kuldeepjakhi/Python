#!/usr/bin/python3
def test(pram):
	pram.append('50')

pram2 = ['10','20','30','40']
test(pram2)

print(pram2)


# though the test function append function scope is local but but both the varible poiting to same 
# list so pram2 output will be 10','20','30','40', '50'