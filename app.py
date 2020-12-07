#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import jsonify, request
from uuid import uuid4
from os import unlink
from Buffer import load_buffer
from LexicalAnalyzer import tokenize
from server import app


@app.route('/api/result', methods=['POST'])
def result():
    fileName = ""
    if 'projectName' in request.get_json():
        fileName = request.get_json()['projectName']
    if fileName == "":
        fileName = str(uuid4()) + '.c'
    else:
        fileName += '.c'
    fileBuffer = open(fileName, 'w')
    fileBuffer.write(request.get_json()['code'])
    fileBuffer.close()

    # Lists for every list returned list from the function tokenize
    token = []
    lexeme = []
    row = []
    column = []

    # Tokenize and reload of the buffer
    for i in load_buffer(fileName):
        t, lex, lin, col = tokenize(i)
        token += t
        lexeme += lex
        row += lin
        column += col

    result = dict(zip(lexeme, token))

    unlink(fileName)
    # We use 'jsonify' to return JSON
    return jsonify(result)


if __name__ == '__main__':
    app.debug = True
    app.run()
