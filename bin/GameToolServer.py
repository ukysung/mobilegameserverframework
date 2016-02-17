
import sys
from flask import Flask, g, request, make_response, session, render_template, redirect
from werkzeug import secure_filename
import pymysql, redis, urllib.parse, http.client, json, hashlib

if len(sys.argv) < 2:
	print('Usage: sudo python3 ./GameToolServer.py develop')
	sys.exit()

phase = sys.argv[1]

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.secret_key = 'app_secret_key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

cfg = {}
with open('../cfg/' + phase + '.json', encoding='utf-8') as cfg_file:
	cfg = json.loads(cfg_file.read())

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.before_request
def before_request():
	g.db = {}
	g.cursor = {}

def connect_database(key):
	g.db[key] = pymysql.connect(
		host=cfg[key]['host'],
		port=cfg[key]['port'],
		user=cfg[key]['userid'],
		passwd=cfg[key]['passwd'],
		db=cfg[key]['database'],
		charset=cfg[key]['charset'],
	)
	g.db[key].autocommit(1)
	g.cursor[key] = g.db[key].cursor()

@app.teardown_request
def teardown_request(exception):
	if hasattr(g, 'cursor'):
		for key in g.cursor:
			g.cursor[key].close()

	if hasattr(g, 'db'):
		for key in g.db:
			g.db[key].close()

@app.route('/')
def index():
	res = {'phase':phase, 'session':session}
	return render_template('index.html', res=res)

@app.route('/user/signin')
def user_signin():
	res = {'phase':phase, 'session':session}
	return render_template('user_signin.html', res=res)

@app.route('/user/auth', methods=['POST'])
def user_auth():
	res = {'phase':phase, 'session':session}

	username = request.form['username']
	passwd = request.form['passwd']

	if username == '' or passwd == '':
		res['message'] = 'error : user_auth failed(1)'
		return render_template('message.html', res=res)

	connect_database('db_idx')
	g.cursor['db_idx'].execute('SELECT userid FROM users_idx WHERE username = %s', (username, ))
	row = g.cursor['db_idx'].fetchone()

	if row is None:
		res['message'] = 'error : user_auth failed(2)'
		return render_template('message.html', res=res)

	userid = row[0]
	shard = cfg['db_shard']['db_shard_format'] % (userid % cfg['db_shard']['db_shard_count'])

	connect_database(shard)
	g.cursor[shard].execute('SELECT userid FROM users WHERE userid = %s AND passwd = %s', (userid, hashlib.md5(passwd.encode()).hexdigest()))
	row = g.cursor[shard].fetchone()

	if row is None:
		res['message'] = 'error : user_auth failed(3)'
		return render_template('message.html', res=res)

	session['userid'] = userid
	session['username'] = username

	return redirect('/forum/index')

@app.route('/user/signout')
def user_signout():
	session['userid'] = ''
	session['username'] = ''

	res = {'phase':phase, 'session':session}
	return redirect('/forum/index')

@app.route('/user/signup')
def user_signup():
	res = {'phase':phase, 'session':session}
	return render_template('user_signup.html', res=res)

@app.route('/user/post', methods=['POST'])
def user_post():
	res = {'phase':phase, 'session':session}

	platformtype = request.form['platformtype']
	platformid = request.form['platformid']
	username = request.form['username']
	passwd = request.form['passwd']
	retypepasswd = request.form['retypepasswd']

	if platformtype == '' or platformid == '' or username == '' or passwd == '' or passwd != retypepasswd:
		res['message'] = 'error : user_post failed(1)'
		return render_template('message.html', res=res)

	connect_database('db_idx')
	g.cursor['db_idx'].execute('SELECT userid FROM users_idx WHERE username = %s', (username, ))
	row = g.cursor['db_idx'].fetchone()

	if row is not None:
		res['message'] = 'error : user_post failed(2)'
		return render_template('message.html', res=res)

	g.cursor['db_idx'].execute("CALL USP_GET_UNIQUE_KEYS('users_idx', %s)", (1, ))
	row = g.cursor['db_idx'].fetchone()

	if row is None:
		res['message'] = 'error : user_post failed(3)'
		return render_template('message.html', res=res)

	userid = row[0]
	platformid = userid

	g.cursor['db_idx'].execute('INSERT INTO users_idx(userid, platformtype, platformid, username, inserttime, updatetime) VALUES(%s, %s, %s, %s, NOW(), NOW())', (userid, platformtype, platformid, username))

	shard = cfg['db_shard']['db_shard_format'] % (userid % cfg['db_shard']['db_shard_count'])
	connect_database(shard)

	g.cursor[shard].execute('INSERT INTO users(userid, passwd, inserttime, updatetime) VALUES(%s, %s, NOW(), NOW())', (userid, hashlib.md5(passwd.encode()).hexdigest()))

	return redirect('/user/signin')

@app.route('/forum/index')
@app.route('/forum/index/<page>')
@app.route('/forum/index/<page>/<field>/<keyword>')
def forum_index(page=1, field=0, keyword=''):
	if ('userid' in session) == False or session['userid'] == '':
		return redirect('/user/signin')

	res = {'phase':phase, 'session':session}

	connect_database('db_etc')
	g.cursor['db_etc'].execute('SELECT COUNT(seq) AS forum_count FROM forum')
	res['forum_count'] = g.cursor['db_etc'].fetchone()[0]

	g.cursor['db_etc'].execute('SELECT seq, title, username, updatetime FROM forum ORDER BY seq DESC')
	res['forum_list'] = [dict(seq=row[0], title=row[1], username=row[2], updatetime=row[3]) for row in g.cursor['db_etc'].fetchall()]

	return render_template('forum_index.html', res=res)

@app.route('/forum/show/<seq>')
def forum_show(seq):
	if ('userid' in session) == False or session['userid'] == '':
		return redirect('/user/signin')

	res = {'phase':phase, 'session':session}

	connect_database('db_etc')
	g.cursor['db_etc'].execute('SELECT seq, title, username, content, inserttime, updatetime FROM forum WHERE seq = %s', seq)
	res['forum_show'] = [dict(seq=row[0], title=row[1], username=row[2], content=row[3], inserttime=row[4], updatetime=row[5]) for row in g.cursor['db_etc'].fetchall()]

	return render_template('forum_show.html', res=res)

@app.route('/forum/form/<seq>', defaults={'seq':None})
def forum_update(seq):
	if ('userid' in session) == False or session['userid'] == '':
		return redirect('/user/signin')

	res = {'phase':phase, 'session':session}
	return render_template('forum_form.html', res=res)

@app.route('/forum/delete/<seq>')
def forum_delete(seq):
	if ('userid' in session) == False or session['userid'] == '':
		return redirect('/user/signin')

	res = {'phase':phase, 'session':session}

	connect_database('db_etc')
	g.cursor['db_etc'].execute('DELETE FROM forum WHERE seq = %s', seq)

	return redirect('/forum/index')

@app.route('/forum/post', methods=['POST'])
def forum_post():
	res = {'phase':phase, 'session':session}

	seq = 0
	if request.form['seq'] != '':
		seq = request.form['seq']

	connect_database('db_etc')

	if seq == 0:
		g.cursor['db_etc'].execute("CALL USP_GET_UNIQUE_KEYS('forum', %s)", (1, ))
		row = g.cursor['db_etc'].fetchone()

		if row is None:
			res['message'] = 'error : forum_insert failed(1)'
			return render_template('message.html', res=res)

		seq = row[0]

		g.cursor['db_etc'].execute('INSERT INTO forum(seq, title, content, file1, file2, userid, username, inserttime, updatetime) VALUES(%s, %s, %s, %s, %s, %s, %s, NOW(), NOW())', (seq, request.form['title'], request.form['content'], '', '', session['userid'], session['username']))

	else:
		g.cursor['db_etc'].execute('UPDATE forum SET title = %s, content = %s, file1 = %s, file2 = %s, username = %s, updatetime = NOW() WHERE seq = %s AND userid = %s', (request.form['title'], request.form['content'], '', '', session['username'], seq))

	return redirect('/forum/index')

@app.route('/', methods=['POST'])
def upload_file():
	f = request.files['file']
	if f and allowed_file(f.filename):
		filename = secure_filename(f.filename)
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

	tmp = {}
	resp = make_response(json.dumps(tmp))
	resp.headers['Content-Type'] = 'application/json'

	return resp

if __name__ == '__main__':
	app.run(debug=True, threaded=True, host='0.0.0.0', port=50003)

