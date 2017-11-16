```
@import 'more-or-less/less/fn/_for';
.for(5);.-each(@i){
    item-@{i} {
        height: 10px * @i;
    }
}
```
