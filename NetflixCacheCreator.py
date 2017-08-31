import pickle
#from requests import get
#from array import array
#import numpy as np


def downloadTextFile():
    for i in range(1, 18000):
        fileName = "mv_" + str(i).zfill(7) + ".txt"
        fileWrite = open(fileName, "w")
        webAddress = "http://www.cs.utexas.edu/users/fares/netflix/training_data/" + fileName
        bytes = get(webAddress).content
        print(fileName)
        # print(bytes)
        fileWrite.write(bytes.decode("utf-8"))
        fileWrite.close()

def createMovieNumYearTitle():
    file = open("C:/Users/Nick/Desktop/netflixcache/movie_titles.txt", "r")  # "r" is for reading only

    dictionaryMoviesByYear = {}

    for eachLine in file:  # read each line individually without
        line = eachLine  # reading the entire file first.
        movieNumber = (int)(line[:line.index(",")])
        line = line[line.index(",") + 1:]
        tempYear = line[:line.index(",")]  # this tempVariable is used to check if the year is a real
        if tempYear.isdigit():  # number since some movies don't include a year.
            movieYear = (int)(line[:line.index(",")])
        else:
            movieYear = -1
        line = line[line.index(",") + 1:]
        movieTitle = line
        if movieYear in dictionaryMoviesByYear:
            dictionaryMoviesByYear[movieYear].append(movieNumber)
        else:
            dictionaryMoviesByYear[movieYear] = [movieNumber]

    with open('dictionaryMoviesByYear.pickle', 'wb') as f:
        pickle.dump(dictionaryMoviesByYear, f, pickle.HIGHEST_PROTOCOL)

def createMovieNumYearTitleUsingArray():
    file = open("C:/Users/Nick/Desktop/netflixcache/movie_titles.txt", "r")  # "r" is for reading only

    dictionaryMoviesByYear = {}
    dictionaryMoviesByYearAsArray = {}
    for eachLine in file:  # read each line individually without
        line = eachLine  # reading the entire file first.
        movieNumber = (int)(line[:line.index(",")])
        line = line[line.index(",") + 1:]
        tempYear = line[:line.index(",")]  # this tempVariable is used to check if the year is a real
        if tempYear.isdigit():  # number since some movies don't include a year.
            movieYear = (int)(line[:line.index(",")])
        else:
            movieYear = -1
        line = line[line.index(",") + 1:]
        movieTitle = line
        if movieYear in dictionaryMoviesByYear:
            dictionaryMoviesByYear[movieYear].append(movieNumber)
        else:
            dictionaryMoviesByYear[movieYear] = [movieNumber]

    for key, value in dictionaryMoviesByYear.items():
        a = array('i', value)
        dictionaryMoviesByYearAsArray[key] = a

    with open('dictionaryMoviesByYearAsArray.pickle', 'wb') as f:
        pickle.dump(dictionaryMoviesByYearAsArray, f, pickle.HIGHEST_PROTOCOL)

def createCustomerAndRatings():
    dictionaryCustomerAndRatings = {}
    for i in range(1, 17700 + 1):

        fileName = "mv_" + str(i).zfill(7) + ".txt"
        file = open("C:/Users/Nick/Desktop/netflixcache/" + fileName, "r")  # "r" is for reading only

        for firstLine in file:
            movieNumber = firstLine[:firstLine.index(":")]
            break;
        for eachLine in file:
            customerNumber = (int)(eachLine[:eachLine.index(",")])
            eachLine = eachLine[eachLine.index(",") + 1:]
            individualRating = (int)(eachLine[:eachLine.index(",")])
            eachLine = eachLine[eachLine.index(",") + 1:]
            yearRated = (int)(eachLine[:4])
            if customerNumber in dictionaryCustomerAndRatings:
                dictionaryCustomerAndRatings[customerNumber].append(individualRating)
            else:
                dictionaryCustomerAndRatings[customerNumber] = [individualRating]
        file.close()

    with open('dictionaryCustomerAndRatings.pickle', 'wb') as f:
        pickle.dump(dictionaryCustomerAndRatings, f, pickle.HIGHEST_PROTOCOL)

def createCustomerAndRatingsAsArray():
    count = 1
    dictionaryCustomerAndRatings = {}
    dictionaryCustomerAndRatingsAsArray ={}
    for i in range(1, 17770+1):

        fileName = "mv_" + str(i).zfill(7) + ".txt"
        file = open("C:/Users/Nick/Desktop/netflixcache/" + fileName, "r")  # "r" is for reading only

        for firstLine in file:
            movieNumber = firstLine[:firstLine.index(":")]
            break;
        for eachLine in file:
            customerNumber = (int)(eachLine[:eachLine.index(",")])
            eachLine = eachLine[eachLine.index(",") + 1:]
            individualRating = (int)(eachLine[:eachLine.index(",")])
            eachLine = eachLine[eachLine.index(",") + 1:]
            yearRated = (int)(eachLine[:4])
            if customerNumber in dictionaryCustomerAndRatings:
                dictionaryCustomerAndRatings[customerNumber].append(individualRating)
            else:
                dictionaryCustomerAndRatings[customerNumber] = [individualRating]
        file.close()

    for key, value in dictionaryCustomerAndRatings.items():
        a = array('b', value)
        dictionaryCustomerAndRatingsAsArray[key] = a

    with open('dictionaryCustomerAndRatings.pickle', 'wb') as f:
        pickle.dump(dictionaryCustomerAndRatings, f, pickle.HIGHEST_PROTOCOL)
    with open('dictionaryCustomerAndRatingsAsArrayChar.pickle', 'wb') as f:
        pickle.dump(dictionaryCustomerAndRatingsAsArray, f, pickle.HIGHEST_PROTOCOL)

def createCustomerAndAvgRating():
    print("Begin loading cache into memory")
    with open("C:/Users/Nick/Desktop/netflixcache/cache/key-Customer-value-AllRatingsGiven.pickle", "rb") as f:
        dictionaryCustomerAndRatings = pickle.load(f)
    print("Cache loaded into memory")
    dictionaryCustomerAvgRating = {}
    for key, value in dictionaryCustomerAndRatings.items():
        totalRating = 0
        for rating in value:
            totalRating += rating
        totalRating /= len(value)
        dictionaryCustomerAvgRating[key] = "%.4f" % totalRating

    with open('dictionaryCustomerAvgRating.pickle', 'wb') as f:
        pickle.dump(dictionaryCustomerAvgRating, f, pickle.HIGHEST_PROTOCOL)

def createMovieRatings():
    dictionaryMovieAndRatings = {}
    for i in range(1, 17770 + 1):
        fileName = "mv_" + str(i).zfill(7) + ".txt"
        file = open("C:/Users/Nick/Desktop/netflixcache/" + fileName, "r")  # "r" is for reading only

        for firstLine in file:
            movieNumber = (int)(firstLine[:firstLine.index(":")])
            break;
        for eachLine in file:
            eachLine = eachLine[eachLine.index(",") + 1:]
            individualRating = (int)(eachLine[:eachLine.index(",")])
            if movieNumber in dictionaryMovieAndRatings:
                dictionaryMovieAndRatings[movieNumber].append(individualRating)
            else:
                dictionaryMovieAndRatings[movieNumber] = [individualRating]
        file.close()

    with open('dictionaryMovieAndRatings.pickle', 'wb') as f:
        pickle.dump(dictionaryMovieAndRatings, f, pickle.HIGHEST_PROTOCOL)


    #with open('dictionaryCustomerAvgRating.pickle', 'wb') as f:
    #    pickle.dump(dictionaryCustomerAvgRating, f, pickle.HIGHEST_PROTOCOL)

def createMovieAndAvgRating():
    print("Begin loading cache into memory")
    with open("C:/Users/Nick/Desktop/netflixcache/cache/key-Movie-value-AllRatingsGiven.pickle", "rb") as f:
        dictionaryMovieAndRatings = pickle.load(f)
    print("Cache loaded into memory")
    dictionaryMovieAvgRating = {}
    """for key, value in dictionaryMovieAndRatings.items():
        totalRating = 0
        for rating in value:
            totalRating += rating
        totalRating /= len(value)
        dictionaryMovieAvgRating[key] = "%.4f" % totalRating"""

    #with open('dictionaryMovieAvgRating.pickle', 'wb') as f:
    #    pickle.dump(dictionaryMovieAvgRating, f, pickle.HIGHEST_PROTOCOL)
    dictionaryMovieStats ={}
    dictionaryMovieSTD = {}
    dictionaryMovieMedian = {}
    dictionaryMovieMean = {}
    for key, value in dictionaryMovieAndRatings.items():
        a = np.array(dictionaryMovieAndRatings[key])
        #dictionaryMovieStats[key] = ["%.4f" % np.mean(a),"%.4f" % np.median(a),"%.4f" % np.std(a)]
        dictionaryMovieMean[key] = (float)("%.4f" % (float)(np.mean(a)))
        dictionaryMovieMedian[key] = (float)("%.4f" % (float)(np.median(a)))
        dictionaryMovieSTD[key] = (float)("%.4f" % (float)(np.std(a)))

    with open('dictionaryMovieSTD.pickle', 'wb') as f:
        pickle.dump(dictionaryMovieSTD, f, pickle.HIGHEST_PROTOCOL)

    with open('dictionaryMovieMean.pickle', 'wb') as f:
        pickle.dump(dictionaryMovieMean, f, pickle.HIGHEST_PROTOCOL)

    with open('dictionaryMovieMedian.pickle', 'wb') as f:
        pickle.dump(dictionaryMovieMedian, f, pickle.HIGHEST_PROTOCOL)

    #print(dictionaryMovieStats[3195])
    #print(np.std(a))
    #print(np.median(a))
    #print(np.mean(a))
    #print(dictionaryMovieAndRatings[3195])
    #print(dictionaryMovieAvgRating[3195])

def keyCustValueDiff():
    #with open('C:/Users/Nick/Desktop/netflixcache/cache/key-Movie-value-AvgRatingGiven.pickle', 'rb') as f:
    #   dictionaryMovieAvgRating = pickle.load(f)

    dictionaryCustomerAndRatings = {}
    for i in range(1, 17770+1):

        fileName = "mv_" + str(i).zfill(7) + ".txt"
        file = open("C:/Users/Nick/Desktop/netflixcache/" + fileName, "r")  # "r" is for reading only

        for firstLine in file:
            movieNumber = (int)(firstLine[:firstLine.index(":")])
            break;
        for eachLine in file:
            customerNumber = (int)(eachLine[:eachLine.index(",")])
            eachLine = eachLine[eachLine.index(",") + 1:]
            individualRating = (int)(eachLine[:eachLine.index(",")])
            eachLine = eachLine[eachLine.index(",") + 1:]
            yearRated = (int)(eachLine[:4])
            if customerNumber in dictionaryCustomerAndRatings:
                dictionaryCustomerAndRatings[customerNumber].append([movieNumber,individualRating])
            else:
                dictionaryCustomerAndRatings[customerNumber] = [[movieNumber,individualRating],]
        file.close()

    #with open('dictionaryCustMovieNumAndRating.pickle', 'wb') as f:
    #    pickle.dump(dictionaryCustomerAndRatings, f, pickle.HIGHEST_PROTOCOL)

def createThing():

    dictionaryCustomerRawDiff = {}
    dictionaryCustNumMovieRating = {}
    dictionaryMovieAvgRating = {}
    print("load big")
    with open('C:/Users/Nick/Desktop/netflixcache/cache/dictionaryCustMovieNumAndRating.pickle', 'rb') as file:
        dictionaryCustNumMovieRating = pickle.load(file)
    print("load medium")
    with open('C:/Users/Nick/Desktop/netflixcache/cache/dictionaryMovieMean.pickle', 'rb') as file:
        dictionaryMovieAvgRating = pickle.load(file)
    with open('C:/Users/Nick/Desktop/netflixcache/cache/dictionaryMovieSTD.pickle', 'rb') as file:
        dictionaryMovieSTD = pickle.load(file)
    print("done loading")

    for key, value in dictionaryCustNumMovieRating.items():
        listDifference = []
        for combo in value:
            movieAvg = dictionaryMovieAvgRating[combo[0]]
            theirRating = combo[1]
            listDifference.append((theirRating - movieAvg)/dictionaryMovieSTD[combo[0]])
        dictionaryCustomerRawDiff[key] = np.mean(listDifference)

    with open('CustomerSTDDifference.pickle', 'wb') as file:
        pickle.dump(dictionaryCustomerRawDiff, file, pickle.HIGHEST_PROTOCOL)

    print(dictionaryCustomerRawDiff[472124])
    # print(dictionaryMovieAvgRating[17707])

def offset():
    with open("dictionaryCustomerAvgRating.pickle", "rb") as file:
        customerAvg = pickle.load(file)
    average = 0
    numer = 0
    newOffsetDictionary = {}
    avgCustOver = 3.67419
    avgMovie = 3.22833
    with open("dictionaryMovieAverages.pickle", "rb") as file:
        movieAvg = pickle.load(file)
    for k, v in customerAvg.items():
        newOffsetDictionary[int(k)] = float(float(v) - avgMovie)
        #numer += 1
        #average += float(v)
    """for k, v in movieAvg.items():
        numer += 1
        average += float(v)
    average = average/numer
    print(average)"""
    with open('CustomerOffsetFromAverage.pickle', 'wb') as file:
        pickle.dump(newOffsetDictionary, file, pickle.HIGHEST_PROTOCOL)

def main():
    # downloadTextFile()
    # createMovieNumYearTitle()
    # createCustomerAndRatings()
    # createMovieNumYearTitleUsingArray()
    # createCustomerAndRatingsAsArray()
    # createCustomerAndAvgRating()
    # createMovieRatings()
    # createMovieAndAvgRating()
    # keyCustValueDiff()
    # createThing()
    # createMovieRatings()
    offset()

    #movieNumber = 10008
    #customerNumber = 2048630

    """with open('C:/Users/Nick/Desktop/netflixcache/cache/key-Customer-value-AvgRatingGiven.pickle', 'rb') as file:
        flor = pickle.load(file)
    print("CUST AVG " + str(flor[customerNumber]))

    with open('C:/Users/Nick/Desktop/netflixcache/cache/CustomerRawDifference.pickle', 'rb') as file:
        boob = pickle.load(file)
    with open('C:/Users/Nick/Desktop/netflixcache/cache/CustomerSTDDifference.pickle', 'rb') as file:
        poop = pickle.load(file)
    print("RAW DIFF " + str(boob[customerNumber]))
    print("STD " + str(poop[customerNumber]))

    with open('C:/Users/Nick/Desktop/netflixcache/cache/key-Movie-value-AvgRatingGiven.pickle', 'rb') as file:
        ol = pickle.load(file)
    print("AVG MOVIE RATING " + str(ol[movieNumber]))

    with open('C:/Users/Nick/Desktop/netflixcache/cache/dictionaryMovieSTD.pickle', 'rb') as file:
        otl = pickle.load(file)
    print("MOVIE STD " + str(otl[movieNumber]))

    with open('C:/Users/Nick/Desktop/netflixcache/cache/dictionaryCustMovieNumAndRating.pickle', 'rb') as file:
        yor = pickle.load(file)
    for lists in yor[customerNumber]:
        if lists[0] == movieNumber:
            print("ACTUAL CUSTOMER RATING " + str(lists[1]))"""
            #if group[0]:
            #    print("CUST ACTUAL RATING " + str(thing[1]))
            #    break;
    #print(newDic[2142919])

    #print(dictionaryMovieAvgRating[17707])

main()
