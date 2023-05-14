file(REMOVE_RECURSE
  "libEarth-static.a"
  "libEarth-static.pdb"
)

# Per-language clean rules from dependency scanning.
foreach(lang CXX)
  include(CMakeFiles/Earth-static.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
