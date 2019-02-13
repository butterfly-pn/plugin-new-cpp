mkdir ~/.new

echo "#include <iostream>

using namespace std;

int main()
{

  return 0;
}" > ~/.new/main.cpp

echo "
run: output input.in
	./output < input.in

output: main.cpp
	g++ main.cpp -o output

clear:
	rm output" > ~/.new/Makefile
