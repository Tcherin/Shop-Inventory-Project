from db.run_sql import run_sql

from models.director import Director
from models.video import Video
import repositories.video_repository as video_repository


def save(director):
    sql = "INSERT INTO directors (name, contact_number, activity) VALUES (%s, %s, %s) RETURNING *"
    values = [director.name, director.contact_number, director.activity]
    results = run_sql(sql, values)
    id = results[0]['id']
    director.id = id
    return director


def select_all():
    directors = []

    sql = "SELECT * FROM directors"
    results = run_sql(sql)

    for row in results:
        director = Director(row['name'], row['contact_number'], row['activity'], row['id'] )
        directors.append(director)
    return directors


def select(id):
    director = None
    sql = "SELECT * FROM directors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        director = Director(result['name'], result['contact_number'], result['activity'],  result['id'] )
    return director


def delete_all():
    sql = "DELETE  FROM directors"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM directors WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(director):
    sql = "UPDATE directors SET name = %s WHERE id = %s"
    values = [director.name, director.contact_number, director.activity, director.id]
    run_sql(sql, values)

def videos(director):
    videos = []

    sql = "SELECT * FROM videos WHERE director_id = %s"
    values = [director.id]
    results = run_sql(sql, values)

    for row in results:
        video = Video(row['title'], row['genre'], row['description'], row['stock_quantity'], row['buying_cost'], row['selling_price'], row['director_id'], row['id'] )
        videos.append(video)
    return videos