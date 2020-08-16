{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Stats_Python.py",
      "provenance": [],
      "authorship_tag": "ABX9TyPIUP0hM+TrRSdjlEQS+VTz",
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
          "height": 67
        },
        "outputId": "28d2a191-d1d8-46b1-bf4e-fadf6f18c545"
      },
      "source": [
        "import numpy as np\n",
        "from scipy import stats\n",
        "\n",
        "def getNpArray(array):\n",
        "  return np.array(array);\n",
        "\n",
        "np_array_1 = getNpArray([86, 47, 45, 47, 40]);\n",
        "np_array_2 = getNpArray([86, 47, 45, 47, 40, 97, 98, 75, 65, 83])\n",
        "np_array_3 = getNpArray([26, 15, 8, 44, 26, 13, 38, 24, 17, 29]);\n",
        "array_4 = [11, 22, 33]\n",
        "\n",
        "def centralisation_factors():\n",
        "  #Mean (Average of array values)\n",
        "  print('Mean of the array : {}'.format(np.mean(np_array_1)))\n",
        "  #Median (Middle Value in array)\n",
        "  print('Median of the array : {}'.format(np.median(np_array_1)))\n",
        "  #Mode (most frequent value in array)\n",
        "  print('Mode of the array : {}'.format(stats.mode(np_array_3)))\n",
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
        "  print(\"Inter Quartiles range with 25,75 is : {}\".format(stats.iqr(np_array_3,rng= (25,75),interpolation=\"lower\")))\n",
        "  #Variance - Average of squared difference with average mean\n",
        "  print(\"Variance of the array : {}\".format(np.var(np_array_2)))\n",
        "  #Standard deviation ; square root of variance\n",
        "  print('Standard Deviation of the array is : {}'.format(np.std(np_array_2)))\n",
        "  #Skew : If the most data points are aligned to one side of the distribution\n",
        "  print('Skewness of the array is : {}'.format(stats.skew(np_array_3)))\n",
        "  #Kurtosis : How much data is concentrated in the mean position or shape of the distribution\n",
        "  print(\"Kutosis of the array is : {}\".format(stats.kurtosis(np_array_3)))\n",
        "\n",
        "\n",
        "def hands_on():\n",
        "  print(np.mean(np_array_3))\n",
        "  print(np.median(np_array_3))\n",
        "  print(stats.mode(np_array_3))\n",
        "  print(np.percentile(np_array_3,25,interpolation=\"lower\"))\n",
        "  print(np.percentile(np_array_3,75,interpolation=\"lower\"))\n",
        "  print(stats.iqr(np_array_3,rng=(25,75),interpolation=\"lower\"))\n",
        "  print(stats.skew(np_array_3))\n",
        "  print(stats.kurtosis(np_array_3))\n",
        "\n",
        "\n",
        "\n",
        "def playing_with_random():\n",
        "  #Choice - selecting elements from an array randomly\n",
        "  print('Select {} values from array to produce : {}'.format(2,np.random.choice(array_4, 2, replace=False)))\n",
        "  #Seed - Producing the same random  number\n",
        "  np.random.seed(100)\n",
        "  print(np.random.rand())\n",
        "  np.random.seed(100)  \n",
        "  print(np.random.rand())\n",
        "\n",
        "\n",
        "#centralisation_factors()\n",
        "#dispersion_factors()\n",
        "#hands_on()\n",
        "playing_with_random()\n",
        "\n",
        "\n",
        "\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Select 2 values from array to produce : [22 33]\n",
            "0.5434049417909654\n",
            "0.5434049417909654\n"
          ],
          "name": "stdout"
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