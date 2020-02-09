project(gst-tools C)
cmake_minimum_required(VERSION 2.8.11)


include(FindPkgConfig)
pkg_search_module(GSTREAMER gstreamer-1.0 REQUIRED)
pkg_search_module(AUDIORESOURCES audioresource REQUIRED)

set(CMAKE_AUTOMOC ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

add_executable(gst-launch-1.0 gst-launch.c)
add_executable(gst-inspect-1.0 gst-inspect.c)

set_property(TARGET gst-launch-1.0
  PROPERTY INCLUDE_DIRECTORIES "${GSTREAMER_INCLUDE_DIRS}" "${AUDIORESOURCES_INCLUDE_DIRS}")

set_property(TARGET gst-inspect-1.0
  PROPERTY INCLUDE_DIRECTORIES "${GSTREAMER_INCLUDE_DIRS}" )

add_definitions(-DSAILFISH)
add_definitions(-DGST_DISABLE_OPTION_PARSING )
add_definitions(-DGST_PACKAGE_ORIGIN=\"Sailfish\" )
add_definitions(-DGST_API_VERSION=\"1.0\" )

target_link_libraries(gst-launch-1.0 ${GSTREAMER_LDFLAGS} ${AUDIORESOURCES_LDFLAGS})
target_link_libraries(gst-inspect-1.0 ${GSTREAMER_LDFLAGS})

install(TARGETS gst-launch-1.0
RUNTIME DESTINATION bin)
install(TARGETS gst-inspect-1.0
RUNTIME DESTINATION bin)

