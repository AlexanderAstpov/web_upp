from database.db import Base, Sessionlocal, engine
from models.orders import Order
from models.products import Product

def init_database():
    Base.metadata.drop_all(bind=engine)  # удалить все таблички из БД
    Base.metadata.create_all(bind=engine) # создать таблички в БД

    # Заполняем таблицы
    session = Sessionlocal()

        
    p1 = Product(name = "Молоко 1л", price=85, count=15)
    session.add(p1) # так добавляем только одну строку

    lst = [
        Product(name = "Хлеб 1л", price=25, count=5),
        Product(name = "Гречка", price=85, count=56),
        Product(name = "Сахар 1л", price=60, count=50)
    ]
    session.add_all(lst) # добовляем больше одной записи.
    session.commit()


    lst2 = [
        Order(
            customer_name="Петя", 
            phone_nomer="89991112233", 
            product_id = 1, 
            count=5
            ),
        Order(
            customer_name="Вася", 
            phone_nomer="89991112244", 
            product_id = 2, 
            count=1
            ),
        Order(
            customer_name="Коля", 
            phone_nomer="89991112255", 
            product_id = 3, 
            count=2
            ),
        Order(
            customer_name="Оля", 
            phone_nomer="89991112266", 
            product_id = 1, 
            count=4
            )
    ]
    session.add_all(lst2)
    session.commit()

    session.close()



if __name__ == "__main__":
    init_database()