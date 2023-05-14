foreach(Planets ${PlanetsList})
  add_subdirectory(${Planets})
  target_link_libraries(OrbitSim ${detector})
endforeach()
