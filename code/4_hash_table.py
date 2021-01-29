hash_table = [0 for _ in range(8)]

def get_key(key):
    return hash(key)

def hash_function(key):
    return key % 8

def save_data(key, value):
    index_key = get_key(key) #키값이름으로 저장될 값
    hash_address =hash_function(index_key) #실제로 hash_table의 주소

    # 해쉬테이블에 키가 없으면
    if hash_table[hash_address] != 0:
        # 포문을돌려서 빈곳을 찾는다
        for i in range(hash_address, len(hash_table)):
            # 만약 테이블이 비어 있으면 넣어주고
            if hash_table[i] == 0:
                hash_table[i] = [index_key, value]
            else:
                # 만약 키값이 중복이면 위에 덮어쓴다
                if hash_table[i][0] == index_key:
                    hash_table[i][1] = value
                    return value
    else:
        # 테이블값이 비어있으면 값을 넣어준다
        hash_table[hash_address] = [index_key, value]

def read_data(key):
    index_key = get_key(key) #키값이름으로 저장될 값
    hash_address =hash_function(index_key) #실제로 hash_table의 주소
    if hash_table[hash_address] != 0:
        for i in range(hash_address, len(hash_table)):
            if hash_table[i][0] == index_key:
                return hash_table[i][1]


save_data("saouk", "123")
save_data("saouk", "12345")
print(read_data("saouk"))