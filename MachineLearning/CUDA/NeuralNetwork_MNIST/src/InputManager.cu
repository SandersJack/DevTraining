#include "InputManager.hh"

#include <fstream>
#include <iostream>

InputManager::InputManager(){
    
}

InputManager::~InputManager(){}

void InputManager::InitTraningData(){

    std::ifstream file("dataset/train-images-idx3-ubyte", std::ios::binary);
    std::ifstream file_targets("dataset/train-labels-idx1-ubyte", std::ios::binary);

    if (file.is_open())
    {
        int magic_number=0;
        int number_of_images=0;
        int n_rows=0;
        int n_cols=0;
        int magic_number_target=0;
        int number_of_images_target=0;
        //
        file.read((char*)&magic_number,sizeof(magic_number)); 
        magic_number= reverseInt(magic_number);
        file_targets.read((char*)&magic_number_target,sizeof(magic_number_target)); 
        magic_number_target= reverseInt(magic_number_target);
        //
        file.read((char*)&number_of_images,sizeof(number_of_images));
        number_of_images= reverseInt(number_of_images);
        file_targets.read((char*)&number_of_images_target,sizeof(number_of_images_target));
        number_of_images_target= reverseInt(number_of_images_target);
        //
        file.read((char*)&n_rows,sizeof(n_rows));
        n_rows= reverseInt(n_rows);
        file.read((char*)&n_cols,sizeof(n_cols));
        n_cols= reverseInt(n_cols);
        std::cout << "[InputManager] Size of Images: " << n_rows << "x" << n_cols <<std::endl;
        for(int i=0;i<number_of_images;++i)
        {
            fTraingData.push_back(Matrix(Shape(n_rows,n_cols)));
            fTraingData[i].allocateMemory();

            fTargets.push_back(Matrix(Shape(1,10)));
            fTargets[i].allocateMemory();
            for (int t=0; t<10;t++){
                fTargets[i][t] = 0;
            }

            unsigned char temp_tar=0;
            file_targets.read((char*)&temp_tar,sizeof(temp_tar));
            fTargets[i][(int)temp_tar] = 1;

            for(int r=0;r<n_rows;++r)
            {
                for(int c=0;c<n_cols;++c)
                {
                    unsigned char temp=0;
                    file.read((char*)&temp,sizeof(temp));
                    fTraingData[i][r*fTraingData[i].shape.x + c] = (int)temp;
                }
            }
        }
    }
    std::cout << "[InputManager] Training Data Loaded" << std::endl;
}


int InputManager::reverseInt(int i) {
    // Reverses the int
    unsigned char c1, c2, c3, c4;

    c1 = i & 255;
    c2 = (i >> 8) & 255;
    c3 = (i >> 16) & 255;
    c4 = (i >> 24) & 255;

    return ((int)c1 << 24) + ((int)c2 << 16) + ((int)c3 << 8) + c4;
}