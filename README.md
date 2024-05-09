-- Usage

Currently values such as the location of the csv file are hardcoded in the script 
```
johnblaas@Johns-MacBook-Pro membership-scripts % python3 expired-member-parse.py 
    First Name  Last Name                 E-mail
0         xxxx     xxxxxx    xxxxxxxxxxxxxxxxxx
1        xxxxx      xxxxx   xxxxxxxxxxxxxxxxxxx
2      xxxxxxx  xxxxxxxxx     xxxxxxxxxxxxxxxxx
3         xxxx      xxxxx      xxxxxxxxxxxxxxxx
4          xxx      xxxxx    xxxxxxxxxxxxxxxxxx
..         ...        ...                    ...
124     xxxxxx      xxxx       xxxxxxxxxxxxxxxx
125      xxxxx      xxxx      xxxxxxxxxxxxxxxxx
126       xxxx     xxxxx  xxxxxxxxxxxxxxxxxxxxx
127        xxx   xxxxxxx         xxxxxxxxxxxxxx
128     xxxxxx     xxxxx      xxxxxxxxxxxxxxxxx

[127 rows x 3 columns]
```
After running the program you can find a full listing of expired members and addresses in a file called `expired_members.csv `

```
johnblaas@Johns-MacBook-Pro membership-scripts % cat expired_members.csv | wc -l
     128
```
