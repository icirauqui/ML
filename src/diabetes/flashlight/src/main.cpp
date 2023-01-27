#include <iostream>


#include <arrayfire.h>
#include "flashlight/fl/flashlight.h"


af::array StandardScaler(af::array A, int axis = 0, bool inplace = false) {
  af::array mean = af::mean(A, axis);
  af::array std = af::stdev(A, axis);

  af::dim4 dims = A.dims();
  af::array sc = A;

  for (int i = 0; i < dims[axis]; i++) {
    sc(i, af::span) = sc(i, af::span) - mean;
    sc(i, af::span) = sc(i, af::span) / std;
  }

  if (inplace) {
    A = sc;
  }

  return sc;
}



int main() {
  std::cout << "Hello, World!" << std::endl << std::endl;

  float data[] = {1,  2,   3,   4,
                  2,  6,  12,  20,
                  4, 18,  48, 100,
                  8, 54, 192, 500};

  af::array A(4, 4, data);
  af::print("A", A);

  /*
  af::array mean = af::mean(A, 0);
  af::print("mean", mean);

  af::array std = af::stdev(A, 0);
  af::print("std", std);

  // Dimensions
  af::dim4 dims = A.dims();
  std::cout << std::endl 
            << "Dimensions: " 
            << dims[0] << " " 
            << dims[1] << " " 
            << dims[2] << " " 
            << dims[3] 
            << std::endl << std::endl;

  // Substract mean to each row in A
  af::array scaled = A;
  for (int i = 0; i < dims[0]; i++) {
    scaled(i, af::span) = A(i, af::span) - mean;
  }
  af::print("scaled", scaled);

  // Divice each row in A by std element-wise
  af::array scaled2 = scaled;
  for (int i = 0; i < dims[0]; i++) {
    scaled2(i, af::span) = scaled(i, af::span) / std;
  }
  af::print("scaled2", scaled2);


  af::print("A", A);
  */


  af::array sc = StandardScaler(A);
  af::print("sc", sc);
  af::print("A", A);
  A = StandardScaler(A);
  af::print("sc", sc);
  af::print("A", A);




  return 0;
}
