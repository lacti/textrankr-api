# Textrankr-api

- [Textrankr](https://github.com/theeluwin/textrankr)

## Requirements

- NodeJS 12+
- python 3.8
- AWS profiles to deploy SAM stack.

```bash
# Setup py env for development
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

# Setup nodeJS env for deployment
npm i
npm run start # for local test
npm run build # for packaging
npm run deploy # for deployment
```

### Environment variable

- `PHRASER_API_URL`

You can make this API using [phrases-api](https://github.com/lacti/phrases-api).

## Usage

```bash
curl -XPOST "https://textrankr-api/summerize" -d "YOUR-TEXT-IN-HERE"
```

```bash
time curl -s -XPOST "https://API_ID.execute-api.AWS_REGION.amazonaws.com/dev/summerize" -d '애국가의 가사는 1900년대 초에 쓰여졌다. 작사자는 크게 윤치호라는 설과 안창호라는 설 두 가지가 있으며, 국사편찬위원회의 공식적인 입장으로는 미상이다. 작사자 윤치호 설은 윤치호가 애국가의 가사를 1907년에 써서 후에 그 자신의 이름으로 출판했다는 것이다. 한편 안창호가 썼다는 주장은 안창호가 애국가를 보급하는 데에 앞장섰다는 데에 중점을 두고 있다. 1908년에 출판된 가사집 《찬미가》에 수록된 것을 비롯한 많은 일제 강점기의 애국가 출판물은 윤치호를 작사자로 돌리고 있는 등 윤치호 설에는 증거가 많은 반면 안창호 설에는 실증적인 자료가 부족하다.
윤치호의 사촌동생 윤치영은 윤치호가 대한민국의 애국가 가사의 일부를 썼다고 주장했다. 윤치영에 의하면 애국가 가사의 앞부분은 최병헌 목사가 짓고, 후렴구는 윤치호가 지었다는 것이다. 최병헌은 윤치호가 다니던 정동감리교회의 목사였다. 윤치호와 최병헌이 함께 지었다는 애국가 사본이 2002년 한남대학교 교수 박정규에 의해 발견되기도 했다. 이는 윤치호의 《무궁화 노래》(1896)와 김인식의 《코리아》(1910)가 합쳐진 형태로, 후렴이 현재의 애국가와 같다. 또한 애국가의 원본은 그가 지었으나, 후에 대한민국 임시정부에서 일부 개사했다고도 한다.
그밖에 "성자신손 오백년은, 우리 황실이요"로 시작되는 협성회 무궁화가 역시 윤치호가 작사를 하였다는 설이 있다. 윤치호가 지은 노래 중 안창호가 가사의 성자신손 오백년은 우리 황실이요 를 문제삼아 가사를 바꾸라고 요청하자 동해물과 백두산이 마르고 닳도록 으로 고쳤다. 그러나 1919년 대한민국 임시 정부에 참여한 안창호는 윤치호가 지었다가 본인 스스로 수정한 부분 중에서도 우리 대한 만세를 우리 나라 만세로, 이기상과 이맘으로 임금을 섬기며를 이기상과 이맘으로 충성을 다하며로 안창호가 다시 고쳤다는 것이다.'

작사자 윤치호 설은 윤치호가 애국가의 가사를 1907년에 써서 후에 그 자신의 이름으로 출판했다는 것이다.
윤치호의 사촌동생 윤치영은 윤치호가 대한민국의 애국가 가사의 일부를 썼다고 주장했다.
윤치영에 의하면 애국가 가사의 앞부분은 최병헌 목사가 짓고, 후렴구는 윤치호가 지었다는 것이다.
real	0m1.396s
user	0m0.034s
sys	0m0.000s
```

## License

MIT
