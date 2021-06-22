# 函数
函数是带名字的代码块，用于完成具体的工作。要执行函数定义的特定任务，可调用该函数。
需要在程序中多次执行同一项任务时，无需反复编写完成该任务的代码。


## 定义函数

```
def greet_user():
    """ 显示简单的问候语。 """
    print('Hello!')

greet_user()

```
**关键字：def**

### 向函数传递信息

```
def greet_user(username):
    """ 显示简单的问候语。 """
    print(f"Hello, {username.title()}!")

greet_user('hash')

```

### 实参和形参

**形参**：函数完成工作所需要的信息。上面的“username”。
**实参**：调用函数时传递给函数的信息。上面的“hash”。

## 传递实参

### 位置实参
就是有顺序，不要随便颠倒。

```
def describe_pet(animal_type, pet_name):
    """ 显示宠物的信息。 """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}`s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

```

### 关键字实参
传递给函数的名称值对。直接在实参中将名臣和值关联起来，传递时不会混淆

```
def describe_pet(animal_type, pet_name):
    """ 显示宠物的信息 """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}`s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='catty', animal_type='dog')

```
有了关键字实参，这个时候顺序无关紧要了。**但务必准确指定函数定义中形参名。**

### 默认值
没有指定时，就是用那个值。
```
def describe_pet(pet_name, animal_type='dog')
    """ 显示宠物的信息 """
    print(f"\nI have a {animal_type}.)
    print(f"My {animal_type}`s name is {pet_name.title()}.")

describe_pet(pet_name='abraham')

```

### 等效的函数调用
```
# 给其中一个形参提供了默认值
def describe_pet(pet_name, animal_type='dog')

# 对刚才那个函数的所有调用都ok
describe_pet('white')
describe_pet(pet_name='white')

describe_pet('cathy', 'cat')
describe_pet(pet_name='cathy', animal_type='cat')
describe_pet(animal_type='cat', pet_name='cathy')

```

### 避免实参错误
比如，你没有实参，形参也没有缺省值，traceback会指出错误在什么地方。


## 返回值

### 返回简单值

```
def get_formatted_name(first_nme, last_name):
    """ 返回整洁的姓名 """
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('tim', 'elephant')
print(musician)

```

### 让实参变得可选

```
def get_formatted_name(first_name, middle_name, last_name):
    """ 返回整洁的姓名 """ 
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)


```

如果有的人没有中间名呢？

```
def get_formatted_name(first_name, last_name, middle_name=''):
    """ 返回整洁的姓名 """ 
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"

    else:
        full_name=f"{first_name} {last_name}"

    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

musician = get_formatted_name('tom',  'alan')
print(musician)

```

### 返回字典

```
def build_person(first_name, last_name):
    """ 返回一个字典，其中包含有关一个人的信息 """
    person = {'first': first_name, 'last': last_name}
    return person
    
musician = build_person('Yang', 'goat')
print(musician)

```

字典可以扩展,比如其他要存储的信息,下面这个例子包含了年龄,并在形参中设置了缺省值None.

```
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('Yang', 'goat', age=27)
print(musician)

```



### 结合while


```
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

```
上面的例子还定义了退出条件


## 传递列表


每个用户都能看到一条个性化的问候语
```
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

```

### 在函数中修改列表

修改都是永久的，这让你能高效处理大量数据

```
# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 模拟打印每个设计，知道没有未打印的设计为止
# 打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# 显示打印好的所有模型。
print("\nThe following models have been printed")
for completed_model in completed_models:
    print(completed_model)

```
重组后，编写两个函数，每个都做自己该做的事

```
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，知道没有未打印的设计为止。
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """ 显示打印好的所有模型."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

```

### 禁止函数修改列表

向函数传递列表的副本而不是原件
```
# 切片表示法[:]用于创建列表的副本

function_name(list_name[:])

print_models(unprinted_designs[:], completed_models)

```





