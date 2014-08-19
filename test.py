from producerpool import Pool


def f(x):
    return x*x               


def my_all_callback(result):
    """This callback will be run for each result as it completes."""
    print("One result recieved: {}".format(result))
    return


def my_final_callback(result):
    """This callback will be run once MapResult is ready."""
    print("All Results Received: {}".format(result))
    return


def main():
    """Main code to run."""
    #Create an iterable to feed the pool
    data = (x for x in range(100))

    #Create the pool with 4 process
    pool = Pool(processes=4)

    #map_async with the all_callback parameter
    pool.map_async(f, data, callback=my_final_callback,
                   all_callback=my_all_callback)

    #Wait for everything to finish
    pool.close()
    pool.join()
    return


if __name__ == "__main__":
    main()
