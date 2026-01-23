def format_name(f_name, l_name):
	formated_f_name = f_name.title()
	formated_l_name = l_name.title()
	return f"{formated_f_name} {formated_l_name}"

formatted_name = format_name("PeDro", "lUcAs")
print(formatted_name)


# Usage of return
def function1(text):
	return text + text

def function2(text):
	return text.title()

output = function2(function1("hello"))
print(output)