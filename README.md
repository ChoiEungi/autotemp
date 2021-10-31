# Zeus Temperature Registration

## Usage



### Environment Variables

* USER_ID: Zeus User ID
* USER_PW: Zeus User Password

```bash
$ python main.py
```

### Submission

<img src= "https://raw.githubusercontent.com/ChoiEungi/git-blog-image/upload/img/202110312311075.png">





### Improvement

```python
 value = random.randrange(360, 370, 1)/10 # set random range 36.0 ~ 37.0
```

cron을 통해 자동화를 진행하기 위해 실행이 되면 자동으로 입력되도록 코드를 변경했습니다.



### Crontab Automatation

`crontab -e`

```
20 0 * * * /Users/choeeungi/Desktop/baedalGeek_Studty/temp_check/auto.sh
20 13 * * * /Users/choeeungi/Desktop/baedalGeek_Studty/temp_check/auto.sh
```

매일 오전 12시 20분과 오후 13시 20분에 코드가 실행된다. `auto.sh` 는 환경변수 때문에 사용했습니다. gitignore로 인해 보이지 않음.



**Crontab Example**

https://crontab.guru/examples.html





### Crontab Mac Setting 

https://medium.com/macoclock/automate-running-a-script-using-crontab-on-macos-88a378e0aeac



