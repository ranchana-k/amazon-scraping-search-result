import sqlite3

def store_db(product_asin, product_name, product_price, product_ratings, product_ratings_num, product_link):
    conn = sqlite3.connect('amazon_search.db')
    curr = conn.cursor()
    # curr.execute('''DROP TABLE IF EXISTS search_result''')
    # create table
    
    curr.execute('''CREATE TABLE IF NOT EXISTS search_result (ASIN text, name text, price real, ratings text, ratings_num text, details_link text)''')
    # insert data into a table
    curr.executemany("INSERT INTO search_result (ASIN, name, price, ratings, ratings_num, details_link) VALUES (?,?,?,?,?,?)", 
                    list(zip(product_asin, product_name, product_price, product_ratings, product_ratings_num, product_link)))
        
    conn.commit()
    conn.close()



