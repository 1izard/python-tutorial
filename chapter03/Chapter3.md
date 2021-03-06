# Chapter 3 基本構文

プログラムの流れを制御するために必要な構文を導入します．  
この章では if 文と while 文について説明し，for 文については Chapter 4 で取り上げます．  
なお，Python には case 文，do-while 文はありません．  

| 文 (Statement) |   説明   |
| :-----------: | :------: |
|     if 文      |   分岐   |
|     for 文     | 繰り返し |
|    while 文    | 繰り返し |

<br>

# if 文

条件によってプログラムの処理を分岐させます．  
書式は以下のようになります．  

![if_format](img/if_format.png)

else 節はすべての条件に当てはまらなかった場合に実行されます．  

if 文の内側の処理のインデント (文頭の空白) は **必須** です．  
キーボードの tab キーを押して入力しましょう．  
インデントは基本 (半角) 4 文字分です．  

条件文には比較演算子を使います．  

| 比較演算子 | 説明(以下の場合 `True` となる) |
| :--------: | :--------------------------: |
| op1 == op2 |   op1 と op2 が等しい (同値)    |
| op1 != op2 |     op1 と op2 が等しくない     |
| op1 < op2  |      op1 が op2 より小さい      |
| op1 <= op2 |         op1 が op2 以下         |
| op1 > op2  |      op1 が op2 より大きい      |
| op1 >= op2 |         op1 が op2 以上         |
| op1 in op2 |     op1 は op2 の要素である     |
| op1 is op2 |    op1 は op2 である (同一)     |


いくつか例を見ていきましょう．  

例 1-1. 変数aの値が偶数ならば `Even`，奇数ならば `Odd` とコンソールに表示するプログラム  

```python
a = 4

if a % 2 == 0:    # aを2で割った余りが0なら偶数
    print("Even")
else:             # そうでないなら奇数
    print("Odd")

# 出力: Even
```

`a = 4` で偶数なので，if 文の最初の条件式 `a % 2 == 0` は `True` となります．  
内側の処理に入り，`print("Even")` で `Even` と出力します．  
1 つの条件式が `True` となった場合ほかの処理 (この例では else 節) を行わずすぐに抜けます．  


例 1-2. 変数 `you` と変数 `cpu` について，`you` の値が `cpu` より大きければ `You Win !!`，同じであれば `Tie`，小さければ `You Lose...` と表示するプログラム

```python
you = 9
cpu = 9

if you > cpu:
    print("You Win !!")   # section 1
elif you == cpu:
    print("Tie")          # section 2
else:
    print("You Lose...")  # section 3

# 出力: Tie
```

`you = 9`，`cpu = 9` なので，最初の条件式 `you > cpu` は `False` となり，section 1には入りません．  
2 番目の条件式 `you == cpu` では `True` となるので，`print("Tie")` を実行して if 文を抜けます．  


例 1-3. 変数 `score` が 90 以上であれば `A`，80 以上 90 未満であれば `B`，50 以上 80 未満であれば `C`，30 以上 50 未満であれば `D`，30 未満であれば `E` と表示するプログラム

```python
score = 10

if score >= 90:
    print("A")
elif 80 <= score and score < 90:
    print("B")
elif 50 <= score and score < 80:
    print("C")
elif 30 <= score and score < 50:
    print("D")
else:
    print("E")

# 出力: E
```

始めから else 節までのすべての条件式は `False` になります．  
最後に else 節に入り，`print("E")` を実行して終了します．  

多くのプログラムではブール演算の AND の記号として `&&`，OR に `||`，NOT に `!` を用いますが，ブール値の項目で見たように Python では AND に `and`，OR に `or`，NOT に `not` を用います．  
ほかの言語に慣れている方は注意してください．  

また，Pythonでは `<=`，`<`，`>=`，`>` を連続させて条件式を書くことができます．  
例えば例 1-3 は次のようにも書けます．  

```python
score = 10

if score >= 90:
    print("A")
elif 80 <= score < 90:  # ここと
    print("B")
elif 50 <= score < 80:  # ここと
    print("C")
elif 30 <= score < 50:  # ここが変わった
    print("D")
else:
    print("E")

# 出力: E
```

例 1-4. 文字列 a と文字列 b を辞書順で出力するプログラム

```python
a = "abra"
b = "Ekans"

if a < b:
    print(a, b)
else:
    print(b, a)

# 出力: Ekans abra
```

文字列の比較は辞書順で行われます．  
辞書順では大文字の方が小文字より先です．  


## False と評価される値

条件式に値を置くだけでも評価されます．  
次の表は，`False` と評価される値をまとめたものです．  
これ以外の値は `True` になります．  

|  False となる値   |
| :--------------: |
|   False (bool)   |
|       None       |
|        0         |
|       0.0        |
|   "" (空文字)    |
| `[]` (空リスト)  |
| `()` (空タプル)  |
|  `{}` (空辞書)   |
| `set()` (空集合) |


例 1-5.  

```python
n = 1

if n:
    print("True")
else:
    print("False")

# 出力: True
```

例 1-6.  

負の数も `True` になります．  

```python
n = -1

if n:
    print("True")
else:
    print("False")

# 出力: True
```

例 1-7.  

```python
n = 0

if n:
    print("True")
else:
    print("False")

# 出力: False
```


例 1-8.  

```python
s = "False"

if s:
    print("True")
else:
    print("False")

# 出力: True
```

例 1-9.  

空白も `True` になります．  

```python
s = " "   # 空白

if s:
    print("True")
else:
    print("False")

# 出力: True
```

変数を置くだけで評価されるとはいうものの，Python は変数に int 型でも str 型でも何でも代入できるので，変数だけではどんな条件を評価しているのかわかりづらいです．  
なので，数が 0 でないか，あるいは文字列が空文字でないかといった評価は，以下のように比較対象を明示することをおすすめします．  

例 1-10. 整数 n が 0 でないなら `Not zero`，0 なら `Zero` と出力

```python
n = 1

if n != 0:
    print("Not zero")
else:
    print("Zero")

# 出力: Not zero
```

例 1-11. 文字列sが空文字でないなら `Not empty`，空文字なら `Empty` と出力

```python
s = ""

if s != "":
    print("Not empty")
else:
    print("Empty")

# 出力: "Empty"
```

## None

`None` は値がないことを表す値で，ほかのどの値とも等しくありません．  
`None` は少し特殊で，比較には `is` 演算子を使用します．  

```python
a = None

if a is None:
    print("a is None.")
else:
    print("a is not None.")

# 出力: a is None
```

次の例では，文字列 s の長さをコンソールに出力するプログラムです．  
変数 s は自分の書いているプログラムではなくほかのプログラムから渡される文字列だと思ってください．  
このプログラムは s が `None` の場合エラーになります．  

```python
s = ?

print(len(s))   # Noneの場合 TypeError: object of type 'NoneType' has no len()
```

理由は `len()` が `None` をサポートしていないからです．  
Python は変数に様々な型の値を代入することができます (`None` もよく入ります) が，`None` に適用できない関数やメソッドが多くあるので，変数の中身が不明瞭の場合は以下のように None チェックすることが多いです．  

```python
s = ?

if s is not None:
    print(len(s))
```

## 条件式の評価順序

1つの条件式は左から順に評価 (= 計算) されます．  
そして，`and` 演算は左辺が `False` であったとき，右辺を評価せず直ちに `False` を返します．  
また，`or` 演算は左辺が `True` であったとき，右辺を評価せず直ちに `True` を返します．  

次のプログラムは，文字列 s が `None` でなく，かつ長さが 10 以上であることを判定するプログラムです．  
条件式は左から評価されるため，`len(s) > 10 and s is not None` の部分は `len(s) > 10` から評価されます．  
したがって，このプログラムは s が `None` のときエラーになります．  

```python
s = ?

if len(s) >= 10 and s is not None:    # s が None の場合ここでエラー
    print("Yes")
else:
    print("No")

# sがNoneの場合: TypeError: object of type 'NoneType' has no len()
```

`and` は左辺が `False` になった場合右辺を評価せずに `False` を返すので，`len(s) > 10`より先に `s is not None` を評価すれば正しく動きます，  


```python
s = ?

if s is not None and len(s) > 10:
    print("Yes")
else:
    print("No")
```

以下は，同じプログラムを `and` ではなく `or` で書いたものです．  
左辺 `s is None` が `True` となった場合右辺は評価されず，この条件式はすぐに `True` となるので，このプログラムも期待通りに動きます．  

```python
s = ?

if s is None or len(s) < 10:
    print("No")
else:
    print("Yes")
```


## ネスト

複雑な条件は，if 文はネストさせることで表現できます．  

例 1-10. 整数 a (>= 0) が整数 b (>= 0) の倍数であるか判定するプログラム

```python
a = 5
b = 2


if b > 0:
    if a % b == 0:
        print("aはbの倍数です")
    elif:
        print("aはbの倍数じゃないです")
else:
    print("0で割ることはできません")

# 出力: aはbの倍数じゃないです
```

例 1-11. プレイヤー A の出した手 a とプレイヤー B の出した手 b をもとにジャンケンの結果を表示するプログラム (このプログラムはもっと簡潔に書けます → 練習問題 Q 9)

| a, b  |   手   |
| :---: | :----: |
|   0   |  グー  |
|   1   | チョキ |
|   2   |  パー  |

```python
a = 1
b = 2

if a == 0:
    if b == 0:
        print("Tie")
    elif b == 1:
        print("A win")
    else:
        print("B win")
elif a == 1:
    if b == 0:
        print("B win")
    elif b == 1:
        print("Tie")
    else:
        print("A win")
else:
    if b == 0:
        print("A win")
    elif b == 1:
        print("B win")
    else:
        print("Tie")

# 出力: A win
```

(Extra)  

## 三項演算子

多くのプログラミング言語にあるように，Python も三項演算子が使えます (ちょっとほかの言語と書式が違いますが)．  
三項演算子を使うと，簡単な if 文を 1 行にまとめて値の代入まで行えるのでコードを簡潔に書くことができます．  

次のプログラムは，整数 n が偶数の場合変数 s に `Even`，奇数の場合 `Odd` を代入します．  

```python
n = 4

if n % 2 == 0:
    s = "Even"
else:
    s = "Odd"
```

このプログラムは，三項演算子を用いると次のように書けます．  

```python
n = 4

s = "Even" if n % 2 == 0 else "Odd"
```

(ここまで Extra)  

<br>

# while 文

繰り返し同じ処理を行うときは，while 文と for 文を使います．  

while 文の書式は次の通りです．  
条件式が `False` になるまで処理を繰り返します．  

![while_format](img/while_format.png)

これも例を順に見ていきましょう．  

例 2-1. 1 から 3 までの整数を出力するプログラム

```python
i = 1

while i <= 3:
    print(i)
    i += 1

# 1
# 2
# 3
```

i を1ずつ増やし，各 i の値を `print()` で出力します．  
i が 4 になったとき while 文を抜けます．  


例 2-2. 文字列 s の中のアルファベット `e` の数を数えるプログラム

```python
s = "eevee"
i = 0
n = len(s)  # 5

cnt = 0
while i < n:
    if s[i] == "e":
        cnt += 1
    i += 1

print(cnt)    # 4
```

文字列 s の最後のインデックスまで i をインクリメントし，s の i 番目が `e` の場合 cnt をインクリメントすることで s 中のアルファベット `e` の数を数えられます．  


例 2-3. 自然数 n (> 0) を素因数分解したときの 2 の個数

```python
n = 40    # 2 * 2 * 2 * 5
cnt = 0

while n % 2 == 0:
    n //= 2
    cnt += 1

print(cnt)    # 3
```

自然数 n が 2 で割れなくなるまで割り続け，その数を数えます．  


## break 文

break 文を使うと，条件式の結果に関わらず while 文や for 文の中から直ぐに抜けることができます．  
次のプログラムは，文字列中にアルファベット `o` があるかどうかを判定するプログラムです．  
文字列 `s = "Slowpoke"` には `o` が 2 個含まれますが，1 個目が見つかれば文字列の最後まで見る必要はないので，`o` が見つかり次第 break 文で while 文を抜けるようになっています．  

```python
s = "Slowpoke"

i = 0
n = len(s)
found = False
while i < n:
    print(i)
    if s[i] == "o":
        found = True
        break
    i += 1

if found:
    print("Found")
else:
    print("Not found")

"""
出力: 
0
1
2
Found
"""
```


## 無限ループ

条件式を `True` とすると，break 文で抜けない限り (あるいはエラーが起きてプログラムが停止するまで) ループし続けます．  
使いどころとしては，while 文の終了条件が定まらなかったり，while 文を抜けるタイミングや条件がいまいちまとまらなくて break 文で好きなタイミングで抜けたかったりするときとかがあります．  

次のプログラムは，終了文字 `q` が入力されるまでユーザからの入力をストックします．  

```python
input_lines = []

while True:
    s = input("[q: quit] > ")
    if s == "q":
        break
    input_lines.append(s)
```

組込み関数 `input()` については本章の練習問題で，list については次の章で取り上げます．  


## continue 文

continue 文は，次のループに続くことを明示する文です．  
continue 文に遭遇すると，プログラムは **すぐに** 次のループに移ります．  
なくても同じ処理を書けるんですが，後続の処理を行わない条件を強調してわかりやすくしたいときとかに使います．  

```python
i = 0
while i < 10:
    if i % 2 == 0:
        i += 1
        continue

    print(i)
    i += 1
"""
1
3
5
7
9
"""
```

## ネスト

while 文もネストすることができます．  
次のプログラムは，文字列 s 中でアルファベット `e` が連続している部分の個数をカウントします．  

```python
s = "eevee"

i = 0
n = len(s)
cnt = 0
while i < n:
    while i < n and s[i] != "e":  # "e"じゃない部分を飛ばす
        i += 1
    if i >= n:  # iがn以上なら抜ける
        break
    while i < n and s[i] == "e":  # "e"が続くだけ文字列を読む
        i += 1
    cnt += 1    # "e"が途切れたのでカウント

print(cnt)    # 2
```


# スコープ

変数の有効範囲をスコープといいます．  
ほかのいくつかの言語と違い，Python の if 文，while 文，for 文はスコープを作りません．  

例えば，C++ の場合次のコードはエラーになります．  
このコードは，変数 n が偶数の場合変数 ans に `Even`，奇数の場合 `Odd` を代入し，最後に `ans` の文字列を出力しようとしています．  
ここでの `ans` のように，C/C++ や Java などの多くの言語では if 文内で定義された変数のスコープは if 文内となります．  

```c++
#include <iostream>
#include <string>

using namespace std;

int main() {
  int n = 4;
  if (n % 2 == 0) {
    string ans = "Even";
  } else {
    string ans = "Odd";
  }
  cout << ans << endl;    // error: use of undeclared identifier 'ans'
}
```

図解するとこんな感じです．  

![if_scope_cpp](img/if_scope_cpp.png)

Python だと，if 文はスコープをつくらないので if 文内で ans を定義しているにも関わらず次のコードは正しく動作します．  

例 3-1. 

```python
n = 4

if n % 2 == 0:
    ans = "Even"
else:
    ans = "Odd"

print(ans)    # Even
```

では，次の 2 つのコードはどうなるでしょうか．  

```python
n = 4

if n % 2 == 0:
    ans = "Even"

print(ans)  # Even
```

```python
n = 3

if n % 2 == 0:
    ans = "Even"

print(ans)  # NameError: name 'ans' is not defined
```

2 つのうち，上は正常に動きますが，下はエラーになります．  
上の場合，`n = 4` なので `n % 2 == 0` が `True` となり if 文内に入り，`ans` に `Even` が代入されて if 文を抜けます．  
一方，下の場合は `n = 3` なので `n % 2 == 0` が `False` となり，if 文内に入りません．  
その結果，`ans` に何も代入されないまま `print(ans)` が実行されてエラーになります．  

例 3-1くらいの小さな分岐程度であれば，以下のように if 文の前で予め変数を用意しておく必要はないと思います．  

```python
n = 4

ans = ""    # めんどい
if n % 2 == 0:
    ans = "Even"
else:
    ans = "Odd"

print(ans)
```

しかし，分岐が多かったり処理が長かったりするif 文，while 文，for 文の場合は，処理が追いづらくなり，これらの文を抜けた後にどの変数が使えるのかわからなくなるので，これらの文に入る前に予め変数を置いておくことをおすすめします．  

<br>


# 練習問題 3

## 準備

この章の練習問題からコンソールの入力 (標準入力) を使用します．  
Python では，標準入力用に組込み関数 `input()` があります．  
この関数が実行されると，ユーザの入力が完了するまでプログラムが待機し，完了 (エンターキーを押す) するとユーザの入力を文字列 (str 型) として返します．  

例1.  
次のプログラムを実行すると，コンソール上に `> ` が出力されると思います．  
試しに `Pikachu` と入力してエンターキーを押してみてください．  
すると，プログラムが入力された文字を読み取って，コンソール上に `You typed Pikachu` と表示します．  
`print()` にキーワード引数として `end=""` を指定すると改行されません．  
これによって，コンソール上の `> ` と同じ行の右側に入力させることができます．  

```python
print("> ", end="")     # 入力を促す
s = input()

print("You typed", s)   # You typed Pikachu
```

例2.  
連続して入力を受け付けることもできます．  

```python
print("> ")
s1 = input()
print("> ")
s2 = input()
print("> ")
s3 = input()

print(f"You typed {s1}, {s2}, and {s3}")
```

例3.  
`input()` が返すのは str 型なので，int 型にしたい場合は `int()` を，float 型にしたい場合は `float()` を使います．  
次の例は，入力された2つの整数の和を計算して表示するプログラムです．  
int 型に変換できない文字列を入力した場合はエラーになります．  

```python
print("a > ")
a = int(input())
print("b > ")
b = int(input())

print(f"a + b = {a + b}")
```


## Q 1

入力された自然数 (> 0) について，3 の倍数である場合 `Yes`，それ以外の場合は `No` と出力するプログラムを実装してみましょう．  

次の 3 通りの入力で正しい結果が出るようにしてください．  

| 入力  | 出力  |
| :---: | :---: |
|   3   |  Yes  |
|  13   |  No   |
| 2019  |  Yes  |

```python
n = int(input())
```


## Q 2

入力された自然数 (n > 0) について，7 の倍数であり，かつ偶数の場合 `Yes`，それ以外の場合は `No` と出力するプログラムを実装してみましょう．  

次の 3 通りの入力で正しい結果が出るようにしてください．  

| 入力  |       |
| :---: | :---: |
|  21   |  No   |
|  28   |  Yes  |
| 7826  |  Yes  |

```python
n = int(input())
```



## Q 3

入力された自然数 n (> 0) について，以下のように動作するプログラムを実装してみましょう (FizzBuzz 問題)．
- 3で割り切れる場合 `Fizz` と表示
- 5で割り切れる場合 `Buzz` と表示
- 3と5で割り切れる場合 `FizzBuzz` と表示
- それ以外の場合数字をそのまま表示

次の 4 通りの入力で正しい結果が出るようにしてください．  

| 入力  |   出力   |
| :---: | :------: |
|   9   |   Fizz   |
|  13   |    13    |
|  25   |   Buzz   |
|  15   | FizzBuzz |


```python
n = int(input())
```

## Q 4

モンスターボール，スーパーボール，ハイパーボールを売っているショップが 2 軒あります．  
それぞれのショップではボールの個数によって割引も行っています．  
各ショップでのそれぞれのボールの値段は次の通りです．  

|      ボール      |          トキワショップ           |          ハナダショップ          |
| :--------------: | :-------------------------------: | :------------------------------: |
| モンスターボール |                100                |               200                |
|  スーパーボール  |                400                |               500                |
|  ハイパーボール  |               1200                |               1000               |
|       割引       | ハイパーボール 10 個につき 900 円割引 | スーパーボール 5 個につき 500 円割引 |

次の 3 通りの入力について，3 種類のボールを買う値段が **安い方** のショップを出力してください．  
**値段が同じ場合は `トキワショップ` を出力** してください．  
入力は上から順にモンスターボール，スーパーボール，ハイパーボールの個数となっています．  
下のコードを実行したあと，入力の 3 行はまとめてコピペして読み込めます．  


|        入力        |      出力      |
| :----------------: | :------------: |
| 10<br>12<br>10<br> | トキワショップ |
| 22<br>20<br>20<br> | トキワショップ |
|   30<br>30<br>30   | ハナダショップ |


```python
a = int(input())
b = int(input())
c = int(input())
```


## Q 5

while 文を使って，1 以上 10 以下の整数を 1 から順に 1 行ずつ出力してみましょう．  

```python
i = 1
```


## Q 6

1 から 100 まで (1，100 を含む) の整数の和を求めて出力してみましょう．  

```python
total = 0
i = 1
```


## Q 7

while 文 を使って次の機能をもつプログラムを実装してみましょう．  
- 入力された文字列 s について，s 中に含まれるアルファベット `e` のうち先頭から 1 個目のインデックスを出力する
- s 中に 1 つも `e` がない場合は `-1` と出力する

例えば，文字列 `ninetales` の場合は `3`，文字列 `vulpix` の場合は `-1` となります．  

次の 3 通りの入力で正しい結果が出力されるようにしてください．  


|    入力    | 出力  |
| :--------: | :---: |
|  caterpie  |   3   |
|   kakuna   |  -1   |
| butterfree |   4   |

```python
s = input()
```


## Q 8

while 文 を使って次の機能をもつプログラムを実装してみましょう．  
- 入力された文字列 s について，s 中に含まれるアルファベット `a` のうち **末尾から2個目** のインデックスを出力する
- s 中に 2 個目の `a` がない，あるいは 1 つも `a` がない場合は `-1` と出力する

例えば，文字列 `omastar` の場合は`2`，文字列 `omanyte` の場合は `-1`となります．  

次の 3 通りの入力で正しい出力がされるようにしてください．  

|    入力    | 出力  |
| :--------: | :---: |
|  chansey   |  -1   |
|  tangela   |   1   |
| kangaskhan |   4   |

```python
s = input()
```


## Q 9

プレイヤー A の出した手 a とプレイヤー B の出した手 b をもとにジャンケンの結果を表示するプログラムを，if 文をネストさせずに実装してみましょう．  
プレイヤー A が勝った場合は `A win`，プレイヤー B が勝った場合は `B win`，引き分けの場合は `Tie` と出力してください．  

| a, b  |   手   |
| :---: | :----: |
|   0   |  グー  |
|   1   | チョキ |
|   2   |  パー  |

<details>
  <summary>ヒント</summary>
  <p>a と b の組合せを，A が勝つ場合，B が勝つ場合，引き分けの場合の 3 通りに分けてみましょう</p>
</details>


# Q 10

整数 n (> 0)が与えられます．  
はじめ，自分は 1 の位にいます．  
1 回の移動で，自分は今いる桁の数だけ左の桁に移動します．  
何回の移動で最も高い位に辿り着けるでしょうか．
最高位に辿り着くには，最後の移動で最高位と同じか超えられればよいとします．  
また，辿り着けない場合は `-1` を出力してください．  

|                     入力                      | 出力  |
| :-------------------------------------------: | :---: |
|                   87654321                    |   3   |
|         63601359361457022378165821613         |  -1   |
| 736493918437987129890182737846732874297192273 |   9   |

```python
n = input()
```

(Extra)  

## Q 11

random モジュールの randint メソッドは，`randint(a, b)` で呼び出すと a 以上 b 以下の整数 (a, b を含む) をランダムに返します．  
randint メソッドの出力をグー (= 0)，チョキ (= 1)，パー(= 2)にうまく合わせることで，CPU の手をランダムに出させることができます．  
`input()` で自分の手を入力し，それと CPU の出した手を比較して勝敗を表示するジャンケンゲームを実装してみてください．  
また，あいこになるたびに自分の手を入力し直し，CPU の手をランダムに出させるようにしてください．  
プログラムの出力は，実行例を参考にしてください．  

実行例 1

```
さいしょはグー，じゃんけん > 0
プレイヤー:0，CPU:0
あいこで > 1
プレイヤー:1，CPU:1
あいこで > 2
プレイヤー:2，CPU:0
プレイヤーのかち!
```

実行例 2

```
さいしょはグー，じゃんけん > 0
プレイヤー:0，CPU:2
CPUのかち！
```

(ここまで Extra)  


<hr>

[Chapter 3 練習問題解答例](Answers3.md)  
[Index](../README.md)
