<img src="https://cdn.rawgit.com/oh-my-fish/oh-my-fish/e4f1c2e0219a17e2c748b824004c8d0b38055c16/docs/logo.svg" align="left" width="144px" height="144px"/>

#### new-cpp
> A plugin for [Oh My Fish][omf-link]. New cpp project.

[![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square)](/LICENSE)
[![Fish Shell Version](https://img.shields.io/badge/fish-v2.2.0-007EC7.svg?style=flat-square)](https://fishshell.com)
[![Oh My Fish Framework](https://img.shields.io/badge/Oh%20My%20Fish-Framework-007EC7.svg?style=flat-square)](https://www.github.com/oh-my-fish/oh-my-fish)

<br/>

[![asciicast](https://asciinema.org/a/241025.png)](https://asciinema.org/a/241025)

## Install

```fish
$ omf install https://github.com/pniedzwiedzinski/plugin-new-cpp
```


## Usage

```fish
new-cpp <project_name>

# nano window will be open to enter test input
```

Project folder structure
```fish
Makefile
input.in   # test input data
main.cpp   # main file
output     # binary, you need to compile first
```

To compile and run program
```fish
make

# or step by step

make output     # compile main.cpp to output file
make run        # run binary with test input data
```

To remove binaries
```fish
make clean
```

## Customization

You can add in `~/.new/header` content of header for `main.cpp` file.

# License

[MIT][mit] © [Patryk Niedźwiedziński][author] et [al][contributors]


[mit]:            https://opensource.org/licenses/MIT
[author]:         https://github.com/pniedzwiedzinski
[contributors]:   https://github.com/pniedzwiedzinski/plugin-new-cpp/graphs/contributors
[omf-link]:       https://www.github.com/oh-my-fish/oh-my-fish

[license-badge]:  https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square
