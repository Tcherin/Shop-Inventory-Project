from db.run_sql import run_sql

from models.video import Video
from models.director import Director
import repositories.director_repository as director_repository


def save(video):
    sql = "INSERT INTO videos (title, genre, description, stock_quantity, buying_cost, selling_price, director_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [video.title, video.genre, video.description, video.stock_quantity, video.buying_cost, video.selling_price, video.director.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    video.id = id
    return video


def select_all():
    videos = []

    sql = "SELECT * FROM videos"
    results = run_sql(sql)

    for row in results:
        director = director_repository.select(row['director_id'])
        video = Video(row['title'], row['genre'], row['description'], row['stock_quantity'], row['buying_cost'], row['selling_price'], director, row['id'] )
        videos.append(video)
    return videos



def select(id):
    video = None
    sql = "SELECT * FROM videos WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        director = director_repository.select(result['director_id'])
        video = Video(result['title'], result['genre'], result['description'], result['stock_quantity'], result['buying_cost'], result['selling_price'], director, result['id'] )
    return video


def delete_all():
    sql = "DELETE  FROM videos"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM videos WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(video):
    sql = "UPDATE videos SET (title, genre, description, stock_quantity, buying_cost, selling_price, director_id) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [video.title, video.genre, video.description, video.stock_quantity, video.buying_cost, video.selling_price, video.director.id, video.id]
    run_sql(sql, values)