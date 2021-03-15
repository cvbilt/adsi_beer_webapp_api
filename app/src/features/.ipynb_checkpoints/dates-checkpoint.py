{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def convert_to_date(df, cols:list):\n",
    "    \"\"\"Convert specified columns from a Pandas dataframe into datetime\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    df : pd.DataFrame\n",
    "        Input dataframe\n",
    "    cols : list\n",
    "        List of columns to be converted\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    pd.DataFrame\n",
    "        Pandas dataframe with converted columns\n",
    "    \"\"\"\n",
    "    import pandas as pd\n",
    "    \n",
    "    for col in cols:\n",
    "        if col in df.columns:\n",
    "            df[col] = pd.to_datetime(df[col])\n",
    "    return df"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
