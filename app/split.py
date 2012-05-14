#!/usr/bin/env python
# encoding: utf-8
'''
File: split.py
Author: NYU ITP team
Description: Holds the specification for an individual
    split as calculated by splitter.py
'''
import sys, os, logging
import json
from bson import json_util,son


class MongoInputSplit():
    """
    Will hold spec for an individual split,
    and is able to pass that split's data to disco
    """

    def __init__(self, inputURI, keyField, query, fields=None, sort=None, limit=0, skip=0, timeout=True,slave_ok=False):
        self.inputURI = inputURI
        self.keyField = keyField
        self.query = query
        self.fields = fields
        self.sort = sort
        self.limit = limit
        self.skip = skip
        self.timeout = timeout
        self.slave_ok = slave_ok


        logging.info("LOOK HERE")
        logging.info("%s" % query)
        logging.info("%s" % fields)


    def format_uri_with_query(self):
        """
        returns a formatted uri like scheme_mongo expects
        we put the query object in a json'd list so we can put it back
        into an ordered SON
        mongodb://local/test.in?query=<json of query>&limit=234&skip=293
        """
        base = self.inputURI
        queryObj = son.SON()
        queryObj['inputURI'] = self.inputURI
        queryObj['keyField'] = self.keyField
        queryObj['query'] = self.query
        queryObj['fields'] = self.fields
        queryObj['sort'] = self.sort
        queryObj['limit'] = self.limit
        queryObj['skip'] = self.skip
        queryObj['timeout'] = self.timeout
        queryObj['slave_ok'] = self.slave_ok

        str = json.dumps(queryObj,default=json_util.default)
        return str

    def __str__(self):
        return self.format_uri_with_query()
