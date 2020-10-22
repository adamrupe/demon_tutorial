def a_thing(my_rank, size, my_param):
    '''
    Prints stuff. Just used as an example function to demonstrate importing
    from your own module.
    '''
    my_str = "Hello, my rank is {} of {}, and my parameter is {}".format(my_rank,
                                                                     size,
                                                                     my_param)
    return my_str
