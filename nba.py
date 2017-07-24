#########################################################################
# File Name: nba.py
# Author: caochenglong
# mail: caochenglong@163.com
# Created Time: 2017-07-24 12:36:02
# Last modified:2017-07-24 12:36:52
#########################################################################
# !/usr/bin/python3
# _*_coding: utf-8_*_

from neo4j.v1 import GraphDatabase


class Nba(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def create(self, message):
        with self._driver.session() as sess:
            sess.write_transaction(self._create_and_return_greeting, message)

    def query(self, query_s):
        with self._driver.session() as sess:
            res = sess.run(query_s)
        return res

    def delete(self):
        with self._driver.session() as sess:
            sess.run("MATCH (n) DETACH delete n")

    @staticmethod
    def _create_and_return_greeting(tx, message):
        create_url = None
        with open("create", "r") as f:
            create_url = f.readline()
        result = tx.run(create_url, message=message)


if __name__ == "__main__":
    nba = Nba("bolt://localhost:7687/", "neo4j", "123")
    #  nba.create("hehe")
    #  #  print(help(nba.query("MATCH (n) RETURN n")))
    #  #  print(nba.query('MATCH (BOS:Team:E) where BOS.Name\
    #  #  ="Milwaukee"  RETURN BOS.Name').data())
    query_s = 'MATCH (t)-[]->(p:Playoff) WHERE p.Year = "2015" RETURN t,p'
    print(nba.query(query_s).data())
    #  nba.delete()
