## Diamond Price Prediction.
### Project Description:
The goal of this project is to predict the price of a diamond based on its features. The dataset used for this project is the Diamonds dataset from Kaggle. The dataset contains 193572 rows and 11 columns. The dataset contains the following columns: carat, cut, color, clarity, depth, table, price, x, y, z. The dataset is a regression problem. The target variable is the price of the diamond.

### Technologies Used:
* Python
* Pandas
* Numpy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

### Introduction About the Data :

**The dataset** The goal is to predict `price` of given a diamond.

There are 10 independent variables (including `id`):

* `id` : unique identifier of each diamond
* `carat` : Carat (ct.) refers to the unique unit of weight measurement used exclusively to weigh gemstones and diamonds.
* `cut` : Quality of Diamond Cut
* `color` : Color of Diamond
* `clarity` : Diamond clarity is a measure of the purity and rarity of the stone, graded by the visibility of these characteristics under 10-power magnification.
* `depth` : The depth of diamond is its height (in millimeters) measured from the culet (bottom tip) to the table (flat, top surface)
* `table` : A diamond's table is the facet which can be seen when the stone is viewed face up.
* `x` : Diamond X dimension
* `y` : Diamond Y dimension
* `x` : Diamond Z dimension

Target variable:
* `price`: Price of the given Diamond.

Dataset Source Link :
[https://www.kaggle.com/competitions/playground-series-s3e8/data?select=train.csv](https://www.kaggle.com/competitions/playground-series-s3e8/data?select=train.csv)

### Getting Started:
Clone this repository to your local machine.
```bash
git clone
```
Once downloaded, activate your virtual environment and run by :
```bash
python setup.py
```
### Usage:
After the models are trained, the user can input the features of the diamond and the model will predict the price of the diamond.
