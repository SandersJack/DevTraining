# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/jack/Code/DevTraining/Apps/Orbits

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/jack/Code/DevTraining/Apps/Orbits

# Include any dependencies generated for this target.
include Planets/Earth/CMakeFiles/EARTH.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include Planets/Earth/CMakeFiles/EARTH.dir/compiler_depend.make

# Include the progress variables for this target.
include Planets/Earth/CMakeFiles/EARTH.dir/progress.make

# Include the compile flags for this target's objects.
include Planets/Earth/CMakeFiles/EARTH.dir/flags.make

Planets/Earth/CMakeFiles/EARTH.dir/src/EarthParameters.cc.o: Planets/Earth/CMakeFiles/EARTH.dir/flags.make
Planets/Earth/CMakeFiles/EARTH.dir/src/EarthParameters.cc.o: Planets/Earth/src/EarthParameters.cc
Planets/Earth/CMakeFiles/EARTH.dir/src/EarthParameters.cc.o: Planets/Earth/CMakeFiles/EARTH.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jack/Code/DevTraining/Apps/Orbits/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object Planets/Earth/CMakeFiles/EARTH.dir/src/EarthParameters.cc.o"
	cd /home/jack/Code/DevTraining/Apps/Orbits/Planets/Earth && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT Planets/Earth/CMakeFiles/EARTH.dir/src/EarthParameters.cc.o -MF CMakeFiles/EARTH.dir/src/EarthParameters.cc.o.d -o CMakeFiles/EARTH.dir/src/EarthParameters.cc.o -c /home/jack/Code/DevTraining/Apps/Orbits/Planets/Earth/src/EarthParameters.cc

Planets/Earth/CMakeFiles/EARTH.dir/src/EarthParameters.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/EARTH.dir/src/EarthParameters.cc.i"
	cd /home/jack/Code/DevTraining/Apps/Orbits/Planets/Earth && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jack/Code/DevTraining/Apps/Orbits/Planets/Earth/src/EarthParameters.cc > CMakeFiles/EARTH.dir/src/EarthParameters.cc.i

Planets/Earth/CMakeFiles/EARTH.dir/src/EarthParameters.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/EARTH.dir/src/EarthParameters.cc.s"
	cd /home/jack/Code/DevTraining/Apps/Orbits/Planets/Earth && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jack/Code/DevTraining/Apps/Orbits/Planets/Earth/src/EarthParameters.cc -o CMakeFiles/EARTH.dir/src/EarthParameters.cc.s

# Object files for target EARTH
EARTH_OBJECTS = \
"CMakeFiles/EARTH.dir/src/EarthParameters.cc.o"

# External object files for target EARTH
EARTH_EXTERNAL_OBJECTS =

Planets/Earth/libEARTH.a: Planets/Earth/CMakeFiles/EARTH.dir/src/EarthParameters.cc.o
Planets/Earth/libEARTH.a: Planets/Earth/CMakeFiles/EARTH.dir/build.make
Planets/Earth/libEARTH.a: Planets/Earth/CMakeFiles/EARTH.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/jack/Code/DevTraining/Apps/Orbits/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX static library libEARTH.a"
	cd /home/jack/Code/DevTraining/Apps/Orbits/Planets/Earth && $(CMAKE_COMMAND) -P CMakeFiles/EARTH.dir/cmake_clean_target.cmake
	cd /home/jack/Code/DevTraining/Apps/Orbits/Planets/Earth && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/EARTH.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
Planets/Earth/CMakeFiles/EARTH.dir/build: Planets/Earth/libEARTH.a
.PHONY : Planets/Earth/CMakeFiles/EARTH.dir/build

Planets/Earth/CMakeFiles/EARTH.dir/clean:
	cd /home/jack/Code/DevTraining/Apps/Orbits/Planets/Earth && $(CMAKE_COMMAND) -P CMakeFiles/EARTH.dir/cmake_clean.cmake
.PHONY : Planets/Earth/CMakeFiles/EARTH.dir/clean

Planets/Earth/CMakeFiles/EARTH.dir/depend:
	cd /home/jack/Code/DevTraining/Apps/Orbits && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/jack/Code/DevTraining/Apps/Orbits /home/jack/Code/DevTraining/Apps/Orbits/Planets/Earth /home/jack/Code/DevTraining/Apps/Orbits /home/jack/Code/DevTraining/Apps/Orbits/Planets/Earth /home/jack/Code/DevTraining/Apps/Orbits/Planets/Earth/CMakeFiles/EARTH.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : Planets/Earth/CMakeFiles/EARTH.dir/depend

