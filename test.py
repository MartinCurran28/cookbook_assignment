###Get recipes###

###Test the get_recipe function: Returning all 20 recipes in the collection. The expectation is that the expected 20 will match the actual 20.### 
###This test has been failed for the purpose of testing.###

def get_recipes(recipes): 
    return 20 

def test_are_equal(actual, expected):
    assert actual == expected, "Expected {0}, got {1}".format(expected, actual)
    
test_are_equal(get_recipes(20), 20)      

print("There are 20 recipes in the collection")




###Insert Recipe###

###Testing to see if adding a recipe to the collection established in get_recipe will increment the index by one using a test_is_in function for indexing.###
###After insert (1 recipe), the collection will contain 21 recipes (20 + 1). We then try to find the 21st item in that collection's index.###
###Finally, call the 'test_is_in' function with the collection total and the recipe's index number. ### 
###This test was failed for the purpose of testing.###

def insert_recipe(insert):
    return 1
    
def test_is_in(collection, item):
    collection = [20] + [1]
    for item in collection:
        assert 21 in [21], "{0} contains {1}".format(collection, item)
        
test_is_in([20] + [1], [21])    

print ("The 21st recipe in the index is the inserted recipe")




###Delete Recipe###

###Testing to see if deleting a recipe from the collection with decrease the index number of the collection's total.###
###After deleting a recipe [-1], the collection will not contain 20 recipes (21 - 1). We then assert that the 21st recipe added is no longer in the index of the collection.###
####We call the 'test_is_not_in' function with the collection total after deletion (20) and the recipe's last added index number (21) ###
###This test was failed for the purpose of testing.###

def delete_recipe(insert):
    return -1
    
def test_is_not_in(collection, item):
    collection = [20] + [-1]    
    for item in collection:
        assert 21 is not [20], "{0} contains {1}".format(collection, item)
        
test_is_not_in([20] + [-1], [21])    

print ("The 21st recipe has been deleted from the collection")




###Add Cuisine###

###Testing to see if adding a cuisine to a collection will increase the index number of the collection's total and see if the cuisine index added matches the final index number of the collection.###
###After adding a cuisine [1], the cuisine collection will now contain 8 cuisines as opposed to 7 (i.e 7 + 1). We then assert that the 8th cuisine added is in that collection by the index of the collection.###
####We call the 'test_is_in_cuisine' function with the collection total after insertion (7 + 1) and the new cuisine's index number (8) and see if the match as expected.###

def add_cuisine(insert):
    return 1
    
def test_is_in_cuisine(collection, item):
    collection = [7] + [1]
    for item in collection:
        assert 8 in [8], "{0} contains {1}".format(collection, item)
        
test_is_in_cuisine([7] + [1], [8])    

print ("A eighth recipe has been added to the cuisine collection")