DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DIR=$(dirname "$(dirname "${DIR}")")

export CPPSOURCE="${DIR}/CPPLearn"
alias CPPSQL="${CPPSOURCE}/build/CPPSQL"

alias make_clean="rm build/* -r"

alias make="cmake -Bbuild/ -S.; cd build; make; cd .."
