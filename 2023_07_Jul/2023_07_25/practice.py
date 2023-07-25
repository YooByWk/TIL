# 혈액형 인원수 세기
# 결과 => {'A' : 3, "B0 : 3", 'O' : 3, "AB" : 3}
blood_types = ['A', 'B', 'A', 'O', 'AB' ,'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

#[]
new_dict = {}
# types 순회하며
for blood_type in blood_types:
    #기존에 키가 있다면
    if blood_type in new_dict:
        #기존 키 값 +1
        new_dict[blood_type] += 1
    #키가 없다면  
    else:
        new_dict[blood_type] = 1
print(new_dict)


# .get() # 키 조회, 값을 얻어냄 없다면 default 설정 가능
# .get() 만으로 if/else 대체 가능
new_dict = {}
for blood_type in blood_types:
    new_dict[blood_type] = new_dict.get(blood_type, 0) + 1
    #bdtpye의 값 = +1 (만약 없다면 0부터 시작하고, 1씩 더해줌)
    
print(new_dict)     

#. setdefault()

new_dict = {}
for blood_type in blood_types:
    new_dict.setdefault(blood_type, 0) #없다면 0 만들어줌.
    new_dict[blood_type] += 1
    #new_dict.setdefault(blood_type, 0) + 1 #a   0b  0 o 0 ab 0

print(new_dict)


#얕 복
a = [1,2, [1, 2]]

b = a[:]
b[2][0] = 999
print(a,b)

a = [1,2, [1, 2]]

b = a[:]
b[2][0] = 999
print(a,b) # [1, 2, [999, 2]] [1, 2, [999, 2]]

a = [1,2, [1, 2]]
c= a.copy()
c[2][0] = 999
print(a, c)

#깊은복사
import copy

original_list = [1,2, [1, 2]]
deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[2][0] = 999

print(original_list, deep_copied_list) #[1, 2, [1, 2]] [1, 2, [999, 2]] 살았다!