+++
title = "讓 Git 使用起來更方便的一些 tips"
date = "2014-10-10T17:28:00.001Z"
slug = "讓-git-使用起來更方便的一些-tips"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2014/10/git-tips.html"
bloggerID = "6283022408433599776"
tags = ["git"]
[cover]
  image = "/images/blogger/6283022408433599776/PA081264.jpg"
+++

[![](/images/blogger/6283022408433599776/PA081264.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZu1ZXsrOHqAPXjjfmiBXHkZ4Ah6nk8k5QMLTUogaa-gXESjSbVADmcgn7R9Dbqyg0fy6kw682S9UDsfl-RbazdeA8StfMyIvRw0xNdOJAWRNb23n-oTUf4YWFvf5hdx-zABscEhjySmM/s1600/PA081264.jpg)

(Full Moon.Taipei)  
  
第一件事是讓 terminal 可以支援 git command 還有 branch name 的自動補齊，不用每次都要記落落長的分支名稱。  
  
1. 下載 autocomplete 的 shell script  
  
`curl https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash -o ~/.git-completion.bash`  

```
 
```

```
2. 在 ~/.bash_profile 中加入下面的 script
```

```
if [ -f ~/.git-completion.bash ]; then
  . ~/.git-completion.bash
fi 
```

```
 
```

```
然後重新載入一下 .bash_profile 就可以了。
```

```
  
```

```
第二件事是讓 terminal 的 prompt 可以顯示目前是在哪個分支。
```

```
方法也很簡單，在 PS1 這個變數中，適當的位置加入 \$(__git_ps1) 就可以了。
```

```
像我的設法是：
```

```
 
```

```
export PS1='\[\e[36;1m\][\h]\[\e[33;1m\]\t \[\e[0m\]\[\e[32;1m\]\w \[\e[0m\]$(__git_ps1 "(%s)")\n$'
```

```
 
```

```
REF: 
```

```
1. http://code-worrier.com/blog/autocomplete-git/
```

```
2. http://code-worrier.com/blog/git-branch-in-bash-prompt/
```

```
 
```

```
 
```

```
 
```

```
 
```
