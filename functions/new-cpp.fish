function new-cpp --description 'creates new cpp project'
  if test "$argv" = "--help"
    echo "usage: new-cpp project_name

Create new C++ Project"
  else
    echo Creating new C++ project $argv
    mkdir $argv
    if test -e ~/.new/header
      cat ~/.new/header > $argv/main.cpp
      cat ~/.new/main.cpp >> $argv/main.cpp
    else
      cp ~/.new/main.cpp $argv
    end
    touch $argv/input.in
    nano $argv/input.in
    cp ~/.new/Makefile $argv
    cd $argv
  end
end
