forms_data = {}

def foo(data):
	for k,v in data.items():
		if forms_data.get('form_'+str(k.split('-')[1])):
			forms_data['form_'+str(k.split('-')[1])].update({k:v})
		else:
			forms_data['form_'+str(k.split('-')[1])] = {k:v}
	print(forms_data)
	return forms_data


if __name__ == '__main__':
	data = {'id_form-0-choices': 'sadf,ee',
 'id_form-0-question_text': 'sdfsdf',
 'id_form-0-question_type': 'radio',
 'id_form-0-required': True,
 'id_form-1-choices': 'qq,ll',
 'id_form-1-question_text': 'eeee',
 'id_form-1-question_type': 'select-multiple',
 'id_form-1-required': True,
 'id_form-2-choices': '',
 'id_form-2-question_text': '',
 'id_form-2-question_type': 'text',
 'id_form-2-required': True,
 'id_form-3-choices': '',
 'id_form-3-question_text': '',
 'id_form-3-question_type': 'text',
 'id_form-3-required': True,
 'id_form-4-choices': '',
 'id_form-4-question_text': '',
 'id_form-4-question_type': 'text',
 'id_form-4-required': True}
	foo(data)
