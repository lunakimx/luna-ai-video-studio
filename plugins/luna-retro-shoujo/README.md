# 루나 레트로 순정만화 프사

사진을 정사각형 레트로 순정만화 프사로 바꾸는 루나 스킬의 공개 배포본입니다. 여자·남자 참고 그림과 최신 머리카락 표현 지침을 포함합니다.

## 친구에게 공유하기

- [사용 안내와 바로 쓰는 프롬프트](START-HERE-KO.md)
- [플러그인 ZIP 다운로드](https://github.com/lunakimx/luna-ai-video-studio/raw/refs/heads/main/downloads/luna-retro-shoujo-1.0.0.zip)
- [스킬 지침](skills/luna-retro-shoujo-avatar/SKILL.md)

GitHub 공개 링크는 누구나 파일을 볼 수 있는 배포 링크입니다. 기존 개인 ChatGPT 스킬의 열람 권한을 바꾸지 않으며, ChatGPT 공개 디렉터리에 등록됐다는 뜻도 없습니다.

## 설치

ChatGPT 웹에서 플러그인 ZIP 업로드 권한과 메뉴가 제공되는 계정은 다운로드한 ZIP을 업로드합니다. 관리형 워크스페이스에서는 관리자가 Admin Console → Plugins → Add → Upload plugin에서 업로드합니다. 일반 대화창에 ZIP을 첨부하는 것만으로 설치가 되지는 않습니다.

Codex CLI 또는 지원되는 데스크톱 환경에서는 이 저장소의 마켓플레이스를 추가합니다.

```sh
codex plugin marketplace add lunakimx/luna-ai-video-studio --ref main
```

데스크톱 플러그인 목록에서 **Luna Public Skills**를 선택하고 **루나 레트로 순정만화 프사**를 설치합니다. GitHub 마켓플레이스 이용 가능 여부는 클라이언트와 계정에 따라 다릅니다. 이미지 생성 기능이 있는 환경이 필요합니다.

설치 메뉴가 없는 친구는 START-HERE-KO.md의 사진·참고 그림·프롬프트 방법을 사용합니다.

## 포함한 표현

- 어두운 머리: 넓은 색면과 적은 윤곽선, 절제된 셀 하이라이트
- 밝은 머리: 큰 S자 머리 덩어리와 긴 곡선 묶음
- 남자: 실제 머리 길이·가르마·눈썹·턱과 나이 인상을 유지하며 작은 선 입과 절제된 속눈썹 적용
- 한 장 생성 후 실제 결과를 확인하고, 요청한 부분만 수정

배포 파일과 연결된 참고 파일을 검사했습니다. 모든 인물에서 같은 결과를 보장하는 반복 시각 검증은 완료되지 않았습니다. 현재 스킬은 한 사람의 프사에 맞춰져 있습니다.

## 라이선스와 문의

작성한 지침·템플릿·배포 파일은 [MIT](LICENSE)로 공개합니다. 참고 그림의 권리는 별도이며 [ASSET-NOTICE.md](ASSET-NOTICE.md)를 확인하세요. 오류와 개선 제안은 [GitHub Issues](https://github.com/lunakimx/luna-ai-video-studio/issues)에 남겨 주세요.

## 공식 설치 안내

- https://help.openai.com/en/articles/20001256-plugins-in-chatgpt
- https://developers.openai.com/plugins/build/plugins
