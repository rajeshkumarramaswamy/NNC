from django.shortcuts import render


def index(request):
	data = {
	"Azure NOC" : ["2nd Watch", "2W Demo"],
	"ANN NOC" : ["Accudata System", "ACES"],
	"BVRM NOC" : ["ACUTEC", "Adelbrook"],
	"CBU AID1" : ["AKUITY Technologies", "Aqueduct Technologies", "Axis Business Solutions", "Databranch Inc", "Datavox1"],
	" CBU Manage1" : ["", ""],
}
	return render(request, 'index.html', {'data': data})
