from mini.web import models as m


def request(request, to_username=None):
    m.FriendRequest
    #친구요청 보내기
    pass


def accept(request, from_username=None):
    #친구요청 수락
    pass


def decline(request, from_username=None):
    #친구요청 거절
    pass


def read(request, username=None):
    #친구목록 보기
    pass


def request_list(request):
    #친구요청목록 보기
    pass


def unfriend(request, to_username=None):
    #친구 삭제
    pass