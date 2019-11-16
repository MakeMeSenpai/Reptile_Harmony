#test driven code and tests for past code to keep website running safely
from flask import Flask, request,render_template
import unittest 
from app import app, index


class tester_Liz(unittest.TestCase):
    #things to do before every test
    def setUp(self): 
        self.client = app.test_client()
        app.config['TESTING'] = True

    #tests our index/home page
    def tests_index(self):
            result = self.client.get('/')
            self.assertEqual(index(), result)
            self.assertEqual(index(), render_template("index.html"))
    
    #tests our shop page
    def tests_shop(self):
            result = self.client.get('/shop')
            self.assertEqual(index(), result)
            self.assertEqual(index(), render_template("shop.html"))

    #tests our cart page
    def tests_cart(self):
            result = self.client.get('/cart')
            self.assertEqual(index(), result)
            self.assertEqual(index(), render_template("cart.html"))

    #tests our other page
    def tests_other(self):
            result = self.client.get('/other')
            self.assertEqual(index(), result)
            self.assertEqual(index(), render_template("other.html"))

    #look at django or somewhere else for safer programming of the admin page. we do not want 
    # outsiders gaining access to the admin page!! also remember to run $ py.test [name of file]


#runs our tests and closes our runtime
if __name__ == "__main__":
    unittest.TestCase() #both make test run and might be redundant,
    unittest.main() # do research on unittests.
    app.run(debug=True)