#include "Person.hh"

Person::Person(): 
    fPersonID(0), fName(""), fEmail(""), fAge(0)
{}

Person::Person(int PersonID,string Name,string Email,int Age):
    fPersonID(PersonID), fName(Name), fEmail(Email), fAge(Age) {

}

