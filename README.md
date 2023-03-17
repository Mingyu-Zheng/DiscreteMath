# DiscreteMath
> 《离散数学及其应用——Python建模与实现》代码整理
>

### 数理逻辑篇

文件夹名：`logic`

1-4章 `logic.py`

#### 函数介绍

| 函数名          | 函数功能                                        | 参数解释                     |
| --------------- | ----------------------------------------------- | ---------------------------- |
| dualformula     | 将公式变换为对偶式                              | s：公式字符串                |
| print01         | 输出真值表中的一行                              | truthtable：布尔值列表       |
| truthtable2     | 输出二元公式（仅限Q，R）所对应的真值表          | s：公式字符串                |
| truthtable3     | 输出三元公式（仅限P，Q，R）所对应的真值表       | s：公式字符串                |
| isargument2     | 输出真值表验证二元逻辑推论（仅限Q，R）          | pre：前提集合，s：推论       |
| isargument3     | 输出真值表验证三元逻辑推论（仅限P，Q，R）       | pre：前提集合，s：推论       |
| isequation2     | 输出真值表验证二元等价关系（仅限Q，R）          | e1：公式1，e2：公式2         |
| isequation3     | 输出真值表验证三元等价关系（仅限P，Q，R）       | e1：公式1，e2：公式2         |
| issubstitution2 | 输出真值表验证二元代换式前后等值（仅限Q，R）    | s：公式，t：子式，s1：替换式 |
| issubstitution3 | 输出真值表验证三元代换式前后等值（仅限P，Q，R） | s：公式，t：子式，s1：替换式 |
| invassignment   | 为命题变元实现相反指派                          | s：公式字符串                |
| dualreplace     | 将逻辑运算符转换为python逻辑运算符              | s：公式字符串                |

#### 运行示例

用pycharm或vscode打开文件夹，并运行`test.py`文件（或打开`test.py`文件所在位置，在命令行中运行`python test.py`）

程序将输出一段真值表如下：

```
'Q   R   (Q and R)'
0   0   0   
0   1   0
1   0   0
1   1   1
```

可参照`test.py`中的代码逻辑应用`logic`模块中实现的函数
