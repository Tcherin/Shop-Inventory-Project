from flask import Blueprint, render_template, request, redirect
from repositories import video_repository, supplier_repository
from models.video import Video

videos_blueprint = Blueprint("videos",__name__)

@videos_blueprint.route("/videos")
def videos():
    all_videos = video_repository.select_all()
    return render_template("videos/index.html", all_videos=all_videos)


@videos_blueprint.route("/videos/new")
def new_video():
    suppliers = supplier_repository.select_all()
    return render_template("videos/new.html", all_suppliers=suppliers)


@videos_blueprint.route("/videos", methods=['POST'])
def create_video():
    title = request.form['title']
    genre = request.form['genre']
    description = request.form['description']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    supplier_id = request.form['supplier_id']

    supplier = supplier_repository.select(supplier_id)
    video = Video(title, genre, description, stock_quantity, buying_cost, selling_price, supplier)
    video_repository.save(video)

    return redirect('/videos')


@videos_blueprint.route("/videos/<id>")
def show_video(id):
    video = video_repository.select(id)
    return render_template("videos/show.html", video=video)


@videos_blueprint.route("/videos/<id>/edit")
def edit_video(id):
    video = video_repository.select(id)
    suppliers = supplier_repository.select_all()
    return render_template("videos/edit.html", video=video, all_suppliers=suppliers)


@videos_blueprint.route("/videos/<id>", methods=['POST'])
def update_video(id):
    title = request.form['title']
    genre = request.form['genre']
    description = request.form['description']
    stock_quantity = request.form['stock_quantity']
    buying_cost =  request.form['buying_cost']
    selling_price = request.form['selling_price']
    supplier_id = request.form['supplier_id']

    supplier = supplier_repository.select(supplier_id)
    video = Video(title, genre, description, stock_quantity, buying_cost, selling_price, supplier, id)
    video_repository.update(video)
    return redirect('/videos')


@videos_blueprint.route("/videos/<id>/delete", methods=["POST"])
def delete_video(id):
    video_repository.delete(id)
    return redirect('/videos')


@videos_blueprint.route("/filtervideos", methods=['POST'])
def filter_by_supplier(id):
    videos = video_repository.select_all()
    filtered_videos = []

    for video in videos:
        if video.supplier.id == id:
            filtered_videos.append(video)
    return render_template("videos/index.html", all_videos=filtered_videos)