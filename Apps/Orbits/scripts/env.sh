DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DIR=$(dirname "$(dirname "${DIR}")")

export ORBITSOURCE="${DIR}/Orbits"
alias ORBITS="${ORBITSOURCE}/OrbitSim"