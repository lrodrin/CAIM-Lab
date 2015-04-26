from pymongo import MongoClient
import sys
import argparse
from bson.code import Code
import csv
import json
from codecs import encode, decode
import math


conn = MongoClient();
db = conn.test;

def mapreduce_counts_word():
	mapper = Code(""" 
		function () {
			for (var i = 0; i < this.content.length; i++) { 
				emit(this.content[i],1) ;
			}
		}""");
	
	reducer = Code(""" 
		function (key , values ) {
			var total = 0;
			for (var i = 0; i < values.length; i++) {
				total += values[i];
			}
			return total;
		}""");

	r = db.transactions.map_reduce(mapper, reducer ,"counts");
	return r

def mapreduce_counts_pairs():
	mapper = Code(""" 
		function () {
			for (var i = 0; i < this.content.length; i++) { 
				for (var j = i+1; j < this.content.length; j++) {
					emit(this.content[i]+' , '+this.content[j],1);
					emit(this.content[j]+' , '+this.content[i],1);
				}
			}
		}""");
	
	reducer = Code(""" 
		function (key , values ) {
			var total = 0;
			for (var i = 0; i < values.length; i++) {
				total += values[i];
			}
			return total;
		}""");

	r = db.transactions.map_reduce(mapper, reducer ,"counts_pairs");
	return r

def association(support, confidence, num_rows):
	#value = db.counts.find_one(sort=[("value", -1)])
	#print value['value'];
	llista_1 = [];
	num_total = 0;
	for doc in db.counts.find():
		if ((doc['value'] *100 // num_rows) >= support):
			llista_1.append(doc);


	for item_tot in llista_1:
		item = item_tot['_id'];
		for doc in db.counts_pairs.find():
			#print doc['_id'].strip().split(' , ')[0]
			if (doc['_id'].strip().split(' , ')[0] == item):
				#print item;
				#print doc['value']*100 // item_tot['value'];
				if ((doc['value']*100 // item_tot['value']) >= confidence):
					num_total = num_total+1;
	
	return num_total;

def associationPrintRules(support, confidence, num_rows):
	#value = db.counts.find_one(sort=[("value", -1)])
	#print value['value'];
	print "Rules found to support: " + str(support) + " confidence: " + str(confidence);
	llista_1 = [];
	num_total = 0;
	for doc in db.counts.find():
		if ((doc['value'] *100 // num_rows) >= support):
			llista_1.append(doc);


	for item_tot in llista_1:
		item = item_tot['_id'];
		for doc in db.counts_pairs.find():
			#print doc['_id'].strip().split(' , ')[0]
			if (doc['_id'].strip().split(' , ')[0] == item):
				#print item;
				#print doc['value']*100 // item_tot['value'];
				if ((doc['value']*100 // item_tot['value']) >= confidence):
					#num_total = num_total+1;
					print doc['_id'];
	
	return;


def main(argv=None):
	parser = argparse.ArgumentParser();
	parser.add_argument('-csv', default='nul');
	args = parser.parse_args();
	num_rows = 0;

	db.drop_collection('transactions');
	with open(args.csv, "rb") as f:
		reader = csv.reader(f, delimiter="\t")
		for line in enumerate(reader):
			num_rows = num_rows+1;
			llegit = [];
			for word in str(line[1]).strip().split(','):
				word = word.replace('[\'','');
				word = word.replace('\']','');
				word = decode(word.strip(),'latin2','ignore');
				llegit.append(word);
			d = {};
			d['content'] = llegit;
			db.transactions.insert(d);
			#llegit = llegit + line;

	mapreduce_counts_word();
	mapreduce_counts_pairs();
	print "TASK 1";
	print "Row1 \t support: 1 \t confidence: 25 \t" + str(association(1,25,num_rows));
	print "Row2 \t support: 1 \t confidence: 50 \t" + str(association(1,50,num_rows));
	print "Row3 \t support: 1 \t confidence: 75 \t" + str(association(1,75,num_rows));
	print "Row4 \t support: 5 \t confidence: 50 \t" + str(association(5,50,num_rows));
	print "Row5 \t support: 10 \t confidence: 25 \t" + str(association(10,25,num_rows));
	print "Row6 \t support: 20 \t confidence: 25 \t" + str(association(20,25,num_rows));
	print "Row7 \t support: 50 \t confidence: 25 \t" + str(association(50,25,num_rows));

	print "TASK 2";
	associationPrintRules(5,50,num_rows);
	associationPrintRules(10,25,num_rows);
	associationPrintRules(20,25,num_rows);

	return

if __name__ == "__main__":
	sys.exit(main())