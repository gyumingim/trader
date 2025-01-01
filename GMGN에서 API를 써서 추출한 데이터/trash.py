import json

# JSON 파일을 UTF-8 인코딩으로 읽기
with open('a.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# base_address 추출
pairs = data['data']['pairs']
base_addresses = [pair['base_address'] for pair in pairs]

# 추출된 base_address를 텍스트 파일로 저장
with open('GMGN에서 API를 써서 추출한 데이터/base_output.txt', 'w', encoding='utf-8') as output_file:
    for address in base_addresses:
        output_file.write(address + '\n')
