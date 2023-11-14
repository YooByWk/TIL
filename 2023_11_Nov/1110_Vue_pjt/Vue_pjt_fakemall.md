# 2023_11_10 PJT

```
npm install axios
```

의존성 관리하세요.

app : 
RouterLink & RouterView

home : 
1. 데이터 불러오기
2. products 출력
3. 상세 페이지 이동
4. 장바구니 추가
5. axios import
6. then / catch 로 정보 확인
7. 로딩중 출력도 해봅시다 // 비어있는 리스트 또한 true 판단이 된다.
   1. 인라인 코드 줄여라. <- 새로운 결과값만 필요하다면?! computed
   2. ```js
        const productIsEmpty = computed(() =>{
      return products.value.length > 0 ? true : false
      })
      ```
8. console 혹은 출력 후 확인한 다음, 적절한 코드로 불러내자
9. 이미지 css 작업. <- card 형태로 출력할 것.
10. btn go detail func
11. 라우터를 이용하여 디테일 페이지로 넘어가는 방법
    1.  params
        1.  /1 /2 /3 <- 변수로 쓰겠다
    2.  query
        1.  ?q = 'key' 의 타입 // ?id=2 
12. ```js
      const goDetail = (product) => {
      router.push(`/${product.id}`)
      }
    ```


detail : 
1. style scoped & without sscoped
   1. maybe


# let's make Cart ! 
- when clicked some item, cart has to get it's info and keep or save what I've added
- "coupang" <- their URL doesn't change ? ? ??  ? then ? ? ? ? ?
- creo que se ha dado del servidor 
- Cookies -> localstorage !
- temporalmente deben guardar lo que se ha selecionado.
- -> espacio del navegador.
- se llama "Local Storage" -> el espacio donde se puede guardar semi-permanente en el navegador
-  -> aunque lo apaga, estara guardado, normalmente es capaz de guardar 5MB de los datos
-  -> guarda mas datos que  "Cookie"
-  -> un problama de la seguridad : tienen que ahorrar los datos que no sean importantes
-  -> si quiere guardar, ... se puede usar
-  ` localStorage.setItem('A','B')` asi se escribe  ::
   -  :: mantiene solo  String !!!!!!!!
-  ` localStorage.getItem('A','B')` asi se escribe\
- JSON.stringify(product) convierte de Obj a String
- ayayay...... sobrescribe!!!!!!!!


# Cart



# vue 문법
> -> 외부 API + vue 가가가가가가가가각
- Youtube API 데이터 수집
youtube api docs - dev - dataAPI - 참조 - 검색 / 구독 / 썸네일 etc
