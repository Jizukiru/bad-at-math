This README serves a list of the programs in the repo and a short description of them. They are not, by default, meant to work/communicate with other programs in the repo. Kinks and intricacies caused by, frankly, lack of skill will also be listed here.

Polynomials.py : Old Python program initially meant to solve quadratic equations; now also able to do polynomial factorization of polynomials of the n-th degree if provided with a root.
My programming proved insufficient to deal with non-integer factors of x when solving quadratics. Thus the program forces integer values using a try-except block and recursively calling the calculator function. The calculator also only produces results in the Real domain.
