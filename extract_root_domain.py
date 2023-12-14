def extract_root_domain(ext_domain):

    with open("tld.txt", "r", encoding="utf-8") as file:
        tld_array = file.read().splitlines()

    found_match = False  

    for tld in tld_array:
        if ext_domain.endswith(tld):
            index = ext_domain.find(tld)
            if index >= 0:
                previous_element = ext_domain[:index].rsplit('.', 1)[-1]
                result = previous_element + tld
                found_match = True 
                return result

    if not found_match:
        pass

domain_to_check = "www.baidu.com"
result = extract_root_domain(domain_to_check)
print(result)
