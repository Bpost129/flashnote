from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
  return render_template("home.html", user=current_user)

@views.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
  if request.method == 'POST':
    title = request.form.get('title')
    content = request.form.get('content')

    if len(content) < 1:
      print('note is too short')
    else:
      new_note = Note(title=title, content=content, user_id=current_user.id)
      db.session.add(new_note)
      db.session.commit()
      print('note added')

  return render_template("notes.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
  note = json.loads(request.data)
  noteId = note['noteId']
  note = Note.query.get(noteId)
  if note:
    if note.user_id == current_user.id:
      db.session.delete(note)
      db.session.commit()

  return jsonify({})