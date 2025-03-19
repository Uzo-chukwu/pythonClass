def switch_list(list,element):
	rearranged_list = []
	
	for i in range(len(list)):
		if i == element:
			continue
		rearranged_list.append(list[i])
		
	rearranged_list.append(list[element])
	return rearranged_list

def divide_list(list):
	final_list = []
	firstlist = []
	secondlist = []
	firstlistlength = round(len(list)/2)
	count = 0
	for i in list:
		if count <= firstlistlength:
			firstlist.append(list[i])
		else:
			secondlist.append(i+firstlistlength)
		count+=1
	final_list.extend((firstlist,secondlist))
	return final_list



def check_odd_and_even_elements(numbers):
	result = []
	for number in numbers:
		if number % 2 == 0:
			result.append(True)
		else:
			result.append(False)
	return result
