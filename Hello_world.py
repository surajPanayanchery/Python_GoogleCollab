{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Hello_world.py",
      "provenance": [],
      "authorship_tag": "ABX9TyM5hZrYTa8ZpLMugCvE3mCO",
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
        "<a href=\"https://colab.research.google.com/github/surajPanayanchery/Python_GoogleCollab/blob/master/Hello_world.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Pn59hY0dTFsi",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from bs4 import BeautifulSoup as soup\n",
        "import requests\n",
        "import time\n",
        "from datetime import datetime\n",
        "import pandas as pd\n",
        "\n",
        "data = {}\n",
        "\n",
        "def getHtml(url):\n",
        "  \n",
        "  r = requests.get(url)   \n",
        "  return soup(r.content, 'html5lib') \n",
        "\n",
        "\n",
        "def StockValue():\n",
        "  URL = \"https://in.finance.yahoo.com/quote/FEDERALBNK.NS?p=FEDERALBNK.NS&.tsrc=fin-srch\"\n",
        "  html = getHtml(URL)  \n",
        "  page = html.findAll('div',attrs ={'class':'YDC-Lead'});\n",
        "  header = html.findAll('div',attrs={'class':'My(6px) Pos(r) smartphone_Mt(6px)'})\n",
        "  value = html.findAll('span',attrs={'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})\n",
        "  return value.pop().text\n",
        "\n",
        "\n",
        "def getHistoy():\n",
        "  html = getHtml(\"https://in.finance.yahoo.com/quote/FEDERALBNK.NS/history?p=FEDERALBNK.NS\");\n",
        "  navBar = html.find('div',attrs = {'class':'quote-nav'})  \n",
        "  print(navBar)\n",
        "\n",
        "\n",
        "#Start Scraping\n",
        "def startCollecting() : \n",
        "  count = 2\n",
        "  while count > 0:      \n",
        "    data['{}'.format(datetime.today())] = StockValue();\n",
        "    time.sleep(1)\n",
        "    count -= 1\n",
        "\n",
        "\n",
        "columns = ['Federal Bank']\n",
        "startCollecting()\n",
        "pd.DataFrame.from_dict(data,orient='index',columns=columns).to_csv('data.csv');\n"
      ],
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qDBZpUupMzm8",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import pandas as pd\n",
        "\n",
        "help(pd.DataFrame.to_csv)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NchptF2-j0vw",
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