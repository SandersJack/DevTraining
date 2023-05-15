DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DIR=$(dirname "$(dirname "${DIR}")")

export ORBITSOURCE="${DIR}/Orbits"
alias ORBITS="${ORBITSOURCE}/build/OrbitSim"

alias make_clean="rm build/* -r"

alias make="cmake -Bbuild/ -S.; cd build; make; cd .."


source /home/jack/Code/root/bin/thisroot.sh