# new-cpp

Create new cpp project with ease from terminal. And run it with `make`.

[![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square)](/LICENSE)
![Version: v2.0](https://img.shields.io/badge/version-v2.0-blue)

<br/>

[![asciicast](https://asciinema.org/a/241025.png)](https://asciinema.org/a/241025)

## Install

```bash
$ omf install https://github.com/pniedzwiedzinski/plugin-new-cpp
```

## Usage

```bash
new-cpp <project_name>

# nano window will be open to enter test input
```

Project folder structure

```bash
Makefile
input.in   # test input data
main.cpp   # main file
output     # binary, you need to compile first
```

To compile and run program

```bash
make

# or step by step

make output     # compile main.cpp to output file
make run        # run binary with test input data
```

To remove binaries

```bash
make clean
```

## Customization

You can add in `~/.new/header` content of header for `main.cpp` file.

# License

[MIT][mit] © [Patryk Niedźwiedziński][author] et [al][contributors]

[mit]: https://opensource.org/licenses/MIT
[author]: https://github.com/pniedzwiedzinski
[contributors]: https://github.com/pniedzwiedzinski/plugin-new-cpp/graphs/contributors
[license-badge]: https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square
