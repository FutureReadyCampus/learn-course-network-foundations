---
id: u3-l01-osi-seven-layers
title: 택배로 훑어보는 OSI 7계층
page_groups:
- title: 택배 여정을 일곱 역할로 나눠 보기
  sections: [1]
- title: 7계층 응용 · 무엇을 주고받을까
  sections: [2]
- title: 6계층 표현 · 어떤 형식으로 읽을까
  sections: [3]
- title: 5계층 세션 · 대화를 어떻게 이어 갈까
  sections: [4]
- title: 4계층 전송 · 어느 프로그램까지 보낼까
  sections: [5]
- title: 3계층 네트워크 · 어느 네트워크로 갈까
  sections: [6]
- title: 2계층 데이터 링크 · 다음 이웃에게 어떻게 건넬까
  sections: [7]
- title: 1계층 물리 · 신호를 어떻게 실어 보낼까
  sections: [8]
- title: 일곱 계층 순서 다시 보기
  sections: [9]
page_metadata:
- terms: [OSI 7계층 (OSI 7 layers)]
  animations:
  - file: l01-osi-layer-stack.svg
    title: 위에서 아래로 쌓인 OSI 7계층
    alt: 위에서 아래로 7 응용, 6 표현, 5 세션, 4 전송, 3 네트워크, 2 데이터 링크, 1 물리 계층이 쌓여 있습니다. 아래 방향 화살표와 함께 계층이 차례로 강조됩니다.
    caption: 먼저 순서의 모양만 살펴보세요. 다음 페이지부터 각 역할을 택배 여정에 기대어 짧게 확인합니다.
  illustrations:
  - file: assets/animations/u3l01-osi-p1-parcel-seven-roles.svg
    title: "택배 여정을 일곱 역할로"
    alt: "위에서 아래로 응용, 표현, 세션, 전송, 네트워크, 데이터 링크, 물리가 쌓여 있고 각 줄 옆에 무엇을 보낼지, 포장, 배송 안내, 보내는 사람에서 받는 사람, 주소와 분류, 가까운 구간 인계, 실제 이동 수단이 나타납니다. 택배 상자가 위에서 아래로 내려가고 받는 쪽에서는 아래에서 위로 올라옵니다."
    caption: "택배 장면은 낯선 역할을 기억하기 위한 비유이며, 택배와 네트워크가 일곱 부서로 똑같이 움직인다는 뜻은 아닙니다."
    after_paragraph: 1
  illustration_after_paragraph: [1]
- terms: [응용 계층 (Application layer)]
  question_placements:
  - question_id: u3-osi-layer-q08
    after_paragraph: 1
  - question_id: u3-osi-review-q03
    after_paragraph: 2
  questions:
  - id: u3-osi-layer-q08
    kind: choice
    difficulty: easy
    prompt: 응용 계층은 어떤 일을 하나요?
    choices:
    - id: a
      text: 프로그램이 네트워크로 주고받을 기능이나 요청을 다룹니다.
      feedback: 맞아요. 응용 계층은 프로그램이 네트워크로 이용하는 기능과 요청을 다룹니다.
    - id: b
      text: 데이터가 서로 읽히도록 표현 형식을 맞추거나 바꿉니다.
      feedback: 이 설명은 표현 계층에 가깝습니다. 응용 계층은 프로그램이 주고받을 기능이나 요청을 다룹니다.
    - id: c
      text: 통신 대화를 시작하고 이어 가다가 마칩니다.
      feedback: 이 설명은 세션 계층에 가깝습니다. 응용 계층은 프로그램이 주고받을 기능이나 요청을 다룹니다.
    - id: d
      text: 통신 양 끝의 프로그램 사이로 데이터를 전달합니다.
      feedback: 이 설명은 전송 계층에 가깝습니다. 응용 계층은 프로그램이 주고받을 기능이나 요청을 다룹니다.
    - id: e
      text: IP 주소를 바탕으로 목적지 네트워크까지의 경로를 찾습니다.
      feedback: 이 설명은 네트워크 계층에 가깝습니다. 응용 계층은 프로그램이 주고받을 기능이나 요청을 다룹니다.
    answer: a
  - id: u3-osi-review-q03
    kind: choice
    difficulty: easy
    prompt: 받을 사람이 요청한 책이나 물건처럼, 네트워크에서 프로그램이 주고받으려는 기능이나 내용을 다룹니다. 어느 계층일까요?
    choices:
    - id: a
      text: 전송 계층
      feedback: 전송 계층은 통신 양 끝의 프로그램 사이로 데이터를 전달합니다.
    - id: b
      text: 네트워크 계층
      feedback: 네트워크 계층은 목적지 네트워크까지 갈 경로를 찾습니다.
    - id: c
      text: 응용 계층
      feedback: 맞아요. 응용 계층은 프로그램이 네트워크로 이용하는 기능과 요청을 다룹니다.
    - id: d
      text: 표현 계층
      feedback: 표현 계층은 데이터가 표현되는 형식과 변환을 다룹니다.
    - id: e
      text: 세션 계층
      feedback: 세션 계층은 통신 대화가 이어지고 마무리되는 흐름을 다룹니다.
    answer: c
  illustrations:
  - file: assets/animations/u3l01-osi-p2-application.svg
    title: "응용 계층: 무엇을 보낼까"
    alt: "7계층이 강조된 계층 목록에서 위에서 내려온 택배 상자가 응용 계층에 머물고, 보내는 사람이 “이 책 한 권 보내 주세요”라고 부탁하는 장면과 웹 페이지 요청, 이름 주소 묻기 예시가 나옵니다. 상자는 아래 표현 계층으로 넘어가고 받는 쪽에서는 위로 올라옵니다."
    caption: "응용 계층은 프로그램이 주고받을 일을 다룹니다. 택배 앱이나 배달원 자체를 뜻하지는 않습니다."
    after_paragraph: 1
- terms: [표현 계층 (Presentation layer)]
  question_placements:
  - question_id: u3-osi-layer-q09
    after_paragraph: 1
  - question_id: u3-osi-review-q07
    after_paragraph: 2
  questions:
  - id: u3-osi-layer-q09
    kind: choice
    difficulty: easy
    prompt: 표현 계층은 어떤 일을 하나요?
    choices:
    - id: a
      text: 프로그램이 네트워크로 주고받을 기능이나 요청을 다룹니다.
      feedback: 이 설명은 응용 계층에 가깝습니다. 표현 계층은 데이터의 형식과 변환을 다룹니다.
    - id: b
      text: 통신 대화를 시작하고 이어 가다가 마칩니다.
      feedback: 이 설명은 세션 계층에 가깝습니다. 표현 계층은 데이터의 형식과 변환을 다룹니다.
    - id: c
      text: 통신 양 끝의 프로그램 사이로 데이터를 전달합니다.
      feedback: 이 설명은 전송 계층에 가깝습니다. 표현 계층은 데이터의 형식과 변환을 다룹니다.
    - id: d
      text: IP 주소를 바탕으로 목적지 네트워크까지의 경로를 찾습니다.
      feedback: 이 설명은 네트워크 계층에 가깝습니다. 표현 계층은 데이터의 형식과 변환을 다룹니다.
    - id: e
      text: 데이터 형식을 맞추고 필요하면 변환하거나 압축·암호화합니다.
      feedback: 맞아요. 표현 계층은 데이터가 읽히는 형식과 필요한 변환을 다룹니다.
    answer: e
  - id: u3-osi-review-q07
    kind: choice
    difficulty: easy
    prompt: 받는 사람이 읽을 수 있도록 내용의 형식을 맞추고, 필요하면 바꾸거나 보호합니다. 어느 계층의 역할일까요?
    choices:
    - id: a
      text: 응용 계층
      feedback: 응용 계층은 프로그램이 네트워크로 이용하는 기능을 다룹니다.
    - id: b
      text: 표현 계층
      feedback: 맞아요. 표현 계층은 데이터의 표현 형식을 맞추고 변환하거나 보호합니다.
    - id: c
      text: 세션 계층
      feedback: 세션 계층은 통신 대화를 이어 가고 마무리하는 역할입니다.
    - id: d
      text: 데이터 링크 계층
      feedback: 데이터 링크 계층은 바로 이웃한 장치 사이로 프레임을 전달합니다.
    - id: e
      text: 전송 계층
      feedback: 전송 계층은 양 끝 프로그램 사이의 전달을 맡습니다.
    answer: b
  illustrations:
  - file: assets/animations/u3l01-osi-p3-presentation.svg
    title: "표현 계층: 어떤 형식일까"
    alt: "6계층이 강조된 계층 목록에서 택배 상자가 표현 계층에 머물고, 안녕하세요와 Hello 문서가 읽을 수 있는 형식으로 맞춰지고 필요하면 압축이나 암호화가 되는 봉투 장면이 나옵니다. 상자는 아래 세션 계층으로 넘어갑니다."
    caption: "표현 계층은 데이터의 형식과 필요한 변환을 다룹니다. 실제 변환이나 암호화가 항상 별도의 한 계층에서만 일어나는 것은 아닙니다."
    after_paragraph: 1
- terms: [세션 계층 (Session layer)]
  question_placements:
  - question_id: u3-osi-layer-q10
    after_paragraph: 1
  - question_id: u3-osi-review-q02
    after_paragraph: 2
  questions:
  - id: u3-osi-layer-q10
    kind: choice
    difficulty: easy
    prompt: 세션 계층은 어떤 일을 하나요?
    choices:
    - id: a
      text: 프로그램이 네트워크로 주고받을 기능이나 요청을 다룹니다.
      feedback: 이 설명은 응용 계층에 가깝습니다. 세션 계층은 통신 대화의 흐름을 다룹니다.
    - id: b
      text: 데이터 형식을 맞추고 필요하면 변환하거나 보호합니다.
      feedback: 이 설명은 표현 계층에 가깝습니다. 세션 계층은 통신 대화의 흐름을 다룹니다.
    - id: c
      text: 통신 양 끝의 프로그램 사이로 데이터를 전달합니다.
      feedback: 이 설명은 전송 계층에 가깝습니다. 세션 계층은 통신 대화의 흐름을 다룹니다.
    - id: d
      text: 통신 대화를 시작하고 이어 가다가 마칩니다.
      feedback: 맞아요. 세션 계층은 통신 대화의 시작·유지·마무리를 다룹니다.
    - id: e
      text: 같은 네트워크 구간에서 이웃한 장치 사이로 프레임을 전달합니다.
      feedback: 이 설명은 데이터 링크 계층에 가깝습니다. 세션 계층은 통신 대화의 흐름을 다룹니다.
    answer: d
  - id: u3-osi-review-q02
    kind: choice
    difficulty: easy
    prompt: 배송 상황을 서로 주고받으며 대화를 시작하고 이어 가고 마칩니다. OSI에서 이 기능에 가까운 계층은 무엇일까요?
    choices:
    - id: a
      text: 표현 계층
      feedback: 표현 계층은 데이터 표현 형식과 변환을 다룹니다.
    - id: b
      text: 세션 계층
      feedback: 맞아요. 세션 계층은 통신 대화를 시작하고 이어 가고 마치는 역할입니다.
    - id: c
      text: 응용 계층
      feedback: 응용 계층은 프로그램이 네트워크로 이용하는 기능을 다룹니다.
    - id: d
      text: 데이터 링크 계층
      feedback: 데이터 링크 계층은 바로 이웃한 장치 사이에서 프레임을 전달합니다.
    - id: e
      text: 전송 계층
      feedback: 전송 계층은 양 끝 프로그램 사이의 데이터 전달을 맡습니다.
    answer: b
  illustrations:
  - file: assets/animations/u3l01-osi-p4-session.svg
    title: "세션 계층: 대화를 이어 가요"
    alt: "5계층이 강조된 계층 목록에서 택배 상자가 세션 계층에 머물고, 배송 시작, 이동 중, 배송 완료 알림처럼 대화가 시작되고 이어지고 마치는 장면이 나옵니다. 택배에 딱 맞는 담당자는 없다고 표시됩니다."
    caption: "세션 계층은 통신 대화의 시작, 유지, 마무리를 다룹니다. 택배에는 정확히 같은 담당자가 없고 대화 흐름을 붙잡는 비유일 뿐입니다."
    after_paragraph: 1
- terms: [전송 계층 (Transport layer)]
  question_placements:
  - question_id: u3-osi-layer-q11
    after_paragraph: 1
  - question_id: u3-osi-review-q05
    after_paragraph: 2
  questions:
  - id: u3-osi-layer-q11
    kind: choice
    difficulty: easy
    prompt: 전송 계층은 어떤 일을 하나요?
    choices:
    - id: a
      text: 프로그램이 네트워크로 주고받을 기능이나 요청을 다룹니다.
      feedback: 이 설명은 응용 계층에 가깝습니다. 전송 계층은 양 끝의 프로그램 사이 전달을 다룹니다.
    - id: b
      text: 데이터 형식을 맞추고 필요하면 변환하거나 보호합니다.
      feedback: 이 설명은 표현 계층에 가깝습니다. 전송 계층은 양 끝의 프로그램 사이 전달을 다룹니다.
    - id: c
      text: 통신 양 끝의 프로그램 사이에서 데이터를 전달합니다.
      feedback: 맞아요. 전송 계층은 통신하는 양 끝의 프로그램 사이에서 데이터를 전달합니다.
    - id: d
      text: 통신 대화를 시작하고 이어 가다가 마칩니다.
      feedback: 이 설명은 세션 계층에 가깝습니다. 전송 계층은 양 끝의 프로그램 사이 전달을 다룹니다.
    - id: e
      text: IP 주소를 바탕으로 목적지 네트워크까지의 경로를 찾습니다.
      feedback: 이 설명은 네트워크 계층에 가깝습니다. 전송 계층은 양 끝의 프로그램 사이 전달을 다룹니다.
    answer: c
  - id: u3-osi-review-q05
    kind: choice
    difficulty: easy
    prompt: 보낸 쪽의 프로그램에서 받을 쪽의 프로그램까지 데이터를 전달합니다. 어느 계층의 역할일까요?
    choices:
    - id: a
      text: 세션 계층
      feedback: 세션 계층은 통신 대화가 이어지는 일을 다룹니다.
    - id: b
      text: 네트워크 계층
      feedback: 네트워크 계층은 IP 주소를 바탕으로 목적지 쪽 경로를 찾습니다.
    - id: c
      text: 데이터 링크 계층
      feedback: 데이터 링크 계층은 바로 이웃한 장치 사이의 한 구간을 맡습니다.
    - id: d
      text: 응용 계층
      feedback: 응용 계층은 프로그램이 네트워크로 이용하는 기능을 다룹니다.
    - id: e
      text: 전송 계층
      feedback: 맞아요. 전송 계층은 통신 양 끝의 프로그램 사이에서 데이터를 전달합니다.
    answer: e
  illustrations:
  - file: assets/animations/u3l01-osi-p5-transport.svg
    title: "전송 계층: 어느 프로그램까지"
    alt: "4계층이 강조된 계층 목록에서 택배 상자가 전송 계층에 머물고, 보내는 사람의 상자가 받는 컴퓨터 안의 브라우저, 게임, 메신저 중 알맞은 프로그램에 닿는 장면이 나옵니다."
    caption: "전송 계층은 통신 양 끝의 프로그램 사이에서 데이터를 전달합니다. 장치까지는 3계층, 그 안의 프로그램까지는 4계층입니다."
    after_paragraph: 1
- terms: [네트워크 계층 (Network layer)]
  question_placements:
  - question_id: u3-osi-layer-q12
    after_paragraph: 1
  - question_id: u3-osi-review-q06
    after_paragraph: 2
  questions:
  - id: u3-osi-layer-q12
    kind: choice
    difficulty: easy
    prompt: 네트워크 계층은 어떤 일을 하나요?
    choices:
    - id: a
      text: 통신 양 끝의 프로그램 사이에서 데이터를 전달합니다.
      feedback: 이 설명은 전송 계층에 가깝습니다. 네트워크 계층은 목적지 네트워크까지의 경로를 찾습니다.
    - id: b
      text: 통신 대화를 시작하고 이어 가다가 마칩니다.
      feedback: 이 설명은 세션 계층에 가깝습니다. 네트워크 계층은 목적지 네트워크까지의 경로를 찾습니다.
    - id: c
      text: 같은 구간에서 이웃한 장치 사이로 프레임을 전달합니다.
      feedback: 이 설명은 데이터 링크 계층에 가깝습니다. 네트워크 계층은 목적지 네트워크까지의 경로를 찾습니다.
    - id: d
      text: IP 주소를 바탕으로 목적지 네트워크까지의 경로를 찾습니다.
      feedback: 맞아요. 네트워크 계층은 목적지 네트워크와 그곳까지의 경로를 다룹니다.
    - id: e
      text: 비트를 전기·빛·무선 신호로 바꾸어 전달합니다.
      feedback: 이 설명은 물리 계층에 가깝습니다. 네트워크 계층은 목적지 네트워크까지의 경로를 찾습니다.
    answer: d
  - id: u3-osi-review-q06
    kind: choice
    difficulty: easy
    prompt: 주소를 보고 상자가 어느 지역과 경로를 거쳐 갈지 정합니다. 네트워크에서 목적지 쪽 경로를 찾는 계층은 무엇일까요?
    choices:
    - id: a
      text: 네트워크 계층
      feedback: 맞아요. 네트워크 계층은 IP 주소를 바탕으로 목적지까지 갈 경로를 찾습니다.
    - id: b
      text: 표현 계층
      feedback: 표현 계층은 데이터의 표현 형식을 맞추거나 바꿉니다.
    - id: c
      text: 물리 계층
      feedback: 물리 계층은 비트를 실제 신호로 실어 보냅니다.
    - id: d
      text: 데이터 링크 계층
      feedback: 데이터 링크 계층은 바로 다음 이웃 장치까지 프레임을 전달합니다.
    - id: e
      text: 전송 계층
      feedback: 전송 계층은 끝에 있는 프로그램 사이에서 데이터를 전달합니다.
    answer: a
  illustrations:
  - file: assets/animations/u3l01-osi-p6-network.svg
    title: "네트워크 계층: 어느 네트워크로"
    alt: "3계층이 강조된 계층 목록에서 택배 상자가 네트워크 계층에 머물고, 주소를 읽고 여러 지역 가운데 출발에서 목적지까지의 분류 경로를 고르는 장면이 나옵니다."
    caption: "네트워크 계층은 IP 주소를 바탕으로 목적지 네트워크까지의 경로를 찾습니다. 한 구간 전달을 맡는 데이터 링크 계층과 범위가 다릅니다."
    after_paragraph: 1
- terms: [데이터 링크 계층 (Data Link layer)]
  question_placements:
  - question_id: u3-osi-layer-q13
    after_paragraph: 1
  - question_id: u3-osi-review-q01
    after_paragraph: 2
  questions:
  - id: u3-osi-layer-q13
    kind: choice
    difficulty: easy
    prompt: 데이터 링크 계층은 어떤 일을 하나요?
    choices:
    - id: a
      text: IP 주소를 바탕으로 목적지 네트워크까지의 경로를 찾습니다.
      feedback: 이 설명은 네트워크 계층에 가깝습니다. 데이터 링크 계층은 이웃한 장치 사이의 한 구간을 다룹니다.
    - id: b
      text: 같은 네트워크 구간에서 이웃한 장치 사이로 프레임을 전달합니다.
      feedback: 맞아요. 데이터 링크 계층은 바로 이웃한 장치 사이의 한 구간에서 프레임을 전달합니다.
    - id: c
      text: 통신 양 끝의 프로그램 사이에서 데이터를 전달합니다.
      feedback: 이 설명은 전송 계층에 가깝습니다. 데이터 링크 계층은 이웃한 장치 사이의 한 구간을 다룹니다.
    - id: d
      text: 비트를 전기·빛·무선 신호로 바꾸어 전달합니다.
      feedback: 이 설명은 물리 계층에 가깝습니다. 데이터 링크 계층은 프레임을 한 구간 전달합니다.
    - id: e
      text: 통신 대화를 시작하고 이어 가다가 마칩니다.
      feedback: 이 설명은 세션 계층에 가깝습니다. 데이터 링크 계층은 이웃한 장치 사이의 한 구간을 다룹니다.
    answer: b
  - id: u3-osi-review-q01
    kind: choice
    difficulty: easy
    prompt: 같은 네트워크 구간에서 바로 이웃한 장치로 프레임을 건넵니다. 어느 계층의 역할일까요?
    choices:
    - id: a
      text: 데이터 링크 계층
      feedback: 맞아요. 데이터 링크 계층은 한 구간에서 이웃한 장치 사이로 프레임을 전달합니다.
    - id: b
      text: 네트워크 계층
      feedback: 네트워크 계층은 목적지 네트워크 쪽 경로를 찾습니다.
    - id: c
      text: 전송 계층
      feedback: 전송 계층은 통신 양 끝의 프로그램 사이에서 데이터를 전달합니다.
    - id: d
      text: 물리 계층
      feedback: 물리 계층은 비트를 실제 신호로 실어 보냅니다.
    - id: e
      text: 세션 계층
      feedback: 세션 계층은 통신 대화의 흐름을 다룹니다.
    answer: a
  illustrations:
  - file: assets/animations/u3l01-osi-p7-data-link.svg
    title: "데이터 링크: 다음 이웃에게"
    alt: "2계층이 강조된 계층 목록에서 택배 상자가 데이터 링크 계층에 머물고, 노트북에서 공유기로 건네는 한 구간이 강조되고 그 뒤 목적지까지는 점선으로 표시됩니다."
    caption: "데이터 링크 계층은 같은 네트워크 구간에서 이웃한 장치 사이로 프레임을 전달합니다. 최종 목적지까지의 전체 경로와는 범위가 다릅니다."
    after_paragraph: 1
- terms: [물리 계층 (Physical layer)]
  question_placements:
  - question_id: u3-osi-layer-q14
    after_paragraph: 1
  - question_id: u3-osi-review-q04
    after_paragraph: 2
  questions:
  - id: u3-osi-layer-q14
    kind: choice
    difficulty: easy
    prompt: 물리 계층은 어떤 일을 하나요?
    choices:
    - id: a
      text: 프로그램이 네트워크로 주고받을 기능이나 요청을 다룹니다.
      feedback: 이 설명은 응용 계층에 가깝습니다. 물리 계층은 비트를 실제 신호로 전달합니다.
    - id: b
      text: 통신 대화를 시작하고 이어 가다가 마칩니다.
      feedback: 이 설명은 세션 계층에 가깝습니다. 물리 계층은 비트를 실제 신호로 전달합니다.
    - id: c
      text: IP 주소를 바탕으로 목적지 네트워크까지의 경로를 찾습니다.
      feedback: 이 설명은 네트워크 계층에 가깝습니다. 물리 계층은 비트를 실제 신호로 전달합니다.
    - id: d
      text: 같은 네트워크 구간에서 이웃한 장치 사이로 프레임을 전달합니다.
      feedback: 이 설명은 데이터 링크 계층에 가깝습니다. 물리 계층은 비트를 실제 신호로 전달합니다.
    - id: e
      text: 비트를 전기·빛·무선 신호로 바꾸어 매체를 통해 전달합니다.
      feedback: 맞아요. 물리 계층은 비트를 실제 신호로 실어 보냅니다.
    answer: e
  - id: u3-osi-review-q04
    kind: choice
    difficulty: easy
    prompt: 상자를 실은 차량이 도로를 달리듯, 비트를 전기·빛·무선 신호로 실어 보냅니다. 어느 계층일까요?
    choices:
    - id: a
      text: 전송 계층
      feedback: 전송 계층은 통신 양 끝의 프로그램 사이에서 데이터를 전달합니다.
    - id: b
      text: 데이터 링크 계층
      feedback: 데이터 링크 계층은 한 구간에서 프레임을 주고받습니다.
    - id: c
      text: 네트워크 계층
      feedback: 네트워크 계층은 목적지 네트워크로 갈 경로를 찾습니다.
    - id: d
      text: 물리 계층
      feedback: 맞아요. 물리 계층은 비트를 매체를 따라가는 신호로 전달합니다.
    - id: e
      text: 세션 계층
      feedback: 세션 계층은 통신 대화를 이어 가는 흐름을 다룹니다.
    answer: d
  illustrations:
  - file: assets/animations/u3l01-osi-p8-physical.svg
    title: "물리 계층: 신호로 실어 보내요"
    alt: "1계층이 강조된 계층 목록에서 택배 상자가 물리 계층에 머물고, 구리선, 광섬유, 무선 세 길 위에서 비트가 전기, 빛, 전파 신호로 실려 가는 장면이 나옵니다."
    caption: "물리 계층은 비트를 전기, 빛, 무선 신호로 바꾸어 케이블, 광섬유, 공기를 통해 전달합니다."
    after_paragraph: 1
- terms: [OSI 7계층 (OSI 7 layers)]
  illustrations:
  - file: assets/animations/u3l01-osi-p9-order-recap.svg
    title: "응·표·세 / 전·네 / 데·물"
    alt: "일곱 계층이 응·표·세, 전·네, 데·물 세 묶음으로 차례로 강조되고, 보내는 쪽은 위에서 아래로 받는 쪽은 아래에서 위로 읽는 화살표가 나옵니다. 택배는 기억을 돕는 장면일 뿐이라고 표시됩니다."
    caption: "응용, 표현, 세션, 전송, 네트워크, 데이터 링크, 물리를 위에서 아래로 끊어 읽으면 기억하기 쉽습니다. 택배 비유는 실제 네트워크와 일대일로 대응하지 않습니다."
    after_paragraph: 0
animations_dir: units/03-layer2-switching/lessons/01-osi-seven-layers/assets/animations
---
Unit 1에서 층층이 그려진 통신 지도를 봤고, Unit 2에서는 택배 한 상자가 여러 장소와 사람을 거쳐 도착하는 여정을 따라갔습니다. 이제 그 익숙한 택배 여정을 일곱 역할로 나눠, OSI 계층의 이름과 순서를 먼저 훑어보겠습니다. 오늘은 프로토콜이나 장치의 세부 동작을 외우지 않아도 됩니다.

## 택배 여정을 일곱 역할로 나눠 보기

택배 한 건에는 보내려는 물건과 요청, 알아볼 수 있는 포장, 배송 중 주고받는 안내, 목적지 주소, 가까운 구간의 인계, 그리고 실제 이동 수단이 있습니다. 네트워크 통신도 한 가지 일로 끝나지 않고, 서로 다른 역할이 이어져 데이터를 전달합니다. 이 역할을 설명하기 위한 대표적인 지도가 OSI 7계층입니다.

OSI 계층은 **위에서 아래로 응용 → 표현 → 세션 → 전송 → 네트워크 → 데이터 링크 → 물리** 순서입니다. 아래 그림은 이 순서와 위아래 방향만 먼저 보여 줍니다. 다음 일곱 페이지에서 계층마다 맡은 일을 택배 여정의 장면 하나와 함께 살펴보겠습니다.

택배와 네트워크가 똑같이 일곱 부서로 움직인다는 뜻은 아닙니다. 택배 장면은 낯선 역할을 기억하기 위한 비유이고, 특히 세션처럼 택배와 딱 맞는 단계가 없는 계층도 있습니다. 실제 인터넷 기술이 언제나 OSI 일곱 층에 하나씩 정확히 들어맞는 것도 아닙니다. 여기서는 각 이름이 가리키는 역할과 위에서 아래 순서를 익히면 충분합니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** OSI 7계층의 위→아래 이름 순서를 한 번 소리 내어 읽는다.
- **적용하기 (Apply):** 택배의 전체 여정과 통신 기능을 여러 역할로 나누는 생각을 연결한다.
- **찾아보기 (Lookup):** 실제 프로토콜과 장치의 자세한 동작은 뒤의 Lesson에서 확인한다.

## 7계층 응용 · 무엇을 주고받을까

응용 계층(Application)은 네트워크를 사용하는 프로그램이 어떤 기능이나 요청을 주고받을지 다룹니다. 웹페이지를 요청하거나 도메인 이름의 주소를 물어보는 일이 예입니다.

택배로 떠올리면 보내려는 물건이나 부탁이 무엇인지 정하는 장면과 비슷합니다. 여기서 응용 계층은 택배 회사의 앱이나 배달원 자체를 뜻하지 않습니다. **기억 문장:** 응용은 프로그램이 주고받을 일을 다룹니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 응용 계층은 프로그램이 네트워크로 이용하는 기능을 다룬다.
- **적용하기 (Apply):** 웹 요청처럼 프로그램이 네트워크에 부탁하는 일을 응용 계층과 연결한다.
- **찾아보기 (Lookup):** HTTP나 DNS가 데이터를 주고받는 구체적인 방식은 뒤에서 살펴본다.

## 6계층 표현 · 어떤 형식으로 읽을까

표현 계층(Presentation)은 데이터가 서로 알아볼 수 있도록 표현 형식을 맞추고, 필요하면 다른 형식으로 바꾸거나 압축·암호화하는 역할로 설명합니다.

택배로는 상자 안의 문서가 받는 사람에게 읽히도록 언어와 형식을 맞추고, 내용이 보이지 않도록 봉투로 보호하는 장면을 떠올릴 수 있습니다. 다만 실제 통신의 형식 변환이나 암호화가 항상 별도의 한 계층에서만 일어나는 것은 아닙니다. **기억 문장:** 표현은 데이터를 어떤 형식으로 읽을지 다룹니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 표현 계층은 데이터의 형식과 필요한 변환을 다룬다.
- **적용하기 (Apply):** 같은 내용이라도 서로 읽을 수 있는 표현으로 맞춰야 한다는 점을 설명한다.
- **찾아보기 (Lookup):** 실제 인코딩·압축·암호화 방식은 관련 기술을 배울 때 확인한다.

## 5계층 세션 · 대화를 어떻게 이어 갈까

세션 계층(Session)은 두 프로그램 사이의 통신 대화를 시작하고, 이어 가고, 마치는 역할로 설명합니다.

택배에서는 배송 알림이나 문의처럼 배송 중 오가는 대화를 떠올릴 수 있습니다. 하지만 택배 여정에 세션 계층과 정확히 같은 담당자가 있는 것은 아닙니다. 이 비유는 ‘대화의 흐름을 관리한다’는 생각을 붙잡기 위한 것입니다. **기억 문장:** 세션은 통신 대화의 시작·유지·마무리를 다룹니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 세션 계층은 프로그램 사이의 대화가 이어지는 흐름을 다룬다.
- **적용하기 (Apply):** 대화를 시작하고 계속하다가 마치는 일을 하나의 흐름으로 설명한다.
- **찾아보기 (Lookup):** 실제 통신에서 이 기능이 어떻게 구현되는지는 뒤의 프로토콜 설명과 연결한다.

## 4계층 전송 · 어느 프로그램까지 보낼까

전송 계층(Transport)은 통신하는 양 끝의 프로그램 사이에서 데이터를 전달합니다. 한 컴퓨터 안에서도 여러 프로그램이 네트워크를 사용하므로, 어느 통신 상대에게 전달할지 구분하는 역할이 필요합니다.

택배에서는 보내는 사람에게서 받는 사람까지 배송을 맡는 큰 흐름에 비유할 수 있습니다. 3계층이 목적지 네트워크를 찾는다면, 4계층은 그 장치의 어떤 통신 상대까지 데이터를 전달할지 다룹니다. **기억 문장:** 전송은 끝에 있는 프로그램 사이의 전달입니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 전송 계층은 통신 양 끝의 프로그램 사이에서 데이터를 전달한다.
- **적용하기 (Apply):** 목적지 장치까지의 경로와 장치 안의 프로그램까지의 전달을 구분한다.
- **찾아보기 (Lookup):** 포트 번호와 TCP·UDP의 차이는 뒤의 Unit에서 확인한다.

## 3계층 네트워크 · 어느 네트워크로 갈까

네트워크 계층(Network)은 IP 주소를 바탕으로 데이터가 목적지 네트워크까지 갈 경로를 찾습니다. 라우터는 이 계층의 주소와 경로 정보를 이용해 다음 방향을 정합니다.

택배에서는 주소를 읽고 어느 지역과 분류 경로로 보낼지 고르는 장면과 닮았습니다. 이는 ‘어느 네트워크 쪽으로 갈까?’에 답하며, 바로 옆 장치에 한 구간 전달을 맡는 데이터 링크 계층과는 범위가 다릅니다. **기억 문장:** 네트워크는 목적지와 경로를 찾습니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 네트워크 계층은 목적지 네트워크까지의 경로를 찾는다.
- **적용하기 (Apply):** 지역과 경로를 고르는 택배 장면을 목적지 IP 주소와 연결한다.
- **찾아보기 (Lookup):** IPv4 주소와 라우터의 자세한 역할은 뒤의 Unit에서 살펴본다.

## 2계층 데이터 링크 · 다음 이웃에게 어떻게 건넬까

데이터 링크 계층(Data Link)은 같은 네트워크 구간에서 바로 이웃한 장치 사이로 프레임을 전달합니다. 노트북이 Wi-Fi 공유기로 데이터를 보내는 첫 구간을 예로 들 수 있습니다.

택배에서 상자를 가까운 분류 장소나 다음 담당자에게 넘기는 장면을 떠올려 보세요. 상자가 최종 목적지에 도착할 전체 경로와 달리, 데이터 링크는 지금 이어진 한 구간을 맡습니다. **기억 문장:** 데이터 링크는 이웃 사이 한 구간을 잇습니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 데이터 링크 계층은 한 구간에서 프레임을 전달한다.
- **적용하기 (Apply):** 최종 목적지 경로와 다음 이웃까지의 전달 범위를 구분한다.
- **찾아보기 (Lookup):** MAC 주소와 Ethernet·Wi-Fi 프레임은 이어지는 Lesson에서 배운다.

## 1계층 물리 · 신호를 어떻게 실어 보낼까

물리 계층(Physical)은 비트를 전기, 빛, 무선 신호로 바꾸어 케이블·광섬유·공기를 통해 전달합니다. 이 계층은 데이터를 어떤 실제 신호와 매체로 보낼지 다룹니다.

택배의 도로와 차량처럼 상자가 실제로 이동할 수단을 떠올릴 수 있습니다. 도로와 차량은 비트나 프레임 자체가 아니라 이동을 가능하게 하는 바탕입니다. **기억 문장:** 물리는 비트를 실제 신호로 보냅니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 물리 계층은 비트를 실제 신호로 실어 보낸다.
- **적용하기 (Apply):** 구리선·광섬유·무선처럼 신호가 지나가는 매체의 예를 든다.
- **찾아보기 (Lookup):** Ethernet 케이블과 Wi-Fi의 신호 방식은 다음 Lesson에서 연결한다.

## 일곱 계층 순서 다시 보기

위에서 아래로 **응용 → 표현 → 세션 → 전송 → 네트워크 → 데이터 링크 → 물리**입니다. “응·표·세 / 전·네 / 데·물”로 끊어 읽으면 순서를 기억하기 쉽습니다. 이제 각 설명을 보고 어떤 계층인지 골라 보세요. 택배 비유는 기억을 돕는 장면이며, 실제 네트워크와 일대일로 대응하는 구조는 아닙니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 일곱 계층을 위에서 아래 순서로 말한다.
- **적용하기 (Apply):** 한 가지 네트워크 기능 설명을 듣고 알맞은 계층을 고른다.
- **찾아보기 (Lookup):** 장치·주소·프로토콜의 구체적인 학습은 다음 Lesson부터 이어진다.
