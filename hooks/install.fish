if not test -d ~/.new
  mkdir ~/.new
end

if not test -e ~/.new/Makefile
  cp ../Makefile.new ~/.new/Makefile
end

if not test -e ~/.new/main.cpp
  cp ../main.cpp.new ~/.new/main.cpp
end
