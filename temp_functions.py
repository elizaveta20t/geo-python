{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMKz+SV/TfluJejoc+azQNS",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/elizaveta20t/geo-python/blob/main/temp_functions.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "eDJkcnUWkJg_"
      },
      "outputs": [],
      "source": [
        "#file <temp_functions.py>\n",
        "# создание функции, которая переводит градусы по Фаренгейту в градусы по Цельсию\n",
        "def fahr_to_celsius(temp_fahrenheit):\n",
        "  \"\"\"Функция принимает температуру в градусах Фаренгейта и преобразует ее в градусы Цельсия\n",
        "     :параметр temp_fahrenheit: температура в градусах Фаренгейта\n",
        "     :return: возвращает преобразованную температуру в Цельсиях\n",
        "     \"\"\"\n",
        "  #преобразование темературы\n",
        "  converted_temp = (temp_fahrenheit - 32) / 1.8\n",
        "  #возвращение значения преобразованной температуры\n",
        "  return converted_temp\n",
        "\n",
        "#создание функции, которая классифицирует температуры\n",
        "def temp_classifier(temp_celsius):\n",
        "    \"\"\"Функция принимает и классифицирует температуры в градусах Цельсия по 4 категориям\n",
        "      :параметр temp_celsius: температура в градусах Цельсия\n",
        "      :return: возвращает значение класса температуры\"\"\"\n",
        "    if temp_celsius < -2:\n",
        "      return(0)\n",
        "    elif temp_celsius >= -2 and temp_celsius < 2:\n",
        "      return(1)\n",
        "    elif temp_celsius >= 2 and temp_celsius < 15:\n",
        "      return(2)\n",
        "    elif temp_celsius >=15:\n",
        "      return(3)"
      ]
    }
  ]
}