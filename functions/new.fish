function new --description 'creates new cpp project'
    echo Creating new C++ project $argv
    mkdir $argv
    cp ~/.new/main.cpp $argv
    touch $argv/input.in
    nano $argv/input.in
    cp ~/.new/Makefile $argv
    cd $argv
end
