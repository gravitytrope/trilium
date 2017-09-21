import base64
import math
import random
import string
import time

from flask import Blueprint, jsonify
from flask import request
from flask_login import login_required

from sql import delete
from sql import execute, insert, commit
from sql import getResults, getSingleResult

notes_history_api = Blueprint('notes_history_api', __name__)

@notes_history_api.route('/notes-history/<string:note_id>', methods = ['GET'])
@login_required
def getNoteHistory(note_id):
    history = getResults("select * from notes_history where note_id = ?", [note_id])

    return jsonify(history)