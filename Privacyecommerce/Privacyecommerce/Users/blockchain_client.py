from collections import OrderedDict

import binascii
import functools 
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from dbconnect import connection

import requests
from flask import Flask, jsonify, request, render_template


class Transaction:

    def __init__(self, sender_address, sender_private_key, recipient_address, value):
        self.sender_address = sender_address
        self.sender_private_key = sender_private_key
        self.recipient_address = recipient_address
        self.value = value

    def __getattr__(self, attr):
        return self.data[attr]

    def to_dict(self):
        return OrderedDict({'sender_address': self.sender_address,
                            'recipient_address': self.recipient_address,
                            'value': self.value})

    def sign_transaction(self):
        """
        Sign transaction with private key
        """
        private_key = RSA.importKey(binascii.unhexlify(self.sender_private_key))
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')



app = Flask(__name__)

@app.route('/')
def index():
	return render_template('./index.html')

@app.route('/make/transaction')
def make_transaction():
    return render_template('./make_transaction.html')
@app.route('/make/transaction1')
def make_transaction1():
    return render_template('./make_transaction1.html')
@app.route('/make/transaction2')
def make_transaction2():
    return render_template('./make_transaction2.html')
@app.route('/contract/private')
def make_transaction3():
    return render_template('./privatecontract.html')

@app.route('/view/transactions')
def view_transaction():
    return render_template('./view_transactions.html')

@app.route('/wallet/new', methods=['GET'])
def new_wallet():
	random_gen = Crypto.Random.new().read
	private_key = RSA.generate(1024, random_gen)
	public_key = private_key.publickey()
	response = {
		'private_key': binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'),
		'public_key': binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')
	}

	return jsonify(response), 200

@app.route('/generate/transaction', methods=['POST'])
def generate_transaction():
    sender_address = request.form['sender_address']
    sender_private_key = request.form['sender_private_key']
    recipient_address = request.form['recipient_address']
    value = request.form['amount']
    pid = request.form['pid']
    c, conn = connection()
    sql='select amount from  product where id="%s"'% \
             (pid)
    c.execute(sql);
    amount=0;
    result=c.fetchall();
    count=0;
    for cc in result:
        count=1
        amount=cc
    if(count==1):
        sql='select amount from  usdtoken where sid="%s"'% \
             (sender_address)
        c.execute(sql);
        result1=c.fetchall();
        count=0;
        amm=0
        count=0
        for cc1 in result1:
            count=1
            amm=cc1
        sql='select amount from  usdtoken where sid="%s"'% \
             (recipient_address)
        c.execute(sql);
        result1=c.fetchall();
        count=0;
        amm1=0
        count1=0
        for cc1 in result1:
            count1=1
            amm1=cc1
        if(count==1):
            res = functools.reduce(lambda sub, ele: sub * 10 + ele, amm)
            res1 = functools.reduce(lambda sub, ele: sub * 10 + ele, amount)

            res2 = functools.reduce(lambda sub, ele: sub * 10 + ele, amm1)
            result=int(res1)-int(res)
            result2=int(res2)+int(res)
            sql1='update usdtoken set amount="%s" where sid="%s"' % \
                      (result,sender_address)
            c.execute(sql1)
            conn.commit()
            sql1='update usdtoken set amount="%s" where sid="%s"' % \
                      (result2,recipient_address)
            c.execute(sql1)
            conn.commit()
            sql1='insert into trans(sid,rid,pid) values("%s", "%s","%s")' % \
                      (sender_address,recipient_address,pid)
            c.execute(sql1)
            conn.commit()
            conn.close()
            value=res+" "+pid
    transaction = Transaction(sender_address, sender_private_key, recipient_address, value)
    response = {'transaction': transaction.to_dict(), 'signature': transaction.sign_transaction(),'pid': pid}
    return jsonify(response), 200

@app.route('/contract/smart', methods=['POST'])
def smart_contract():
	
	sender_address = request.form['sender_address']
	sender_private_key = request.form['sender_private_key']
	recipient_address = request.form['recipient_address']
	value = request.form['amount']
	c, conn = connection()
	sql1='insert into smartcontract(sid,key1,rid,pid,status) values("%s", "%s","%s","%s","%s")' % \
             (sender_address,sender_private_key,recipient_address,value,"Deliverd")
	c.execute(sql1)
	conn.commit()
	conn.close()
	value=value+"   Deliverd";
	transaction = Transaction(sender_address, sender_private_key, recipient_address, value)
	response = {'transaction': transaction.to_dict(), 'signature': transaction.sign_transaction()}
	return jsonify(response), 200


@app.route('/generate/transaction1', methods=['POST'])
def generate_transaction1():
    sender_address = request.form['sender_address']
    sender_private_key = request.form['sender_private_key']
    product = request.form['name']
    quantity = request.form['quan']
    amount = request.form['amount']
    value=product+","+str(quantity)+","+str(amount)
    transaction = Transaction(sender_address, sender_private_key, sender_address, value)
    c, conn = connection()
    sql='select * from  register where master="%s" AND private="%s"'% \
             (sender_address,sender_private_key)
    c.execute(sql);
    result=c.fetchall();
    count=0;
    for cc in result:
        count=1
    if(count==1):
        sql1='insert into product(sid,pkey,product,quantity,amount,token) values("%s", "%s","%s","%s","%s","%s")' % \
             (sender_address,sender_private_key,product,quantity,amount,transaction.sign_transaction())
        print(sql1)
        c.execute(sql1)
        conn.commit()
        conn.close()
    response = {'transaction': transaction.to_dict(), 'signature': transaction.sign_transaction()}
    return jsonify(response), 200

@app.route('/generate/useradding', methods=['POST'])
def useradding():
	
	random_gen = Crypto.Random.new().read
	private_key = RSA.generate(1024, random_gen)
	public_key = private_key.publickey()
	name = request.form['name']
	mno = request.form['mno']
	address = request.form['address']
	c, conn = connection()
	pri=binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii')
	pub=binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')
	sql1='insert into register(name, mno,address,master,private) values("%s", "%s","%s","%s","%s")' % \
             (name,mno,address,pub,pri)
	c.execute(sql1)
	conn.commit()
	conn.close()
	
	response = {
		'private_key': binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'),
		'public_key': binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')
	}

	return jsonify(response), 200

	



@app.route('/generate/transaction2', methods=['POST'])
def generate_transaction2():
    sender_address = request.form['sender_address']
    sender_private_key = request.form['sender_private_key']
    recipient_address = sender_address
    value = request.form['amount']
    transaction = Transaction(sender_address, sender_private_key, recipient_address, value)
    c, conn = connection()
    sql='select * from  register where master="%s" and private="%s"'% \
         (sender_address,sender_private_key)
    c.execute(sql);
    result=c.fetchall();
    count=0;
    for cc in result:
        count=1
    if(count==1):
        sql='select amount from  usdtoken where sid="%s" and pkey="%s"'% \
             (sender_address,sender_private_key)
        c.execute(sql);
        result1=c.fetchall();
        count=0;
        amm=0
        for cc1 in result1:
            count=1
            amm=cc1
        if(count==1):
            res = functools.reduce(lambda sub, ele: sub * 10 + ele, amm) 
            amount=int(res)+int(value)
            sql1='insert into usdtoken(sid,pkey,amount,token) values("%s", "%s","%s","%s")' % \
                      (sender_address,sender_private_key,amount,transaction.sign_transaction())
            c.execute(sql1)
            conn.commit()
            conn.close()
        else:
            sql1='insert into usdtoken(sid,pkey,amount,token) values("%s", "%s","%s","%s")' % \
                      (sender_address,sender_private_key,value,transaction.sign_transaction())
            c.execute(sql1)
            conn.commit()
            conn.close()
    response = {'transaction': transaction.to_dict(), 'signature': transaction.sign_transaction()}
    return jsonify(response), 200


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8080, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='127.0.0.1', port=port)
