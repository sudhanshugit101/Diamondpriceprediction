## Diamond Price Prediction.
### Project Description:
The goal of this project is to predict the price of a diamond based on its features. The dataset used for this project is the Diamonds dataset from Kaggle. The dataset contains 53940 rows and 11 columns. The dataset contains the following columns: carat, cut, color, clarity, depth, table, price, x, y, z. The dataset is a regression problem. The target variable is the price of the diamond.

### Technologies Used:
* Python
* Pandas
* Numpy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

### Features:
* carat: weight of the diamond (0.2--5.01)
* cut: quality of the cut (Fair, Good, Very Good, Premium, Ideal)
* color: diamond colour, from J (worst) to D (best)
* clarity: a measurement of how clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best))
* depth: total depth percentage = z / mean(x, y) = 2 * z / (x + y) (43--79)
* table: width of top of diamond relative to widest point (43--95)
* price: price in US dollars (\$326--\$18,823)
* x: length in mm (0--10.74)
* y: width in mm (0--58.9)
* z: depth in mm (0--31.8)

### Getting Started:
Clone this repository to your local machine.
```bash
git clone
```
Once downloaded, activate your virtual environment and run by _____________
```bash
python setup.py
```
### Usage:
After the models are trained, the user can input the features of the diamond and the model will predict the price of the diamond.
