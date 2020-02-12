from django.db import models

# Create your models here.
from django.utils import timezone
import random

class GuessNumbers(models.Model):
    name = models.CharField(max_length = 24) # 로또 번호 리스트의 이름
    text = models.CharField(max_length = 255) # 로또 번호 리스트에 대한 설명
    lottos = models.CharField(max_length= 255,

        default='[1,2,3,4,5,6]') #로또 번호들이 담길 str
    num_lotto = models.IntegerField(default=5) # 6개 번호 set의 갯수
    update_date = models.DateTimeField()

    def generate(self):
        self.lottos = ""
        origin = list(range(1,46)) #1~46의 숫자 리스트
        # 6개 번호 set 갯수만큼 1~46 뒤섞은 후 앞의 6개 골라내어 sorting
        for _ in range(0, self.num_lotto):
            random.shuffle(origin)
            guess = origin[:6] #앞에서 6개
            guess.sort() # 오름차순 정렬
            self.lottos += str(guess) + '\n'

        self.update_date = timezone.now()
        self.save() # GuessNumbers object를 db에 저장

    def _str_(self):# admin page에서 display되는 텍스트에 대한 변경
        return "pk {}:{}-{}".format(self.pk, self.name, self.text)
        # pk는 자동생성됨 프라이머리 키 = 되게 중요해서 자동 생성
