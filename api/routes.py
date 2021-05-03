#!flask/bin/python3
#import sys
#sys.path.append('./crawler/')
from flask import Flask, jsonify, abort, request
from api import app
from api.filter import news_unfiltered
from api.filter import clickbait_filter
from api.filter import nonclickbait_filter
from api.filter import news_unfiltered_paged
from api.crawler import news_crawler_viva
#from api import db
#from api.models import Berita_clickbait
###############################
#########ERROR MESSAGE HANDLING
###############################
def bad_request(message):
    response = jsonify({'message': message})
    response.status_code = 400
    return response

###############################
#######################HOMEPAGE
###############################
@app.route('/')
def index():
	'''
	u = Berita_clickbait(link='http://www.johasasdan.com', title='menangkap maling di kebun kita', label='clickbait')
	db.session.add(u)
	db.session.commit()
	users = Berita_clickbait.query.all()
	for u in users:
		db.session.delete(u)
	db.session.commit()
	'''
	return 'Welcome brother'

###############################
################UNFILTERED NEWS
###############################
@app.route('/news/unfiltered', methods=['GET'])
def news_unf():
	if request.headers.get('key') != 'masahmadbagus006':
		return bad_request('Unauthorized Access')
	return jsonify({
		'status': 'ok',
		'article': news_unfiltered.unfiltered()
		})

###############################
####UNFILTERED NEWS WITH PAGING
###############################
@app.route('/news/unfiltered_paged', methods=['GET'])
@app.route('/news/unfiltered_paged/<int:page>', methods=['GET'])
def news_unf_paged(page=0):
	if request.headers.get('key') != 'masahmadbagus006':
		return bad_request('Unauthorized Access')
	if news_unfiltered_paged.unfiltered_paged(page) == False:
		return jsonify({
			'status': 'false',
			'article': 'Berita Habis'
			})
	return jsonify({
		'status': 'ok',
		'article': news_unfiltered_paged.unfiltered_paged(page)
		})

###############################
########FILTERED NEWS CLICKBAIT
###############################
@app.route('/news/clickbait', methods=['GET'])
def clickbaited():
	if request.headers.get('key') != 'masahmadbagus006':
		return bad_request('Unauthorized Access')
	a = clickbait_filter.filtered()
	return jsonify({
		'status': 'ok',
		'article': a
		})

###############################
####FILTERED NEWS NON-CLICKBAIT
###############################
@app.route('/news/nonclickbait', methods=['GET'])
def nonclickbaited():
	if request.headers.get('key') != 'masahmadbagus006':
		return bad_request('Unauthorized Access')
	a = nonclickbait_filter.filtered()
	return jsonify({
		'status': 'ok',
		'article': a
		})

###############################
##############ABOUT APPLICATION
###############################
@app.route('/news/about', methods=['GET'])
def about():
	b = {
	'nama_apl': 'Kliken',
	'versi': '1.0',
	'license': 'MIT',
	'description': 'Aplikasi untuk menghilangkan berita clickbait yang ada di portal berita indonesia',
	'creator': ['Sivi Almanaf Ali Shahab','Muhammad Salma Abdul Aziz', 'Rauzan Sumara','Bagas Alfiandhi Nugroho','Thomi Dhia']
	}
	return jsonify(b)

###############################
#################ENDPOINT COBA2
###############################
@app.route('/news/try', methods=['GET'])
def unf():
	return jsonify(news_crawler_viva.data_json)
