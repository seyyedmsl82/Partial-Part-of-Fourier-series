# Fourier Series Approximation for Sawtooth Wave

This code implements a Fourier series approximation for a sawtooth wave. It calculates the Fourier coefficients and uses them to approximate the original function using a specified number of terms.

## Prerequisites

The code requires the following dependencies:

- Python 3.x
- NumPy
- Matplotlib
- SciPy

You can install the dependencies using the following command:

```shell
pip install numpy matplotlib scipy
```

## Usage

To run the code, follow these steps:

1. Save the code in a Python file (e.g., `fourier_series.py`).

2. Open a terminal or command prompt and navigate to the directory containing the Python file.

3. Run the code using the following command:

```shell
python fourier_series.py
```

4. The code will generate a series of plots showing the Fourier series approximation for the sawtooth wave with different numbers of terms. Each plot displays the original function (sawtooth wave) and the Fourier approximation.

5. Close the plot window to move to the next approximation or press Ctrl+C to stop the program.

## Customization

You can modify the code to customize the sawtooth wave function, the range of approximation, and the number of terms. Here are the key parameters you can change:

- `li`: Start of the interval for approximation.
- `lf`: End of the interval for approximation.
- `function`: The original sawtooth wave function. Modify the `function(x)` implementation to define a different function.
- `n`: Number of terms to use for the Fourier series approximation. Modify the range in the for loop to specify the desired number of terms.

You can experiment with different parameters to observe the effect on the Fourier series approximation.

## License

This code is provided under the MIT License. Please refer to the LICENSE file for more information.

## Acknowledgments

This code is inspired by the concept of Fourier series and its approximation. It uses the NumPy, Matplotlib, and SciPy libraries to perform the calculations and generate the plots.

## References

- [Wikipedia: Fourier Series](https://en.wikipedia.org/wiki/Fourier_series)
