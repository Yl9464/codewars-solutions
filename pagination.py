
class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
      pass
    
    # returns the number of items within the entire collection
    def item_count(self):
        pass
    
    # returns the number of pages
    def page_count(self):
        pass
    
collection = ['a','b','c','d','e','f']
helper = PaginationHelper(collection, 4)
print(PaginationHelper.collection)