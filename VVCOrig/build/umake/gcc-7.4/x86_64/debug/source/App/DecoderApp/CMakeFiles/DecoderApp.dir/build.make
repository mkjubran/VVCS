# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
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
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/mjubran/HMStitching/VVCS/VVCOrig

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/mjubran/HMStitching/VVCS/VVCOrig/build/umake/gcc-7.4/x86_64/debug

# Include any dependencies generated for this target.
include source/App/DecoderApp/CMakeFiles/DecoderApp.dir/depend.make

# Include the progress variables for this target.
include source/App/DecoderApp/CMakeFiles/DecoderApp.dir/progress.make

# Include the compile flags for this target's objects.
include source/App/DecoderApp/CMakeFiles/DecoderApp.dir/flags.make

source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecApp.cpp.o: source/App/DecoderApp/CMakeFiles/DecoderApp.dir/flags.make
source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecApp.cpp.o: ../../../../../source/App/DecoderApp/DecApp.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/mjubran/HMStitching/VVCS/VVCOrig/build/umake/gcc-7.4/x86_64/debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecApp.cpp.o"
	cd /home/mjubran/HMStitching/VVCS/VVCOrig/build/umake/gcc-7.4/x86_64/debug/source/App/DecoderApp && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/DecoderApp.dir/DecApp.cpp.o -c /home/mjubran/HMStitching/VVCS/VVCOrig/source/App/DecoderApp/DecApp.cpp

source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecApp.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/DecoderApp.dir/DecApp.cpp.i"
	cd /home/mjubran/HMStitching/VVCS/VVCOrig/build/umake/gcc-7.4/x86_64/debug/source/App/DecoderApp && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/mjubran/HMStitching/VVCS/VVCOrig/source/App/DecoderApp/DecApp.cpp > CMakeFiles/DecoderApp.dir/DecApp.cpp.i

source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecApp.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/DecoderApp.dir/DecApp.cpp.s"
	cd /home/mjubran/HMStitching/VVCS/VVCOrig/build/umake/gcc-7.4/x86_64/debug/source/App/DecoderApp && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/mjubran/HMStitching/VVCS/VVCOrig/source/App/DecoderApp/DecApp.cpp -o CMakeFiles/DecoderApp.dir/DecApp.cpp.s

source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecApp.cpp.o.requires:

.PHONY : source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecApp.cpp.o.requires

source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecApp.cpp.o.provides: source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecApp.cpp.o.requires
	$(MAKE) -f source/App/DecoderApp/CMakeFiles/DecoderApp.dir/build.make source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecApp.cpp.o.provides.build
.PHONY : source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecApp.cpp.o.provides

source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecApp.cpp.o.provides.build: source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecApp.cpp.o


source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecAppCfg.cpp.o: source/App/DecoderApp/CMakeFiles/DecoderApp.dir/flags.make
source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecAppCfg.cpp.o: ../../../../../source/App/DecoderApp/DecAppCfg.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/mjubran/HMStitching/VVCS/VVCOrig/build/umake/gcc-7.4/x86_64/debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecAppCfg.cpp.o"
	cd /home/mjubran/HMStitching/VVCS/VVCOrig/build/umake/gcc-7.4/x86_64/debug/source/App/DecoderApp && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/DecoderApp.dir/DecAppCfg.cpp.o -c /home/mjubran/HMStitching/VVCS/VVCOrig/source/App/DecoderApp/DecAppCfg.cpp

source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecAppCfg.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/DecoderApp.dir/DecAppCfg.cpp.i"
	cd /home/mjubran/HMStitching/VVCS/VVCOrig/build/umake/gcc-7.4/x86_64/debug/source/App/DecoderApp && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/mjubran/HMStitching/VVCS/VVCOrig/source/App/DecoderApp/DecAppCfg.cpp > CMakeFiles/DecoderApp.dir/DecAppCfg.cpp.i

source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecAppCfg.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/DecoderApp.dir/DecAppCfg.cpp.s"
	cd /home/mjubran/HMStitching/VVCS/VVCOrig/build/umake/gcc-7.4/x86_64/debug/source/App/DecoderApp && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/mjubran/HMStitching/VVCS/VVCOrig/source/App/DecoderApp/DecAppCfg.cpp -o CMakeFiles/DecoderApp.dir/DecAppCfg.cpp.s

source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecAppCfg.cpp.o.requires:

.PHONY : source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecAppCfg.cpp.o.requires

source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecAppCfg.cpp.o.provides: source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecAppCfg.cpp.o.requires
	$(MAKE) -f source/App/DecoderApp/CMakeFiles/DecoderApp.dir/build.make source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecAppCfg.cpp.o.provides.build
.PHONY : source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecAppCfg.cpp.o.provides

source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecAppCfg.cpp.o.provides.build: source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecAppCfg.cpp.o


source/App/DecoderApp/CMakeFiles/DecoderApp.dir/decmain.cpp.o: source/App/DecoderApp/CMakeFiles/DecoderApp.dir/flags.make
source/App/DecoderApp/CMakeFiles/DecoderApp.dir/decmain.cpp.o: ../../../../../source/App/DecoderApp/decmain.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/mjubran/HMStitching/VVCS/VVCOrig/build/umake/gcc-7.4/x86_64/debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object source/App/DecoderApp/CMakeFiles/DecoderApp.dir/decmain.cpp.o"
	cd /home/mjubran/HMStitching/VVCS/VVCOrig/build/umake/gcc-7.4/x86_64/debug/source/App/DecoderApp && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/DecoderApp.dir/decmain.cpp.o -c /home/mjubran/HMStitching/VVCS/VVCOrig/source/App/DecoderApp/decmain.cpp

source/App/DecoderApp/CMakeFiles/DecoderApp.dir/decmain.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/DecoderApp.dir/decmain.cpp.i"
	cd /home/mjubran/HMStitching/VVCS/VVCOrig/build/umake/gcc-7.4/x86_64/debug/source/App/DecoderApp && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/mjubran/HMStitching/VVCS/VVCOrig/source/App/DecoderApp/decmain.cpp > CMakeFiles/DecoderApp.dir/decmain.cpp.i

source/App/DecoderApp/CMakeFiles/DecoderApp.dir/decmain.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/DecoderApp.dir/decmain.cpp.s"
	cd /home/mjubran/HMStitching/VVCS/VVCOrig/build/umake/gcc-7.4/x86_64/debug/source/App/DecoderApp && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/mjubran/HMStitching/VVCS/VVCOrig/source/App/DecoderApp/decmain.cpp -o CMakeFiles/DecoderApp.dir/decmain.cpp.s

source/App/DecoderApp/CMakeFiles/DecoderApp.dir/decmain.cpp.o.requires:

.PHONY : source/App/DecoderApp/CMakeFiles/DecoderApp.dir/decmain.cpp.o.requires

source/App/DecoderApp/CMakeFiles/DecoderApp.dir/decmain.cpp.o.provides: source/App/DecoderApp/CMakeFiles/DecoderApp.dir/decmain.cpp.o.requires
	$(MAKE) -f source/App/DecoderApp/CMakeFiles/DecoderApp.dir/build.make source/App/DecoderApp/CMakeFiles/DecoderApp.dir/decmain.cpp.o.provides.build
.PHONY : source/App/DecoderApp/CMakeFiles/DecoderApp.dir/decmain.cpp.o.provides

source/App/DecoderApp/CMakeFiles/DecoderApp.dir/decmain.cpp.o.provides.build: source/App/DecoderApp/CMakeFiles/DecoderApp.dir/decmain.cpp.o


# Object files for target DecoderApp
DecoderApp_OBJECTS = \
"CMakeFiles/DecoderApp.dir/DecApp.cpp.o" \
"CMakeFiles/DecoderApp.dir/DecAppCfg.cpp.o" \
"CMakeFiles/DecoderApp.dir/decmain.cpp.o"

# External object files for target DecoderApp
DecoderApp_EXTERNAL_OBJECTS =

../../../../../bin/umake/gcc-7.4/x86_64/debug/DecoderApp: source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecApp.cpp.o
../../../../../bin/umake/gcc-7.4/x86_64/debug/DecoderApp: source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecAppCfg.cpp.o
../../../../../bin/umake/gcc-7.4/x86_64/debug/DecoderApp: source/App/DecoderApp/CMakeFiles/DecoderApp.dir/decmain.cpp.o
../../../../../bin/umake/gcc-7.4/x86_64/debug/DecoderApp: source/App/DecoderApp/CMakeFiles/DecoderApp.dir/build.make
../../../../../bin/umake/gcc-7.4/x86_64/debug/DecoderApp: ../../../../../lib/umake/gcc-7.4/x86_64/debug/libCommonLib.a
../../../../../bin/umake/gcc-7.4/x86_64/debug/DecoderApp: ../../../../../lib/umake/gcc-7.4/x86_64/debug/libDecoderLib.a
../../../../../bin/umake/gcc-7.4/x86_64/debug/DecoderApp: ../../../../../lib/umake/gcc-7.4/x86_64/debug/libUtilities.a
../../../../../bin/umake/gcc-7.4/x86_64/debug/DecoderApp: ../../../../../lib/umake/gcc-7.4/x86_64/debug/libCommonLib.a
../../../../../bin/umake/gcc-7.4/x86_64/debug/DecoderApp: source/App/DecoderApp/CMakeFiles/DecoderApp.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/mjubran/HMStitching/VVCS/VVCOrig/build/umake/gcc-7.4/x86_64/debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX executable ../../../../../../../../bin/umake/gcc-7.4/x86_64/debug/DecoderApp"
	cd /home/mjubran/HMStitching/VVCS/VVCOrig/build/umake/gcc-7.4/x86_64/debug/source/App/DecoderApp && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/DecoderApp.dir/link.txt --verbose=$(VERBOSE)
	cd /home/mjubran/HMStitching/VVCS/VVCOrig/build/umake/gcc-7.4/x86_64/debug/source/App/DecoderApp && /usr/bin/cmake -E copy /home/mjubran/HMStitching/VVCS/VVCOrig/bin/umake/gcc-7.4/x86_64/debug/DecoderApp    /home/mjubran/HMStitching/VVCS/VVCOrig/bin/DecoderAppStaticd   

# Rule to build all files generated by this target.
source/App/DecoderApp/CMakeFiles/DecoderApp.dir/build: ../../../../../bin/umake/gcc-7.4/x86_64/debug/DecoderApp

.PHONY : source/App/DecoderApp/CMakeFiles/DecoderApp.dir/build

source/App/DecoderApp/CMakeFiles/DecoderApp.dir/requires: source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecApp.cpp.o.requires
source/App/DecoderApp/CMakeFiles/DecoderApp.dir/requires: source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DecAppCfg.cpp.o.requires
source/App/DecoderApp/CMakeFiles/DecoderApp.dir/requires: source/App/DecoderApp/CMakeFiles/DecoderApp.dir/decmain.cpp.o.requires

.PHONY : source/App/DecoderApp/CMakeFiles/DecoderApp.dir/requires

source/App/DecoderApp/CMakeFiles/DecoderApp.dir/clean:
	cd /home/mjubran/HMStitching/VVCS/VVCOrig/build/umake/gcc-7.4/x86_64/debug/source/App/DecoderApp && $(CMAKE_COMMAND) -P CMakeFiles/DecoderApp.dir/cmake_clean.cmake
.PHONY : source/App/DecoderApp/CMakeFiles/DecoderApp.dir/clean

source/App/DecoderApp/CMakeFiles/DecoderApp.dir/depend:
	cd /home/mjubran/HMStitching/VVCS/VVCOrig/build/umake/gcc-7.4/x86_64/debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/mjubran/HMStitching/VVCS/VVCOrig /home/mjubran/HMStitching/VVCS/VVCOrig/source/App/DecoderApp /home/mjubran/HMStitching/VVCS/VVCOrig/build/umake/gcc-7.4/x86_64/debug /home/mjubran/HMStitching/VVCS/VVCOrig/build/umake/gcc-7.4/x86_64/debug/source/App/DecoderApp /home/mjubran/HMStitching/VVCS/VVCOrig/build/umake/gcc-7.4/x86_64/debug/source/App/DecoderApp/CMakeFiles/DecoderApp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : source/App/DecoderApp/CMakeFiles/DecoderApp.dir/depend

