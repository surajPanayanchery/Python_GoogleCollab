{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Stats_Python.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPwzy7vONmuKMxWOvaCFC+V",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/surajPanayanchery/Python_GoogleCollab/blob/master/Stats_Python.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "brepfIZWMx9x",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 406
        },
        "outputId": "05669145-05d2-442a-ce6c-a8cd72ebf22d"
      },
      "source": [
        "import numpy as np\n",
        "from scipy import stats\n",
        "import patsy;\n",
        "import statsmodels.api as sm\n",
        "import statsmodels.formula.api as smf\n",
        "import pandas as pd\n",
        "from statsmodels.stats import anova\n",
        "\n",
        "\n",
        "def getNpArray(array):\n",
        "  return np.array(array);\n",
        "\n",
        "np_array_1 = getNpArray([86, 47, 45, 47, 40]);\n",
        "np_array_2 = getNpArray([86, 47, 45, 47, 40, 97, 98, 75, 65, 83])\n",
        "\n",
        "array_4 = [11, 22, 33]\n",
        "\n",
        "def centralisation_factors():\n",
        "  #Mean (Average of array values)\n",
        "  print('Mean of the array : {}'.format(np.mean(np_array_1)))\n",
        "  #Median (Middle Value in array)\n",
        "  print('Median of the array : {}'.format(np.median(np_array_1)))\n",
        "  #Mode (most frequent value in array)\n",
        "  print('Mode of the array : {}'.format(stats.mode(np_array_2)))\n",
        "\n",
        "\n",
        "def dispersion_factors():\n",
        "  #Range (Highest - lowest)\n",
        "  print('Range: {}'.format(np.ptp(np_array_1)))\n",
        "  #Percentile Value below which this much percentage points exists\n",
        "  print('Value with 45 percentile : {}'.format(np.percentile(np_array_2,45,interpolation=\"lower\")))\n",
        "  #Quartiles Split array according to percentages (3 quartiles) \n",
        "  print('Quartiles with 25,50,27 of the array are  : {}'.format(np.percentile(np_array_2,[25,50,75],interpolation=\"lower\")))\n",
        "  #Inter Quartiles Range - Highest - lowest in the two quartile range of the array\n",
        "  print(\"Inter Quartiles range with 25,75 is : {}\".format(stats.iqr(np_array_2,rng= (25,75),interpolation=\"lower\")))\n",
        "  #Variance - Average of squared difference with average mean\n",
        "  print(\"Variance of the array : {}\".format(np.var(np_array_2)))\n",
        "  #Standard deviation ; square root of variance\n",
        "  print('Standard Deviation of the array is : {}'.format(np.std(np_array_2)))\n",
        "  #Skew : If the most data points are aligned to one side of the distribution\n",
        "  print('Skewness of the array is : {}'.format(stats.skew(np_array_2)))\n",
        "  #Kurtosis : How much data is concentrated in the mean position or shape of the distribution\n",
        "  print(\"Kutosis of the array is : {}\".format(stats.kurtosis(np_array_2)))\n",
        "\n",
        "\n",
        "def playing_with_random():\n",
        "  #Random array\n",
        "  print('Created random 2*3 array : \\n {}'.format(np.random.rand(2,3)))\n",
        "  #Choice - selecting elements from an array randomly\n",
        "  print('Select {} values from array to produce : {}'.format(2,np.random.choice(array_4, 2, replace=False)))\n",
        "  #Seed - Producing the same random  number\n",
        "  np.random.seed(100)\n",
        "  print('Same Random Values using seed')\n",
        "  print(np.random.rand())\n",
        "  np.random.seed(100)  \n",
        "  print(np.random.rand())\n",
        "  #Discrete Distribution takes only integer values -binomial discrete random variable\n",
        "  #Coninuous Distribution takes real values - normal continuous random variable of 1 mean and 2.5 std\n",
        "  nm = stats.norm(loc=1.0,scale=2.5)\n",
        "  #Probability distribution function (continuous) or probability mass function (discrete).\n",
        "  print('probability distribution factorat 1, 0 and -1 respectively are {} '.format(nm.pdf([1,0,-1])))\n",
        "  #Cumulative distribution factor\n",
        "  print('Cumulative distribution factor at 1,0,-1 are {}'.format(nm.cdf([-1, 0, 1])))\n",
        "  #Survival function (1-cdf)\n",
        "  print(\"Survival function: {}\".format(nm.sf([-1,0,1])))\n",
        "  #Generate random number  from the distribution\n",
        "  print(\"Random Number :{}\".format(nm.rvs((2,3))))\n",
        "\n",
        "def hypothesis_testing():\n",
        "  print('methodology for evaluating if a claim is acceptable or not, based on data.')\n",
        "  #Null hypothesis- represents currently accepted state of knowledge  \n",
        "  #Alternative Hypothesis - new claim which challenges the currently accepted state of knowledge\n",
        "  #Test with mean values given\n",
        "  #print('Tests if the mean of a poplation is the given value'.format(stats.ttest_1samp()))\n",
        "  #print('Tests if mean of two independent values sample are equal {}'.format(stats.ttest_ind()))\n",
        "  #print('Tests if mean of two paired samples are equal {}'.format(stats.ttest_rel()))\n",
        "\n",
        "  #Create and random distribution of mean 0.8 and 0.5 and contain 100 samples to test for mean 1\n",
        "  np.random.seed(100)\n",
        "  nd = stats.norm(loc=0.8,scale=0.5)\n",
        "  samples = nd.rvs(100);\n",
        "  print(np.mean(samples))\n",
        "\n",
        "  statits,pvalue = stats.ttest_1samp(samples,0.74)\n",
        "  print(statits)\n",
        "  print(pvalue)\n",
        "\n",
        "def different_models():  \n",
        "  y = np.array([1, 2, 3, 4, 5])\n",
        "  x1 = np.array([6, 7, 8, 9, 10])\n",
        "  x2 = np.array([11, 12, 13, 14, 15])\n",
        "  X = np.vstack([np.ones(5), x1, x2, x1*x2]).T\n",
        "\n",
        "  print('values: {}'.format(y))\n",
        "  print('coeffients : {}'.format(X))\n",
        "\n",
        "  y = np.array([1, 2, 3, 4, 5])\n",
        "  x1 = np.array([6, 7, 8, 9, 10])\n",
        "  x2 = np.array([11, 12, 13, 14, 15])\n",
        "  data = {'y':y, 'x1':x1, 'x2':x2}\n",
        "\n",
        "  y, X = patsy.dmatrices('y ~ 1 + x1 + x2 + x1*x2', data)\n",
        "\n",
        "  print(y)\n",
        "  print(X)\n",
        "\n",
        "def stats_model_library():\n",
        "  #Cancer data set\n",
        "  bc_cancer_set = sm.datasets.cancer\n",
        "  bc_cancer = bc_cancer_set.load_pandas()\n",
        "  bc_cancer_data = bc_cancer.data\n",
        "  #print(type(bc_cancer_data))\n",
        "\n",
        "  #Linear Regression model using stats\n",
        "  icecream_data = sm.datasets.get_rdataset(\"Icecream\",\"Ecdat\").data\n",
        "  #print(\"Icecream data shape shape {}\".format( icecream_data.shape))\n",
        "  #print(\"Columns : {}\".format(icecream_data.columns))\n",
        "\n",
        "  #Model using price and temp\n",
        "  linear_model1 = smf.ols('cons ~ temp + price',icecream_data )\n",
        "  result = linear_model1.fit()\n",
        "  #print(result.summary())#R-squared = 0.633 means model is not a proper fit\n",
        "  #Coefficient of price  = 0.141 this is high that means it accepts null hypothesis hence values of price is zero\n",
        "  #Hence conclude cons doesnot depend on price\n",
        "\n",
        "  #New Model with cons ~ income + temp\n",
        "  lmodel_2 = smf.ols('cons ~ income + temp',icecream_data)\n",
        "  result2 = lmodel_2.fit()\n",
        "  #print('cons ~ income + temp \\n :{}'.format(result2.summary()))\n",
        "  #R-squared 0.702 high - better model\n",
        "  #Coefficient of price 0.006 is low hence is depends\n",
        "  #Probability value of intercept is high  \n",
        "  lmodel_3 = smf.ols('cons ~ -1 + income + temp',icecream_data)\n",
        "  result3 = lmodel_3.fit()\n",
        "  #print('Model without intercept : \\n {}'.format(result3.summary()))\n",
        "\n",
        "  #Discrete Models\n",
        "  # Logit: for Logistic Regression\n",
        "  df = sm.datasets.get_rdataset(\"iris\").data \n",
        "  #df.info()\n",
        "  # print(df.Species.unique() )\n",
        "  df_subset = df[(df.Species == \"versicolor\") | (df.Species == \"virginica\")].copy()\n",
        "  # print(df_subset.Species.unique() )\n",
        "  df_subset.Species = df_subset.Species.map({\"versicolor\": 1, \"virginica\": 0}) \n",
        "  df_subset.rename(columns={\"Sepal.Length\": \"Sepal_Length\", \"Sepal.Width\": \"Sepal_Width\",\t\"Petal.Length\": \"Petal_Length\", \"Petal.Width\": \"Petal_Width\"}, inplace=True) \n",
        "  model = smf.logit('Species ~ Petal_Length + Petal_Width',data= df_subset)\n",
        "  results = model.fit()\n",
        "  # print(results.summary())\n",
        "\n",
        "  df_new = pd.DataFrame({\"Petal_Length\": np.random.randn(20)*0.5 + 5,\n",
        "                        \"Petal_Width\": np.random.randn(20)*0.5 + 1.7})\n",
        "  df_new[\"P-Species\"] = results.predict(df_new)\n",
        "  df_new[\"P-Species\"].head(3)\n",
        "\n",
        "  df_new[\"Species\"] = (df_new[\"P-Species\"] > 0.5).astype(int)\n",
        "  df_new.head()\n",
        "\n",
        "  # MNLogit: for Multinomial Logistic Regression\n",
        "\n",
        "  # Poisson: for Poisson Regression\n",
        "  #Poisson Model describes a process where dependent variable refers to success count of many attempts and each attempt has a very low probability of success.\n",
        "  # fetching data\n",
        "  awards_df = pd.read_csv(\"https://stats.idre.ucla.edu/stat/data/poisson_sim.csv\")\n",
        "  poisson_model = smf.poisson('num_awards ~ math + C(prog)', awards_df)\n",
        "\n",
        "  results_pois = poisson_model.fit()\n",
        "  #print(results_pois.summary())\n",
        "\n",
        "\n",
        "  #Anova\n",
        "  model_anova_1 = smf.ols('cons ~ temp', icecream_data).fit()\n",
        "  print(anova.anova_lm(model_anova_1))\n",
        "  model_anova_2 = smf.ols('cons ~ income + temp', icecream_data).fit()\n",
        "  print(anova.anova_lm(model_anova_2))\n",
        "  \n",
        "  print(anova.anova_lm(model_anova_1, model_anova_2))\n",
        "\n",
        "\n",
        "#centralisation_factors()\n",
        "#dispersion_factors()\n",
        "#playing_with_random()\n",
        "#hypothesis_testing()\n",
        "# different_models()\n",
        "stats_model_library()\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Optimization terminated successfully.\n",
            "         Current function value: 0.102818\n",
            "         Iterations 10\n",
            "Optimization terminated successfully.\n",
            "         Current function value: 0.913761\n",
            "         Iterations 6\n",
            "            df    sum_sq   mean_sq         F        PR(>F)\n",
            "temp       1.0  0.075514  0.075514  42.27997  4.789215e-07\n",
            "Residual  28.0  0.050009  0.001786       NaN           NaN\n",
            "            df    sum_sq   mean_sq          F        PR(>F)\n",
            "income     1.0  0.000288  0.000288   0.208231  6.518069e-01\n",
            "temp       1.0  0.087836  0.087836  63.413711  1.470071e-08\n",
            "Residual  27.0  0.037399  0.001385        NaN           NaN\n",
            "   df_resid       ssr  df_diff   ss_diff         F    Pr(>F)\n",
            "0      28.0  0.050009      0.0       NaN       NaN       NaN\n",
            "1      27.0  0.037399      1.0  0.012611  9.104375  0.005506\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/scipy/stats/_distn_infrastructure.py:903: RuntimeWarning: invalid value encountered in greater\n",
            "  return (a < x) & (x < b)\n",
            "/usr/local/lib/python3.6/dist-packages/scipy/stats/_distn_infrastructure.py:903: RuntimeWarning: invalid value encountered in less\n",
            "  return (a < x) & (x < b)\n",
            "/usr/local/lib/python3.6/dist-packages/scipy/stats/_distn_infrastructure.py:1912: RuntimeWarning: invalid value encountered in less_equal\n",
            "  cond2 = cond0 & (x <= _a)\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9zi-n8mXegXq",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}