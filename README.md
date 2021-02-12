# Simpson-Integration
Performing approximation to a function by quadratic interpolation (order 2 curve).
Through all 3 points, the function is approximated using a Class 2 polynomial and the integral is calculated, using the Lagrange method.
Below each approximation are 3 points and 2 segments, so n must be even.


# How it works? 
First of all we need to calculate N = how many parts we can divide the area imprisoned in the area we have determined (boundary) <br/>
then we will use the Trapeziodal Method to calculate the area between our boundary
we will use Lagrange method: <br/>

![Simpson and Lagrange method](https://i.ibb.co/d24hwmF/simpson.jpg)


next we will calculate the Error precentage:<br/>
![Simpson and Lagrange method](https://i.ibb.co/BC03LG4/error-precentage.jpg)


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install sympy and Texttable.

```bash
pip install sympy
```

```bash
pip install Texttable
```


## Contributing
I built the algorithm in the form of object-oriented programming, in order to simplify the idea behind it. <br/>
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
