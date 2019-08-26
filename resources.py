"""
This is the actual business logic file which defines all the functions called
from app.py file.
"""
from flask import jsonify
from database_setup import Chores
from populate_db import session

def get_chores():
    """This returns all the chores in the json format"""
    chores = session.query(Chores).all()
    return jsonify([c.serialize for c in chores])

def get_chore(chore_id):
    """This returns a chore with the chore id in the json format. However, the
    output will not display in the serialized form, as the question demands
    only the HEAD request"""
    try:
        chore = session.query(Chores).filter_by(chore_title=chore_id).one()
        if chore:
            return jsonify(chore.serialize)
    except:
        return "No such chores exist\n"

def make_a_new_chore(chore):
    """This adds a new chore in the database and also returns the json
    format of the chores added"""
    title, task = chore.items()[0]
    addedchore = Chores(chore_title=title, chore=task)
    existing_titles = [elem.chore_title for elem in session.query(Chores).all()]
    if addedchore.chore_title not in existing_titles:
        session.add(addedchore)
        session.commit()
        return jsonify(addedchore.serialize)
    else:
        return "Chore title already exist.\n"

def update_a_chore(title, task):
    """This just update an existing chore with newer task"""
    try:
        tobe_updatedchore = session.query(Chores).filter_by(chore_title=title).one()
        tobe_updatedchore.chore = task
        session.merge(tobe_updatedchore)
    except:
        tobe_updatedchore = Chores(chore_title=title, chore=task)
        session.add(tobe_updatedchore)
    session.commit()
    return "Updated the chore with id %s\n" % title

def delete_a_chore(choreid):
    """It deletes a chore with the chore_title"""
    try:
        chore_to_delete = session.query(Chores).filter_by(chore_title=choreid).one()
    except:
        return "No such chores exist\n"

    session.delete(chore_to_delete)
    session.commit()
    return "Removed Chore with id %s\n" % choreid

def delete_all_chores():
    """It deletes all the chores from the database."""
    try:
        num_rows_deleted = session.query(Chores).delete()
        session.commit()
        return "{} records deleted\n".format(num_rows_deleted)
    except:
        session.rollback()
