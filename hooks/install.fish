if not test -d ~/.new
  mkdir ~/.new
done  

if not test -e ~/.new/Makefile
  cp Makefile.new ~/.new/Makefile
done

if not test -e ~/.new/main.cpp
  cp main.cpp.new ~/.new/main.cpp
done
