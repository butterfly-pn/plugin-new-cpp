if (cd ~/.new) do
  echo
else
  mkdir ~/.new
  cp Makefile.new ~/.new/Makefile
  cp main.cpp.new ~/.new/main.cpp
done
