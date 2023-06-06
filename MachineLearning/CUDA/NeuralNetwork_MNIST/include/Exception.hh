#pragma once

#include <exception>
#include <iostream>

class Exception: std::exception {
    public:
        Exception(const char* exception_message):
            exception_message(exception_message)
            {}

        virtual const char* what() const throw()
        {
            return exception_message;
        }

        static void throwIfDeviceErrorOccurred(const char* exception_message){
            cudaError_t error = cudaGetLastError();
            if (error != cudaSuccess) {
                std::cerr << error << ": " << exception_message;
                throw Exception(exception_message);
            }            
        }
    
    private:
        const char* exception_message;
};