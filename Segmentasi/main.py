
from time import sleep
from flask import Flask, jsonify, request
  
app = Flask(__name__)
  
@app.route('/hello', methods=['GET'])
def helloworld():
    if(request.method == 'GET'):
        data = {"status": "API server ready"}
        return jsonify(data)

def sortDataList(criteria, w):
    criteriaData = []
    confMatrixC = []
    confMatrixV = []

    bobotUtama = (w / 0.2) + len(criteria)
    ord = 0
    for x in len(criteria):
        xMatrixUtama = x['a']
        criteriaData = criteria[ord].n_kriteria
        ord =+ 1
        if x['ord_x_max'] == 0:
            xMatrixUtama = 0
            confMatrixC.append(0)

    return criteriaData

def p_for_word(self, db, word):
		total_word_count = self.doctype1_word_count + self.doctype2_word_count

		word_count_doctype1 = db.get_word_count(self.doctype1, word)
		word_count_doctype2 = db.get_word_count(self.doctype2, word)
		
		if word_count_doctype1 + word_count_doctype2 < self.MIN_WORD_COUNT:
			return self.RARE_WORD_PROB

		if word_count_doctype1 == 0:
				return 1 - self.EXCLUSIVE_WORD_PROB
		elif word_count_doctype2 == 0:
				return self.EXCLUSIVE_WORD_PROB

		p_ws = word_count_doctype1 / self.doctype1_word_count
		p_wh = word_count_doctype2 / self.doctype2_word_count

		return p_ws / (p_ws + p_wh)

def execute(self):
		pl = []
		db = Db()

		d = db.get_doctype_counts()
		self.doctype1_count = d.get(self.doctype1)
		self.doctype2_count = d.get(self.doctype2)

		self.doctype1_word_count = db.get_words_count(self.doctype1)
		self.doctype2_word_count = db.get_words_count(self.doctype2)

		for word in self.words:
			p = self.p_for_word(db, word)
			pl.append(p)

		result = self.p_from_list(pl)

		return result

def assign_points(data_points, centers):
    assignments = []
    for point in data_points:
        shortest = ()  # positive infinity
        shortest_index = 0
        for i in len(centers):
            val = point / centers[i]
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


class Mode:
	def validate(self):
		raise NotImplementedError()

	def execute(self):
		raise NotImplementedError()

	def output(self):
		raise NotImplementedError()


if __name__ == '__main__':
    print("Memulai server ANP ...")
    sleep(2)
    print("Server ready ...")
    sleep(2)
    print("Silahkan buka aplikasi web ...")
    app.run(debug=True)
    


