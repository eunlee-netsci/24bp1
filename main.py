# import calcpkg.operation    # calcpkg 패키지의 operation 모듈을 가져옴
# import calcpkg.geometry     # calcpkg 패키지의 geometry 모듈을 가져옴

# import calcpkg.operation as op   # calcpkg 패키지의 operation 모듈을 가져옴
# import calcpkg.geometry as geo    # calcpkg 패키지의 geometry 모듈을 가져옴
 
from calcpkg_original.operation import add, multi, divide

print(add(10, 20))    # operation 모듈의 add 함수 사용
print(multi(10, 20))    # operation 모듈의 multi 함수 사용
print(op.divide(10, 20))    # operation 모듈의 divide 함수 사용



# print(calcpkg.operation.add(10, 20))    # operation 모듈의 add 함수 사용
# print(calcpkg.operation.multi(10, 20))    # operation 모듈의 mul 함수 사용
 
# print(calcpkg.geometry.triangle_area(30, 40))    # geometry 모듈의 triangle_area 함수 사용
# print(calcpkg.geometry.rectangle_area(30, 40))   # geometry 모듈의 rectangle_area 함수 사용



# import Calcpkg.operation    # calcpkg 패키지의 operation 모듈을 가져옴
# import Calcpkg.geometry     # calcpkg 패키지의 geometry 모듈을 가져옴
# print(Calcpkg.operation.add(10, 20))    # operation 모듈의 add 함수 사용
# print(Calcpkg.operation.multi(10, 20))    # operation 모듈의 mul 함수 사용
 
# print(Calcpkg.geometry.triangle_area(30, 40))    # geometry 모듈의 triangle_area 함수 사용
# print(Calcpkg.geometry.rectangle_area(30, 40))   # geometry 모듈의 rectangle_area 함수 사용

# --- 
# import Calcpkg.operation as op   # calcpkg 패키지의 operation 모듈을 가져옴
# import Calcpkg.geometry as geo     # calcpkg 패키지의 geometry 모듈을 가져옴

# print(op.add(10,20))
# print(geo.triangle_area(10,20))

# --- 

from Calcpkg.operation import add, multi, divide

print(add(10,2))
print(multi(10,20))
print(op.divide(10,20))
