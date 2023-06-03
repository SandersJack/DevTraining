alias make_clean="rm build/* -r"

alias make="cmake -Bbuild/ -S.; cd build; make; cd .."
