#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from . import data_location, info

class Matrix:
    """
    """
    def __init__(self):
        l = open(data_location + info).readlines()
        self.rating_matrix = np.zeros([int(val.split()[0]) + 1 for val in l][:-1])

    def create_rating_matrix(self, users):
        """
        The first row and first column will be blank and should not be used as the user id and item id starts from 1
        
        :param users: contains user ids as keys and instance of :py:mod:`mrs.datamodel.user.User` as values
        :type users:  dict
        """
        for user_id, user_profile in users.items():
            for movie, rating in user_profile.get_movie_rating().items():
                self.rating_matrix[user_id, movie] = rating[0]
