from flask import Blueprint, render_template, request, redirect
from repositories import supplier_repository, video_repository
from models.supplier import Supplier
import pdb

suppliers_blueprint = Blueprint("suppliers",__name__)


@suppliers_blueprint.route("/suppliers")
def suppliers():
    all_suppliers = supplier_repository.select_all()
    return render_template("suppliers/index.html", all_suppliers=all_suppliers)


@suppliers_blueprint.route("/suppliers/new")
def new_supplier():
    return render_template("suppliers/new.html")


@suppliers_blueprint.route("/suppliers", methods=['POST'])
def create_supplier():
    name = request.form['name']
    contact_number = request.form['contact_number']
    activity = request.form['active']

    supplier = Supplier(name, contact_number, activity)
    supplier_repository.save(supplier)

    return redirect('/suppliers')


@suppliers_blueprint.route("/suppliers/<id>")
def show_supplier(id):
    supplier = supplier_repository.select(id)
    return render_template("suppliers/show.html", supplier=supplier)


@suppliers_blueprint.route("/suppliers/<id>/edit")
def edit_supplier(id):
    supplier = supplier_repository.select(id)
    return render_template("suppliers/edit.html", supplier=supplier)


@suppliers_blueprint.route("/suppliers/<int:id>", methods=['POST'])
def update_supplier(id):
    name = request.form['name']
    contact_number = request.form['contact_number']
    activity = request.form['activity']

    supplier = Supplier(name, contact_number, activity, id)
    supplier_repository.update(supplier)
    return redirect('/suppliers')


@suppliers_blueprint.route("/suppliers/<id>/delete", methods=["POST"])
def delete_supplier(id):
    supplier_repository.delete(id)
    return redirect('/suppliers')


@suppliers_blueprint.route("/filtersuppliers", methods=['POST'])
def filter_by_suppliers():
    search_term = request.form['supplier_name']
    all_suppliers = supplier_repository.select_all()
    found_suppliers = []
    for supplier in all_suppliers:
        if search_term in supplier.name:
            found_suppliers.append(supplier)
    return render_template("suppliers/index.html", all_suppliers=found_suppliers)