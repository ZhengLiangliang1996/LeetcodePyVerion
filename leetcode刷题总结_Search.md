### Search
1. dfs模板:

```php
void dfs(...) 
{
    // 结束递归的条件
    if (...) {
        ..... // 把“当前结果” 加入 “结果集容器” 中
        return;
    }

    // 继续递归，里面可能有回溯，也可能没有
    if (...) {

        ... // 在容器中保存当前数据 !!!非常重要
        dfs() 
        ... // 在容器中删除上面保存的数据（注：这种情况下就称为回溯，很明显它是dfs的一个步骤）
    }
}
```
刷提遇见的技巧 将小写字母转换成大写字母
因为a和A差32,其实就是2进制当中的亦或，将0->1,1->0.ord(X ^ (1 << 5))

2. bfs模板
```php
void bfs(...)
{
    queue q;
    q.push(startRoot);
    while (!q.empty()) {
        // 按照节点处理
        curNode = q.front();
        q.pop();

        if (...) {
            // 处理curNode,并把curNode的相邻Nodes加入队列
        }
    }

}

```

字符串的一些小技巧
- 递归的时候 用word[1:]可以每次都去掉首个字符
- python中的去掉某个index下的呀unsu S = S[:i] + S[i+1:]