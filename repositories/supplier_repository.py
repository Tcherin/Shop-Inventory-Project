from db.run_sql import run_sql

from models.supplier import Supplier
from models.video import Video
import repositories.video_repository as video_repository


def save(supplier):
    sql = "INSERT INTO suppliers (name, contact_number, activity) VALUES (%s, %s, %s) RETURNING *"
    values = [supplier.name, supplier.contact_number, supplier.activity]
    results = run_sql(sql, values)
    id = results[0]['id']
    supplier.id = id
    return supplier


def select_all():
    suppliers = []

    sql = "SELECT * FROM suppliers"
    results = run_sql(sql)

    for row in results:
        supplier = Supplier(row['name'], row['contact_number'], row['activity'], row['id'] )
        suppliers.append(supplier)
    return suppliers


def select(id):
    supplier = None
    sql = "SELECT * FROM suppliers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        supplier = Supplier(result['name'], result['contact_number'], result['activity'],  result['id'] )
    return supplier


def delete_all():
    sql = "DELETE  FROM suppliers"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM suppliers WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(supplier):
    sql = "UPDATE suppliers SET (name, contact_number, activity) = (%s, %s, %s) WHERE id = %s"
    values = [supplier.name, supplier.contact_number, supplier.activity, supplier.id]
    run_sql(sql, values)

def videos(supplier):
    videos = []

    sql = "SELECT * FROM videos WHERE supplier_id = %s"
    values = [supplier.id]
    results = run_sql(sql, values)

    for row in results:
        video = Video(row['title'], row['genre'], row['description'], row['stock_quantity'], row['buying_cost'], row['selling_price'], row['supplier_id'], row['id'] )
        videos.append(video)
    return videos