#!/usr/bin/env python3

#------------------------------------------------------
# Netflix.py
# A program to predict customers' Netflix movie ratings
# By: Kyle Kimery and Nick Frawley
#------------------------------------------------------

# -------
# imports
# -------

from math import sqrt
import pickle
from requests import get
from os import path
from numpy import sqrt, square, mean, subtract


def create_cache(filename):
    """
    filename is the name of the cache file to load
    returns a dictionary after loading the file or pulling the file from the public_html page
    """
    cache = {}
    filePath = "/u/fares/public_html/netflix-caches/" + filename
    if path.isfile(filePath):
        with open(filePath, "rb") as f:
            cache = pickle.load(f)
    else:
        webAddress = "http://www.cs.utexas.edu/users/fares/netflix-caches/" + \
            filename
        bytes = get(webAddress).content
        cache = pickle.loads(bytes)
    return cache

#------------------------------------------------------------------------------#
# Caches have been created that store:
#   -Customer's average offset from mean movie score (dictionaryCustomerOffset)
#   -Average score of each movie (dictonaryMovieAverage)
#   -Standard deviation of ratings by movie (dictionaryMovieSTD)
#   -A customer's difference in score given in terms of number of standard deviations
#       (dictionaryCustomerSTDDiff)
#-------------------------------------------------------------------------------#

actual_scores_cache = create_cache("cache-actualCustomerRating.pickle")
dictionaryCustomerOffset = create_cache("krk893-njf388-CustomerDiffOff.pickle")
dictionaryMovieAverage = create_cache("krk893-njf388-MovieMean.pickle")
dictionaryMovieSTD = create_cache("krk893-njf388-MovieStandDiff.pickle")
customerSTDDiff = create_cache("krk893-njf388-CustomerSTDDiff.pickle")


# ------------
# netflix_eval
# ------------

def netflix_eval(reader, writer):
    """
    reads in a movie ID and customer IDs. predicts a customer's score for each
    movie and then compares this prediction to their actual rating in order to 
    judge how accurate the prediction was.
    """
    predictions = []
    actual = []

    for line in reader:
        line = line.strip()
        if line[-1] == ':':
            # It's a movie
            current_movie = line.rstrip(':')
            movieAvg = dictionaryMovieAverage[int(current_movie)]
            movieSTD = dictionaryMovieSTD[int(current_movie)]
            writer.write(line + '\n')
        else:
            # It's a customer
            current_customer = line
            keyV = (int(current_customer), int(current_movie))
            actual.append(actual_scores_cache[keyV])
            #----------------------------------------
            # Prediction is based off a customer's
            # average number of standard deviations
            # from a movie's average and their offset
            #----------------------------------------
            offset = dictionaryCustomerOffset[int(current_customer)]
            prediction = movieAvg + movieSTD * customerSTDDiff[int(current_customer)]
            prediction = prediction + offset
            if prediction > 5:
                prediction = 5.0
            predictions.append(prediction)
            writer.write(str(prediction)[:3] + '\n')

    # calculate rmse for predications and actuals
    rmse = sqrt(mean(square(subtract(predictions, actual))))
    writer.write(str(rmse)[:4] + '\n')
