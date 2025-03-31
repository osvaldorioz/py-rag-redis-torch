cmake_minimum_required(VERSION 3.12)
project(RAGRedis)

# sudo apt-get install libhiredis-dev
# git clone https://github.com/sewenew/redis-plus-plus.git
# cd redis-plus-plus
# mkdir build && cd build
# cmake .. -DCMAKE_PREFIX_PATH=$(python -m pybind11 --cmakedir)
# Estándar C++17 requerido por redis-plus-plus
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Python3 COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 REQUIRED)

# Buscar hiredis y redis-plus-plus
find_library(HIREDIS_LIBRARY NAMES hiredis HINTS /usr/lib /usr/local/lib)
find_library(REDIS_PLUS_PLUS_LIBRARY NAMES redis++ HINTS /usr/local/lib)

if (NOT HIREDIS_LIBRARY)
    message(FATAL_ERROR "No se encontró la biblioteca hiredis")
endif()
if (NOT REDIS_PLUS_PLUS_LIBRARY)
    message(FATAL_ERROR "No se encontró la biblioteca redis++")
endif()

add_library(rag_module MODULE bindings.cpp)
target_include_directories(rag_module PRIVATE /usr/local/include) # Para redis-plus-plus
target_link_libraries(rag_module PRIVATE 
    pybind11::module 
    ${Python3.12_LIBRARIES}
    ${HIREDIS_LIBRARY}
    ${REDIS_PLUS_PLUS_LIBRARY}
)
set_target_properties(rag_module PROPERTIES PREFIX "" SUFFIX ".so")