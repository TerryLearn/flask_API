
from flask import Blueprint

from app.libs.redprints import Redprint

api = Redprint('user')


@api.route('/get')
def get_user():
    return 'I am Terry'


@api.route('/create')
def create_user():
    return 'create user'