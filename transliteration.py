#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 11:51:59 2020

@author: prakhar
"""

from flask import Flask, request
from flask_cors import CORS

scheme = {
	'kh': '\u0916',
	'ai': '\u0910',
	'ma': '\u092e',
	'm': '\u092e',
	'jha': '\u091d',
	'ka': '\u0915',
	'k': '\u0915',
	'n': '\u0928',
	'na': '\u0928',
	'da': '\u0921',
	'a': '\u0905',
	't': '\u0924',
	'ta': '\u0924',
	'tt': '\u091f',
	'ba': '\u092c',
	'j': '\u091c',
	'ja': '\u091c',
	'z': '\u091c',
	'r': '\u0930',
	'h': '\u0939',
	'g': '\u0917',
	'ga': '\u0917',
	'u': '\u0909',
	'uu': '\u090a',
	'ee': '\u0908',
	'e': '\u0907',
	'o': '\u0913',
	'au': '\u0914',
	'gha': '\u0918',
	'ch': '\u091a',
	'chh': '\u091b',
	'th': '\u0925',
	'd': '\u0926',
	'dh': '\u0927',
	'p': '\u092a',
	'pa': '\u092a',
	'f': '\u092b',
	'ph': '\u092b',
	'b': '\u092c',
	'bh': '\u092d',
	'y': '\u092f',
	'ya': '\u092f',
	'r': '\u0930',
	'ra': '\u0930',
	'v': '\u0935',
	'va': '\u0935',
	'l': '\u0932',
	'la': '\u0932',
    'sh': '\u0936',
    'sha': '\u0937',
	's': '\u0938',
	'sa': '\u0938',
	'tha': '\u0920',
	
	'A': '\u093e',
	'AE': '\u0947',
	'II': '\u0940',
	'I': '\u093f',
	'AYE': '\u0948',
	'O': '\u094b',
	'OO': '\u094c',
	'U':'\u0941',
	'UU':'\u0942',

	'1': '\u0967',
	'2': '\u0968',
	'3': '\u0967',
	'4': '\u0968',
	'5': '\u096b',
	'6': '\u096c',
	'7': '\u096d',
	'8': '\u096e',
	'9': '\u096f',
	'0': '\u0966',

	'.': '\u0964'

}

app = Flask(__name__)
CORS(app)

@app.route('/transliterate', methods=['POST'])
def trans():
	inp = request.form.get('text')
	s=''
	start=0
	slidelen=0
	tmp = inp[:]
	if not len(tmp): return ''
	while True:
		final = []
		for idx, c in enumerate(tmp):
			consideration = tmp[:idx+1]
	
			if consideration in scheme:
				final.append(consideration)
			else: continue
		
		if not len(tmp): break
		
		f = max(final, key=len)
		slidelen += len(f)
		s += scheme[f]
		start+=1
		tmp=inp[slidelen:]
		
	return s

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5555, debug=True, threaded=True)
