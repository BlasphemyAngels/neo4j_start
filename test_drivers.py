#########################################################################
# File Name: test_drivers.py
# Author: caochenglong
# mail: caochenglong@163.com
# Created Time: 2017-07-24 11:14:51
# Last modified:2017-07-24 11:15:23
#########################################################################
# !/usr/bin/python3
# _*_coding: utf-8_*_

from neo4j.v1 import GraphDatabase


class HelloWorldExample(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def print_greeting(self, message):
        with self._driver.session() as session:
            greeting = session.write_transaction(
                self._create_and_return_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)",
                        message=message)
        return result.single()[0]


if __name__ == "__main__":
    hello = HelloWorldExample("bolt://localhost:7687/", "neo4j", "123")
    hello.print_greeting("hehe")
