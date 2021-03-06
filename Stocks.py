{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Stocks.py",
      "provenance": [],
      "authorship_tag": "ABX9TyN2tEWSWwhJDRg3YG0iUDln",
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
        "<a href=\"https://colab.research.google.com/github/surajPanayanchery/Python_GoogleCollab/blob/master/Stocks_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "raps5tmpQFo-",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import pandas as pd;\n",
        "\n",
        "filePath = 'FDStockHistory.csv'\n",
        "\n",
        "def getMovingAvg(list):\n",
        "  i=5;    \n",
        "  mvCol = []\n",
        "  while(i <= len(list)):\n",
        "    sum = 0;\n",
        "    for el in list[i-5:i]:\n",
        "      sum += el\n",
        "    \n",
        "    mvCol.append(sum/5)\n",
        "    i +=1;\n",
        "  mvCol.extend([0,0,0,0])\n",
        "  return mvCol\n",
        "\n",
        "stockDF = pd.read_csv(filePath);\n",
        "#print(stockDF.head());\n",
        "#print()\n",
        "#len(getMovingAvg(stockDF['Close']))\n",
        "#len(stockDF)\n",
        "stockDF['MovingAverage']=getMovingAvg(stockDF['Close'])\n",
        "stockDF.to_csv('withMovAvg.csv');\n",
        "#print(stockDF['Moving Average'] = )\n",
        "\n",
        "\n",
        "\n"
      ],
      "execution_count": 42,
      "outputs": []
    }
  ]
}
