import switch

dia = 4

with switch(dia) as s:
	if s.case(1):
		print('lunes')
	if s.case(2):
		print('martes')
	if s.case(3):
		print('miércoles')
	if s.case(4):
		print('jueves')
	if s.case(5):
		print('viernes')
	if s.case(6):
		print('sábado')
	if s.case(7):
		print('domingo')
	if s.default():
		print('error')